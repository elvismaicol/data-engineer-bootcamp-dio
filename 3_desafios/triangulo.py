lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
    #TODO Preencha a formula do perímeto do triangulo (soma de todos os lados).
    p_triangulo = a + b + c
    print(f"Perimetro = { p_triangulo :.1f}")
else:
    #TODO Preencha a formula da área do trapézio: AREA = ((A + B) x C) / 2
    a_trapezio = ((a + b) * c) / 2
    print(f"Area = {a_trapezio :.1f}")