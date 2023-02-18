void updateInstance(T instance) {
        T oldInstance = this.instance.getAndSet(Preconditions.checkNotNull(instance, "instance"));
        if (oldInstance != null && oldInstance != instance) {
            oldInstance.close();
        }
    }