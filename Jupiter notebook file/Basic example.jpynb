# Tiêu đề: Phân Tích Dữ Liệu Mẫu
# Mô tả: Đây là một notebook mẫu bao gồm các bước cơ bản để xử lý và phân tích dữ liệu.

# 1. Import thư viện
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập hiển thị
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 2. Nạp và xem dữ liệu
# Đọc dữ liệu từ file CSV (ví dụ: 'data.csv')
# Bạn cần thay đường dẫn bằng file của riêng bạn
data = pd.read_csv("data.csv")
print("Thông tin dữ liệu:")
print(data.info())
print("\nXem trước dữ liệu:")
print(data.head())

# 3. Tiền xử lý dữ liệu
# Kiểm tra và xử lý giá trị bị thiếu
print("\nSố lượng giá trị thiếu mỗi cột:")
print(data.isnull().sum())
data.fillna(method='ffill', inplace=True)

# Loại bỏ các dòng hoặc cột không cần thiết
# data.drop(columns=['Unwanted_Column'], inplace=True)

# 4. Phân tích dữ liệu
# Phân phối dữ liệu
sns.histplot(data['Column_Name'], kde=True)
plt.title("Phân phối dữ liệu")
plt.show()

# Quan hệ giữa hai biến
sns.scatterplot(x=data['Feature_1'], y=data['Feature_2'])
plt.title("Mối quan hệ giữa Feature_1 và Feature_2")
plt.show()

# 5. Xây dựng mô hình (nếu cần)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Chuẩn bị dữ liệu
X = data.drop(columns=['Target'])
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện mô hình
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test)
print("Độ chính xác của mô hình:", accuracy_score(y_test, y_pred))

# 6. Kết luận
# Tổng kết lại những phân tích và kết quả.
print("Notebook hoàn thành!")
