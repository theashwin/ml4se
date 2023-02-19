public static <T> Iterator<T> removeNull(final Iterator<T> itr) {
        return com.google.common.collect.Iterators.filter(itr, Predicates.notNull());
    }