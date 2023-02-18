def help(module=None, *args):
    '''
    Display help on Ansible standard module.

    :param module:
    :return:
    '''
    if not module:
        raise CommandExecutionError('Please tell me what module you want to have helped with. '
                                    'Or call "ansible.list" to know what is available.')
    try:
        module = _resolver.load_module(module)
    except (ImportError, LoaderError) as err:
        raise CommandExecutionError('Module "{0}" is currently not functional on your system.'.format(module))

    doc = {}
    ret = {}
    for docset in module.DOCUMENTATION.split('---'):
        try:
            docset = salt.utils.yaml.safe_load(docset)
            if docset:
                doc.update(docset)
        except Exception as err:
            log.error("Error parsing doc section: %s", err)
    if not args:
        if 'description' in doc:
            description = doc.get('description') or ''
            del doc['description']
            ret['Description'] = description
        ret['Available sections on module "{}"'.format(module.__name__.replace('ansible.modules.', ''))] = doc.keys()
    else:
        for arg in args:
            info = doc.get(arg)
            if info is not None:
                ret[arg] = info

    return ret