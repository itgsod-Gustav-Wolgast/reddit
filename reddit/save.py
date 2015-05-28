class Save(object):
    def __init__(self, data):
        self.data = data

    def save_link(self):
        url = self.data['url']

        f = open("urls.txt", "r+")

        for r in f.readlines():
            if r + "\n" == url:
                file.close()

        f.write(url + "\n")

        f.close()

