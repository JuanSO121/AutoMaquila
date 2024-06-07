# gemini_app/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserUploadForm
from .gemini import geminiApi, generate_word_document, generate_pdf_document
import os

def hu_imagen(request):
    if request.method == 'POST':
        form = UserUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_upload = form.save()
            file_path = user_upload.file.path
            description = form.cleaned_data['description']
            
            api = geminiApi()
            api.configure()
            textos = api.generate_user_story(file_path, description, 'image')
            
            request.session['textos'] = textos  # Almacenar en sesión
            
            return render(request, 'hu_imagen.html', {'form': form, 'textos': textos})
    else:
        form = UserUploadForm()
    return render(request, 'hu_imagen.html', {'form': form, 'textos': None})

def download_document(request, format):
    textos = request.session.get('textos')
    if not textos:
        return redirect('hu_imagen')
    
    if format == 'word':
        file_data = generate_word_document(textos)
        response = HttpResponse(file_data, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="user_stories.docx"'
    elif format == 'pdf':
        file_data = generate_pdf_document(textos)
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="user_stories.pdf"'
    else:
        return redirect('hu_imagen')
    
    return response
