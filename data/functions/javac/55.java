@ExperimentalApi("https://github.com/grpc/grpc-java/issues/4477")
  public static <T extends Message> Metadata.BinaryMarshaller<T> metadataMarshaller(T instance) {
    return ProtoLiteUtils.metadataMarshaller(instance);
  }