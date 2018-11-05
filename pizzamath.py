from math import pi, pow
def pizza_math(dia, price, *half):
    surface = round(pi * pow(dia / 2, 2), 2)
    cm2_price = round(surface / price, 2)

    if 'checked' in half:
        return surface / 2, cm2_price, True
    else:
        return surface, cm2_price, False