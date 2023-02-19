def kernels_pull_cli(self,
                         kernel,
                         kernel_opt=None,
                         path=None,
                         metadata=False):
        """ client wrapper for kernels_pull
        """
        kernel = kernel or kernel_opt
        effective_path = self.kernels_pull(
            kernel, path=path, metadata=metadata, quiet=False)
        if metadata:
            print('Source code and metadata downloaded to ' + effective_path)
        else:
            print('Source code downloaded to ' + effective_path)