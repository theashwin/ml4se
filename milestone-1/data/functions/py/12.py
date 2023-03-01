def xpathNewValueTree(self):
        """Create a new xmlXPathObjectPtr of type Value Tree (XSLT)
           and initialize it with the tree root @val """
        ret = libxml2mod.xmlXPathNewValueTree(self._o)
        if ret is None:raise xpathError('xmlXPathNewValueTree() failed')
        return xpathObjectRet(ret)