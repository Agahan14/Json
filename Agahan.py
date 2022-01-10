import json
json_string = """
{
"student": {
    "information" : [{
        "name": "James",
        "surname": "Bond",
        "age": 20,
        "university": "Oxford",
        "faculty": "Software engineering",
        "worker": ["programmer",{"worker_place":"Google"}, "husband for an hour"],
        "hobbies": [
            "coding", "music", "reading books", "footbal", "painting", "travelling"
        ],
        "married": false
        }]
    }
}
"""
data = json.loads(json_string)
for i in data["student"]["information"]:
    print(i)
new_json = json.dumps(data, indent=2)
print(new_json)
with open("my.json", "w") as file:
    json.dump(data, file, indent=3)