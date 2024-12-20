import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#rect (rectangle) đại diện cho một thanh cụ thể trong danh sách rects (tập hợp các thanh của biểu đồ). [trả về trong hàm bar]

def bubble_sort_visual(arr):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge", color='y')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    swaps = [0]  # Đếm số lần hoán vị

    def update_fig(data, rects, swaps):
        arr, j, swapped = data
        for rect, val in zip(rects, arr):
            rect.set_height(val)
            rect.set_color('y')  # Đặt lại màu mặc định
        if j is not None:
            rects[j].set_color('r')  # Cột đang xét
            rects[j+1].set_color('g')  # Cột kế tiếp
        if swapped:
            swaps[0] += 1  # Tăng số lần hoán vị
        text.set_text(f"Number of swaps: {swaps[0]}")

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    yield arr, j, True  # Trả về trạng thái hoán vị
                else:
                    yield arr, j, False  # Không hoán vị
            if not swapped:
                break
        yield arr, None, False  # Hoàn tất

    anim = animation.FuncAnimation(
        fig, func=update_fig, 
        frames=bubble_sort(arr), 
        fargs=(bar_rects, swaps), 
        repeat=False, 
        blit=False, 
        interval=300
    )

    plt.show()

# Ví dụ sử dụng
arr = np.random.randint(1, 50, 20)  # Mảng ngẫu nhiên với 20 phần tử
bubble_sort_visual(arr)
