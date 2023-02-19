public byte[][] readImagesUnsafe(int nImages) throws IOException {
        byte[][] out = new byte[nImages][0];
        for (int i = 0; i < nImages; i++) {
            out[i] = new byte[rows * cols];
            read(out[i]);
        }
        return out;
    }