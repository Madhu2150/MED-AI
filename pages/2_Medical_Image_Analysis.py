import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import api_key

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

SYSTEM_PROMPT = """
You are a medical imaging specialist. Analyze the image:

1. Detailed Analysis: Identify anomalies, lesions, fractures, opacities.
2. Findings Report: Structured bullet points of observations.
3. Recommendations: Further tests (MRI, biopsy, bloodwork).
4. Treatment Suggestions: Conservative options only.

IMPORTANT:
- Only respond if image is medical/human health.
- If unclear: "Unable to determine — image quality insufficient."
- Always end: "⚠️ Consult a doctor before any decisions."
"""

model_g = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=SYSTEM_PROMPT,
)

st.set_page_config(page_title="MEDIAI — Image Analysis", page_icon="🔬", layout="wide")

with st.sidebar:
    st.markdown("### 🔬 Image Analysis")
    st.markdown("Upload X-ray, MRI, CT, skin photos.")
    st.markdown("---")
    st.caption("Supported: PNG, JPG, JPEG")

st.markdown("## 🔬 Medical Image Analysis")
st.caption("Upload a medical image for AI-powered analysis")

uploaded_file = st.file_uploader("Choose image", type=["png", "jpg", "jpeg"])

col_img, col_res = st.columns([1, 2])

if uploaded_file:
    with col_img:
        st.image(uploaded_file, caption="Uploaded Image", width=300)

    if st.button("🔍 Analyze", type="primary", use_container_width=True):
        with st.spinner("Analyzing image... 🔬"):
            try:
                image_data = uploaded_file.getvalue()
                response = model_g.generate_content([
                    {"mime_type": "image/jpeg", "data": image_data},
                ])
                with col_res:
                    st.success("✅ Analysis Complete")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    with col_res:
        st.info("👆 Upload a medical image to begin analysis.")