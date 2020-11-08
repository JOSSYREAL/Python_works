sentence = input("Enter sentence: ")

#defining the class for the Longest word
class LongestWord:
	word_length = {}

	#definig the constructor
	def __init__(self, sentence):
		self.sentence = sentence
		self.word_list = []

	# @property
	def word_len_cal(self):
		self.length = 0
		self.longest = ""
		self.sent_split = self.sentence.split(" ")
		for word in self.sent_split:
			self.new_word = ""
			for letter in word:
				if not letter.isalpha():
					continue
				self.new_word += letter
			if self.new_word in self.word_list:
				continue
			self.word_list.append(self.new_word)
		for word in self.word_list:
			if len(word) > self.length:
				self.length = len(word)
				self.longest = word
		return f'Longest Word: {self.longest}\nLetters: {self.length}'

#creating an instance object of the class
longest = LongestWord(sentence)
print(longest.word_len_cal())
