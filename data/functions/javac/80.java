Driver provideHiveDriver() {
    HiveConf hiveConf = provideHiveConf();
    SessionState.start(hiveConf);

    return new Driver(hiveConf);
  }