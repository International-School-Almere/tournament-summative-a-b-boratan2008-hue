import json

# --- DEFINE THE DATA ---
data = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "music"]
}

# --- WRITE TO JSON FILE ---
with open("file.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON file created!")

# --- READ THE JSON FILE ---
with open("file.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Loaded data:", loaded)
print("Name:", loaded["name"])
print("City:", loaded["city"])