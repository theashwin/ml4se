def error_info():
    """Return information about failed tasks."""
    worker = global_worker
    worker.check_connected()
    return (global_state.error_messages(driver_id=worker.task_driver_id) +
            global_state.error_messages(driver_id=DriverID.nil()))