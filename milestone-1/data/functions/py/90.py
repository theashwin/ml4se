def find_user(name, api_key=None):
    '''
    Find a user by name and return it.

    :param name:        The user name.
    :param api_key:     The Slack admin api key.
    :return:            The user object.

    CLI Example:

    .. code-block:: bash

        salt '*' slack.find_user name="ThomasHatch"

        salt '*' slack.find_user name="ThomasHatch" api_key=peWcBiMOS9HrZG15peWcBiMOS9HrZG15
    '''
    if not api_key:
        api_key = _get_api_key()

    ret = list_users(api_key)
    if ret['res']:
        users = ret['message']
        if users:
            for user in range(0, len(users)):
                if users[user]['name'] == name:
                    return users[user]
    return False