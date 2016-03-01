import re

s = r'ABC\-001'

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

