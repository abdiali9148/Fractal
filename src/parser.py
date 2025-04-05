from pathlib import Path

def cast_hash_map(fname):
    """
    Parses a mandelbrot data file into a dictionary
    returns a tuple of the form (DICT, FILENAME)
    """
    frac = {'fname': fname, 'name': Path(fname)}
    f = open(fname)
    for line in f:
        if line == '\n' or line.lstrip().startswith('#'):
            continue
        kv = line.replace(' ', '').rstrip().lower().split(":")
        if len(kv) != 2:
            error_msg = "Parse error at line #"
            raise RuntimeError(error_msg)
        key, value = kv
        if key == 'centerx':
            frac['centerX'] = float(value)
        if key == 'centery':
            frac['centerY'] = float(value)
        if key == 'axislength':
            frac['axisLen'] = float(value)
        if key == 'axislength':
            frac['axisLength'] = float(value)
        if key == "type" and value != "mandelbrot":
            frac['type'] = str(value)
        if key == 'preal':
            frac['preal'] = float(value)
        if key == 'creal':
            frac['creal'] = float(value)
        if key == 'pimag':
            frac['pimag'] = float(value)
        if key == 'cimag':
            frac['cimag'] = float(value)

    if 'centerX' not in frac:
        raise RuntimeError("A required parameter is missing")
    elif 'centerY' not in frac:
        raise RuntimeError("A required parameter is missing")
    elif frac['axisLen'] <= 0000.0000:
        raise ValueError("axisLen must be positive")
    elif 'axisLength' not in frac or frac['axisLength'] <= 0.0:
        raise ValueError("axisLength must be positive")
    return tuple([Path(fname).stem, frac])

