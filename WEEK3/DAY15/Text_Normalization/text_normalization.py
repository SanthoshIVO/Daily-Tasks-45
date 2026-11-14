class Text_Normalization():

    def __init__(self, data):
        self.data = data
        self.start()
    def start(self):
        print('''
                1) Coverting strings to lower case
                2) Removing punctuations
                3) removing spl chars
                4) handling emoji's
                5) removing extra spaces
                6) contractions
                7) Correcting the words
              ''')
    

    def strings_lowercase(self, data):
        # this function will return updated text
        self.data = self.data.lower()

    def removing_punctuations(self):
        chars = self.data
        import string
        punctuations = string.punctuation
        for char in punctuations:
            chars = chars.replace(char,'')
        self.data = chars

    def removing_spl_char(self, data):
        char = self.data
        for char in data:
            if not char.isalnum() and not ord(char) == 32:
                chars = chars.replace(char, '')
        self.data = chars

    def normalizedtext(self, data):
        pass

obj = Text_Normalization(data = 'hello man')
