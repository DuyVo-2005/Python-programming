import json
# Dữ liệu Python (dictionary hoặc list)
data_to_write = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Ghi dữ liệu vào tệp JSON
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data_to_write, file, ensure_ascii=False, indent=4)  # Ghi dữ liệu dạng JSON