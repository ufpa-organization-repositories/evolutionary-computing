PRECISION_BINARY = 25
import math
def to_binary(number_dec):
    def to_bin_virg(number_dec):
        list_bin = []
        # number = float('0.' + number_dec)
        number = float("%.5f" % (float('0.' + number_dec)))
        for i in range(PRECISION_BINARY - 2):  # para deixar dois caracteres para o primeiro bit e o '.'
            number *= 2
            if number != 1:
                int_bin = int(number)
                list_bin.append(str(int_bin))
                number -= int_bin
            else:
                list_bin.append(str(int(number)))
                break
        return ''.join(list_bin)

    dec_split = str(number_dec).split('.')
    integer = bin(int(float("%.5f" %float(dec_split[0])))).replace('0b', '')
    if len(dec_split) == 1:  # possui apenas a parte inteira
        return integer
    elif len(dec_split) == 2:  # possui a parte inteira e a parte real
        floating = to_bin_virg(dec_split[1])
        result = integer + '.' + floating
        return result
    else:  # possui numero errado de virgulas para representar o numero
        raise Exception('Numero Decimal com mais de uma virgula')

# a = to_binary(-5)
# b = to_binary(5)
#
# print(a, b)


