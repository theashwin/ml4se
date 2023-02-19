private static void registerFactory(Type t, Class<? extends TypeInfoFactory> factory) {
		Preconditions.checkNotNull(t, "Type parameter must not be null.");
		Preconditions.checkNotNull(factory, "Factory parameter must not be null.");

		if (!TypeInfoFactory.class.isAssignableFrom(factory)) {
			throw new IllegalArgumentException("Class is not a TypeInfoFactory.");
		}
		if (registeredTypeInfoFactories.containsKey(t)) {
			throw new InvalidTypesException("A TypeInfoFactory for type '" + t + "' is already registered.");
		}
		registeredTypeInfoFactories.put(t, factory);
	}