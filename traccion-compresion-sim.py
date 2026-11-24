import math

n_mats = 1

while n_mats < 5:
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
        print("EL LÍMITE DE ROTURA NO PUEDE SER MENOR AL LÍMITE ELÁSTICO")
        print("--------")

    elif D <= 0:
        print("--------")
        print("EL DIÁMETRO NO PUEDE SER MENOR O IGUAL A 0")
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
        print(f"Tensión = {abs(T)} MPa")
        print(f"Deformación = {e}")
        print(f"Alargamiento ZZ max = {delta} mm")
        print(f"Rigidez de la barra = {k} N/mm")
        n_mats += 1

        if T < T_e:
            print("--TRABAJA DENTRO DE ZONA ELÁSTICA--")
            print("--------")
        else:
            print("--TRABAJA FUERA DE ZONA ELÁSTICA--")
            print("--------")
