public StrBuilder insert(int index, CharSequence csq) {
		if (null == csq) {
			csq = "null";
		}
		int len = csq.length();
		moveDataAfterIndex(index, csq.length());
		if (csq instanceof String) {
			((String) csq).getChars(0, len, this.value, index);
		} else if (csq instanceof StringBuilder) {
			((StringBuilder) csq).getChars(0, len, this.value, index);
		} else if (csq instanceof StringBuffer) {
			((StringBuffer) csq).getChars(0, len, this.value, index);
		} else if (csq instanceof StrBuilder) {
			((StrBuilder) csq).getChars(0, len, this.value, index);
		} else {
			for (int i = 0, j = this.position; i < len; i++, j++) {
				this.value[j] = csq.charAt(i);
			}
		}
		this.position = Math.max(this.position, index) + len;
		return this;
	}