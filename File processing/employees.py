from xml.dom.minidom import parse
import xml.dom.minidom
# Mở file xml bằng minidom parser
DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement
# Lấy tất cả tag là employee
employees = collection.getElementsByTagName("employee")
# Duyệt vòng lặp để lấy toàn bộ dữ liệu ra
for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    id=tag_id.childNodes[0].data
    tag_name = employee.getElementsByTagName('name')[0]
    name=tag_name.childNodes[0].data
    print(id,'\t',name)