public static void binary(Image srcImage, ImageOutputStream destImageStream, String imageType) throws IORuntimeException {
		write(binary(srcImage), imageType, destImageStream);
	}