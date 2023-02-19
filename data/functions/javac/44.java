@SuppressWarnings("unchecked")
	@PublicEvolving
	public static <T, C> ObjectArrayTypeInfo<T, C> getInfoFor(TypeInformation<C> componentInfo) {
		checkNotNull(componentInfo);

		return new ObjectArrayTypeInfo<T, C>(
			(Class<T>)Array.newInstance(componentInfo.getTypeClass(), 0).getClass(),
			componentInfo);
	}