# Documentations at https://instaloader.github.io/as-module.html

from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

USER = 'askzeyknow'
PASSWORD = '?Welcome5'

L = instaloader.Instaloader()
L.login(USER, PASSWORD)   

posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()

SINCE = datetime(2015, 5, 1)
UNTIL = datetime(2015, 3, 1)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, "instagram")