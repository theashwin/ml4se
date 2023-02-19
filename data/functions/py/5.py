def _concat_compat(to_concat, axis=0):
    """
    provide concatenation of an array of arrays each of which is a single
    'normalized' dtypes (in that for example, if it's object, then it is a
    non-datetimelike and provide a combined dtype for the resulting array that
    preserves the overall dtype if possible)

    Parameters
    ----------
    to_concat : array of arrays
    axis : axis to provide concatenation

    Returns
    -------
    a single array, preserving the combined dtypes
    """

    # filter empty arrays
    # 1-d dtypes always are included here
    def is_nonempty(x):
        try:
            return x.shape[axis] > 0
        except Exception:
            return True

    # If all arrays are empty, there's nothing to convert, just short-cut to
    # the concatenation, #3121.
    #
    # Creating an empty array directly is tempting, but the winnings would be
    # marginal given that it would still require shape & dtype calculation and
    # np.concatenate which has them both implemented is compiled.

    typs = get_dtype_kinds(to_concat)
    _contains_datetime = any(typ.startswith('datetime') for typ in typs)
    _contains_period = any(typ.startswith('period') for typ in typs)

    if 'category' in typs:
        # this must be priort to _concat_datetime,
        # to support Categorical + datetime-like
        return _concat_categorical(to_concat, axis=axis)

    elif _contains_datetime or 'timedelta' in typs or _contains_period:
        return _concat_datetime(to_concat, axis=axis, typs=typs)

    # these are mandated to handle empties as well
    elif 'sparse' in typs:
        return _concat_sparse(to_concat, axis=axis, typs=typs)

    all_empty = all(not is_nonempty(x) for x in to_concat)
    if any(is_extension_array_dtype(x) for x in to_concat) and axis == 1:
        to_concat = [np.atleast_2d(x.astype('object')) for x in to_concat]

    if all_empty:
        # we have all empties, but may need to coerce the result dtype to
        # object if we have non-numeric type operands (numpy would otherwise
        # cast this to float)
        typs = get_dtype_kinds(to_concat)
        if len(typs) != 1:

            if (not len(typs - {'i', 'u', 'f'}) or
                    not len(typs - {'bool', 'i', 'u'})):
                # let numpy coerce
                pass
            else:
                # coerce to object
                to_concat = [x.astype('object') for x in to_concat]

    return np.concatenate(to_concat, axis=axis)