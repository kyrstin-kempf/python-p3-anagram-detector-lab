class Anagram:

    def __init__(self, word):
        self.word = sorted([l for l in word])

    def match(self, list):
        new_list = []

        for w in list:
            if sorted([letter for letter in w]) == self.word:
                new_list.append(w)
        
        return new_list