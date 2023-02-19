public static ClassResolver weakCachingResolver(ClassLoader classLoader) {
        return new CachingClassResolver(
                new ClassLoaderClassResolver(defaultClassLoader(classLoader)),
                new WeakReferenceMap<String, Class<?>>(new HashMap<String, Reference<Class<?>>>()));
    }