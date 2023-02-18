public static Method getPublicMethod(Class<?> clazz, String methodName, Class<?>... paramTypes) throws SecurityException {
		return ReflectUtil.getPublicMethod(clazz, methodName, paramTypes);
	}