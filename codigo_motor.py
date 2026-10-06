from wegnologyrest import Client
import time
import random

DEVICE_ID = "6ac54fc02d90ac6fdceef666"
APP_KEY = "4b94f92a-0a29-4504-b192-03af4e3e5278"
APP_SECRET = "eee191067a3ac5fbcc3c2f13849d3a8b336124c7a8ba9589d9c341ced05210f7"

creds = {
    'deviceId': DEVICE_ID,
    'key': APP_KEY,
    'secret': APP_SECRET
}

client = Client()

auth_response = client.auth.authenticate_device(credentials=creds)
client.auth_token = auth_response['token']
APP_ID = auth_response['applicationId']
print("Autenticado com sucesso!")


def ler_sensores_motor():
    return {
        "pressao": round(random.uniform(2.0, 8.0), 2),
        "torque": round(random.uniform(50, 200), 2),
        "temperatura": round(random.uniform(60, 110), 2)
    }


def enviar_dados_motor():
    dados = ler_sensores_motor()
    try:
        state = {'data': dados}
        client.device.send_state(
            deviceId=DEVICE_ID,
            applicationId=APP_ID,
            deviceState=state
        )
        print(f"[OK] Enviado -> Pressão: {dados['pressao']} bar | "
              f"Torque: {dados['torque']} N.m | "
              f"Temperatura: {dados['temperatura']} °C")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar: {e}")


if __name__ == "__main__":
    print("Iniciando monitoramento simulado do motor...")
    while True:
        enviar_dados_motor()
        time.sleep(5)