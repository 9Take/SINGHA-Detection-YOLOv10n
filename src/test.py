import cv2
from ultralytics import YOLO

# 1. โหลดโมเดลตัวที่เทรนมา 100 loops (best.pt)
 # แก้บรรทัดที่ 5 เป็นแบบนี้ (เปลี่ยน path ให้ตรงกับที่อยู่จริงของคุณ)
model = YOLO("/app/runs/detect/1000images/train3/weights/best.pt")
# model = YOLO("/app/runs/detect/555images/train2/weights/best.pt")
# model = YOLO("/app/runs/detect/555images/train/weights/best.pt")
# 2. เปิดกล้อง Webcam
# เลข 0 คือกล้องหลักของโน้ตบุ๊ก, ถ้าต่อ Webcam นอกอาจจะเป็น 1 หรือ 2
cap = cv2.VideoCapture(0)

# ตั้งค่าความละเอียดของกล้อง (ปรับตามสเปก Webcam ของคุณ)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


print("กด 'q' เพื่อออกจากโปรแกรม")

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # 3. รันการตรวจจับ (Inference)
        # conf=0.5: มั่นใจเกิน 50% ถึงจะแสดงผล (ปรับลดได้ถ้าถ่ายไกล 2.5 เมตรแล้วไม่ติด)
        results = model.predict(frame, conf=0.7, stream=True)

        # 4. วาดผลลัพธ์ลงบนภาพเฟรมปัจจุบัน
        for r in results:
            annotated_frame = r.plot()

        # 5. แสดงหน้าต่าง Real-time
        cv2.imshow("Singha Cans Detection - Real-time", annotated_frame)

        # กด 'q' เพื่อปิดหน้าต่าง
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# คืนค่าทรัพยากร
cap.release()
cv2.destroyAllWindows()