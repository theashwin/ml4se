def flush(bank, key=None, cachedir=None):
    '''
    Remove the key from the cache bank with all the key content.
    '''
    if cachedir is None:
        cachedir = __cachedir()

    try:
        if key is None:
            target = os.path.join(cachedir, os.path.normpath(bank))
            if not os.path.isdir(target):
                return False
            shutil.rmtree(target)
        else:
            target = os.path.join(cachedir, os.path.normpath(bank), '{0}.p'.format(key))
            if not os.path.isfile(target):
                return False
            os.remove(target)
    except OSError as exc:
        raise SaltCacheError(
            'There was an error removing "{0}": {1}'.format(
                target, exc
            )
        )
    return True