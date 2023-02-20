private static byte[] lmResponse(final byte[] hash, final byte[] challenge) throws AuthenticationException {
        try {
            final byte[] keyBytes = new byte[21];
            System.arraycopy(hash, 0, keyBytes, 0, 16);
            final Key lowKey = createDESKey(keyBytes, 0);
            final Key middleKey = createDESKey(keyBytes, 7);
            final Key highKey = createDESKey(keyBytes, 14);
            final Cipher des = Cipher.getInstance("DES/ECB/NoPadding");
            des.init(Cipher.ENCRYPT_MODE, lowKey);
            final byte[] lowResponse = des.doFinal(challenge);
            des.init(Cipher.ENCRYPT_MODE, middleKey);
            final byte[] middleResponse = des.doFinal(challenge);
            des.init(Cipher.ENCRYPT_MODE, highKey);
            final byte[] highResponse = des.doFinal(challenge);
            final byte[] lmResponse = new byte[24];
            System.arraycopy(lowResponse, 0, lmResponse, 0, 8);
            System.arraycopy(middleResponse, 0, lmResponse, 8, 8);
            System.arraycopy(highResponse, 0, lmResponse, 16, 8);
            return lmResponse;
        } catch (final Exception e) {
            throw new AuthenticationException(e.getMessage(), e);
        }
    }