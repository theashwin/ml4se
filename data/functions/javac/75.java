private TypeSerializer<Object> createSerializer(Object key, int pos) {
		if (key == null) {
			throw new NullKeyFieldException(pos);
		}
		try {
			TypeInformation<Object> info = TypeExtractor.getForObject(key);
			return info.createSerializer(executionConfig);
		}
		catch (Throwable t) {
			throw new RuntimeException("Could not create key serializer for type " + key);
		}
	}