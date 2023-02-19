def set_dhcp_linklocal_all(interface):
    '''
    Configure specified adapter to use DHCP with linklocal fallback

    Change adapter mode to TCP/IP. If previous adapter mode was EtherCAT, the target will need reboot.

    :param str interface: interface label
    :return: True if the settings were applied, otherwise an exception will be thrown.
    :rtype: bool

    CLI Example:

    .. code-block:: bash

        salt '*' ip.set_dhcp_linklocal_all interface-label
    '''
    if __grains__['lsb_distrib_id'] == 'nilrt':
        initial_mode = _get_adapter_mode_info(interface)
        _save_config(interface, 'Mode', 'TCPIP')
        _save_config(interface, 'dhcpenabled', '1')
        _save_config(interface, 'linklocalenabled', '1')
        if initial_mode == 'ethercat':
            __salt__['system.set_reboot_required_witnessed']()
        else:
            _restart(interface)
        return True
    service = _interface_to_service(interface)
    if not service:
        raise salt.exceptions.CommandExecutionError('Invalid interface name: {0}'.format(interface))
    service = pyconnman.ConnService(os.path.join(SERVICE_PATH, service))
    ipv4 = service.get_property('IPv4.Configuration')
    ipv4['Method'] = dbus.String('dhcp', variant_level=1)
    ipv4['Address'] = dbus.String('', variant_level=1)
    ipv4['Netmask'] = dbus.String('', variant_level=1)
    ipv4['Gateway'] = dbus.String('', variant_level=1)
    try:
        service.set_property('IPv4.Configuration', ipv4)
        service.set_property('Nameservers.Configuration', [''])  # reset nameservers list
    except Exception as exc:
        exc_msg = 'Couldn\'t set dhcp linklocal for service: {0}\nError: {1}\n'.format(service, exc)
        raise salt.exceptions.CommandExecutionError(exc_msg)
    return True