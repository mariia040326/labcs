class Text:
    def __init__(self,words,topic_text):
        self.words=list(words)
        self.topic_text=topic_text
    def num_nothing(self):
        s=0
        for el in self.words:
            if el ==' ':
                el=1
                s+=el
        return print(s)
    def num_letters(self):
        s=0
        for el in self.words:
            if el ==' ':
                continue
            else:
                el=1
                s+=el
        return print(s)

    def change_num(self):
        for el in self.words:
            self.words[0] = 'g'
            self.words[1] = 'o'
            self.words[2] = 'o'
            self.words[3] = 'd'
        return print(self.words)


c=Text('п kg hg')
c.change_num()

