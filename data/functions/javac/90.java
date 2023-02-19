private Pair<Gradient, INDArray> getGradientsAndDelta(INDArray preOut, LayerWorkspaceMgr workspaceMgr) {
        ILossFunction lossFunction = layerConf().getLossFn();
        INDArray labels2d = getLabels2d(workspaceMgr, ArrayType.BP_WORKING_MEM);
        if (labels2d.size(1) != preOut.size(1)) {
            throw new DL4JInvalidInputException(
                            "Labels array numColumns (size(1) = " + labels2d.size(1) + ") does not match output layer"
                                            + " number of outputs (nOut = " + preOut.size(1) + ") " + layerId());
        }

        INDArray delta = lossFunction.computeGradient(labels2d, preOut, layerConf().getActivationFn(), maskArray);

        Gradient gradient = new DefaultGradient();

        INDArray weightGradView = gradientViews.get(CenterLossParamInitializer.WEIGHT_KEY);
        INDArray biasGradView = gradientViews.get(CenterLossParamInitializer.BIAS_KEY);
        INDArray centersGradView = gradientViews.get(CenterLossParamInitializer.CENTER_KEY);

        // centers delta
        double alpha = layerConf().getAlpha();

        INDArray centers = params.get(CenterLossParamInitializer.CENTER_KEY);
        INDArray l = labels.castTo(centers.dataType()); //Ensure correct dtype (same as params); no-op if already correct dtype
        INDArray centersForExamples = l.mmul(centers);
        INDArray diff = centersForExamples.sub(input).muli(alpha);
        INDArray numerator = l.transpose().mmul(diff);
        INDArray denominator = l.sum(0).reshape(l.size(1), 1).addi(1.0);

        INDArray deltaC;
        if (layerConf().getGradientCheck()) {
            double lambda = layerConf().getLambda();
            //For gradient checks: need to multiply dLc/dcj by lambda to get dL/dcj
            deltaC = numerator.muli(lambda);
        } else {
            deltaC = numerator.diviColumnVector(denominator);
        }
        centersGradView.assign(deltaC);



        // other standard calculations
        Nd4j.gemm(input, delta, weightGradView, true, false, 1.0, 0.0); //Equivalent to:  weightGradView.assign(input.transpose().mmul(delta));
        delta.sum(biasGradView, 0); //biasGradView is initialized/zeroed first in sum op

        gradient.gradientForVariable().put(CenterLossParamInitializer.WEIGHT_KEY, weightGradView);
        gradient.gradientForVariable().put(CenterLossParamInitializer.BIAS_KEY, biasGradView);
        gradient.gradientForVariable().put(CenterLossParamInitializer.CENTER_KEY, centersGradView);

        return new Pair<>(gradient, delta);
    }