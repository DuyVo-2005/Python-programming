import json

# Đọc tệp JSON
with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Đọc và parse JSON thành Python dictionary

# Hiển thị dữ liệu
print(data)
