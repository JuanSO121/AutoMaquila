# gemini_app/views.py
from django.shortcuts import render, redirect
from django.views import View
from .gemini import geminiApi
from .forms import UploadFileForm
from .models import UserUpload
from calzado.models import Calzado
from pedido.models import Pedido

class UploadOrderView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'gemini_app/upload.html', {'form': form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            file_path = upload.file.path

            # Procesar la imagen y extraer datos del pedido
            gemini = geminiApi()
            gemini.configure()
            order_data = gemini.extract_order_data(file_path)

            if order_data:
                # Asumimos que order_data es una lista de diccionarios con los datos de los pedidos
                for data in order_data:
                    # Buscar o crear la referencia de calzado
                    referencia_calzado, created = Calzado.objects.get_or_create(
                        id=data.get('referencia_calzado')
                    )
                    
                    # Crear el objeto Pedido
                    Pedido.objects.create(
                        numero_pedido=data.get('numero_pedido'),
                        bloque=data.get('bloque'),
                        tipo_servicio=data.get('tipo_servicio'),
                        fecha_pedido=data.get('fecha_pedido'),
                        fecha_entrega=data.get('fecha_entrega'),
                        cliente=data.get('cliente'),
                        referencia_calzado=referencia_calzado,
                        lista_pares=data.get('lista_pares'),
                        total_pares=data.get('total_pares')
                    )
                return redirect('order_list')  # Redirige a una lista de pedidos o alguna otra vista
            else:
                form.add_error(None, "No se pudieron extraer los datos del pedido de la imagen.")
        return render(request, 'gemini_app/upload.html', {'form': form})
