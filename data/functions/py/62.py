def from_api_repr(cls, resource):
        """Factory: construct parameter from JSON resource.

        :type resource: dict
        :param resource: JSON mapping of parameter

        :rtype: :class:`~google.cloud.bigquery.query.ScalarQueryParameter`
        :returns: instance
        """
        name = resource.get("name")
        type_ = resource["parameterType"]["type"]
        value = resource["parameterValue"]["value"]
        converted = _QUERY_PARAMS_FROM_JSON[type_](value, None)
        return cls(name, type_, converted)