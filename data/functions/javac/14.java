public static String getType(String fileStreamHexHead) {
		for (Entry<String, String> fileTypeEntry : fileTypeMap.entrySet()) {
			if(StrUtil.startWithIgnoreCase(fileStreamHexHead, fileTypeEntry.getKey())) {
				return fileTypeEntry.getValue();
			}
		}
		return null;
	}