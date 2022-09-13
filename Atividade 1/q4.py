import math

def truncate(number, decimal_places):
    aux = str(number).split('.')
    return float(aux[0] + '.'+  aux[1][:decimal_places])


def round_number(number, decimal_places):
    return round(number, decimal_places)

print(truncate(3.14159265358979, 3))
print(round_number(3.14159265358979, 3))