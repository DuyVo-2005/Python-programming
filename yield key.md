Trong Python, từ khóa `yield` được sử dụng trong hàm để tạo ra **generator** (trình tạo), một loại hàm đặc biệt trả về giá trị từng phần thay vì trả về toàn bộ giá trị một lần như hàm thông thường (`return`). Điều này đặc biệt hữu ích khi làm việc với các bộ dữ liệu lớn hoặc cần hiệu suất cao.

Cụ thể:

- Khi hàm chứa từ khóa `yield`, nó không còn là một hàm thông thường mà trở thành một generator.
- Mỗi lần hàm được gọi hoặc lặp lại, câu lệnh `yield` sẽ trả về một giá trị và tạm dừng trạng thái của hàm tại đó, chờ lần gọi tiếp theo.

Nếu bạn thấy cụm từ `yield arr` trong mã, điều này có nghĩa rằng hàm đang trả về giá trị của biến `arr` (hoặc một phần tử nào đó trong mảng `arr`) tại thời điểm đó và tạm dừng ở dòng `yield`.

### Ví dụ minh họa:
```python
def generate_numbers(arr):
    for num in arr:
        yield num

# Sử dụng hàm
arr = [1, 2, 3, 4]
gen = generate_numbers(arr)

# Duyệt qua generator
for value in gen:
    print(value)
```

**Kết quả:**
```
1
2
3
4
```

**Giải thích:**
1. `yield num` trả về từng giá trị trong danh sách `arr`.
2. Mỗi lần `for` lặp lại, generator tiếp tục từ nơi nó dừng lại.

### Điểm khác biệt giữa `yield` và `return`:
| Đặc điểm                 | `yield`                          | `return`                  |
|--------------------------|-----------------------------------|---------------------------|
| Kết quả trả về           | Trả về từng phần, tiếp tục chạy. | Trả về giá trị và kết thúc hàm. |
| Bộ nhớ                   | Tiết kiệm bộ nhớ (lazy evaluation). | Có thể tiêu tốn nhiều bộ nhớ hơn. |
| Sử dụng với vòng lặp     | Tương thích tốt với lặp lớn.     | Không tối ưu với lặp lớn. | 

Nói cách khác, `yield` là công cụ quan trọng để làm việc với **dữ liệu tuần tự lớn** hoặc **xử lý từng phần** trong các hàm generator.
