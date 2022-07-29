# Meta caracteres: ^ $ ( )
# * 0 o n
# + 1 ou n
# ? 0 ou 1

import re

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase 3</p> <div></div>
"""

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto, flags=re.I))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto, flags=re.I))
