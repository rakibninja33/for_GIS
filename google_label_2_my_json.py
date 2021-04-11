import json

hand = open('Labeled places 21-4-11.json')

info = json.load(hand)
fileForWrite = 'info.csv'

label = dict()
coordinates = list()

# print(info['features'])

for var in info['features']:
    name = var['properties']['name']
    lat = str(var['geometry']['coordinates'][1])
    lon = str(var['geometry']['coordinates'][0])

    label[name] = [lat, lon]

print(label)

print(json.dumps(label, indent=2))

f = open('new_label.json', 'w')
json.dump(label, f, indent=2)