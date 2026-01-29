import streamlit as st
import base64  # For embedding images or SVGs if needed

# Function to get base64 of SVG logo (you can replace with actual base64 if image)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Simulated SVG logo for Pharos LeaseBridge (lighthouse + bridge theme)
logo_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="100" height="100">
    <path fill="#3b82f6" d="M24 4L4 20v24h40V20L24 4z"/>
    <path fill="#d97706" d="M24 4l20 16v24H4V20L24 4zM24 12l-12 8v16h24V20l-12-8z"/>
    <circle fill="#fff" cx="24" cy="28" r="4"/>
    <path fill="#3b82f6" d="M20 40h8v4h-8z"/>
</svg>
"""

# Background CSS - futuristic lighthouse theme (radial gradient with blue/gold)
background_css = """
body {
    background: radial-gradient(circle at 50% 30%, rgba(59, 130, 246, 0.3) 0%, transparent 70%),
                url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?auto=format&fit=crop&w=1920') no-repeat center/cover;
    background-blend-mode: overlay;
}
"""

# Main Streamlit app
st.set_page_config(page_title="Pharos LeaseBridge | Decentralized RWA Leasing Platform", layout="wide")

# Custom CSS for better design (standard RWA dapp style: clean, dark mode, hero, sections)
st.markdown(f"""
    <style>
        {background_css}
        .stApp {{
            color: #f1f5f9;
            font-family: 'Inter', sans-serif;
        }}
        .hero {{
            text-align: center;
            padding: 50px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            margin-bottom: 40px;
        }}
        .section {{
            padding: 30px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            margin-bottom: 30px;
        }}
        button {{
            background-color: #3b82f6;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
        }}
        button:hover {{
            background-color: #2563eb;
        }}
    </style>
""", unsafe_allow_html=True)

# Header with logo
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown(logo_svg, unsafe_allow_html=True)
with col2:
    st.title("Pharos LeaseBridge")

# Connect Wallet Button (simulated - integrate real JS if needed)
if st.button("Connect Wallet"):
    st.write("Wallet connected! Address: 0x...")

# Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.header("Bridge Real World Assets to Blockchain")
st.write("Pharos LeaseBridge empowers decentralized leasing of premium RWAs. Secure, transparent, and efficient – guided by the light of Pharos blockchain.")
st.markdown('</div>', unsafe_allow_html=True)

# Project Description Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("About the Project")
st.write("""
Pharos LeaseBridge is a pioneering platform on the Pharos blockchain, enabling seamless leasing of Real World Assets (RWAs) through NFTs. 
Our vision merges the reliability of a lighthouse (Pharos) with innovative bridging of traditional assets to DeFi. 
Features include secure rentals, admin controls, revenue withdrawal, and more.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Features Section (standard for RWA dapps)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Key Features")
features = [
    "Per-property rental rates",
    "Time-based leasing without ownership transfer",
    "Revenue sharing with beneficiaries",
    "Oracle verification for assets",
    "Yield farming for renters"
]
for feature in features:
    st.write(f"- {feature}")
st.markdown('</div>', unsafe_allow_html=True)

# RWA Gallery (placeholder - integrate real dapp logic)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("RWA Registry")
st.write("Browse and lease available assets here. (Integrate with ethers.js for real functionality)")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Contact Us")
st.write("Email: info@pharosleasebridge.com")
st.write("Discord: discord.gg/pharos")
st.write("X: @pharos_network")
contact_form = st.form(key="contact")
name = contact_form.text_input("Your Name")
email = contact_form.text_input("Your Email")
message = contact_form.text_area("Message")
submit = contact_form.form_submit_button("Send")
if submit:
    st.write("Message sent! (Simulated - add real backend)")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("© 2026 Pharos LeaseBridge. All rights reserved.")

# To run: streamlit run this_file.py
