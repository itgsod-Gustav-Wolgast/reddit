class SpellChecker(object):
    def __init__(self, data):
        self.data = data

    def check_if_alot(self):
        for s in self.data.split(" "):
            if s == "alot" or s == "Alot":
                return True


