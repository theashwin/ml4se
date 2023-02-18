def list_topic_rules(topic=None, ruleDisabled=None,
            region=None, key=None, keyid=None, profile=None):
    '''
    List all rules (for a given topic, if specified)

    Returns list of rules

    CLI Example:

    .. code-block:: bash

        salt myminion boto_iot.list_topic_rules

    Example Return:

    .. code-block:: yaml

        rules:
          - {...}
          - {...}

    '''
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        kwargs = {}
        if topic is not None:
            kwargs['topic'] = topic
        if ruleDisabled is not None:
            kwargs['ruleDisabled'] = ruleDisabled
        rules = []
        for ret in __utils__['boto3.paged_call'](conn.list_topic_rules,
                                 marker_flag='nextToken',
                                 marker_arg='nextToken',
                                 **kwargs):
            rules.extend(ret['rules'])
        if not bool(rules):
            log.warning('No rules found')
        return {'rules': rules}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}