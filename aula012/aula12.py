import re


texto = '''
(21) 9 8852-5214
(11) 9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''
regex = re.compile(r'^((\(\d{2}\)\s*)(9\s*)(\d{4}-\d{4}))$', flags=re.M)

for telefone in regex.findall(texto):
    telefone_completo, ddd, _, numero = telefone
    print(telefone_completo)
