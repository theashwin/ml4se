@Override
    @JsonIgnore
    public String getId() {
        if (instanceId != null && !instanceId.isEmpty()) {
            return instanceId;
        } else if (dataCenterInfo instanceof AmazonInfo) {
            String uniqueId = ((AmazonInfo) dataCenterInfo).getId();
            if (uniqueId != null && !uniqueId.isEmpty()) {
                return uniqueId;
            }
        }
        return hostName;
    }