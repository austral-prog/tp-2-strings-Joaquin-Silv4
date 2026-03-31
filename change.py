def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    dinero_gastado=float(input("ingresar gasto:"))
    dinero_recibido=float(input("ingresar dinero recibido:"))
    vuelto_total=dinero_recibido-dinero_gastado
    pesos_parte_entera=int(vuelto_total)
    centvos=vuelto_total%1

    print(vuelto_total)
    print(pesos_parte_entera)
    print(centvos)


change()
