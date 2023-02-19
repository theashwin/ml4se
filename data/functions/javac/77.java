public static String toFloatUnit(long size) {
		if (size < BYTE_UNIT_KILO) {
			return String.format("%5d", size);
		}

		if (size < BYTE_UNIT_MEGA) {
			return String.format("%5.1fk", size / (1d * BYTE_UNIT_KILO));
		}

		if (size < BYTE_UNIT_GIGA) {
			return String.format("%5.1fm", size / (1d * BYTE_UNIT_MEGA));
		}

		if (size < BYTE_UNIT_TERA) {
			return String.format("%5.1fg", size / (1d * BYTE_UNIT_GIGA));
		}

		return String.format("%5.1ft", size / (1d * BYTE_UNIT_TERA));
	}