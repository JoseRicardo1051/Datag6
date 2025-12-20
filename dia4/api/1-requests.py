import requests

URL = 'https://randomuser.me/api/?results=2'

response = requests.get(URL)

if response.status_code == 200:
    print('conexión a api exitosa')
    data = response.json()
    for dic_user in data['results']:
        nombre = dic_user['name']['first'] + ' ' + dic_user['name']['last']
        pais = dic_user['location']['country']
        email = dic_user['email']
        telefono = dic_user['phone']
        foto = dic_user['picture']['large']
        print('****************************************')
        print(f'Nombre  : {nombre}')
        print(f'Pais    : {pais}')
        print(f'Email   : {email}')
        print(f'Telefono: {telefono}')
        print(f'Foto    : {foto}')
else:
    print(f'error : {response.status_code}')