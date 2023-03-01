def find_elt(modvars, keyword, match_last=False):
    "Attempt to resolve keywords such as Learner.lr_find. `match_last` starts matching from last component."
    keyword = strip_fastai(keyword)
    if keyword in modvars: return modvars[keyword]
    comps = keyword.split('.')
    comp_elt = modvars.get(comps[0])
    if hasattr(comp_elt, '__dict__'): return find_elt(comp_elt.__dict__, '.'.join(comps[1:]), match_last=match_last)