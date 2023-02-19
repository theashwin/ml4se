def _is_installation_local(name):
    """Check whether the distribution is in the current Python installation.

    This is used to distinguish packages seen by a virtual environment. A venv
    may be able to see global packages, but we don't want to mess with them.
    """
    loc = os.path.normcase(pkg_resources.working_set.by_key[name].location)
    pre = os.path.normcase(sys.prefix)
    return os.path.commonprefix([loc, pre]) == pre