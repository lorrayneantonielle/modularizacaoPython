import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentando 10% no valor de {moeda.moeda(p)} fica {moeda.aumentar(p, 10, True)}.')
print(f'Diminuindo 13% no valor de {moeda.moeda(p)} fica {moeda.diminuir(p, 13, True)}.')