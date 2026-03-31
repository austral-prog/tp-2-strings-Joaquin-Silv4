def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre=input("ingrese nombre:").lower()
    tiene_a="a" in nombre
    tiene_e="e" in nombre
    tiene_i="i" in nombre
    tiene_o="o" in nombre
    tiene_u="u" in nombre

    print(f"¿Tiene 'a'?: {tiene_a}")
    print(f"¿Tiene 'e'?: {tiene_e}")
    print(f"¿Tiene 'i'?: {tiene_i}")
    print(f"¿Tiene 'o'?: {tiene_o}")
    print(f"¿Tiene 'u'?: {tiene_u}")

check_vowels()
