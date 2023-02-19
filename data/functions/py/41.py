def list_dfu_devices(*args, **kwargs):
    """Prints a lits of devices detected in DFU mode."""
    devices = get_dfu_devices(*args, **kwargs)
    if not devices:
        print("No DFU capable devices found")
        return
    for device in devices:
        print("Bus {} Device {:03d}: ID {:04x}:{:04x}"
              .format(device.bus, device.address,
                      device.idVendor, device.idProduct))
        layout = get_memory_layout(device)
        print("Memory Layout")
        for entry in layout:
            print("    0x{:x} {:2d} pages of {:3d}K bytes"
                  .format(entry['addr'], entry['num_pages'],
                          entry['page_size'] // 1024))