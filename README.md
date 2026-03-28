# Singha Detection (YOLO)

Object detection project for Singha cans using Ultralytics YOLO and OpenCV.

This repository is prepared for Docker-based sharing.

## What Is Included In The Docker Build

- `src/` application code
- `runs/detect/train2/` trained weights used at runtime
- `requirements.txt`

## What Is Excluded

- `data/` is excluded from Docker build context
- Under `runs/detect`, only `train2` is included

This behavior is enforced by `.dockerignore`.

## Runtime Defaults

- Default model path in container: `/app/runs/detect/train2/weights/best.pt`
- Entry command: `python src/main.py`
- You can override model path with env var `MODEL_PATH`

## Requirements

- Docker installed on the host machine
- Webcam access if running real-time camera detection
- GUI/X11 support when running with display output (`cv2.imshow`)

## Build The Image

Run from repository root:

```bash
docker build -f docker/Dockerfile -t singha-detector:train2 .
```

## Run The Container

Basic run:

```bash
docker run --rm -it singha-detector:train2
```

Run with custom model path:

```bash
docker run --rm -it \
	-e MODEL_PATH=/app/runs/detect/train2/weights/best.pt \
	singha-detector:train2
```

## Export Image To Share With A Friend

Create tar file:

```bash
docker save -o singha-detector-train2.tar singha-detector:train2
```

Send `singha-detector-train2.tar` to your friend.

## Load And Run On Friend Machine

Load image:

```bash
docker load -i singha-detector-train2.tar
```

Run:

```bash
docker run --rm -it singha-detector:train2
```

## Notes For Webcam And GUI

The app uses `cv2.VideoCapture(0)` and opens a display window with `cv2.imshow`.

If camera/display does not work in Docker, pass device/display permissions appropriate to your OS.
Example for Linux hosts (may vary by setup):

```bash
docker run --rm -it \
	--device=/dev/video0 \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	singha-detector:train2
```

## Python Dependencies

- `numpy`
- `matplotlib`
- `pandas`
- `opencv-python`
- `ultralytics`

## Project Structure (Relevant)

```text
docker/Dockerfile
src/main.py
runs/detect/train2/weights/best.pt
requirements.txt
.dockerignore
```
