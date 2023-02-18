def check(set=None, entry=None, family='ipv4'):
    '''
    Check that an entry exists in the specified set.

    set
        The ipset name

    entry
        An entry in the ipset.  This parameter can be a single IP address, a
        range of IP addresses, or a subnet block.  Example:

        .. code-block:: cfg

            192.168.0.1
            192.168.0.2-192.168.0.19
            192.168.0.0/25

    family
        IP protocol version: ipv4 or ipv6

    CLI Example:

    .. code-block:: bash

        salt '*' ipset.check setname '192.168.0.1 comment "Hello"'

    '''
    if not set:
        return 'Error: Set needs to be specified'
    if not entry:
        return 'Error: Entry needs to be specified'

    settype = _find_set_type(set)
    if not settype:
        return 'Error: Set {0} does not exist'.format(set)

    current_members = _parse_members(settype, _find_set_members(set))

    if not current_members:
        return False

    if isinstance(entry, list):
        entries = _parse_members(settype, entry)
    else:
        entries = [_parse_member(settype, entry)]

    for current_member in current_members:
        for entry in entries:
            if _member_contains(current_member, entry):
                return True

    return False