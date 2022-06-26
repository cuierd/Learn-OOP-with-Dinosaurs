#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Cui Ding(olatname: cding)
# Matriculation Numbers: 21-718-945
# 			Mia Tatjana Egli (olatname: miaegl)
# Matriculation Numbers: 21-700-406


import time
from typing import List, Tuple
import re
import random
import csv

class Joke:
	"""
	Generate joke object,
	which has attributes such as post_num, pure_joke, filtered_joke.
	It also has methods such as tokenize, split_into_sentences and filter_profanity.
	By calling its method tell_joke, each post can be printed to the screen in a build_up way.
	"""
	# post_num = 0
	def __init__(self, raw_joke: list) -> None:
		# self.post_num = Joke.get_post_num()
		self._raw_joke = [items for items in raw_joke if items]
		self.pure_joke = "".join(self._raw_joke[2:-2])
		self.filtered_joke = []
		self.score = int(self._raw_joke[-2])
		self.time = self._raw_joke[-1]
		self.author = self._raw_joke[0]
		self.link = self._raw_joke[1]
		self.profanity_counts = 0
		self.length = 0

	# @classmethod
	# def get_post_num(cls):
	# 	cls.post_num += 1
	# 	return cls.post_num

	def __remove_nonstandard_char(self) -> None:
		"""
		Non-standard characters, like emojis, removed.
		Original format kept.
		"""
		self.pure_joke = "".join([char for char in self.pure_joke if ord(char) < 8300])

	def split_into_sentences(self) -> List[str]:
		"""
		Split a line into a list of sentences.
		The line split at t_he punctuations or \n.
		where the punctuations followed by A-Z,0-9,(.
		"""
		self.__remove_nonstandard_char()
		str_list = [sent for sent in re.split(r'(\n|[A-Z][^.?!")…]+. "$|["(]?[A-Z][^.?!")…]+[.?!")…]+ )', self.pure_joke) if sent]
		self.length = len(str_list)
		return str_list

	def __tokenize(self) -> List[List[str]]:
		"""
		Take a list of sentences.
		Split sentence into tokens.

		:return: a list of lists containing tokens.
		"""
		sentences_str = self.split_into_sentences()
		token_sents_list = []
		for sent in sentences_str:
			# to tokenize punctuation.
			sent = re.sub(r'([!"#$%&*+,()./:;<=>?@[\]^_`{|}~])', r' \1 ', sent)
			token_in_sent = [token for token in sent.split(' ') if token]
			token_sents_list.append(token_in_sent)
 		return token_sents_list

	def _filter_profanity(self, filename="profanities.txt") -> Tuple[List[List[str]], int]:
		"""
		Given the tokens of the sentences of each post,
		censor the profanities which were listed in a given file.

		:param filename: a file containing profanities.
		:return: a tuple of a list and an integer, where the elements mean:
				1. A list of tokenized sentences in the form of lists of tokens,
					profanity is replaced by hashtags of the same length.
				2. counts of profanities per post.
		"""
		filtered_sents_list = []
		token_sents_list = self.__tokenize()
		# get profanities set.
		with open(filename, "r", encoding="utf-8") as infile:
			profanity_set = {line.strip() for line in infile}
		for sents in token_sents_list:
			filtered_sents = []
			for token in sents:
				for profanity_word in profanity_set:
					if token.lower().startswith(profanity_word):
						self.profanity_counts += 1
						token = "#" * len(token)
				filtered_sents.append(token)
			filtered_sents_list.append(filtered_sents)
		return filtered_sents_list, self.profanity_counts

	def __join_filtered_sents(self, filtered_sents_list: List[List[str]]) -> None:
		"""
		Given a list of lists of tokens, join tokens together into sentences.
		Get a list of strings of sentences.
		"""
		sents = [" ".join(sents) for sents in filtered_sents_list]
		for sentence in sents:
			# for print, ignore the "\n".
			if sentence:
				# make the punctuations stick the the words.
				sentence = re.sub(r'" (.+) "', r'"\1"', sentence)
				sentence = re.sub(r'^([("]) | (")$| ([!$%&*+,()-./:;<=>?@\[\]^_`{|}~]+)', r'\1\2\3', sentence)
				self.filtered_joke.append(sentence)

	def tell_joke(self) -> None:
		"""
		After calling function, joke be returned in a manner, that there is a small build up.
		The punchline is always the last sentence of the post.
		There is a small waiting period before the punchline is revealed.
		Also return jokes that are only one sentence long.
		"""
		filtered_sents_list, _ = self._filter_profanity("profanities.txt")
		self.__join_filtered_sents(filtered_sents_list)
		if len(self.filtered_joke) == 1:
			print(self.filtered_joke[0])
		else:
			for sent in self.filtered_joke[:-1]:
				print(sent)
			time.sleep(1)
			print(self.filtered_joke[-1])

	@staticmethod
	def pretty_print() -> None:
		"""
		Print a separate line for each post.
		"""
		# We don't know what to print. We think we've done the work in __join_filtered_sents() function
		# rather than here. It is possible to merge these two function together.
		print("---------------------------------------------------")

	def __repr__(self):
		"""
		print the content of a post of joke,
		as well as the caption line.
		"""
		filtered_sents_list, _ = self._filter_profanity()
		self.__join_filtered_sents(filtered_sents_list)
		return "\n".join(self.filtered_joke)

	def __eq__(self, other):
		"""
		Compare the scores of two posts of jokes.
		Return whether the scores are equal
		and the higher post and its score.
		"""
		if isinstance(other, Joke):
			if self.score > other.score:
				return f"False\n{self.filtered_joke} has higher score: {self.score}."
			elif self.score < other.score:
				return f"False\n{other.filtered_joke} has higher score: {other.score}."
			else:
				return True
		return False

	def __lt__(self, other):
		"""
		Compare whether a joke has lower score than the other.
		Return true or false.
		"""
		if isinstance(other, Joke):
			return self.score < other.score
		return False

	def __gt__(self, other):
		"""
		Compare whether a joke has higher score than the other.
		Return true or false.
		"""
		if isinstance(other, Joke):
			return self.score > other.score
		return False

	def __le__(self, other):
		"""
		Compare whether the score of a joke is lower than or equal to the other's.
		Return true or false.
		"""
		if isinstance(other, Joke):
			return self.score <= other.score
		return False

	def __ge__(self, other):
		"""
		Compare whether the score of a joke is higher than or equal to the other's.
		Return true or false.
		"""
		if isinstance(other, Joke):
			return self.score >= other.score
		return False


