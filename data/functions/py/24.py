def _find_set_members(set):
    '''
    Return list of members for a set
    '''

    cmd = '{0} list {1}'.format(_ipset_cmd(), set)
    out = __salt__['cmd.run_all'](cmd, python_shell=False)

    if out['retcode'] > 0:
        # Set doesn't exist return false
        return False

    _tmp = out['stdout'].split('\n')
    members = []
    startMembers = False
    for i in _tmp:
        if startMembers:
            members.append(i)
        if 'Members:' in i:
            startMembers = True
    return members