# -- Bloco de cores --
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

# -- Design inicial do terminal --
print(BOLD + CYAN + "=" * 70 + RESET)
print(BOLD + CYAN + " SEJA BEM VINDO(A) A CALCULADORA DE LUCRO OU PREJUIZO ".center(70) + RESET)
print(BOLD + CYAN + "=" * 70 + RESET)
print(
    "Como usar? Basta preencher, quando solicitado, o valor pago no carro, o gasto com manutenção e por quanto ele foi vendido!"
)
print("-" * 70)

# -- Bloco de declaração de variaveis mutáveis --
repeticao = int(input("Digite quantas vezes você deseja que o programa se repita: "))
quantidade_de_carros_prejuizo = 0
quantidade_de_carros_lucro = 0
zero_a_zero = 0
soma_lucro = 0
soma_prejuizo = 0

# -- Inicio da lógica --
for i in range(repeticao):
    print("\n" + "-" * 70)
    print(BOLD + f"Entrada {i + 1} de {repeticao}" + RESET)
    preco_pago = float(input("Digite o valor total pago no carro: R$ "))
    preco_manutencao = float(input("Digite o valor total gasto em manutenções: R$ "))
    preco_vendido = float(input("Digite o valor total que o carro foi vendido: R$ "))

    preco_total_gasto = preco_pago + preco_manutencao
    renda_total = preco_vendido - preco_total_gasto

    # -- Bloco de lógica para quantidade de carros em prejuizo/lucro --
    if renda_total < 0:
        print(RED + f"Vish esse carro deu um prejuizo de: R${renda_total:.2f}" + RESET)
        quantidade_de_carros_prejuizo += 1
        soma_prejuizo += renda_total
    elif renda_total > 0:
        print(GREEN + f"Esse carro deu bom, o lucro foi de: {renda_total:.2f}" + RESET)
        quantidade_de_carros_lucro += 1
        soma_lucro += renda_total
    else:
        print(YELLOW + "Esse carro não deu lucro nem prejuizo!" + RESET)
        zero_a_zero += 1


# -- Calculo da média evitando divisão por 0 --
if quantidade_de_carros_lucro > 0:
    media_total_lucro = soma_lucro / quantidade_de_carros_lucro
else:
    media_total_lucro = 0.0

if quantidade_de_carros_prejuizo > 0:
    media_total_prejuizo = soma_prejuizo / quantidade_de_carros_prejuizo
else:
    media_total_prejuizo = 0.0


# -- Bloco para mostrar os resultados -- 
print("\n" + BOLD + CYAN + "=" * 70 + RESET)
print(BOLD + "RESUMO".center(70) + RESET)
print(BOLD + CYAN + "=" * 70 + RESET)
print(f"Foram enviados {repeticao} carros para a calculadora!")
print(GREEN + f"Você teve {quantidade_de_carros_lucro} carros que deram lucro!")
print(RED + f"Você teve {quantidade_de_carros_prejuizo} carros que deram prejuízo!")
print(RESET + f"Você teve {zero_a_zero} carros que não deram lucro e nem prejuízo!")
print(GREEN + f"Você teve uma média de lucro de R$ {media_total_lucro:.2f}!")
print(RED + f"Você teve uma média de prejuízo de R$ {media_total_prejuizo:.2f}!")
print(BOLD + CYAN + "=" * 70 + RESET)
