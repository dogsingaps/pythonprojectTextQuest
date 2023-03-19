import io
file = io.open("metric.txt", encoding="utf8")
text = file.read()


class Text:
    def __init__(self, text):
        self.tekst = text
        self.lang = "rus"
        self.sents = []
        sentences = text.split(".""!""?")
        for s in sentences:
            self.sents.append(Sentence(s))

    def get_asl(self):
        asl = sum([s.get_len_full() for s in self.sents]) / len(self.sents)
        return asl

    def get_asw(self):
        asw = sum([s.get_len_words() for s in self.sents]) / sum(s.get_words() for s in self.sents)
        return asw

    def get_ifk(self):
        ifk = 206.835 - 1.52 * self.get_asl() - 65.14 * self.get_asw()
        return ifk


class Sentence:
    def __init__(self, sent):
        self.sent = sent
        self.words = [Word(w) for w in self.sent.split()]

    def get_len_full(self):
        return len(self.sent)

    def get_len_words(self):
        return sum([w.get_len() for w in self.words])

    def get_words(self):
        return len(self.words)


class Word:
    def __init__(self, word):
        self.word = word

    def get_len(self):
        syll = len(self.word.split("у""е""а""о""э""я""и""ю"))
        return syll


txt1 = Text(text)
print(txt1.get_asl())
print(txt1.get_asw())
print(txt1.get_ifk())

