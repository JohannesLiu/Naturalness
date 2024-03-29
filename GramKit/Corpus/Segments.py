
class Corpus(list):
    def __init__(self, corpus: list):
        self.data = corpus

    def getMoreNatural(self):
        NotImplemented


class Segments(Corpus):
    def __init__(self, corpus: list):
        Corpus.__init__(corpus)


class Segment(object):
    def __init__(self, segment: str):
        self.data = [x.lower() for x in segment.strip().split(" ")]

    def buildNGram(self, pos, n):
        return NGram(self.data[max(0, pos-n): pos])


class NGram():
    def __init__(self, tokens: list):
        self.tokens = tokens

    def __eq__(self, otherNGram):
        if otherNGram.tokens == self.tokens:
            return True
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.tokens))


if __name__ == "__main__":
    s = Segment("I love Python very much.")
    n1 = s.buildNGram(5, 3)
    n2 = s.buildNGram(4, 3)
    print(n1.tokens)


    m = dict()
    m[n1] = n2

    print(m[n1].tokens)
    exit