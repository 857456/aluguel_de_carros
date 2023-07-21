carros = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
# R$60 por dia
# R$0,15 por Km
valor = (carros * 60) + (Km * 0.15)
print('O total a pagar é de {:.2f}'.format(valor))