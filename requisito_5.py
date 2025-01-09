nova_string = input("Digite uma string para ser invertida: ")

string_invertida = ""

for i in range(len(nova_string) - 1, -1, -1):
    string_invertida += nova_string[i]

print(f"String invertida: {string_invertida}")
