@Nullable
  public LookupExtractorFactoryMapContainer getLookup(final String tier, final String lookupName)
  {
    final Map<String, Map<String, LookupExtractorFactoryMapContainer>> prior = getKnownLookups();
    if (prior == null) {
      LOG.warn("Requested tier [%s] lookupName [%s]. But no lookups exist!", tier, lookupName);
      return null;
    }
    final Map<String, LookupExtractorFactoryMapContainer> tierLookups = prior.get(tier);
    if (tierLookups == null) {
      LOG.warn("Tier [%s] does not exist", tier);
      return null;
    }
    return tierLookups.get(lookupName);
  }