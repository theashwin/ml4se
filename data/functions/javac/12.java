public void setListeners(StatsStorageRouter statsStorage, Collection<? extends TrainingListener> listeners) {
        //Check if we have any RoutingIterationListener instances that need a StatsStorage implementation...
        if (listeners != null) {
            for (TrainingListener l : listeners) {
                if (l instanceof RoutingIterationListener) {
                    RoutingIterationListener rl = (RoutingIterationListener) l;
                    if (statsStorage == null && rl.getStorageRouter() == null) {
                        log.warn("RoutingIterationListener provided without providing any StatsStorage instance. Iterator may not function without one. Listener: {}",
                                        l);
                    }
                }
            }

            this.listeners.addAll(listeners);
        } else {
            this.listeners.clear();
        }

        this.storageRouter = statsStorage;
    }