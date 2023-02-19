private static Object callConstructor(final Class<?> cls, final Class<?>[] argTypes,
      final Object[] args) {
    try {
      final Constructor<?> cons = cls.getConstructor(argTypes);
      return cons.newInstance(args);
    } catch (final InvocationTargetException e) {
      throw getCause(e);
    } catch (final IllegalAccessException | NoSuchMethodException | InstantiationException e) {
      throw new IllegalStateException(e);
    }
  }