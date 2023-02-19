public Class<T> getT() {
        Type subTyping = Types.getBaseClass(getClass(), Descriptor.class);
        if (!(subTyping instanceof ParameterizedType)) {
            throw new IllegalStateException(getClass()+" doesn't extend Descriptor with a type parameter.");
        }
        return Types.erasure(Types.getTypeArgument(subTyping, 0));
    }