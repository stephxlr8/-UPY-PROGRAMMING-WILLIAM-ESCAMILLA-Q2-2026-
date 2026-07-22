## spanish verb conjugator

pronouns = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']
terminations = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

vb = input('write a spanish verb: ')

# Reglas de negocio: Python no las detecta solo
if vb != vb.strip():
    print('El verbo no debe tener espacios extra')
    raise SystemExit(1)

if vb != vb.lower():
    print('El verbo debe escribirse en minúsculas')
    raise SystemExit(1)

rz = vb[:-2]
term = vb[-2:]

try:
    list_terminations = terminations[term]
except KeyError:
    print('El verbo debe terminar en ar, er o ir')
    raise SystemExit(1)

for i in range(len(pronouns)):
    print(pronouns[i] + " " + rz + list_terminations[i])
