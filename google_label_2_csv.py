import json

hand = open('Labeled places 21-4-11.json')

info = json.load(hand)
fileForWrite = 'info.csv'


def fileWrite(fileName, message):
    fp = open(fileName, "a+")
    for item in message:
        fp.write(item)

    fp.write("\n")
    fp.close()


#print(info['features'])

sl = 0
for var in info['features']:
    name = var['properties']['name']
    lat = str(var['geometry']['coordinates'][1])
    lon = str(var['geometry']['coordinates'][0])
    sl += 1
    sln = str(sl)
    data = sln + ',' + name +',' + lat + ',' +lon
    print(data)
    fileWrite(fileForWrite, data)