# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline
# re.S -> Dotall

import re

texto = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))