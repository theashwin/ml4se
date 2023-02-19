public static Method getMethodByName(Class<?> clazz, boolean ignoreCase, String methodName) throws SecurityException {
		if (null == clazz || StrUtil.isBlank(methodName)) {
			return null;
		}

		final Method[] methods = getMethods(clazz);
		if (ArrayUtil.isNotEmpty(methods)) {
			for (Method method : methods) {
				if (StrUtil.equals(methodName, method.getName(), ignoreCase)) {
					return method;
				}
			}
		}
		return null;
	}