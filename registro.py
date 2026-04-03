# Abrimos el archivo en modo 'a' (append) para no borrar lo anterior
file = open("equipos.txt", "a")

print("--- Registro de Routers ---")
while True:
    nuevo_router = input("Ingresa el nombre del router (o 'salir' para terminar): ")
    
    if nuevo_router.lower() == "salir":
        print("Registro finalizado.")
        break
    
    file.write(nuevo_router + "\n")
    print(f"Router {nuevo_router} guardado.")

file.close()
