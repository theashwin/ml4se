public static <T, R> Supplier<R> andThen(Supplier<T> supplier, BiFunction<T, Exception, R> handler){
        return () -> {
            try{
                T result = supplier.get();
                return handler.apply(result, null);
            }catch (Exception exception){
                return handler.apply(null, exception);
            }
        };
    }