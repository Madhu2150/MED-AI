<div align="center">

# 🏥 MEDIAI
### *Intelligent Medical Support Platform*

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-red?logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-green?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

[![🚀 LIVE APP](https://img.shields.io/badge/🚀_LIVE_APP-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://mediai-assistant.streamlit.app)
[![📦 GitHub](https://img.shields.io/badge/📦_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/mediai)

🌐 **Live URL:** [https://mediai-assistant.streamlit.app](https://mediai-assistant.streamlit.app)

</div>

---

<details open>
<summary><h2>📑 Table of Contents</h2></summary>

- [🎯 Features](#-features)
- [🚀 Live Demo](#-live-demo)
- [💻 Installation](#-installation)
- [📁 Project Structure](#-project-structure)
- [⚙️ Configuration & API](#️-configuration--api)
- [🤝 Contributing](#-contributing)
- [⚠️ Disclaimer](#️-disclaimer)

</details>

---

## 🎯 Features

| Module | Capabilities | Status |
|--------|--------------|:------:|
| 💬 **Medical Assistant** | Symptom analysis, Differential diagnosis, Treatment guidance, Chat memory | ✅ |
| 🔬 **Image Analysis** | X-Ray/MRI/CT anomaly detection, Structured findings report, Multi-format support | ✅ |
| 🏠 **Dashboard** | Real-time stats, One-click navigation, Interactive sidebar menu | ✅ |

---

## 🚀 Live Demo

> **No installation required! Try it directly in your browser.**

👉 **[Click here to open the Live App](https://mediai-assistant.streamlit.app)**

---

## 💻 Installation

<details open>
<summary><b>🖥️ Local Setup (Quick Start)</b></summary>
<br>

**Prerequisites:** Python 3.10+ and a [Google Gemini API Key](https://aistudio.google.com/app/apikey).

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/mediai.git
cd mediai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your API Key
echo "api_key = 'YOUR_GEMINI_API_KEY'" > api_key.py

# 4. Run the application
python -m streamlit run Home.py
```
🌐 **Local URL:** `http://localhost:8501`

</details>

<details>
<summary><b>☁️ Cloud Deployment (Streamlit Cloud)</b></summary>
<br>

1. Push your code to a **public GitHub repository**.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in.
3. Click **New App** and link your repository.
4. Set `Home.py` as the main file.
5. In **Advanced Settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
6. Click **Deploy**!

</details>

---

## 📁 Project Structure

<details open>
<summary><b>📂 Click to expand directory tree</b></summary>
<br>

```text
mediai/
├── 📄 Home.py                          # 🏠 Main Dashboard & Entry Point
├── 📄 model.py                         # 🤖 Gemini AI Handler & Logic
├── 📄 api_key.py                       # 🔑 API Key Configuration
├── 📄 requirements.txt                 # 📦 Python Dependencies
├── 📄 README.md                        # 📘 Documentation (This file)
├── 📄 .gitignore                       # 🚫 Git Ignore Rules
├── 📁 .streamlit/
│   └── 📄 config.toml                  # 🎨 UI Theme Configuration
└── 📁 pages/                           # 📑 Multi-page Routing
    ├── 📄 1_Medical_Assistant.py       # 💬 Chat Assistant Interface
    └── 📄 2_Medical_Image_Analysis.py  # 🔬 Image Upload & Analysis
```

</details>

---

## ⚙️ Configuration & API

<details>
<summary><b>⚙️ Model Configuration</b></summary>
<br>

Tweak the AI behavior in `model.py`:

```python
generation_config = {
    "temperature": 0.4,        # Lower = more factual/accurate
    "top_p": 0.95,             # Nucleus sampling
    "top_k": 64,               # Token selection pool
    "max_output_tokens": 8192  # Maximum response length
}
```

</details>

<details>
<summary><b>🔌 API Reference</b></summary>
<br>

Core function signature in `model.py`:

```python
from model import model

# Example usage
response = model(info="I have a headache and fever", history=[])
print(response)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `info` | `str` | The user's medical question or symptom description |
| `history` | `list` | Previous chat messages for context |
| **Returns** | `str` | The AI-generated medical response |

</details>

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

- [ ] Fork the repository
- [ ] Create your feature branch (`git checkout -b feature/AmazingFeature`)
- [ ] Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- [ ] Push to the branch (`git push origin feature/AmazingFeature`)
- [ ] Open a Pull Request

---

## ⚠️ Disclaimer

> 🚨 **IMPORTANT: NOT MEDICAL ADVICE**
> 
> MEDIAI is an AI-powered informational tool designed to assist and educate. It **does not** replace professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

<div align="center">

### ⭐ Star this repository if you found it useful!

[![Star This Repo](https://img.shields.io/github/stars/yourusername/mediai?style=social)](https://github.com/Madhu2150/MED-AI)

🔗 **Live App:** [mediai-assistant.streamlit.app](https://mediai-assistant.streamlit.app)
🔗 **Source Code:** [github.com/yourusername/mediai](https://github.com/Madhu2150/MED-AI)

</div>
