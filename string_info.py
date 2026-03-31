def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

    print(palabra[:])

    longitud=len(palabra)
    print(longitud)

    print(palabra[0])

    print(palabra[-1])

    print(palabra[:]*3)

    print(f"***{palabra}***")


string_info()
