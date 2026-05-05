def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio_texto = input()
    descuento_texto = input()
    cantidad_texto = input()
    precio=float(precio_texto)
    cantidad = float(cantidad_texto)
    descuento=float(descuento_texto)
    precio_final_sin_descuento=precio*cantidad
    precio_final_descuento=(precio*cantidad)*(1-descuento/100)
    print(f"el total con descuento es:{precio_final_descuento}")
    print(f"el total sin descuento es:{precio_final_sin_descuento}")

casting()
