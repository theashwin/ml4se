public final AppProfile getAppProfile(String name) {

    GetAppProfileRequest request = GetAppProfileRequest.newBuilder().setName(name).build();
    return getAppProfile(request);
  }