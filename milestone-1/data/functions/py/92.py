def _valid_choices(cla55: type) -> Dict[str, str]:
    """
    Return a mapping {registered_name -> subclass_name}
    for the registered subclasses of `cla55`.
    """
    valid_choices: Dict[str, str] = {}

    if cla55 not in Registrable._registry:
        raise ValueError(f"{cla55} is not a known Registrable class")

    for name, subclass in Registrable._registry[cla55].items():
        # These wrapper classes need special treatment
        if isinstance(subclass, (_Seq2SeqWrapper, _Seq2VecWrapper)):
            subclass = subclass._module_class

        valid_choices[name] = full_name(subclass)

    return valid_choices