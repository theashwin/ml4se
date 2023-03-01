def get_storage_policies(profile_manager, policy_names=None,
                         get_all_policies=False):
    '''
    Returns a list of the storage policies, filtered by name.

    profile_manager
        Reference to the profile manager.

    policy_names
        List of policy names to filter by.
        Default is None.

    get_all_policies
        Flag specifying to return all policies, regardless of the specified
        filter.
    '''
    res_type = pbm.profile.ResourceType(
        resourceType=pbm.profile.ResourceTypeEnum.STORAGE)
    try:
        policy_ids = profile_manager.QueryProfile(res_type)
    except vim.fault.NoPermission as exc:
        log.exception(exc)
        raise VMwareApiError('Not enough permissions. Required privilege: '
                             '{0}'.format(exc.privilegeId))
    except vim.fault.VimFault as exc:
        log.exception(exc)
        raise VMwareApiError(exc.msg)
    except vmodl.RuntimeFault as exc:
        log.exception(exc)
        raise VMwareRuntimeError(exc.msg)
    log.trace('policy_ids = %s', policy_ids)
    # More policies are returned so we need to filter again
    policies = [p for p in get_policies_by_id(profile_manager, policy_ids)
                if p.resourceType.resourceType ==
                pbm.profile.ResourceTypeEnum.STORAGE]
    if get_all_policies:
        return policies
    if not policy_names:
        policy_names = []
    return [p for p in policies if p.name in policy_names]