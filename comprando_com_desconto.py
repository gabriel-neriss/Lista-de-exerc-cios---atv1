# desconto fixo de 10%
# + 1% a cada unidade comprada
# ENTRADAS-  indicando o preço da mercadoria - FLOAT
# ENTRADAS- quantidade de mercadoria comprada - INT
# exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.
#  loja nunca vende mais do que 40 unidades

# Saída -  preço da compra sem o desconto - float
# Saída -  preço final com o desconto aplicado - float

preco_mercadoria = float(input('Qual é o preço da mercadoria? R$'))
qtd_comprada = int(input('Qual é a quantidade da mercadoria?'))

preco_total = preco_mercadoria * qtd_comprada

preco_com_desconto = preco_total - (preco_total * 10/100) - (preco_total * qtd_comprada / 100)

preco_com_desconto_total = preco_com_desconto


print('{:.2f}'.format(preco_total))
print( '{:.2f}'.format(preco_com_desconto_total))
                                    


