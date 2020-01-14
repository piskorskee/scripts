import requests

#request = requests.get('http://api.open-notify.org')
#print(request.text)

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text) # to robi to samo
people_json = people.json()
print(people_json) # co to ;)

# To print the number of people in space
print("Number of people in space:", people_json['number'])
# To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])

location = requests.get('http://api.open-notify.org/iss-now.json')
print(location.text)

location_json = location.json()
pos = location_json['iss_position']
print(pos['longitude'])
print(pos['latitude'])

