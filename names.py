def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre=input("ingrese nombre:")
    apellido=input("ingrese apellido:")
    nombre_completo=nombre+"  "+apellido
    print(nombre_completo.lower())          #todo minusculas
    print(nombre_completo.title())          #con mayusculas al inicio
    print(nombre_completo.upper())          #todo mayusculas
    print(f"\t{nombre_completo}".lower())   #con tabulacion

names()
