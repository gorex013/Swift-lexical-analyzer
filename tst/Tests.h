//
// Created by vasile on 16/09/18.
//

#ifndef SWIFT_LEXICAL_ANALYZER_TESTS_H
#define SWIFT_LEXICAL_ANALYZER_TESTS_H

#include "catch.hpp"
#include <string>


char c() {
    return 'c';
}

TEST_CASE("Constant is correctly declared", "[Constant][Declaration]") {
REQUIRE (c()

== 'c');
}


#endif //SWIFT_LEXICAL_ANALYZER_TESTS_H
