def save(self, file:PathLikeOrBinaryStream= 'data_save.pkl')->None:
        "Save the `DataBunch` in `self.path/file`. `file` can be file-like (file or buffer)"
        if not getattr(self, 'label_list', False):
            warn("Serializing the `DataBunch` only works when you created it using the data block API.")
            return
        try_save(self.label_list, self.path, file)