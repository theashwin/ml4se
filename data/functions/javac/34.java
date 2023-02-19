public static <E> Enumeration<E> asEnumeration(Iterator<E> iter) {
		return new IteratorEnumeration<E>(iter);
	}