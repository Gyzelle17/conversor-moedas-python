
# conversor_moedas.py

# Taxas fixas de câmbio (exemplos fictícios)
TAXA_DOLAR = 5.00  # 1 dólar = 5 reais
TAXA_EURO = 6.00   # 1 euro = 6 reais

print("Bem-vindo ao Conversor de Moedas!")
valor_reais = float(input("Digite o valor em reais (BRL) que deseja converter: "))

valor_em_dolar = valor_reais / TAXA_DOLAR
valor_em_euro = valor_reais / TAXA_EURO

print(f"\nO valor em dólares (USD) é: ${valor_em_dolar:.2f}")
print(f"O valor em euros (EUR) é: €{valor_em_euro:.2f}")
