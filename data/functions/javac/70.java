protected void addMetadataFiltersToMetadataResolver(final AbstractMetadataResolver metadataProvider, final MetadataFilter... metadataFilterList) {
        addMetadataFiltersToMetadataResolver(metadataProvider, Arrays.stream(metadataFilterList).collect(Collectors.toList()));
    }