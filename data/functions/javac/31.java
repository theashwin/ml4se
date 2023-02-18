public void initialize() {
        if (Ignition.state() == IgniteState.STOPPED) {
            this.ignite = Ignition.start(igniteConfiguration);
            LOGGER.debug("Starting ignite cache engine");
        } else if (Ignition.state() == IgniteState.STARTED) {
            this.ignite = Ignition.ignite();
            LOGGER.debug("Ignite cache engine has started");
        }
    }