public static byte getSerializeTypeByContentType(String contentType) throws SofaRpcException {
        if (StringUtils.isNotBlank(contentType)) {
            String ct = contentType.toLowerCase();
            if (ct.contains("text/plain") || ct.contains("text/html") || ct.contains("application/json")) {
                return getSerializeTypeByName(RpcConstants.SERIALIZE_JSON);
            } else if (ct.contains(RpcConstants.SERIALIZE_PROTOBUF)) {
                return getSerializeTypeByName(RpcConstants.SERIALIZE_PROTOBUF);
            } else if (ct.contains(RpcConstants.SERIALIZE_HESSIAN)) {
                return getSerializeTypeByName(RpcConstants.SERIALIZE_HESSIAN2);
            }
        }
        throw new SofaRpcException(RpcErrorType.SERVER_DESERIALIZE, "Unsupported content type " + contentType
            + " in http protocol, please set HTTP HEAD: '" + RemotingConstants.HEAD_SERIALIZE_TYPE + "'.");
    }