
import json
from  registrarclientess import clientes 
from random import randint
from datetime import datetime
guias={}
envios=[]

def guardar_envios_json():
          
    with open("envios.json", "w", encoding="utf-8") as archivo:
        json.dump(envios, archivo, indent=4, ensure_ascii=False)
    print("\n envios guardados en clientes.json\n")

def cargar_envios_json():
    
    global envios
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            envios = json.load(archivo)
        print("\n envios cargados exitosamente.\n")
    except (FileNotFoundError):
     envios=[]   
     print("\n No hay datos previos\n")

def cargar_clientes_json():
    
    global clientes
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
        print("\n Clientes cargados exitosamente.\n")
    except (FileNotFoundError):
     clientes=[]   
     print("\n No hay datos previos\n")
        




documentosregistrados= set()
for cliente in clientes:
    documentosregistrados.add(cliente["Número de Documento"])

def registrar_envio():
 cargar_clientes_json()
 
 documentosregistrados= set()
 for cliente in clientes:
    documentosregistrados.add(cliente["Número de Documento"])

    
    print("DESTINARIO->")
    destinario={
            "Nombres":input("Nombres:"),
            "direccion": input("direccion: "),
            "telofono de contacto": input("telefono de contacto:"),
            "ciudad":input("Ciudad:"),
            "Barrio": input("Barrio:")
        }
    
    
    
    print("\n REMITENTE ->")
    numero_documento = input("# de documento del remitente: ").strip()

    

        
    
    if numero_documento in documentosregistrados:
        print("\nEnvío registrado con éxito.")
        guia= str(randint(10000, 99999))
        destinario["Guía"] = guia
        destinario["Fecha del envío"] = str(datetime.today().date())
        destinario["Hora del envío"] = datetime.now().strftime("%H:%M:%S")
        destinario["Estado"] = "Recibido"
        guias[guia]=destinario
        

        print("\n Envío registrado con éxito.")
        for clave, valor in destinario.items():
            print(f"{clave}: {valor}")
    else:
        print("\n El remitente no está registrado en la base de datos. Debe registrarse primero.")
    
    envios.append(destinario)
    guardar_envios_json()
    break

if __name__ == "__main__":
    registrar_envio()

