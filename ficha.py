from itertools import count


def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    print(nombre.rstrip())
    print(nombre.lstrip())
    print(nombre.strip()    )

    print(frase.upper())
    print(frase.lower())
    print(frase.title())
    print(frase.find("gran"))
    print(frase.replace("programacion","desarrolo"))
    cant_a=frase.count("a")
    print(cant_a)
    python_frase="Python" in frase
    java_frase="java" in frase
    print(python_frase)
    print(java_frase)
    extraccion_python=frase[0:7]
    print(extraccion_python)
    print(extraccion_python[::2])
    print(extraccion_python[::-1])
    nombre_sin_espacios=nombre.strip()
    print(f"{nombre_sin_espacios} sabe {extraccion_python}")
    print(multilinea)

string_methods()
