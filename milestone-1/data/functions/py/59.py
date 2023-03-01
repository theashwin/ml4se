def relaxNGNewMemParserCtxt(buffer, size):
    """Create an XML RelaxNGs parse context for that memory buffer
       expected to contain an XML RelaxNGs file. """
    ret = libxml2mod.xmlRelaxNGNewMemParserCtxt(buffer, size)
    if ret is None:raise parserError('xmlRelaxNGNewMemParserCtxt() failed')
    return relaxNgParserCtxt(_obj=ret)