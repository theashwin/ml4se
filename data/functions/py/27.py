def close(self):
        """
        Close the pickle file, and the zip archive file. The single zip archive
        file can now be shipped around to be loaded by the unpickler.
        """
        if self.file is None:
            return

        # Close the pickle file.
        self.file.close()
        self.file = None

        for f in self.mark_for_delete:
            error = [False]

            def register_error(*args):
                error[0] = True

            _shutil.rmtree(f, onerror = register_error)

            if error[0]:
                _atexit.register(_shutil.rmtree, f, ignore_errors=True)