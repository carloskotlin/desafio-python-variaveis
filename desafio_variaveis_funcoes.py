# UNISUAM - Desafio de Código: Variáveis e Funções
# Desenvolvedor: Carlos Aguiar

def ler_numeros():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))
    return n1, n2, n3

def calcular_soma(numeros):
    return sum(numeros)

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def main():
    numeros = ler_numeros()
    print(f"Números lidos: {numeros}")
    print(f"Soma: {calcular_soma(numeros)}")
    print(f"Média: {calcular_media(numeros)}")

if __name__ == "__main__":
    main()
