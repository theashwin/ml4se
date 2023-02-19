private int readUnsignedVarInt() throws IOException {
    int value = 0;
    int shift = 0;
    int b;
    do {
      b = in.read();
      value |= (b & 0x7F) << shift;
      shift += 7;
    } while ((b & 0x80) != 0);
    return value;
  }