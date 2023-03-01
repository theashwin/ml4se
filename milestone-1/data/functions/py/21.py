def loadACatalog(filename):
    """Load the catalog and build the associated data structures.
      This can be either an XML Catalog or an SGML Catalog It
      will recurse in SGML CATALOG entries. On the other hand XML
       Catalogs are not handled recursively. """
    ret = libxml2mod.xmlLoadACatalog(filename)
    if ret is None:raise treeError('xmlLoadACatalog() failed')
    return catalog(_obj=ret)