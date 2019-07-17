import re 

print("Greedy:")
match = re.findall(r'(<.*>)', '<em>Strong</em> <i>Italic</i>')
for i in match:
    print(i)

print("Non-Greedy:")
match = re.findall(r'(<.*?>)', '<em>Strong</em> <i>Italic</i>')
for i in match:
    print(i)
