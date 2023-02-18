def put_string(self, content, destination_s3_path, **kwargs):
        """
        Put a string to an S3 path.
        :param content: Data str
        :param destination_s3_path: URL for target S3 location
        :param kwargs: Keyword arguments are passed to the boto3 function `put_object`
        """
        self._check_deprecated_argument(**kwargs)
        (bucket, key) = self._path_to_bucket_and_key(destination_s3_path)

        # put the file
        self.s3.meta.client.put_object(
            Key=key, Bucket=bucket, Body=content, **kwargs)