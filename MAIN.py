from registrarclientess import registro_cliente  
from registrarenvioss import registrar_envio,guardar_envios_json,cargar_envios_json
from seguimiento import seguimiento
from actualizarclientes import actualizar_clientes
def empresa():
    while True:
        print("\nCOMPAÑÍA DE EMPRESAS Y VIAJES")
        print('''
        Bienvenido usuario\n
        Menú de opciones:
        1. Registrar cliente
        2. actualizar datos
        3. registrar envio
        4. seguimiento de paquetes
        5. salir del programa
        ''')

        
        accion = int(input("¿Qué acción deseas realizar? : "))
        if accion < 1 or accion > 5:
         print("Opción inválida, intenta nuevamente.")
         continue  

        if accion == 1:
         registro_cliente()

        if accion == 2:
          actualizar_clientes() 
        if accion ==3:
         
         registrar_envio()
         
        if accion==4:
         seguimiento()
        if accion==5:
         print("saliendo del programa....")
         break
             
            
empresa()         