def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    print("="*24)
    nombre_sucio=input("ingrese nombre completo:")
    mail_sucio=input("ingrese mail:")

    nota1=float(input("ingrese nota:"))
    nota2=float(input("ingrese nota:"))
    nota3=float(input("ingrese nota:"))
    print(nota1)
    print(nota2)
    print(nota3)
    suma=nota1+nota2+nota3
    print(suma)
    promedio=(nota1+nota2+nota3)/3
    print(promedio)
    promedio_entero=int(promedio)
    print(promedio_entero)

    nombre_limpio=nombre_sucio.strip().title()
    print(len(nombre_limpio)) #cant de caracteres
    espacio_nombre=nombre_limpio.find(" ")
    iniciales=nombre_limpio[0]+nombre_limpio[espacio_nombre+1]
    print(iniciales)
    apellido_minusculas=nombre_limpio[espacio_nombre+1:].lower()
    nombre_minusculas=nombre_limpio[0:espacio_nombre].lower()
    usuario_con_guion=f"{nombre_minusculas}_{apellido_minusculas}".title()
    print(usuario_con_guion)
    print(nombre_limpio.count("a"))

    mail_limpio=mail_sucio.lower
    print(mail_limpio)
    valor_at=mail_sucio.find("@")
    dom_mail=[valor_at+1]
    print(dom_mail)

    print("="*24)


ficha()
