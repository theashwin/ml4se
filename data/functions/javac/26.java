public static final ByteArray copyFrom(String string) {
    return new ByteArray(ByteString.copyFrom(string, StandardCharsets.UTF_8));
  }