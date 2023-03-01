def shape4d(a, data_format='NHWC'):
    """
    Ensuer a 4D shape, to use with 4D symbolic functions.

    Args:
        a: a int or tuple/list of length 2

    Returns:
        list: of length 4. if ``a`` is a int, return ``[1, a, a, 1]``
            or ``[1, 1, a, a]`` depending on data_format.
    """
    s2d = shape2d(a)
    if get_data_format(data_format, False) == 'NHWC':
        return [1] + s2d + [1]
    else:
        return [1, 1] + s2d