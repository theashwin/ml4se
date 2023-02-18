@Override
  protected Object primTransform(Object anObject) throws Exception {
    return Integer.valueOf(((Long) anObject).toString());
  }