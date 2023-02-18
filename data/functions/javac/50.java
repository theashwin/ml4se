@Override
	public void setup(AbstractInvokable parent) {
		@SuppressWarnings("unchecked")
		final ReduceFunction<IT> red = BatchTask.instantiateUserCode(this.config, userCodeClassLoader, ReduceFunction.class);
		this.reducer = red;
		FunctionUtils.setFunctionRuntimeContext(red, getUdfRuntimeContext());

		TypeSerializerFactory<IT> serializerFactory = this.config.getInputSerializer(0, userCodeClassLoader);
		this.serializer = serializerFactory.getSerializer();

		if (LOG.isDebugEnabled()) {
			LOG.debug("ChainedAllReduceDriver object reuse: " + (this.objectReuseEnabled ? "ENABLED" : "DISABLED") + ".");
		}
	}