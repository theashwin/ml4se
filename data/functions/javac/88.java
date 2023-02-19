private void addNewBuilds(List<BambooJob> enabledJobs,
                              Map<BambooJob, Set<Build>> buildsByJob) {
        long start = System.currentTimeMillis();
        int count = 0;

        for (BambooJob job : enabledJobs) {
            if (job.isPushed()) {
                LOG.info("Job Pushed already: " + job.getJobName());
                continue;
            }
            // process new builds in the order of their build numbers - this has implication to handling of commits in BuildEventListener
            ArrayList<Build> builds = Lists.newArrayList(nullSafe(buildsByJob.get(job)));
            builds.sort((Build b1, Build b2) -> Integer.valueOf(b1.getNumber()) - Integer.valueOf(b2.getNumber()));
            for (Build buildSummary : builds) {
                if (isNewBuild(job, buildSummary)) {
                    Build build = bambooClient.getBuildDetails(buildSummary
                            .getBuildUrl(), job.getInstanceUrl());
                    if (build != null) {
                        build.setCollectorItemId(job.getId());
                        buildRepository.save(build);
                        count++;
                    }
                }
            }
        }
        log("New builds", start, count);
    }