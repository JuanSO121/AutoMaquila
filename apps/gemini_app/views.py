# apps/gemini_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .gemini import geminiApi

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
                return JsonResponse({'order_details': order_details})
            except Exception as e:
                return JsonResponse({'error': str(e)})
    
    return render(request, 'gemini_app/upload.html')
