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
    di = n - (n * porcentagem / 100)
    return di if formato is False else moeda(di)


def dobro(n=0,formato=False):
    do = n * 2
    return do if not formato else moeda(do)


def metade(n=0,formato=False):
    m = n / 2
    return m if not formato else moeda(m)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>8.2f}'.replace('.',',')
