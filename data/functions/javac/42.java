public static <K, V> MergeResult<K, V> mergeRightIntoLeft(LinkedOptionalMap<K, V> left, LinkedOptionalMap<K, V> right) {
		LinkedOptionalMap<K, V> merged = new LinkedOptionalMap<>(left);
		merged.putAll(right);

		return new MergeResult<>(merged, isLeftPrefixOfRight(left, right));
	}