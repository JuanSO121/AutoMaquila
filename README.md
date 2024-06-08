Despliegue:
https://automaquila.onrender.com

Las imagenes de los pedidos para probar la funcionalidad de Auto Pedidos se ecnuentran en la carpeta media

# Proyecto Django - Gestión de Inventario Virtual de Calzado

# INDICE
- [connection of Railway](#connection of Railway)


# connection of Railway
@jackrian97
Editar el archivo `settings.py` que esta en el path `autoMaquila\settings.py`  reemplazar la sección `DATABASES` con los detalles de la base de datos:
autoMaquila\settings.py
```python
#data base of railway
DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway', # variable name PGDATABASE
        'USER': 'postgres', # variable name PGUSER
        'PASSWORD': 'sHhRMpFkckQeoGrLeobiKxWnYAwosVHi', # variable name PGPASSWORD
        'HOST': 'roundhouse.proxy.rlwy.net', # variable name PGHOST
        'PORT': '16828', # variable name PGPORT
    }
}
```
