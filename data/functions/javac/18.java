public Task removeTask(ExecutionAttemptID executionAttemptID) {
		checkInit();

		TaskSlotMapping taskSlotMapping = taskSlotMappings.remove(executionAttemptID);

		if (taskSlotMapping != null) {
			Task task = taskSlotMapping.getTask();
			TaskSlot taskSlot = taskSlotMapping.getTaskSlot();

			taskSlot.remove(task.getExecutionId());

			if (taskSlot.isReleasing() && taskSlot.isEmpty()) {
				slotActions.freeSlot(taskSlot.getAllocationId());
			}

			return task;
		} else {
			return null;
		}
	}