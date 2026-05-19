""" 

khái niệm thứ tự thực thi:

Kiểm tra từng điều kiện theo thứ tự từ trên xuống dưới
Nếu gặp điều kiện đúng đầu tiên:
thực thi khối lệnh tương ứng
bỏ qua toàn bộ các nhánh còn lại

Python gặp điều kiện >100 trước nên chương trình 
dừng luôn tại YELLOW và không tới RED.
"""

heart_rate = int(input("Enter patient's heart rate: "))

if heart_rate > 120:
    print("Priority: RED - Critical. Immediate attention required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Required ultrasound.")
else:
    print("Priority: ORANGE - Moderate. Monitor regularly.")