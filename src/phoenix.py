from palettes import grad


def phoenix_color_palette(z, fc):
    # c = complex(0.5667, 0.0)
    c = complex(fc['creal'], fc['cimag'])
    # phoenix = complex(-0.5, 0.0)
    phoenix = complex(fc['preal'], fc['pimag'])
    zPrev = 0+0j
    for i in range(102):
        zSave = z
        z = z * z + c + (phoenix * zPrev)
        zPrev = zSave
        if abs(z) > 2:
            return grad[i]
    return grad[101]


def fractal_config(d, n):

    if n in d:
        return d[n]
    else:
        return None