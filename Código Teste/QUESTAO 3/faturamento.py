import json

fat={
    "faturamento": "100, 200, 0, 150, 300, 250, 0, 180, 220, 280, 200, 150, 0, 175, 225, 275, 250, 300, 0, 200, 150, 250, 275, 225, 0, 190, 210"
}

object_json = json.dumps(fat, indent=2)

with open("simples.json", "w") as file:
    file.write(object_json)

faturamento = [dia['valor'] for dia in ['faturamento'] if dia['valor'] > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

media_faturamento = sum(faturamento) / len(faturamento)

dias_acima_da_media = sum(1 for valor in faturamento if valor > media_faturamento)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

