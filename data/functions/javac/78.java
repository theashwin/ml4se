public double recall(int classLabel, double edgeCase) {
        double tpCount = truePositives.getCount(classLabel);
        double fnCount = falseNegatives.getCount(classLabel);

        return EvaluationUtils.recall((long) tpCount, (long) fnCount, edgeCase);
    }