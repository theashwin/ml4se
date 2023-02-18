protected boolean isMatchingZXY(Op opA, Op opB) {
        if (opA.z() == opB.x() || opA.z() == opB.y())
            return true;

        return false;
    }