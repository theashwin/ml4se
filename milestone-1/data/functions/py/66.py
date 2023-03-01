def wait_for_compute_global_operation(project_name, operation):
    """Poll for global compute operation until finished."""
    logger.info("wait_for_compute_global_operation: "
                "Waiting for operation {} to finish...".format(
                    operation["name"]))

    for _ in range(MAX_POLLS):
        result = compute.globalOperations().get(
            project=project_name,
            operation=operation["name"],
        ).execute()
        if "error" in result:
            raise Exception(result["error"])

        if result["status"] == "DONE":
            logger.info("wait_for_compute_global_operation: "
                        "Operation done.")
            break

        time.sleep(POLL_INTERVAL)

    return result