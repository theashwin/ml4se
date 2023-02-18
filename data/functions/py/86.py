def _tokenize_mteval_v14_intl(segment):
    r"""Tokenize a string following following the international tokenizer in mteval-v14a.pl.
    See https://github.com/moses-smt/mosesdecoder/"
           "blob/master/scripts/generic/mteval-v14.pl#L954-L983

    Parameters
    ----------
    segment: str
        A string to be tokenized

    Returns
    -------
    The tokenized string
    """
    segment = segment.rstrip()
    segment = unicodeRegex.nondigit_punct_re.sub(r'\1 \2 ', segment)
    segment = unicodeRegex.punct_nondigit_re.sub(r' \1 \2', segment)
    segment = unicodeRegex.symbol_re.sub(r' \1 ', segment)
    return segment.strip()