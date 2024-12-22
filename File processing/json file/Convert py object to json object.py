# Chuyển đổi đối tượng Python sang chuỗi JSON
#Ví dụ:
import json
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}
jsonString = json.dumps(pythonObject)
print(jsonString)