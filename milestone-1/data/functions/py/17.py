def avail(search=None, verbose=False):
    '''
    Return a list of available images

    search : string
        search keyword
    verbose : boolean (False)
        toggle verbose output

    CLI Example:

    .. code-block:: bash

        salt '*' imgadm.avail [percona]
        salt '*' imgadm.avail verbose=True
    '''
    ret = {}
    cmd = 'imgadm avail -j'
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = _exit_status(retcode)
        return ret

    for image in salt.utils.json.loads(res['stdout']):
        if image['manifest']['disabled'] or not image['manifest']['public']:
            continue
        if search and search not in image['manifest']['name']:
            # we skip if we are searching but don't have a match
            continue
        uuid = image['manifest']['uuid']
        data = _parse_image_meta(image, verbose)
        if data:
            ret[uuid] = data

    return ret