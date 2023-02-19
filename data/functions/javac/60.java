public static <ReqT, RespT> ListenableFuture<RespT> futureUnaryCall(
      ClientCall<ReqT, RespT> call, ReqT req) {
    GrpcFuture<RespT> responseFuture = new GrpcFuture<>(call);
    asyncUnaryRequestCall(call, req, new UnaryStreamToFuture<>(responseFuture), false);
    return responseFuture;
  }