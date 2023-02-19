public static SearchFilter newLdaptiveSearchFilter(final String filterQuery, final String paramName, final List<String> params) {
        val filter = new SearchFilter();
        filter.setFilter(filterQuery);
        if (params != null) {
            IntStream.range(0, params.size()).forEach(i -> {
                if (filter.getFilter().contains("{" + i + '}')) {
                    filter.setParameter(i, params.get(i));
                } else {
                    filter.setParameter(paramName, params.get(i));
                }
            });
        }
        LOGGER.debug("Constructed LDAP search filter [{}]", filter.format());
        return filter;
    }