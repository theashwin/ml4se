public FilterOperator<T> filter(FilterFunction<T> filter) {
		if (filter == null) {
			throw new NullPointerException("Filter function must not be null.");
		}
		return new FilterOperator<>(this, clean(filter), Utils.getCallLocationName());
	}