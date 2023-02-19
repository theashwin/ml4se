def _machinectl(cmd,
                output_loglevel='debug',
                ignore_retcode=False,
                use_vt=False):
    '''
    Helper function to run machinectl
    '''
    prefix = 'machinectl --no-legend --no-pager'
    return __salt__['cmd.run_all']('{0} {1}'.format(prefix, cmd),
                                   output_loglevel=output_loglevel,
                                   ignore_retcode=ignore_retcode,
                                   use_vt=use_vt)