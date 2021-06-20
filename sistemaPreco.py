import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {moeda.m(p)}.')
print(f'O dobro de {p} É {moeda.a(p)}.')
print(f'Aumentando 10%, temos {moeda.a(p, 10)}.')
print(f'Aumentando 13%, temos {moeda.a(p, 13)}.')