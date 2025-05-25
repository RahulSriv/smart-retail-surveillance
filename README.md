# Suspicious Activity Detection in Retail using YOLOv8 and Gemini Pro Multimodal AI

---

## 📖 Overview  
This project implements a **smart retail surveillance system** to detect suspicious activities such as shoplifting using advanced **object detection** and **multimodal AI analysis**. The system processes video frames from retail environments to identify people and objects, then uses behavioral analysis powered by **Gemini Pro** multimodal AI to flag potentially suspicious actions — helping retailers enhance store security and reduce theft.

---

## 🛠️ Tech Stack  
- 🚀 **YOLOv8** — Real-time object detection model for people, handbags, backpacks, etc.  
- 🤖 **Gemini Pro Multimodal AI** — Natural language-based behavioral analysis from visual data.  
- 🐍 **Python** — Core scripting language.  
- 🎥 **OpenCV** — Video frame extraction and image processing.  

---

## 🧩 Problem Statement  
Retail theft leads to significant financial losses globally. Traditional CCTV surveillance demands extensive manual monitoring which is error-prone and resource-intensive. Automating suspicious activity detection in real-time can assist security teams by providing timely alerts and reducing false alarms.

---

## 💡 Solution  
- Extract video frames from retail store footage.  
- Detect objects (people, bags) using **YOLOv8**.  
- Perform behavioral analysis on detected objects using **Gemini Pro Multimodal AI**.  
- Flag suspicious activities and save relevant frames for review.  
- Provide detailed natural language behavior summaries for enhanced understanding.

---

## 🧠 AI Models & Techniques Used
✅ YOLOv8 (Fine-Tuned) Object detection trained on custom retail surveillance dataset. Trained to detect multiple objects and complex poses (like reaching into shelves). `shoplifting` treated as a high-level visual pattern label.

✅ Gemini Pro Vision (Multimodal LLM) takes visual input (frame) + prompt. Infers behavior using visual cues (posture, interaction, obscurity, eye direction). Adds human-like reasoning to camera feeds.

---

## 🚀 Workflow
````
1. 📹 Input Video Footage
   - Raw CCTV footage from the retail store.
              ↓
2. 🖼️ Extract Frames from Video
   - Frames are extracted from the video for processing.
              ↓
3. 🤖 Object Detection using YOLOv8
   - YOLOv8 model detects objects and persons in each frame.
              ↓
4. ⚠️ Suspicious Object/Activity Candidate Identified
   - Potential suspicious activity is flagged based on object detection and heuristics.
              ↓
5. 👁️ Scene Description using Gemini Pro Vision
   - Frame is passed to Gemini Pro Vision for detailed scene understanding.
              ↓
6. 🧠 Behavior Analysis using Gemini Pro Multimodal
   - Multimodal AI analyzes objects, positions, and scene context for behavioral cues.
              ↓
7. ✅❌ Flag as Suspicious or Not Suspicious
   - Final decision is made on whether the activity is suspicious.
              ↓
8. 📁 Save Flagged Frames for Review
   - Suspicious frames are saved to 'flagged_frames/' for human review.

````
---

## 🎯 Benefits  
- ⏱️ **Real-time detection** for immediate intervention.  
- 👁️ **Reduced manual effort** for security staff.  
- 🎯 **Improved accuracy** by combining object detection and AI behavioral analysis.  
- ⚙️ **Scalable and extensible** design for future upgrades.

---
## 📂 Repository Structure 
```
smart-retail-surveillance/
├── resources/                          # Contains data and media resources  
│   ├── flagged_frames                  # Frames flagged as suspicious  
│   ├── input                           # Input videos or images for processing  
│   └── output                          # Output files and results  
│       └── extracted_frames            # Frames extracted from input videos  
├── training/                           # Training-related notebooks and scripts  
│   └── training.ipynb             
├── detect_image_yolov8.py              # Script for detecting objects in single images using YOLOv8  
├── detect_video_yolov8.py              # Script for detecting objects in videos using YOLOv8  
├── extract_frames.py                   # Utility to extract frames from video files  
├── describe_scene_using_gemini.py      # Uses Gemini Pro to generate scene descriptions from images  
├── gemini_behavior_analysis.py         # Performs behavioral analysis using Gemini Pro AI  
├── gemini_vision_analysis.py           # Vision-based analysis module using Gemini Pro AI  
├── suspicious_activity_detector.py     # Main script that combines detection and behavioral analysis to flag suspicious activities  
├── requirements.txt              
└── README.md                     
```
---
## 🚀 Setup Instructions

1. **Clone the repository:**

2. **Create and activate a Python virtual environment:**
```bash
python -m venv .venv
# For Linux/macOS:
source .venv/bin/activate
# For Windows:
.venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download YOLOv8 model weights**  
   If not already included, download the YOLOv8 model weights from [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics) or follow the instructions in the code.

5. **Configure API access for Gemini Pro**  
   Set up any required API keys or credentials for Gemini Pro multimodal AI. Refer to your environment or Gemini Pro documentation for details.

---

## 📖 Usage Instructions

Run the main script to process image frames and analyze for suspicious behavior:

```bash
python suspicious_activity_detector.py
```

- The script will:
  - Detect objects using YOLOv8.
  - Use Gemini Pro to analyze scene behavior.
  - Flag suspicious frames and save them for review.

- Console output includes:
  - Detected objects
  - Behavior analysis summary
  - Flagging status per frame

---

## 🖼️ Input

- Input should be image frames extracted from retail store surveillance videos.
- Directory: `resources/input`
- Supported formats: `.jpg`, `.png`, etc.

---

## 📤 Output

- Suspicious frames are saved to: `resources/flagged_frames/`
- File names will include frame numbers for traceability.
- Console logs include:
  - Object detection results
  - Behavior interpretation
  - Frame status (Flagged/Not Flagged)

---

## 🔮 Future Work

- 📈 Improve behavioral context with motion tracking and temporal analysis.
- 🚨 Add real-time alerting system for instant security notification.
- 📊 Build a web-based dashboard to visualize events and analytics.

---