from django.shortcuts import render, redirect
from django.http import JsonResponse
from .gemini import geminiApi
from pedido.models import Pedido
from calzado.models import Calzado
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.urls import reverse

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
                
                # Verificar si todas las claves necesarias están presentes en order_details.
                required_keys = ['numero_pedido', 'bloque', 'tipo_servicio', 'fecha_pedido', 'cliente', 'referencia_calzado', 'lista_pares', 'total_pares']
                for key in required_keys:
                    if key not in order_details or order_details[key] is None:
                        return JsonResponse({'error': f"Clave '{key}' faltante en los detalles del pedido."}, status=400)

                # Verificar y asignar la fecha_pedido y fecha_entrega.
                try:
                    fecha_pedido = datetime.strptime(order_details['fecha_pedido'], '%Y-%m-%d').date()
                except (TypeError, ValueError):
                    return JsonResponse({'error': "Formato de fecha_pedido inválido. Debe ser 'YYYY-MM-DD'."}, status=400)
                
                fecha_entrega_str = order_details.get('fecha_entrega')
                if fecha_entrega_str:
                    try:
                        fecha_entrega = datetime.strptime(fecha_entrega_str, '%Y-%m-%d').date()
                    except (TypeError, ValueError):
                        return JsonResponse({'error': "Formato de fecha_entrega inválido. Debe ser 'YYYY-MM-DD'."}, status=400)
                else:
                    fecha_entrega = datetime(1970, 1, 1).date()  # Valor predeterminado en caso de ausencia

                # Verificar si ya existe un pedido con el mismo número de pedido.
                numero_pedido = order_details['numero_pedido']
                existing_pedidos = Pedido.objects.filter(numero_pedido=numero_pedido)
                if existing_pedidos.exists():
                    # Si ya existe un pedido con el mismo número de pedido,
                    # agregar un número adicional al final del número de pedido.
                    numero_pedido += f'_{existing_pedidos.count() + 1}'

                try:
                    calzado_referencia = Calzado.objects.get(referencia=order_details['referencia_calzado'])
                except Calzado.DoesNotExist:
                    # Usar el objeto de Calzado predeterminado
                    try:
                        calzado_referencia = Calzado.objects.get(referencia='PALM170')
                    except Calzado.DoesNotExist:
                        return JsonResponse({'error': "Referencia de calzado predeterminada no encontrada."}, status=404)

                nuevo_pedido = Pedido(
                    numero_pedido=numero_pedido,  # Usar el número de pedido modificado si es necesario.
                    bloque=order_details['bloque'],
                    tipo_servicio=order_details['tipo_servicio'],
                    fecha_pedido=fecha_pedido,
                    fecha_entrega=fecha_entrega,
                    cliente=order_details['cliente'],
                    referencia_calzado=calzado_referencia,
                    lista_pares=order_details['lista_pares'],
                    total_pares=order_details['total_pares'],
                )
                nuevo_pedido.save()

                # Redirigir a la página de la lista de pedidos después de guardar el nuevo pedido.
                return redirect(reverse('pedido_list'))
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'gemini_app/upload.html')
