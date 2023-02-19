@Override
	public void processElement1(StreamRecord<T1> record) throws Exception {
		processElement(record, leftBuffer, rightBuffer, lowerBound, upperBound, true);
	}