public double[] getColumnPackedCopy()
    {
        double[] vals = new double[m * n];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                vals[i + j * m] = A[i][j];
            }
        }
        return vals;
    }