valores = input("Digite a quantidade de hot dog's consumidos no evento e a qtd de participantes: ").split()
valores_int = [int(v) for v in valores]
H, P = valores_int

media = H / P
print("A média de consumo no evento foi de {:.2f}".format(media))


# Resposta que passou no desafio:
"""valores = input().split()
valores_int = [int(v) for v in valores]
H = valores_int[0]
P = valores_int[1]

media = H / P
print("{:.2f}".format(media))"""
 