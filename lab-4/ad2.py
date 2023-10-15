import json


data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)


print("JSON String:")
print(json_string)

json_data = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'
parsed_data = json.loads(json_data)

print("\nPython Dictionary:")
print(parsed_data)
