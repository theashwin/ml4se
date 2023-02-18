public boolean getBoolean(String key, boolean defaultValue) {
		Object o = getRawValue(key);
		if (o == null) {
			return defaultValue;
		}

		return convertToBoolean(o);
	}