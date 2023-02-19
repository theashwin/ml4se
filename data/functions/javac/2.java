public static boolean cleanDirectory(File dir) {
        if (dir.isDirectory()) {
            String[] children = dir.list();
            if (children != null) {
                for (String aChildren : children) {
                    boolean success = cleanDirectory(new File(dir, aChildren));
                    if (!success) {
                        return false;
                    }
                }
            }
        }
        return dir.delete();
    }