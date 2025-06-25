# GesturAI - Gesture Based Mathematical Problem Solver Using AI and Computer Vision
---

#📌 Features

- ✋ Real-time **hand tracking** with `cvzone` and `OpenCV`
- 🧠 Integrates **Gemini AI** (`gemini-1.5-flash`) for solving drawn math problems
- 🎨 Uses **hand gestures to draw** in the air:
  - ✌️ Index finger up = Draw
  - 👍 Thumb up = Clear screen
  - 🤚 All fingers except index up = Send to AI
- ⚙️ Built with **Streamlit** for a smooth and responsive UI

---

# 🛠️ Tech Stack

- Python 3.8+
- [OpenCV](https://opencv.org/) – for video and image processing
- [cvzone](https://github.com/cvzone/cvzone) – for hand tracking
- [Streamlit](https://streamlit.io/) – for the UI
- [Google Generative AI](https://ai.google.dev/) – for AI-powered math solving
- [Pillow (PIL)](https://python-pillow.org/) – for image conversion

---

# ⚙️ Installation

1. **Clone the repository**
   git clone https://github.com/yourusername/gesture-math-solver.git
   cd gesture-math-solver
3. **Install Dependencies**
   pip install -r requirements.txt
5. **Set your Google Gemini API Key**
   genai.configure(api_key="YOUR_API_KEY_HERE")
7. **Run Application**
   streamlit run app.py

---

# 📷 Demo

<img width="914" alt="output6" src="https://github.com/user-attachments/assets/286d8118-f7b9-46af-820a-f613d4de05fb" />


<img width="919" alt="output7" src="https://github.com/user-attachments/assets/6f8308ca-e0e9-4324-84f1-6d7304cc6a9f" />
