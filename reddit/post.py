class Post():
    def __init__(self, post_data):
        self.post_data = post_data

    def data(self):
        return self.post_data['data']

    def title(self):
        return self.data()['title']

    def url(self):
        return self.data()['url']