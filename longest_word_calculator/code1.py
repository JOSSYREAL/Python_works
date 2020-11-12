#class for word frequency counter


class Counter:

    #defining the constructor
    def __init__(self):
        self.word_freq = {}
        self.new_sentence = ""
        self.word_list = []
    #defining class desciption
    def __str__(self):
        return f'this is for calculating the frequency of words'
    def remov_nonchar(self, sentence):
        for character in sentence:
            if character == " ":
                self.new_sentence += character
            if not character.isalnum():
                continue
            self.new_sentence += character
        return self.new_sentence
    def count(self):
        self.word_list = self.new_sentence.split(" ")
        for word in self.word_list:
            self.word_freq[word] = self.word_freq.get(word, 0)+1
        return self.word_freq

    #to output the word frequency table
    def maxima(self):
        self.high_value = 0
        print("Words","\t","Frequency")
        for word, value in self.word_freq.items():
            print(word, "\t", ":", value)
            if value > self.high_value:
                self.high_value = value
                self.high_word = word
        return f'Highest Frequency: {self.high_word}\nNumber of Times: {self.high_value}'



sentence  = input("Enter sentence: ")
inst = Counter()
inst.remov_nonchar(sentence)
print(inst.count())
print(inst.maxima())
#to print what is inside the __str__ method which is for description
print(inst)
