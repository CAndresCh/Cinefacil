# Precio por entrada
PRECIO_ENTRADA = 35.00

# Lista de funciones predefinidas
funciones_disponibles = [
    {"pelicula": "Oppenheimer", "hora": "18:00"},
    {"pelicula": "Los 4 fantasticos", "hora": "15:30"},
    {"pelicula": "Spider Man", "hora": "20:00"}
]

# Lista para almacenar las reservas
reservas = []

def mostrar_funciones():
    print("\nFunciones disponibles:")
    for i, funcion in enumerate(funciones_disponibles, 1):
        print(f"{i}. {funcion['pelicula']} - {funcion['hora']}")

def hacer_reserva():
    nombre = input("Nombre del cliente: ").strip()
    mostrar_funciones()
    opcion = int(input("Selecciona el número de la función: ")) - 1

    if opcion < 0 or opcion >= len(funciones_disponibles):
        print("Opción inválida.")
        return

    pelicula = funciones_disponibles[opcion]["pelicula"]
    hora = funciones_disponibles[opcion]["hora"]
    cantidad = int(input("Cantidad de boletos: "))

    total = cantidad * PRECIO_ENTRADA

    reserva = {
        "cliente": nombre,
        "pelicula": pelicula,
        "hora": hora,
        "boletos": cantidad,
        "total": total
    }

    reservas.append(reserva)

    print("\nRESERVA EXITOSA ")
    print(f"Cliente: {nombre}")
    print(f"Película: {pelicula}")
    print(f"Hora: {hora}")
    print(f"Boletos: {cantidad}")
    print(f"Total a pagar: Q{total:.2f}")

def mostrar_reservas():
    if not reservas:
        print("\nNo hay reservas registradas.")
        return
    print("\n--- TODAS LAS RESERVAS ---")
    for i, r in enumerate(reservas, 1):
        print(f"\nReserva #{i}")
        print(f"Cliente: {r['cliente']}")
        print(f"Película: {r['pelicula']} ({r['hora']})")
        print(f"Boletos: {r['boletos']} - Total: Q{r['total']:.2f}")

def cancelar_reserva():
    nombre = input("Ingrese el nombre del cliente para cancelar la reserva: ").strip()

    nuevas_reservas = [r for r in reservas if r["cliente"].lower() != nombre.lower()]

    if len(nuevas_reservas) < len(reservas):
        for i in range(len(reservas) - 1, -1, -1):
            if reservas[i]["cliente"].lower() == nombre.lower():
                del reservas[i]
        print("Reserva cancelada exitosamente.")
    else:
        print("No se encontró una reserva con ese nombre.")


def menu():
    while True:
        print("\nSistema CineFácil")
        print("1. Hacer una reserva")
        print("2. Mostrar funciones disponibles")
        print("3. Mostrar todas las reservas")
        print("4. Cancelar una reserva")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            hacer_reserva()
        elif opcion == "2":
            mostrar_funciones()
        elif opcion == "3":
            mostrar_reservas()
        elif opcion == "4":
            cancelar_reserva()
        elif opcion == "5":
            print("Gracias por usar CineFácil.")
            break
        else:
            print("Opción inválida.")

# Ejecutar el sistema directamente
menu()