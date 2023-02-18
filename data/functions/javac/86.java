public void reconnect(final JobID jobId) {
		Preconditions.checkNotNull(jobId, "JobID must not be null.");

		final Tuple2<LeaderRetrievalService, JobManagerLeaderListener> jobLeaderService = jobLeaderServices.get(jobId);

		if (jobLeaderService != null) {
			jobLeaderService.f1.reconnect();
		} else {
			LOG.info("Cannot reconnect to job {} because it is not registered.", jobId);
		}
	}