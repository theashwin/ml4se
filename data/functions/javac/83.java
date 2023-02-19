public static double getStirlingError(double z) {
        double ret;
        if (z < 15.0) {
            double z2 = 2.0 * z;
            if (FastMath.floor(z2) == z2) {
                ret = EXACT_STIRLING_ERRORS[(int) z2];
            } else {
                ret = Gamma.logGamma(z + 1.0) - (z + 0.5) * FastMath.log(z) + z - HALF_LOG_2_PI;
            }
        } else {
            double z2 = z * z;
            ret = (0.083333333333333333333 - (0.00277777777777777777778 - (0.00079365079365079365079365
                            - (0.000595238095238095238095238 - 0.0008417508417508417508417508 / z2) / z2) / z2) / z2)
                            / z;
        }
        return ret;
    }