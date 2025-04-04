import json


clientes=[]
def guardar_clientes_json():
          
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)
    print("\n Datos guardados en clientes.json\n")
    

def cargar_clientes_json():
    
    global clientes
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
        print("\n Clientes cargados exitosamente.\n")
    except (FileNotFoundError):
     clientes=[]   
     print("\n No hay datos previos\n")
        





        
def registro_cliente():
    cargar_clientes_json()
    print("\nREGISTRO DE USUARIOS\nPor favor ingrese la siguiente información:\n") 

    cliente = {
        "Nombres": input("Nombres: ").strip().upper(),
        "Apellidos": input("Apellidos: ").strip().upper(),
        "Tipo de Documento": input("Tipo de documento (CC, TI, CE): ").strip().upper(),
        "Número de Documento": input("Número de identificación: ").strip(),
        "Dirección": input("Dirección: ").strip().upper(),
        "Teléfono Fijo": input("Teléfono fijo: ").strip(),
        "Número de Celular": input("Número de celular: ").strip(),
        "Barrio": input("Barrio de referencia: ").strip().upper()
    }
    
    
    clientes.append(cliente)
    guardar_clientes_json()
    
    print("\n Cliente registrado con éxito.\n")
    
   
    for clave, valor in cliente.items():
        print(f"{clave}: {valor}")
      
   
    


 
 
 
 
 
 
 
 
if __name__ == "__main__":
    
    
    registro_cliente()
