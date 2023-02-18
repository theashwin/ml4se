def multi_find(*patterns, **kwargs):
    '''
    Execute multiple search tasks.
    This function is based on the `find` function.
    Depending on the search items, some information might overlap.

    Optional arguments:

    best: ``True``
        Return only the best match with the interfaces IP networks
        when the saerching pattern is a valid IP Address or Network.

    display: ``True``
        Display on the screen or return structured object? Default: `True` (return on the CLI).


    CLI Example:

    .. code-block:: bash

        $ sudo salt-run net.multi_find Ethernet1/49 xe-0/1/2

    Output Example:

    .. code-block:: text

        Pattern "Ethernet1/49" found in one of the following LLDP details

            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            |    Device    | Interface | Parent Interface | Remote Chassis ID | Remote Port Description | Remote Port ID |          Remote System Description          |   Remote System Name   |
            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            | edge01.oua04 |  xe-0/1/2 |       ae1        | DE:AD:BE:EF:DE:AD |       Ethernet1/49      |                | Cisco NX-OS(tm) n6000, Software (n6000-uk9) | edge07.oua04.dummy.net |
            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        Details for interface xe-0/1/2

            -----------------------------------------------------------------------------------------------------------------------
            |    Device    | Interface | Interface Description | IP Addresses | Enabled |  UP  |    MAC Address    | Speed [Mbps] |
            -----------------------------------------------------------------------------------------------------------------------
            | edge01.oua04 |  xe-0/1/2 |     ae1 sw01.oua04    |              |   True  | True | BE:EF:DE:AD:BE:EF |    10000     |
            -----------------------------------------------------------------------------------------------------------------------

        LLDP Neighbors for interface xe-0/1/2

            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            |    Device    | Interface | Parent Interface | Remote Chassis ID | Remote Port Description | Remote Port ID |          Remote System Description          |   Remote System Name   |
            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            | edge01.oua04 |  xe-0/1/2 |       ae1        | DE:AD:BE:EF:DE:AD |       Ethernet1/49      |                | Cisco NX-OS(tm) n6000, Software (n6000-uk9) | edge07.oua04.dummy.net |
            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    out = {}
    for pattern in set(patterns):
        search_result = find(pattern,
                             best=kwargs.get('best', True),
                             display=kwargs.get('display', _DEFAULT_DISPLAY))
        out[pattern] = search_result
    if not kwargs.get('display', _DEFAULT_DISPLAY):
        return out