class JokeGenerator:
	"""
	Generate jokes from a database.
	"""

	def __init__(self, filename="dadjokes_sample.csv") -> None:
		self.filename = filename
		self.jokes_objects_list = []

	def make_jokes_objects(self) -> None:
		"""
		Open a joke file and get a joke_objects list.
		"""
		with open(self.filename, newline='', encoding='utf-8') as csvfile:
			next(csvfile, None)
			self.jokes_objects_list = [Joke(row) for row in csv.reader(csvfile, delimiter=",", quotechar="|")]

	def generate_jokes(self):
		"""
		From a joke_objects list, take any elements, generate jokes.
		"""
		for joke in self.jokes_objects_list:
			joke.split_into_sentences()
			if joke.length > 1:
				joke.pretty_print()
				joke.tell_joke()
				time.sleep(0.5)

	def random_joke(self):
		"""
		Return any random joke from the whole dataset and print it out
		"""
		random_joke_object = random.choice(self.jokes_objects_list)
		random_joke_object.tell_joke()

	def find_highest_upvoted_joke(self):
		highest_upvoted_joke = self.jokes_objects_list[0]
		for joke in self.jokes_objects_list:
			if joke > highest_upvoted_joke:
				highest_upvoted_joke = joke
		print(f"The highest upvoted joke (score = {highest_upvoted_joke.score}) is:")
		print(highest_upvoted_joke.pure_joke)


if __name__ == '__main__':

	joke_database = JokeGenerator("dadjokes_sample.csv")
	joke_database.make_jokes_objects()
	joke_database.generate_jokes()
	print("------------------------------------------")
	print("Now generate a random joke:")
	joke_database.random_joke()
	print("------------------------------------------")
	joke_database.find_highest_upvoted_joke()



