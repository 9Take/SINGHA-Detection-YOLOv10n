import numpy as np
import matplotlib.pyplot as plt

# สร้างข้อมูลสุ่มด้วย NumPy
x = np.linspace(0, 10, 100)
y = np.sin(x)

print(f"NumPy version: {np.__version__}")

# พล็อตกราฟด้วย Matplotlib
plt.plot(x, y)
plt.title("Singha Detection - Signal Test")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show() # หน้าต่างนี้จะเด้งไปโชว์ที่เครื่อง Ubuntu ของคุณ