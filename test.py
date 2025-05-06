# import cv2

# cap = cv2.VideoCapture('/mnt/datasets/viedo-qa-chuxiang/0-1-0/10-2-chuxiang/viedos/01_10-2-chuxiang_1.mp4')
# if not cap.isOpened():
#     print("❌ Failed to open video file")
# else:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ Cannot read frame — video might be unreadable")
#     else:
#         print("✅ Frame read successfully:", frame.shape)

##################################################################
# import cv2

# cap = cv2.VideoCapture("/mnt/datasets/viedo-qa-chuxiang/0-1-0/10-2-chuxiang/viedos/01_10-2-chuxiang_1.mp4")
# frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print("Frame count:", frame_count)
# cap.release()
###################################################################
# import os
# video_path = "/mnt/datasets/viedo-qa-chuxiang/0-1-0/10-2-chuxiang/viedos/01_10-2-chuxiang_1.mp4"
# print(os.path.exists(video_path), os.path.getsize(video_path))
###################################################################
from decord import VideoReader
video_path = "/mnt/datasets/viedo-qa-chuxiang/0-1-0/10-2-chuxiang/viedos/01_10-2-chuxiang_1.mp4"
try:
    vr = VideoReader(video_path)
    print(f"Video has {len(vr)} frames")
    frames = vr.get_batch([0]).asnumpy()
    print(f"Loaded frame shape: {frames.shape}")
except Exception as e:
    print(f"Error loading video {video_path}: {e}")