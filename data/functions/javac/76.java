public static List<RepoBranch> getRepoBranch(AbstractBuild r) {
        List<RepoBranch> list = new ArrayList<>();
        return getRepoBranchFromScmObject(r.getProject().getScm(), r);
    }