Hàm `enumerate()` trong Python là một hàm tiện ích dùng để lặp qua các phần tử của một chuỗi hoặc danh sách, đồng thời giữ lại chỉ số của mỗi phần tử. Nó trả về một đối tượng liệt kê có thể được chuyển thành danh sách tuple (chỉ số, giá trị). Đây là một công cụ rất hữu ích khi bạn cần cả chỉ số và giá trị của các phần tử trong một vòng lặp `for`.

### Cú pháp
```python
enumerate(iterable, start=0)
```
- `iterable`: Chuỗi hoặc danh sách cần lặp qua.
- `start`: Giá trị bắt đầu của chỉ số (mặc định là 0).

### Ví dụ
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
Kết quả:
```
0 apple
1 banana
2 cherry
```

Trong ví dụ này, `enumerate()` giúp bạn kết hợp chỉ số với mỗi phần tử trong danh sách `fruits`.

Bạn có cần thêm ví dụ khác hoặc có bất kỳ câu hỏi nào về cách sử dụng `enumerate()` không? 😊
