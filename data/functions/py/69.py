def _add_session_callback(self, callback_obj, callback, one_shot, originator):
        ''' Internal implementation for adding session callbacks.

        Args:
            callback_obj (SessionCallback) :
                A session callback object that wraps a callable and is
                passed to ``trigger_on_change``.

            callback (callable) :
                A callable to execute when session events happen.

            one_shot (bool) :
                Whether the callback should immediately auto-remove itself
                after one execution.

        Returns:
            SessionCallback : passed in as ``callback_obj``.

        Raises:
            ValueError, if the callback has been previously added

        '''
        if one_shot:
            @wraps(callback)
            def remove_then_invoke(*args, **kwargs):
                if callback_obj in self._session_callbacks:
                    self._remove_session_callback(callback_obj, originator)
                return callback(*args, **kwargs)
            actual_callback = remove_then_invoke
        else:
            actual_callback = callback

        callback_obj._callback = self._wrap_with_self_as_curdoc(actual_callback)
        self._session_callbacks.add(callback_obj)
        self._callback_objs_by_callable[originator][callback].add(callback_obj)

        # emit event so the session is notified of the new callback
        self._trigger_on_change(SessionCallbackAdded(self, callback_obj))

        return callback_obj