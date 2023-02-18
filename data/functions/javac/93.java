public final ListScanRunsPagedResponse listScanRuns(String parent) {
    ListScanRunsRequest request = ListScanRunsRequest.newBuilder().setParent(parent).build();
    return listScanRuns(request);
  }