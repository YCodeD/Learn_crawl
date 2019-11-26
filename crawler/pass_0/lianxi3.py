import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
music = res.content

f = open('Ranbow.mp3', 'wb')
f.write(music)

f.close()
