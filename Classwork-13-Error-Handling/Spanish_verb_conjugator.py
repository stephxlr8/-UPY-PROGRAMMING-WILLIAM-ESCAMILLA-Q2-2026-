## spanish verb conjugator

while True:

    pronouns= ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
    terminations= {
        'ar' : ['o','as','a','amos', 'ais','an'],
        'er' : ['o','es','e', 'emos','eis','en'],
        'ir' : ['o', 'es','e','imos','is','en']
    }

    vb = input('write a spanish verb: ')
    rz = vb[:-2]
    term = vb[-2:]

    list_terminations = terminations[term]

    for i in range (len(pronouns)):
        print(pronouns[i] + " " + rz + list_terminations[i])

