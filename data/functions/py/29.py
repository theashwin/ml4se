def textMerge(self, second):
        """Merge two text nodes into one """
        if second is None: second__o = None
        else: second__o = second._o
        ret = libxml2mod.xmlTextMerge(self._o, second__o)
        if ret is None:raise treeError('xmlTextMerge() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp