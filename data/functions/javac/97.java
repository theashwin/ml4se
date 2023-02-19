private InputStream getResourceStream(File file, String resourceName) {
        try {
            JarFile jarFile = (JarFile) jarFiles.get(file);
            if (jarFile == null && file.isDirectory()) {
                File resource = new File(file, resourceName);
                if (resource.exists()) {
                    return Files.newInputStream(resource.toPath());
                }
            } else {
                if (jarFile == null) {
                    if (file.exists()) {
                        jarFile = new JarFile(file);
                        jarFiles.put(file, jarFile);
                    } else {
                        return null;
                    }
                    //to eliminate a race condition, retrieve the entry
                    //that is in the hash table under that filename
                    jarFile = (JarFile) jarFiles.get(file);
                }
                JarEntry entry = jarFile.getJarEntry(resourceName);
                if (entry != null) {
                    return jarFile.getInputStream(entry);
                }
            }
        } catch (Exception e) {
            log("Ignoring Exception " + e.getClass().getName() + ": " + e.getMessage()
                    + " reading resource " + resourceName + " from " + file, Project.MSG_VERBOSE);
        }
        return null;
    }