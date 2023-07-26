import re

pattern = re.compile(r"\D")
_string = input("Enter string:\n")

result = pattern.sub('_', _string)

print(result)