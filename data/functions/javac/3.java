public boolean isApplicable(Class<? extends T> targetType) {
        Class<? extends T> applicable = Functions.getTypeParameter(clazz,getP(),0);
        return applicable.isAssignableFrom(targetType);
    }