def list_disk_partitions(disk_id=None, scsi_address=None,
                          service_instance=None):
    '''
    Lists the partitions on a disk.
    The disk can be specified either by the canonical name, or by the
    scsi_address.

    disk_id
        Canonical name of the disk.
        Either ``disk_id`` or ``scsi_address`` needs to be specified
        (``disk_id`` supersedes ``scsi_address``.

    scsi_address`
        Scsi address of the disk.
        ``disk_id`` or ``scsi_address`` needs to be specified
        (``disk_id`` supersedes ``scsi_address``.

    service_instance
        Service instance (vim.ServiceInstance) of the vCenter/ESXi host.
        Default is None.

    .. code-block:: bash

        salt '*' vsphere.list_disk_partitions scsi_address='vmhaba0:C0:T0:L0'

        salt '*' vsphere.list_disk_partitions disk_id='naa.000000000000001'
    '''
    if not disk_id and not scsi_address:
        raise ArgumentValueError('Either \'disk_id\' or \'scsi_address\' '
                                 'needs to be specified')
    host_ref = _get_proxy_target(service_instance)
    hostname = __proxy__['esxi.get_details']()['esxi_host']
    if not disk_id:
        scsi_address_to_lun = \
                salt.utils.vmware.get_scsi_address_to_lun_map(host_ref)
        if scsi_address not in scsi_address_to_lun:
            raise VMwareObjectRetrievalError(
                'Scsi lun with address \'{0}\' was not found on host \'{1}\''
                ''.format(scsi_address, hostname))
        disk_id = scsi_address_to_lun[scsi_address].canonicalName
        log.trace('[%s] Got disk id \'%s\' for scsi address \'%s\'',
                  hostname, disk_id, scsi_address)
    log.trace('Listing disk partitions on disk \'%s\' in host \'%s\'',
              disk_id, hostname)
    partition_info = \
            salt.utils.vmware.get_disk_partition_info(host_ref, disk_id)
    ret_list = []
    # NOTE: 1. The layout view has an extra 'None' partition for free space
    #       2. The orders in the layout/partition views are not the same
    for part_spec in partition_info.spec.partition:
        part_layout = [p for p in partition_info.layout.partition
                       if p.partition == part_spec.partition][0]
        part_dict = {'hostname': hostname,
                     'device': disk_id,
                     'format': partition_info.spec.partitionFormat,
                     'partition': part_spec.partition,
                     'type': part_spec.type,
                     'sectors':
                     part_spec.endSector - part_spec.startSector + 1,
                     'size_KB':
                     (part_layout.end.block - part_layout.start.block + 1) *
                     part_layout.start.blockSize / 1024}
        ret_list.append(part_dict)
    return ret_list