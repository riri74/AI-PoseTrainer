# AI Trainer - Pose Estimation and Counter

This project is an AI-based trainer that uses pose estimation to track the movement of key joints during exercises like dumbbell curls. The system calculates the angle of the arm and keeps count of the number of repetitions performed, providing real-time feedback in the form of on-screen overlays.

## Features
- Pose estimation: Detects the pose using a custom poseestimationmodule.
- Real-time feedback: Displays the percentage of completion for each curl and tracks the total count.
- Dynamic UI: On-screen bar and text elements showing the percentage progress and the repetition count.
- FPS Counter: Displays real-time frames per second (FPS) to monitor performance.

## Demo
The system captures and tracks a dumbbell curl session from a video feed, with an output similar to the following:
- Real-time pose estimation with key point landmarks.
- Percentage completion for curls (shown as a vertical bar).
- Total curl count.
- FPS display for performance tracking.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV (cv2)
- Numpy (numpy)
