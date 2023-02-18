public boolean isMatchingTopic(String topic) {
		if (isFixedTopics()) {
			return getFixedTopics().contains(topic);
		} else {
			return topicPattern.matcher(topic).matches();
		}
	}