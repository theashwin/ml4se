public CouchDbConsentDecision findFirstConsentDecision(final String principal, final String service) {
        val view = createQuery("by_consent_decision").key(ComplexKey.of(principal, service)).limit(1).includeDocs(true);
        return db.queryView(view, CouchDbConsentDecision.class).stream().findFirst().orElse(null);
    }