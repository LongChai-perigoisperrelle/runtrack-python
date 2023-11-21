def est_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "rectangle isocèle"
        else:
            return "isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "rectangle"
    else:
        return "quelconque"


a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))


if est_triangle(a, b, c):
    
    type_tri = type_triangle(a, b, c)
    print(f"Les longueurs {a}, {b}, {c} forment un triangle de type {type_tri}.")
else:
    print("Les longueurs ne permettent pas de former un triangle.")
