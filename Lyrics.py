lyrics = "Baa, baa, black sheep, have you any wool? \
Yes sir, yes sir, three bags full! \
One for the master, \
One for the dame, \
And one for the little boy \
Who lives down the lane \
Baa, baa, black sheep, \
Have you any wool? \
Yes sir, yes sir, \
Three bags full... \
Baa, baa, white sheep, \
have you any wool? \
yes sir, yes sir, \
three needles full."

lyrics = lyrics.replace(",","")
lyrics = lyrics.replace(".","")   
lyrics = lyrics.replace("?","")
lyrics = lyrics.replace("!","")
lyrics = lyrics.lower()
lyrics = lyrics.split()

lyricsDict = {}

for i in lyrics:
    lyricsDict[i] = lyrics.count(i)

print(lyricsDict[input("Find number of times which words appears: ")])

