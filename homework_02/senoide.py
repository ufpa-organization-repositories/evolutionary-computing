from math import sin, pi
from trabalho2.modules import to_binary, to_decimal

def calc_senoide(cromossomo):
    # x = float("%.6f" % cromossomo)
    # print(x)
    # senoide = x * sin(10*pi*x) + 1
    # print(senoide)

    # x_bin = to_binary(cromossomo)
    # print(x_bin)
    senoide = to_decimal(cromossomo) * sin(10*pi*to_decimal(cromossomo)) + 1
    print(senoide)

    return senoide