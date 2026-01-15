import csv,json,requests

student = []

try:
    with open('data.csv') as f:
      reader = csv.DictReader(f)
        for i in reader():
            student.append(i)
except Exception as e:
    print("The Exception occurs ",e)

try:
    json_data =  json.dumps(student, indent=4)
    print(json_data)

api_url = "url"

response = requests.post('url', json= students)

if response.status_code == 200 or response.status_code == 201:
    print("response successfully accepted")
else:
    print(f"Failed to send the json data {response.status_code}")



