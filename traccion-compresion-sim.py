import math

#PROBETA
D = float(input("Ø (mm)= "))
Lo = float(input("Lo (mm)= "))
F = float(input("F (N)= "))

#MATERIAL
E = float(input("Módulo de Young (GPa) "))
T_e = float(input("Límite elástico (MPa) "))
T_r = float(input("Límite de rotura (MPa) "))

if T_r <= T_e:
    print("--------")
    print(f"EL LÍMITE DE ROTURA NO PUEDE SER MENOR AL LÍMITE ELÁSTICO")
    print("--------")

else:
    #CALCULOS
    def calcular_probeta(D, Lo, F, E):
        S = math.pi * D ** 2 /4
        T = F / S
        e = T / E / 1000
        delta = e * Lo
        k = E * 1000 * S / Lo
        return S, T, e, delta, k

    S, T, e, delta, k = calcular_probeta(D, Lo, F, E)

    print("--------")

    print(f"S = {S} mm^2")
    print(f"Tensión = {T} MPa")
    print(f"Deformación = {e}")
    print(f"Alargamiento ZZ max = {delta} mm")
    print(f"Rigidez de la barra = {k} N/mm")

    if T < T_e:
        print(f"--TRABAJA DENTRO DE ZONA ELÁSTICA--")
    else:
        print(f"--TRABAJA FUERA DE ZONA ELÁSTICA--")
