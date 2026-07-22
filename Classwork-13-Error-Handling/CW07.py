rol = input("Ingrese rol sin digito verificador: ")

if not rol.isdigit():
    print("Error: el rol debe contener solo dígitos")
    raise SystemExit(1)

suma = 0
multiplicador = 2

for digito in reversed(rol):
    suma += int(digito) * multiplicador
    multiplicador += 1

    if multiplicador > 7:
        multiplicador = 2

resto = suma % 11
digito_verificador = 11 - resto

print(f"{rol}-{digito_verificador}")
