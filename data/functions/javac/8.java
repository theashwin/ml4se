private boolean[] extractBits(BitMatrix matrix) {
    boolean compact = ddata.isCompact();
    int layers = ddata.getNbLayers();
    int baseMatrixSize = (compact ? 11 : 14) + layers * 4; // not including alignment lines
    int[] alignmentMap = new int[baseMatrixSize];
    boolean[] rawbits = new boolean[totalBitsInLayer(layers, compact)];

    if (compact) {
      for (int i = 0; i < alignmentMap.length; i++) {
        alignmentMap[i] = i;
      }
    } else {
      int matrixSize = baseMatrixSize + 1 + 2 * ((baseMatrixSize / 2 - 1) / 15);
      int origCenter = baseMatrixSize / 2;
      int center = matrixSize / 2;
      for (int i = 0; i < origCenter; i++) {
        int newOffset = i + i / 15;
        alignmentMap[origCenter - i - 1] = center - newOffset - 1;
        alignmentMap[origCenter + i] = center + newOffset + 1;
      }
    }
    for (int i = 0, rowOffset = 0; i < layers; i++) {
      int rowSize = (layers - i) * 4 + (compact ? 9 : 12);
      // The top-left most point of this layer is <low, low> (not including alignment lines)
      int low = i * 2;
      // The bottom-right most point of this layer is <high, high> (not including alignment lines)
      int high = baseMatrixSize - 1 - low;
      // We pull bits from the two 2 x rowSize columns and two rowSize x 2 rows
      for (int j = 0; j < rowSize; j++) {
        int columnOffset = j * 2;
        for (int k = 0; k < 2; k++) {
          // left column
          rawbits[rowOffset + columnOffset + k] =
              matrix.get(alignmentMap[low + k], alignmentMap[low + j]);
          // bottom row
          rawbits[rowOffset + 2 * rowSize + columnOffset + k] =
              matrix.get(alignmentMap[low + j], alignmentMap[high - k]);
          // right column
          rawbits[rowOffset + 4 * rowSize + columnOffset + k] =
              matrix.get(alignmentMap[high - k], alignmentMap[high - j]);
          // top row
          rawbits[rowOffset + 6 * rowSize + columnOffset + k] =
              matrix.get(alignmentMap[high - j], alignmentMap[low + k]);
        }
      }
      rowOffset += rowSize * 8;
    }
    return rawbits;
  }