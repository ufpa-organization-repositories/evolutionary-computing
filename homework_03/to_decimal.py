PRECISION_BINARY = 25
import math

def to_decimal(number_bin):
    def to_dec_virg(number):
        sum_n = 0
        for ind, value in enumerate(number):
            sum_n += int(value) * math.pow(2, -1 * (ind + 1))
        return sum_n

    split = str(number_bin).split('.')

    integer = int(split[0], 2)

    if len(split) == 1:
        return integer

    elif len(split) == 2:
        floating = to_dec_virg(split[1])
        result = integer + floating
        return result

    else:
        pass
        raise Exception('Numero binario com mais de uma virgula')

# a = to_decimal('101')
# b = to_decimal('-101')
#
# print(a, b)