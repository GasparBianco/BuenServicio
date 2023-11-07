import requests
from django.core.management import execute_from_command_line
if __name__ == '__main__':
    response = requests.get('https://raw.githubusercontent.com/GasparBianco/keys/main/keys.json')
    user = "Prueba"
    data = response.json()
    if user in data:
        if data[user]:
            from BuenServicio.wsgi import application 
            host = '0.0.0.0'
            port = 8000
            execute_from_command_line(['manage.py', 'runserver', f'{host}:{port}'])
        else: 
            print("Acceso denegado")
    else: 
        print("Usuario incorrecto")