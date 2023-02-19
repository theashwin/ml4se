private SM2 initCipherParams() {
		try {
			if (null != this.publicKey) {
				this.publicKeyParams = (ECPublicKeyParameters) ECUtil.generatePublicKeyParameter(this.publicKey);
			}
			if (null != privateKey) {
				this.privateKeyParams = (ECPrivateKeyParameters) ECUtil.generatePrivateKeyParameter(this.privateKey);
			}
		} catch (InvalidKeyException e) {
			throw new CryptoException(e);
		}

		return this;
	}