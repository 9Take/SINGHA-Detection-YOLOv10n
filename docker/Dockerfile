# ใช้ Image จาก Ultralytics เป็นฐาน
FROM ultralytics/ultralytics:latest-python

# ติดตั้ง System Dependencies สำหรับ GUI และ OpenCV
RUN apt-get update && apt-get install -y \
    python3-venv \
    python3-tk \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# 1. สร้าง Virtual Environment
RUN python3 -m venv /opt/env

# 2. ตั้งค่า PATH ให้ระบบเรียกใช้ venv เป็นหลัก (ไม่ต้องสั่ง source activate)
ENV PATH="/opt/env/bin:$PATH"

WORKDIR /app

# 3. อัปเกรด pip และติดตั้ง Library ใน venv
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["bash"]