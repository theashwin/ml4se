public MultiLayerConfiguration getMultiLayerConfiguration()
            throws InvalidKerasConfigurationException, UnsupportedKerasConfigurationException {
        if (!this.className.equals(config.getFieldClassNameSequential()))
            throw new InvalidKerasConfigurationException(
                    "Keras model class name " + this.className + " incompatible with MultiLayerNetwork");
        if (this.inputLayerNames.size() != 1)
            throw new InvalidKerasConfigurationException(
                    "MultiLayerNetwork expects only 1 input (found " + this.inputLayerNames.size() + ")");
        if (this.outputLayerNames.size() != 1)
            throw new InvalidKerasConfigurationException(
                    "MultiLayerNetwork expects only 1 output (found " + this.outputLayerNames.size() + ")");

        NeuralNetConfiguration.Builder modelBuilder = new NeuralNetConfiguration.Builder();

        if (optimizer != null) {
            modelBuilder.updater(optimizer);
        }

        NeuralNetConfiguration.ListBuilder listBuilder = modelBuilder.list();

        /* Add layers one at a time. */
        KerasLayer prevLayer = null;
        int layerIndex = 0;
        for (KerasLayer layer : this.layersOrdered) {
            if (layer.isLayer()) {
                int nbInbound = layer.getInboundLayerNames().size();
                if (nbInbound != 1)
                    throw new InvalidKerasConfigurationException(
                            "Layers in MultiLayerConfiguration must have exactly one inbound layer (found "
                                    + nbInbound + " for layer " + layer.getLayerName() + ")");
                if (prevLayer != null) {
                    InputType[] inputTypes = new InputType[1];
                    InputPreProcessor preprocessor;
                    if (prevLayer.isInputPreProcessor()) {
                        inputTypes[0] = this.outputTypes.get(prevLayer.getInboundLayerNames().get(0));
                        preprocessor = prevLayer.getInputPreprocessor(inputTypes);
                    } else {
                        inputTypes[0] = this.outputTypes.get(prevLayer.getLayerName());
                        preprocessor = layer.getInputPreprocessor(inputTypes);
                    }
                    if (preprocessor != null)
                        listBuilder.inputPreProcessor(layerIndex, preprocessor);
                }
                listBuilder.layer(layerIndex++, layer.getLayer());
            } else if (layer.getVertex() != null)
                throw new InvalidKerasConfigurationException("Cannot add vertex to MultiLayerConfiguration (class name "
                        + layer.getClassName() + ", layer name " + layer.getLayerName() + ")");
            prevLayer = layer;
        }

        InputType inputType = this.layersOrdered.get(0).getOutputType();
        if (inputType != null)
            listBuilder.setInputType(inputType);

        /* Whether to use standard backprop (or BPTT) or truncated BPTT. */
        if (this.useTruncatedBPTT && this.truncatedBPTT > 0)
            listBuilder.backpropType(BackpropType.TruncatedBPTT).tBPTTForwardLength(truncatedBPTT)
                    .tBPTTBackwardLength(truncatedBPTT);
        else
            listBuilder.backpropType(BackpropType.Standard);
        return listBuilder.build();
    }