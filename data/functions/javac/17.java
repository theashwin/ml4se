public static String getType(File file) throws IORuntimeException {
		FileInputStream in = null;
		try {
			in = IoUtil.toStream(file);
			return getType(in);
		} finally {
			IoUtil.close(in);
		}
	}