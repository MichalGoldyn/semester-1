# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Arctic Monkeys": [["Whatever People Say I Am, That's What I'm Not", "2006-01-23"], ["Favourite Worst Nightmare", "2007-04-18"], ["Humbug", "2009-08-19"], ["Suck It and See", "2011-06-06"], ["AM", "2013-09-09"], ["Tranquility Base Hotel & Casino", "2018-05-11"], ["The Car", "2022-10-21"]],
    "Radiohead": [["Pablo Honey", "1993-02-22"], ["The Bends", "1995-03-13"], ["OK Computer", "1997-06-16"], ["Kid A", "2000-10-02"], ["Amnesiac", "2001-06-05"], ["Hail to the Thief", "2003-06-09"], ["In Rainbows", "2007-10-10"], ["The King of Limbs", "2011-02-18"], ["A Moon Shaped Pool", "2016-05-08"]],
    "Queen": [["Queen", "1973-07-13"], ["Queen II", "1974-03-08"], ["Sheer Heart Attack", "1974-11-08"], ["A Night at the Opera", "1975-11-21"], ["A Day at the Races", "1976-12-10"], ["News of the World", "1977-10-28"], ["Jazz", "1978-11-10"], ["The Game", "1980-06-30"], ["Innuendo", "1991-02-04"]],
    "Daft Punk": [["Homework", "1997-01-20"], ["Discovery", "2001-03-12"], ["Human After All", "2005-03-14"], ["Random Access Memories", "2013-05-17"]],
    "Billie Eilish": [["When We All Fall Asleep, Where Do We Go?", "2019-03-29"], ["Happier Than Ever", "2021-07-30"], ["Hit Me Hard and Soft", "2024-05-17"]]
}

# Pretty-print the data structure
#pprint(music)
# Display details of one album recorded by a specific artist
#pprint(music.get("Queen"))

totalAlbums = 0
for i in music:
    temp = music.get(i)
    for y in temp:
        totalAlbums += 1


print(totalAlbums)