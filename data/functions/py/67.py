def is_iter(y, ignore=six.string_types):
    '''
    Test if an object is iterable, but not a string type.

    Test if an object is an iterator or is iterable itself. By default this
    does not return True for string objects.

    The `ignore` argument defaults to a list of string types that are not
    considered iterable. This can be used to also exclude things like
    dictionaries or named tuples.

    Based on https://bitbucket.org/petershinners/yter
    '''

    if ignore and isinstance(y, ignore):
        return False
    try:
        iter(y)
        return True
    except TypeError:
        return False