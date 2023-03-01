def _wait_for_completion(conn, promise, wait_timeout, msg):
    '''
    Poll request status until resource is provisioned.
    '''
    if not promise:
        return
    wait_timeout = time.time() + wait_timeout
    while wait_timeout > time.time():
        time.sleep(5)
        operation_result = conn.get_request(
            request_id=promise['requestId'],
            status=True)

        if operation_result['metadata']['status'] == "DONE":
            return
        elif operation_result['metadata']['status'] == "FAILED":
            raise Exception(
                "Request: {0}, requestId: {1} failed to complete:\n{2}".format(
                    msg, six.text_type(promise['requestId']),
                    operation_result['metadata']['message']
                )
            )

    raise Exception(
        'Timed out waiting for asynchronous operation {0} "{1}" to complete.'.format(
            msg, six.text_type(promise['requestId'])
        )
    )