protected void createServiceWarningViewState(final Flow flow) {
        val stateWarning = createViewState(flow, CasWebflowConstants.STATE_ID_SHOW_WARNING_VIEW, CasWebflowConstants.VIEW_ID_CONFIRM);
        createTransitionForState(stateWarning, CasWebflowConstants.TRANSITION_ID_SUCCESS, "finalizeWarning");
        val finalizeWarn = createActionState(flow, "finalizeWarning", createEvaluateAction("serviceWarningAction"));
        createTransitionForState(finalizeWarn, CasWebflowConstants.STATE_ID_REDIRECT, CasWebflowConstants.STATE_ID_REDIRECT);
    }