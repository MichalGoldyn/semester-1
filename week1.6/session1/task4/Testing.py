from datetime import datetime
from quake import *
from feed import *




now = datetime.now()
q = Quake(now, 139.9, 28.0, 473.0, 7.0)
print(q)

feed = QuakeFeed("4.5", "week")
print(feed)
reader = feed.reader()