# Meta caracteres: ^ $ ( )
# () \1
# () () \1 \2
# (())() \1 \2 \3

import re
# from pprint import pprint

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase 3</p> <div>1</div>
"""

# cpf = '147.852.963-12'
# print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
# pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 \3 \4', texto))

# for tag in tags:
#     um, dois, tres = tag
#     print(tres)
