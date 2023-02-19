public List<VocabularyWord> words() {
        List<VocabularyWord> vocab = new ArrayList<>(vocabulary.values());
        Collections.sort(vocab, new Comparator<VocabularyWord>() {
            @Override
            public int compare(VocabularyWord o1, VocabularyWord o2) {
                return Integer.compare(o2.getCount(), o1.getCount());
            }
        });

        return vocab;
    }