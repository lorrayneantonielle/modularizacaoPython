def aumentar(n=0, porcentagem=0, formato=False):
    """
    -> Função aumentar
    :param n: Número a ser calculado
    :param porcentagem: Porcentagem que o número vai sofrer à mais
    :param formato: Define se existe formatação para o resultado ou não. Padrão é False
    :return: Retorna o valor total do preço + a porcentagem aumentada
    """
    a = n * porcentagem / 100 + n
    return a if formato is False else moeda(a)


def diminuir(n=0, porcentagem=0,formato=False):
    """
    -> Função diminuir
    :param n: Número a ser calculado
    :param porcentagem: Porcentagem que o número vai sofrer à menos
    :param formato: Define se existe formatação para o resultado ou não. Padrão é False
    :return: Retorna o valor total do preço + a porcentagem de desconto
    """
    di = n - (n * porcentagem / 100)
    return di if formato is False else moeda(di)


def dobro(n=0,formato=False):
    """
    -> Função dobro
    :param n: Número a ser calculado
    :param formato: Define se existe formatação para o resultado ou não. Padrão é False
    :return: Retorna o valor total do dobro do preço
    """
    do = n * 2
    return do if not formato else moeda(do)


def metade(n=0,formato=False):
    """
    -> Função metade
    :param n: Número a ser calculado
    :param formato: Define se existe formatação para o resultado ou não. Padrão é False
    :return: Retorna o valor total da metade do preço
    """
    m = n / 2
    return m if not formato else moeda(m)


def moeda(n = 0, moeda = 'R$'):
    """
    -> Função moeda
    :param n: Número a ser calculado
    :param moeda: Define o valor atribuído
    :return: Retorna a formtação escolhida para a moeda brasileira (R$)
    """
    return f'{moeda}{n:>8.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10,taxar=5):
    """
    -> Função resumo - Define o resumo do código principal
    :param preço: Preço é o valor definido pelo usuário
    :param taxaa: taxa de aumento do preço em %
    :param taxar: taxa de redução do preço em $
    :return: Função sem retorno
    """
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço:\t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento:\t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução:\t{diminuir(preço, taxar, True)}')
    print('=' * 30)