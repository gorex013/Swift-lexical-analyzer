//
// Created by vasile on 15/09/18.
//

#ifndef SWIFT_LEXICAL_ANALYZER_DEFINITIONS_H
#define SWIFT_LEXICAL_ANALYZER_DEFINITIONS_H

inline bool is_alpha(int c) {
    return 'A' <= c && c <= 'Z' || 'a' <= c && c <= 'z';
}

inline bool is_digit(int c) {
    return '0' <= c && c <= '9';
}

inline bool is_arithmetic_operator(int c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

bool is_in_alphabet(int c) {
    return is_alpha(c) || is_digit(c) || is_arithmetic_operator(c);
}

#endif //SWIFT_LEXICAL_ANALYZER_DEFINITIONS_H
