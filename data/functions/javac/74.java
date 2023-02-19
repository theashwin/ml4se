@SneakyThrows
    public DocumentDbMappingContext createDocumentDbMappingContext() {
        val documentDbMappingContext = new DocumentDbMappingContext();
        documentDbMappingContext.setInitialEntitySet(new EntityScanner(applicationContext).scan(Persistent.class));
        return documentDbMappingContext;
    }