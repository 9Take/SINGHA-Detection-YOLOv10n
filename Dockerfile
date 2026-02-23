# ใช้ Image ที่รองรับ GPU และ YOLOv8/v11
FROM ultralytics/ultralytics:latest-python

# ป้องกันไม่ให้ Matplotlib ถามหาการตั้งค่า Timezone ตอนติดตั้ง
ENV DEBIAN_FRONTEND=noninteractive

# ติดตั้ง System Libraries ที่จำเป็นสำหรับ GUI (ป้องกัน libGL error)
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# ตั้งค่า Working Directory
WORKDIR /app

# Copy requirements และติดตั้ง Python Libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# (Optional) ตั้งค่า Matplotlib backend ให้ทำงานกับ X11 ได้ดีขึ้น
ENV QT_X11_NO_MITSHM=1

CMD ["bash"]