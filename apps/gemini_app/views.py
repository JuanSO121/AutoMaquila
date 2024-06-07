# apps/gemini_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .gemini import geminiApi
from pedido.models import Pedido
from calzado.models import Calzado
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def gemini_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            file_path = f'media/{file.name}'
            with open(file_path, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            
            gemini_api = geminiApi()
            gemini_api.configure()
            
            try:
                order_details = gemini_api.extract_order_details(file_path)
                # Aquí order_details es un diccionario con la información del pedido.
                
                # Verificar si 'fecha_entrega' es None y asignar un valor predeterminado si es necesario.
                fecha_entrega = order_details['fecha_entrega'] or '1970-01-01'  # Valor predeterminado si 'fecha_entrega' es None.

                try:
                    calzado_referencia = Calzado.objects.get(referencia=order_details['referencia_calzado'])
                except Calzado.DoesNotExist:
                    return JsonResponse({'error': f"Referencia de calzado '{order_details['referencia_calzado']}' no encontrada."}, status=404)

                nuevo_pedido = Pedido(
                    numero_pedido=order_details['numero_pedido'],
                    bloque=order_details['bloque'],
                    tipo_servicio=order_details['tipo_servicio'],
                    fecha_pedido=order_details['fecha_pedido'],
                    fecha_entrega=fecha_entrega,  # Asignar la fecha_entrega aquí.
                    cliente=order_details['cliente'],
                    referencia_calzado=calzado_referencia,
                    lista_pares=order_details['lista_pares'],
                    total_pares=order_details['total_pares'],
                )
                nuevo_pedido.save()

                return JsonResponse({'order_details': order_details, 'message': 'Pedido creado exitosamente'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'gemini_app/upload.html')
