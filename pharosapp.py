# app.py
import streamlit as st
from streamlit.components.v1 import html
import time

# ────────────────────────────────────────────────────────────────
# Page config & custom styling
# ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pharos LeaseBridge • Decentralized RWA Leasing",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern dark theme + glass effect
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --bg: #0f172a;
        --surface: #1e293b;
        --accent: #3b82f6;
        --accent-dark: #2563eb;
        --gold: #d97706;
        --text: #e2e8f0;
        --text-muted: #94a3b8;
        --border: rgba(226, 232, 240, 0.08);
    }

    body, .stApp {
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    .stApp > header { background: transparent !important; }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
    }

    /* Glass card */
    .glass-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        margin-bottom: 1.5rem;
    }

    .hero {
        text-align: center;
        padding: 5rem 1rem 4rem;
        background: linear-gradient(135deg, rgba(59,130,246,0.12) 0%, rgba(217,119,6,0.08) 100%);
        border-radius: 0 0 32px 32px;
        margin: -1rem -1rem 3rem -1rem;
    }

    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    .connect-btn {
        background: linear-gradient(90deg, #3b82f6, #2563eb);
        color: white;
        border: none;
        padding: 0.75rem 1.8rem;
        border-radius: 999px;
        font-weight: 600;
        transition: all 0.2s;
    }

    .connect-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 25px rgba(59,130,246,0.4);
    }

    hr.divider {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, var(--border), transparent);
        margin: 3rem auto;
        max-width: 300px;
    }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────
# Simulated state
# ────────────────────────────────────────────────────────────────
if 'connected' not in st.session_state:
    st.session_state.connected = False
    st.session_state.address = None

# ────────────────────────────────────────────────────────────────
# Sidebar
# ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://via.placeholder.com/180x60/1e293b/ffffff?text=Pharos+LeaseBridge", use_column_width=True)
    
    if not st.session_state.connected:
        if st.button("Connect Wallet", key="connect_sidebar", use_container_width=True, type="primary"):
            # Simulate connection
            time.sleep(1.2)
            st.session_state.connected = True
            st.session_state.address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
            st.rerun()
    else:
        st.success(f"Connected: {st.session_state.address[:6]}...{st.session_state.address[-4:]}")
        if st.button("Disconnect", use_container_width=True):
            st.session_state.connected = False
            st.rerun()

    st.divider()
    st.caption("Network: Pharos Atlantic")
    st.caption("Contract: 0xC4F8...91BF")

# ────────────────────────────────────────────────────────────────
# Hero
# ────────────────────────────────────────────────────────────────
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.title("Pharos LeaseBridge")
st.subheader("Real World Assets • Decentralized Leasing • Powered by Pharos")
st.markdown("""
    Securely tokenize, lease, and earn from real estate and infrastructure assets  
    on the fast, low-cost Pharos Atlantic blockchain.
""")
col_a, col_b, col_c = st.columns([1,2,1])
with col_b:
    if st.button("Explore Available Assets", type="primary", use_container_width=True, key="explore_hero"):
        st.switch_page("pages/2_Assets.py")  # You can create this page later
st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────
# Quick stats / trust signals
# ────────────────────────────────────────────────────────────────
cols = st.columns(4)
cols[0].metric("Total Value Locked", "$12.4M", "+18%")
cols[1].metric("Active Leases", "347", "+42")
cols[2].metric("Avg. APY", "9.2%", delta_color="normal")
cols[3].metric("Properties", "19", "+3")

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────
# Features section
# ────────────────────────────────────────────────────────────────
st.header("Why Pharos LeaseBridge?", anchor="features")
st.write("")

feat_cols = st.columns(3)
with feat_cols[0]:
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Per-Asset Rates")
        st.write("Each property has its own customizable daily rate – perfect for hotels, apartments, offices.")
        st.markdown('</div>', unsafe_allow_html=True)

with feat_cols[1]:
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Revenue Sharing")
        st.write("Beneficiaries & renters can participate in yield. Rent-to-invest model supported.")
        st.markdown('</div>', unsafe_allow_html=True)

with feat_cols[2]:
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Fast & Cheap")
        st.write("Built on Pharos Atlantic – sub-second finality, near-zero fees, high throughput.")
        st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────
# Call to action + footer
# ────────────────────────────────────────────────────────────────
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

cta_col1, cta_col2 = st.columns([3,2])
with cta_col1:
    st.subheader("Ready to lease or invest?")
    st.write("Connect your wallet to start exploring live RWAs on Pharos.")
with cta_col2:
    st.button("Connect Wallet & Start", type="primary", use_container_width=True, key="cta_final")

st.markdown("""
    <div style="text-align:center; color:var(--text-muted); margin-top:4rem; font-size:0.9rem;">
    © 2026 Pharos LeaseBridge • Built on Pharos Atlantic • 
    <a href="https://discord.gg/pharos" target="_blank" style="color:var(--accent);">Discord</a> • 
    <a href="https://x.com/pharos_network" target="_blank" style="color:var(--accent);">X</a>
    </div>
""", unsafe_allow_html=True)
