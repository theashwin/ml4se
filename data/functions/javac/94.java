AutoBuffer call(AutoBuffer ab) {
    int tnum = ab.getTask();
    RPC<?> t = ab._h2o.taskGet(tnum);
    // Forgotten task, but still must ACKACK
    if( t == null ) return RPC.ackack(ab,tnum);
    return t.response(ab); // Do the 2nd half of this task, includes ACKACK
  }