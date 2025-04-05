MAX_ITERATIONS = 115

def compute_iteration(c, escape_radius=2):
    z = 0 + 0j
    for iteration in range(MAX_ITERATIONS):
        z = z * z + c
        if abs(z) > escape_radius:
            return iteration
    return MAX_ITERATIONS - 1


def mbrot_color_palette(c, palette, escape_radius=2):
    z = 0 + 0j
    num_colors = len(palette)
    for iteration in range(num_colors):
        z = z * z + c
        if abs(z) > escape_radius:
            return palette[iteration]
    return palette[-1]


def pixel_color(c, palette, escape_radius=2):
    if palette is not None:
        return mbrot_color_palette(c, palette, escape_radius)
    else:
        return compute_iteration(c, escape_radius)