package com.example.designpatterns._11_fliyweight.after;

/**
 * immutable
 * (상속을 막고, setter 를 생성하지 않는다.)
 */
public final class Font {
    final String family;
    final int size;

    public Font(String family, int size) {
        this.family = family;
        this.size = size;
    }

    public String getFamily() {
        return family;
    }

    public int getSize() {
        return size;
    }
}
