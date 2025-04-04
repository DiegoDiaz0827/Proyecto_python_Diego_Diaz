from registrarclientess import clientes
import json  # Asegúrate de importar el módulo json

def cargar_clientes_json():
    global clientes
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
        print("\nClientes cargados exitosamente.\n")
    except FileNotFoundError:
        clientes = []  # Si no se encuentra el archivo, inicializa una lista vacía
        print("\nNo hay datos previos.\n")

def guardar_clientes_json():
    # Guarda los clientes actualizados en el archivo JSON
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)
    print("\nDatos actualizados en clientes.json\n")


def actualizar_clientes():
    cargar_clientes_json()  # Carga los datos antes de hacer cualquier operación

    if not clientes:  # Verifica si la lista de clientes está vacía
        print("\nNo hay clientes registrados.\n")
        return

    print("\nActualización de cliente")
    num_documento = input("Ingrese su número de identificación: ").strip()

    cliente = None
    for c in clientes:
        if c["Número de Documento"] == num_documento:
            cliente = c
            break

    if not cliente:
        print("\nNúmero de identificación inválido. Cliente no encontrado.\n")
        return

    print("\nIngrese los nuevos datos:\n")
    cliente["Nombres"] = input(f"Nombres ({cliente['Nombres']}): ").strip().upper() 
    cliente["Apellidos"] = input(f"Apellidos ({cliente['Apellidos']}): ").strip().upper() 
    cliente["Tipo de Documento"] = input(f"Tipo de documento ({cliente['Tipo de Documento']}): ").strip().upper() 
    cliente["Dirección"] = input(f"Dirección ({cliente['Dirección']}): ").strip().upper() 
    cliente["Teléfono Fijo"] = input(f"Teléfono fijo ({cliente['Teléfono Fijo']}): ").strip() 
    cliente["Número de Celular"] = input(f"Número de celular ({cliente['Número de Celular']}): ").strip() 
    cliente["Barrio"] = input(f"Barrio ({cliente['Barrio']}): ").strip().upper() 

    # Muestra los datos actualizados
    print("\nCliente actualizado con éxito:")
    for clave, valor in cliente.items():
        print(f"{clave}: {valor}")
        
    guardar_clientes_json()

if __name__ == "__main__":  # Asegúrate de tener doble guión bajo en __main__
    actualizar_clientes()