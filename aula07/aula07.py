# \w -> [a-zA-Z0-9À-ú]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [\r\n\f\n\t]
# \S -> [^\r\n\f\n\t]
# \b -> borda
# \B -> não borda


import re

texto = """
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos aualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooooãoooooo, o café ta prontinho aqui. Veeeem"!
"""
# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\be\w+', texto, flags=re.I))
# print(re.findall(r'\w+e\b', texto, flags=re.I))
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
