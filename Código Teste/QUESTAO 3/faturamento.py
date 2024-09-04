import json

with open("dados.json", encoding = 'utf-8') as dados_json:
    dados = json.load(dados_json)


faturamento = [dia['valor'] for dia in ['faturamento'] if dia['valor'] > 0]

menor_faturamento = min(dados)
maior_faturamento = max(dados)

media_faturamento = sum(dados) / len(dados)

dias_acima_da_media = sum(1 for valor in dados if valor > media_faturamento)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

