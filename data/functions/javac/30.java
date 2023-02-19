@BetaApi
  public final AggregatedListVpnTunnelsPagedResponse aggregatedListVpnTunnels(String project) {
    AggregatedListVpnTunnelsHttpRequest request =
        AggregatedListVpnTunnelsHttpRequest.newBuilder().setProject(project).build();
    return aggregatedListVpnTunnels(request);
  }