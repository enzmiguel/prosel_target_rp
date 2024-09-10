def conta_letras_a(string):
    contador = 0  # inicia o contador em 0
    for char in string:  # percorre cada caractere na string
        if char.lower() == 'a':  # verifica se o caractere, em minúsculo, é 'a' (se for maiúsculo, é convertido para minúsculo antes da verificação)
            contador += 1  # incrementa o contador se for 'a'
    return contador  # retorna o total de 'a'

# teste
string_teste = "Aprendizado Acadêmico"
ocorrencias = conta_letras_a(string_teste)
print(f"A letra 'a' ocorre {ocorrencias} vezes na string.")
