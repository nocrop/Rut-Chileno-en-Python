from itertools import cycle

def validar_rut(rut):
    rut = rut.upper().replace("-", "").replace(".", "")
    rut_aux = rut[:-1]
    dv = rut[-1:]

    if not rut_aux.isdigit() or not (1_000_000 <= int(rut_aux) <= 25_000_000):
        return False

    revertido = map(int, reversed(rut_aux))
    factors = cycle(range(2, 8))
    suma = sum(d * f for d, f in zip(revertido, factors))
    residuo = suma % 11

    if dv == 'K':
        return residuo == 1
    if dv == '0':
        return residuo == 11
    return residuo == 11 - int(dv)

def main():
    rut_usuario = input("Ingrese un RUT para validar: ")
    if validar_rut(rut_usuario):
        print("El RUT ingresado es válido.")
    else:
        print("El RUT ingresado es inválido.")

if __name__ == "__main__":
    main()
