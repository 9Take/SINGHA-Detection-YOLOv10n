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

# ... (ส่วนบนของคุณเหมือนเดิม) ...

# 1. ติดตั้ง curl หรือ wget (จำเป็นสำหรับลง Oh My Bash)
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# 2. ติดตั้ง Oh My Bash แบบ Non-interactive
# 2. ติดตั้ง Oh My Bash แบบ Non-interactive (เปลี่ยนจาก sh เป็น bash)
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)" --unattended

# 3. บังคับให้ Bash ใน Docker รู้จัก Virtual Environment เสมอ
# และเปลี่ยน Theme (เลือกได้ตามใจชอบ เช่น font, agnoster, bobby)
RUN sed -i 's/OSH_THEME="font"/OSH_THEME="bobby"/' ~/.bashrc && \
    echo 'export PATH="/opt/env/bin:$PATH"' >> ~/.bashrc

WORKDIR /app

# 3. อัปเกรด pip และติดตั้ง Library ใน venv
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["bash"]