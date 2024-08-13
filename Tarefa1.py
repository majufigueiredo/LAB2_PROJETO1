 def cumprimento(nome):
    return "Olá, " + nome + "! Como vai você hoje?"
print(cumprimento("Maria Júlia Figueiredo"))

import random
def calcular_media_aleatoria():
   # Sorteia três números aleatórios entre 1 e 100
   num1 = random.randint(1, 100)
   num2 = random.randint(1, 100)
   num3 = random.randint(1, 100)
   # Calcula a média
   media = (num1 + num2 + num3) / 3
   return media
# Exemplo de uso da função
media = calcular_media_aleatoria()
print(f"A média dos números sorteados é: {media}")