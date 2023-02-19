@Override
    public void recognition(Term[] terms) {
        this.terms = terms;
        List<Term> termList = recogntion_();
        for (Term term2 : termList) {
            TermUtil.insertTerm(terms, term2, InsertTermType.SCORE_ADD_SORT);
        }
    }