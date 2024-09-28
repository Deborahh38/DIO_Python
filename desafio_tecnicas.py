def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    entrada = input("Insira as vendas mensais (12 valores separados por vírgula): ")
    vendas = list(map(int, entrada.split(',')))
    return vendas

def calcular_indicadores(vendas):
    total_vendas = sum(vendas)
    media_mensal = total_vendas / len(vendas)
    return total_vendas, media_mensal

vendas = obter_entrada_vendas()
total, media = calcular_indicadores(vendas)
print(f"{total} {media:.2f}")
