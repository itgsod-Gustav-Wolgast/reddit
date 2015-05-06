from pprint import pprint

import reddit

url_me = "https://oauth.reddit.com/api/v1/me"
url_about = "https://oauth.reddit.com/api/v1/user/{username}/about"
url_submit = "https://oauth.reddit.com/api/submit"
url_comment = "https://oauth.reddit.com/api/comment"


class User(object):

    def __init__(self, reddit_id):
        self.id = reddit_id


    def me (self):

        return(reddit.client.request(url_me))



    def link_karma (self):

        return reddit.client.request(url_me)['link_karma']