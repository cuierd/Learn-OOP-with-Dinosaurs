#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: # Cui Ding(olatname: cding)
# Matriculation Numbers: # 21-718-945
# 			Mia Tatjana Egli (olatname: miaegl)
# Matriculation Numbers: 21-700-406


from unittest import TestCase, main
from processing import Joke, JokeGenerator
from os import path


class ProcessingTest(TestCase):
    """
    processing.py non functional tests
    """

    def setUp(self):
        self.gen = JokeGenerator("dadjokes_sample.csv")

    def test_attributes(self):
        # We have added some targets here.
        self.gen.make_jokes_objects()
        actual = self.gen.jokes_objects_list[4]
        higher_one = self.gen.jokes_objects_list[22]
        actual.tell_joke()
        higher_one.split_into_sentences()
        

        self.assertEqual(actual.author, "fredinNH")  # TODO: add targets! ??Cannot understand what to do.
        											# we added target above.
        self.assertEqual(actual.link, "https://old.reddit.com/r/dadjokes/comments/rb1tys/why_do_the_numbers_3_and_5_make_such_a_great_team/")
        self.assertEqual(actual.pure_joke, "Why do the numbers 3 and 5 make such a great team? Because together they thrive.")
        self.assertEqual(actual.score, 2578)
        self.assertEqual(actual.time, "2021-12-07 15:36:32")
        self.assertIsInstance(actual._raw_joke, list)
        self.assertEqual(actual.profanity_counts, 0)
        self.assertIn("False", actual==higher_one)
        self.assertIn("12679", actual==higher_one)
        self.assertEqual(higher_one.length, 2)
        

if __name__ == '__main__':
    main()
