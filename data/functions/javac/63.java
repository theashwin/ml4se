public void removesScanResult(String uri, String method) {
		SpiderScanResult toRemove = new SpiderScanResult(uri, method);
		int index = scanResults.indexOf(toRemove);
		if (index >= 0) {
			scanResults.remove(index);
			fireTableRowsDeleted(index, index);
		}
	}