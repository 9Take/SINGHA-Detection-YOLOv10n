FROM ultralytics/ultralytics:latest-python

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-venv \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv /opt/env
ENV PATH="/opt/env/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MODEL_PATH="/app/runs/detect/train2/weights/best.pt"

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY runs/detect/train2 ./runs/detect/train2

CMD ["python", "src/main.py"]