def deployments(namespace='default', **kwargs):
    '''
    Return a list of kubernetes deployments defined in the namespace

    CLI Examples::

        salt '*' kubernetes.deployments
        salt '*' kubernetes.deployments namespace=default
    '''
    cfg = _setup_conn(**kwargs)
    try:
        api_instance = kubernetes.client.ExtensionsV1beta1Api()
        api_response = api_instance.list_namespaced_deployment(namespace)

        return [dep['metadata']['name'] for dep in api_response.to_dict().get('items')]
    except (ApiException, HTTPError) as exc:
        if isinstance(exc, ApiException) and exc.status == 404:
            return None
        else:
            log.exception(
                'Exception when calling '
                'ExtensionsV1beta1Api->list_namespaced_deployment'
            )
            raise CommandExecutionError(exc)
    finally:
        _cleanup(**cfg)