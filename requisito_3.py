import json

arquivo_json = "dados.json"
with open(arquivo_json, "r") as file:
    dados = json.load(file)

faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
