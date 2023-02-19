def user_update(user_id=None, name=None, email=None, enabled=None,
                tenant=None, profile=None, project=None, description=None, **connection_args):
    '''
    Update a user's information (keystone user-update)
    The following fields may be updated: name, email, enabled, tenant.
    Because the name is one of the fields, a valid user id is required.

    CLI Examples:

    .. code-block:: bash

        salt '*' keystone.user_update user_id=c965f79c4f864eaaa9c3b41904e67082 name=newname
        salt '*' keystone.user_update c965f79c4f864eaaa9c3b41904e67082 name=newname email=newemail@domain.com
    '''
    kstone = auth(profile, **connection_args)
    if not user_id:
        for user in kstone.users.list():
            if user.name == name:
                user_id = user.id
                break
        if not user_id:
            return {'Error': 'Unable to resolve user id'}
    user = kstone.users.get(user_id)
    # Keep previous settings if not updating them
    if not name:
        name = user.name
    if not email:
        email = user.email
    if enabled is None:
        enabled = user.enabled

    if _OS_IDENTITY_API_VERSION > 2:
        if description is None:
            description = getattr(user, 'description', None)
        else:
            description = six.text_type(description)

        project_id = None
        if project:
            for proj in kstone.projects.list():
                if proj.name == project:
                    project_id = proj.id
                    break
        if not project_id:
            project_id = getattr(user, 'project_id', None)

        kstone.users.update(user=user_id, name=name, email=email, enabled=enabled, description=description,
                            project_id=project_id)
    else:
        kstone.users.update(user=user_id, name=name, email=email, enabled=enabled)

        tenant_id = None
        if tenant:
            for tnt in kstone.tenants.list():
                if tnt.name == tenant:
                    tenant_id = tnt.id
                    break
            if tenant_id:
                kstone.users.update_tenant(user_id, tenant_id)

    ret = 'Info updated for user ID {0}'.format(user_id)
    return ret