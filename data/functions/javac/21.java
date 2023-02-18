public static void unregisterMXBean(CacheProxy<?, ?> cache, MBeanType type) {
    ObjectName objectName = getObjectName(cache, type);
    unregister(objectName);
  }