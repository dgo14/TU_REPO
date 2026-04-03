file = open("equipos.txt", "a")

print("--- SISTEMA DE INVENTARIO DEVASC ---")

while True:
    nombre = input("Nombre del dispositivo (o 'salir'): ")
    if nombre.lower() == "salir":
        break
        
    ip = input(f"Ingrese la IP para {nombre}: ")
    
    # Creamos una línea con formato profesional
    linea = f"Dispositivo: {nombre} | IP: {ip} | Estado: Activo\n"
    
    file.write(linea)
    print(">>> Datos guardados localmente.\n")

file.close()
print("Proceso finalizado. No olvides subir tus cambios a GitHub.")
