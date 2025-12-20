import requests

API_URL = 'https://apiperu.dev/api/ruc'
TOKEN = 'tutoken'
data_request = {
  "ruc":"20117592899"
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL,json=data_request,headers=headers)

if response.status_code == 200:
    data = response.json()['data']
    print("="*50)
    print(f'RUC : {data['ruc']}')
    print(f'Razon Social : {data["nombre_o_razon_social"]}')
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')