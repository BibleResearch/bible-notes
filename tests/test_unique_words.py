#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find duplicate words."""

import os
import re
import string


def find_duplicate_words(file_path, file_name):
    errors = 0

    with open(file_path) as f:
        file_text = f.read()

    word_pattern = '[^<]\w+'

    words = [word.strip().lower() for word in re.findall(word_pattern, file_text)]

    for index in range(0, len(words)):
        this_word = words[index]

        # don't check 'words' that start with numbers
        if this_word[0] in string.digits:
            continue

        # ignore words that are the name of the book of the bible
        if this_word in file_name:
            continue

        try:
            next_word = words[index + 1]
        except IndexError:
            break

        try:
            assert this_word != next_word
        except AssertionError as e:
            print("Found duplicate words: '{}' in {}".format(this_word, file_path))
            errors += 1

    return errors


def test_duplicate_words_ot():
    errors = 0
    for path, dirs, files in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), '../old_testament'))):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(path, file_name)
                errors += find_duplicate_words(file_path, file_name)

    print("\nFound {} errors in the OT".format(errors))
    assert errors == 0


def test_duplicate_words_nt():
    errors = 0
    for path, dirs, files in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), '../new_testament'))):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(path, file_name)
                errors += find_duplicate_words(file_path, file_name)

    print("\nFound {} errors in the NT".format(errors))
    assert errors == 0
