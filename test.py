from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.post import Post
from reddit.spell_checker import SpellChecker
from reddit.save import Save

bojohan = client.login('gurrren')

# python = Subreddit("python")
#
# python.hot()

# Here I show how the bot works

sub = Subreddit("globaloffensive")

p = Post(sub.hot_children()[0])

spell = SpellChecker(p.title())

if spell.check_if_alot():
    save = Save(p.data())

    save.save_link()

################################







