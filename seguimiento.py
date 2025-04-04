from registrarenvioss import guias
import random
estados= ["Recibido", "En Transito", "En Ciudad Destino", 
                 "En Bodega De La Transportadora", "En Reparto"]

def seguimiento():
    print("\n SEGUIMIENTO DE PAQUETES ")
    
    paquete = input("Ingrese el número de guía del paquete: ").strip()  

    if paquete in guias:
        print("\n Información del paquete:")
        
       
        orden_claves = ["Guía", "Fecha del envío", "Hora del envío", "Estado", 
                        "Nombres", "Dirección", "Teléfono de contacto", "Ciudad", "Barrio"]

        for clave in orden_claves:
            if clave in guias[paquete]: 
                if clave == "Estado":  
                    
                    guias[paquete][clave] = random.choice(estados)   
                print(f"{clave}: {guias[paquete][clave]}")
    else:
        print("\n No se encontró ningún paquete con esa guía.")

if __name__ == "__main__":
    seguimiento()