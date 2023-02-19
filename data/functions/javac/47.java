public static Validation<String> moreThan(int size, String msg) {
        return notEmpty().and(SimpleValidation.from((s) -> s.length() >= size, format(msg, size)));
    }