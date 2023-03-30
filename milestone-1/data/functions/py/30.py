def fileno(self):
        """
        Returns an OS-level file descriptor which can be used for polling, but
        but not for reading or writing.  This is primarily to allow python's
        ``select`` module to work.

        The first time ``fileno`` is called on a channel, a pipe is created to
        simulate real OS-level file descriptor (FD) behavior.  Because of this,
        two OS-level FDs are created, which will use up FDs faster than normal.
        (You won't notice this effect unless you have hundreds of channels
        open at the same time.)

        :return: an OS-level file descriptor (`int`)

        .. warning::
            This method causes channel reads to be slightly less efficient.
        """
        self.lock.acquire()
        try:
            if self._pipe is not None:
                return self._pipe.fileno()
            # create the pipe and feed in any existing data
            self._pipe = pipe.make_pipe()
            p1, p2 = pipe.make_or_pipe(self._pipe)
            self.in_buffer.set_event(p1)
            self.in_stderr_buffer.set_event(p2)
            return self._pipe.fileno()
        finally:
            self.lock.release()