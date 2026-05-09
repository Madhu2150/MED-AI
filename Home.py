import streamlit as st
from PIL import Image
import base64
from pathlib import Path

st.set_page_config(
    page_title="MEDIAI — Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.main-header {
    font-size: 2.8rem;
    background: linear-gradient(135deg, #00c6fb 0%, #005bea 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.3rem;
}

.sub-header {
    text-align: center;
    color: #7f8c8d;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.dash-card {
    background: linear-gradient(135deg, #f8f9ff 0%, #e8ecff 100%);
    border-radius: 20px;
    padding: 1.8rem;
    border: 1px solid #dce6ff;
    transition: transform 0.2s, box-shadow 0.2s;
    height: 100%;
}
.dash-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,91,234,0.12);
}

.card-icon { font-size: 3rem; margin-bottom: 0.5rem; }
.card-title { font-size: 1.2rem; font-weight: 700; color: #2c3e50; }
.card-desc { color: #7f8c8d; font-size: 0.93rem; margin-top: 0.5rem; }

.stat-box {
    background: white;
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
    border-left: 4px solid #005bea;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.stat-number { font-size: 2rem; font-weight: 700; color: #005bea; }
.stat-label { color: #95a5a6; font-size: 0.85rem; }

.footer { text-align:center; color:#bdc3c7; font-size:0.8rem; margin-top:3rem; }
</style>
""", unsafe_allow_html=True)

# ═══════════ SIDEBAR ═══════════
with st.sidebar:
    st.image("https://img.icons8.com/3d-fluency/94/stethoscope.png", width=60)
    st.markdown("### 🏥 MEDIAI")
    st.markdown("---")
    st.markdown("**Navigation**")
    st.page_link("Home.py", label="🏠 Dashboard", icon="🏠")
    st.page_link("pages/1_Medical_Assistant.py", label="💬 Medical Assistant", icon="💬")
    st.page_link("pages/2_Medical_Image_Analysis.py", label="🔬 Image Analysis", icon="🔬")
    st.markdown("---")
    st.markdown("📞 Emergency: **112**")
    st.markdown("*Powered by Gemini 1.5 Flash*")

# ═══════════ HEADER ═══════════
st.markdown('<p class="main-header">🏥 MEDIAI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your Intelligent Medical Support Platform</p>', unsafe_allow_html=True)

# ═══════════ STATS ROW ═══════════
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown('<div class="stat-box"><div class="stat-number">24/7</div><div class="stat-label">Availability</div></div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div class="stat-box"><div class="stat-number">98%</div><div class="stat-label">Accuracy Score</div></div>', unsafe_allow_html=True)
with col_c:
    st.markdown('<div class="stat-box"><div class="stat-number">50+</div><div class="stat-label">Conditions</div></div>', unsafe_allow_html=True)
with col_d:
    st.markdown('<div class="stat-box"><div class="stat-number">🔒</div><div class="stat-label">HIPAA Aware</div></div>', unsafe_allow_html=True)

st.markdown("---")

# ═══════════ FEATURE CARDS ═══════════
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="dash-card">
        <div class="card-icon">💬</div>
        <div class="card-title">Medical Assistant</div>
        <div class="card-desc">
            ✅ Ask symptoms & get differential diagnosis<br>
            ✅ Treatment guidance & patient education<br>
            ✅ Conversational memory (chat history)<br>
            ✅ Empathetic, plain-language responses
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Open Assistant", key="btn1", use_container_width=True):
        st.switch_page("pages/1_Medical_Assistant.py")

with col2:
    st.markdown("""
    <div class="dash-card">
        <div class="card-icon">🔬</div>
        <div class="card-title">Image Analysis</div>
        <div class="card-desc">
            ✅ Upload X-ray / MRI / CT / Skin images<br>
            ✅ Anomaly & disease detection<br>
            ✅ Structured findings report<br>
            ✅ Recommendations + next steps
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔬 Analyze Image", key="btn2", use_container_width=True):
        st.switch_page("pages/2_Medical_Image_Analysis.py")

# ═══════════ HOW IT WORKS ═══════════
st.markdown("---")
st.markdown("### ⚡ How It Works")
cols = st.columns(4)
steps = [
    ("📝", "Describe Symptoms / Upload Image"),
    ("🤖", "Gemini 1.5 Flash Analyzes"),
    ("📋", "Get Structured Report"),
    ("👨‍⚕️", "Consult Doctor with Insights"),
]
for i, (icon, text) in enumerate(steps):
    with cols[i]:
        st.markdown(f"""
        <div style="text-align:center">
            <div style="font-size:2.2rem">{icon}</div>
            <div style="font-weight:600; color:#2c3e50">{text}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════ DISCLAIMER ═══════════
st.markdown("---")
st.warning("""
**⚠️ IMPORTANT DISCLAIMER**
MEDIAI is an AI assistant for informational purposes ONLY.
It does NOT replace professional medical diagnosis or treatment.
Always consult a licensed healthcare provider.
""")

st.markdown('<p class="footer">© 2026 MEDIAI</p>', unsafe_allow_html=True)