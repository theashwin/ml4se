private boolean openTagSet(String filename)
    {
        int max_size = 0;
        InputStreamReader isr = null;
        y_.clear();
        try
        {
            isr = new InputStreamReader(IOUtil.newInputStream(filename), "UTF-8");
            BufferedReader br = new BufferedReader(isr);
            String line;
            while ((line = br.readLine()) != null)
            {
                if (line.length() == 0)
                {
                    continue;
                }
                char firstChar = line.charAt(0);
                if (firstChar == '\0' || firstChar == ' ' || firstChar == '\t')
                {
                    continue;
                }
                String[] cols = line.split("[\t ]", -1);
                if (max_size == 0)
                {
                    max_size = cols.length;
                }
                if (max_size != cols.length)
                {
                    String msg = "inconsistent column size: " + max_size +
                        " " + cols.length + " " + filename;
                    throw new RuntimeException(msg);
                }
                xsize_ = cols.length - 1;
                if (y_.indexOf(cols[max_size - 1]) == -1)
                {
                    y_.add(cols[max_size - 1]);
                }
            }
            Collections.sort(y_);
            br.close();
        }
        catch (Exception e)
        {
            if (isr != null)
            {
                try
                {
                    isr.close();
                }
                catch (Exception e2)
                {
                }
            }
            e.printStackTrace();
            System.err.println("Error reading " + filename);
            return false;
        }
        return true;
    }