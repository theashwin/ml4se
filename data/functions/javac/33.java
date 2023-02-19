public static String resolveWildCardForJarSpec(String workingDirectory, String unresolvedJarSpec,
      Logger log) {

    log.debug("resolveWildCardForJarSpec: unresolved jar specification: " + unresolvedJarSpec);
    log.debug("working directory: " + workingDirectory);

    if (unresolvedJarSpec == null || unresolvedJarSpec.isEmpty()) {
      return "";
    }

    StringBuilder resolvedJarSpec = new StringBuilder();

    String[] unresolvedJarSpecList = unresolvedJarSpec.split(",");
    for (String s : unresolvedJarSpecList) {
      // if need resolution
      if (s.endsWith("*")) {
        // remove last 2 characters to get to the folder
        String dirName = String.format("%s/%s", workingDirectory, s.substring(0, s.length() - 2));

        File[] jars = null;
        try {
          jars = getFilesInFolderByRegex(new File(dirName), ".*jar");
        } catch (FileNotFoundException fnfe) {
          log.warn("folder does not exist: " + dirName);
          continue;
        }

        // if the folder is there, add them to the jar list
        for (File jar : jars) {
          resolvedJarSpec.append(jar.toString()).append(",");
        }
      } else { // no need for resolution
        resolvedJarSpec.append(s).append(",");
      }
    }

    log.debug("resolveWildCardForJarSpec: resolvedJarSpec: " + resolvedJarSpec);

    // remove the trailing comma
    int lastCharIndex = resolvedJarSpec.length() - 1;
    if (lastCharIndex >= 0 && resolvedJarSpec.charAt(lastCharIndex) == ',') {
      resolvedJarSpec.deleteCharAt(lastCharIndex);
    }

    return resolvedJarSpec.toString();
  }