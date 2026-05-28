import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dhairya Panchal | Portfolio",
    page_icon="⚡",
    layout="wide",
)

# Hide Streamlit chrome elements
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stAppViewContainer"] > div:first-child { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTANT: Replace every href="#" below with your actual Google Drive link
# for certifications and events. Example:
#   href="https://drive.google.com/file/d/YOUR_FILE_ID/view"
# ─────────────────────────────────────────────────────────────────────────────

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
:root{
--bg:#0a0a0f;--surface:#13131a;--border:#1e1e2e;
--accent:#00e5ff;--accent2:#7c3aed;
--text:#e2e8f0;--muted:#64748b;
--mono:'Space Mono',monospace;--sans:'DM Sans',sans-serif;
}
body{font-family:var(--sans);background:var(--bg);color:var(--text);overflow-x:hidden;}

/* NAV */
.nav{
display:flex;align-items:center;justify-content:space-between;
padding:1rem 3.5rem;background:rgba(10,10,15,0.92);
backdrop-filter:blur(14px);border-bottom:1px solid var(--border);
position:relative;z-index:10;
}
.nav-logo{font-family:var(--mono);font-size:1.05rem;color:var(--accent);font-weight:700;}
.nav-links{display:flex;gap:1.6rem;list-style:none;flex-wrap:wrap;}
.nav-links a{
color:var(--muted);text-decoration:none;font-size:0.8rem;
letter-spacing:0.06em;text-transform:uppercase;cursor:pointer;
transition:color 0.2s;
}
.nav-links a:hover{color:var(--accent);}

/* HERO */
.hero{
padding:5rem 3.5rem 4rem;position:relative;overflow:hidden;
background:var(--bg);
}
.hero::before{
content:'';position:absolute;inset:0;pointer-events:none;
background:
radial-gradient(ellipse 55% 55% at 78% 50%,rgba(124,58,237,0.13) 0%,transparent 70%),
radial-gradient(ellipse 40% 45% at 8% 80%,rgba(0,229,255,0.08) 0%,transparent 60%);
}
.hero-grid{
display:grid;grid-template-columns:1fr 250px;
gap:3.5rem;align-items:center;
max-width:1100px;margin:0 auto;position:relative;
}
.hero-tag{
font-family:var(--mono);font-size:0.76rem;
color:var(--accent);letter-spacing:0.15em;
text-transform:uppercase;margin-bottom:0.9rem;
}
.hero-name{
font-size:clamp(2.5rem,5vw,4.8rem);font-weight:700;
line-height:1.05;letter-spacing:-0.02em;
background:linear-gradient(135deg,#ffffff 0%,#94a3b8 100%);
-webkit-background-clip:text;-webkit-text-fill-color:transparent;
background-clip:text;margin-bottom:1rem;
}
.hero-role{font-size:1.05rem;color:var(--muted);font-weight:300;margin-bottom:1.9rem;line-height:1.75;}
.hero-role span{color:var(--accent);font-weight:500;}
.hero-btns{display:flex;gap:0.9rem;flex-wrap:wrap;}
.btn-p{
padding:0.68rem 1.7rem;background:var(--accent);color:#0a0a0f;
font-family:var(--mono);font-size:0.77rem;font-weight:700;
letter-spacing:0.05em;text-decoration:none;border-radius:4px;
transition:transform 0.2s,box-shadow 0.2s;display:inline-block;
}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 22px rgba(0,229,255,0.32);}
.btn-o{
padding:0.68rem 1.7rem;border:1px solid var(--border);color:var(--text);
font-family:var(--mono);font-size:0.77rem;letter-spacing:0.05em;
text-decoration:none;border-radius:4px;
transition:border-color 0.2s,color 0.2s;display:inline-block;
}
.btn-o:hover{border-color:var(--accent);color:var(--accent);}

/* PHOTO */
.photo-wrap{width:210px;height:210px;border-radius:50%;position:relative;margin:0 auto;display:flex;align-items:center;justify-content:center;}
.photo-ring{position:absolute;inset:-3px;border-radius:50%;background:conic-gradient(var(--accent),var(--accent2),var(--accent));animation:spin 6s linear infinite;z-index:0;}
@keyframes spin{to{transform:rotate(360deg);}}
.photo-inner{
width:205px;height:205px;border-radius:50%;background:var(--surface);
z-index:1;position:relative;
display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.4rem;
}
.p-icon{font-size:3rem;}
.p-hint{font-size:0.63rem;color:var(--muted);font-family:var(--mono);text-align:center;padding:0 0.8rem;line-height:1.5;}

/* SECTIONS */
.s-alt{background:#0d0d14;}
.s-wrap{max-width:1100px;margin:0 auto;padding:4.5rem 3.5rem;}
.s-label{font-family:var(--mono);font-size:0.72rem;color:var(--accent);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:0.55rem;}
.s-title{font-size:2.2rem;font-weight:700;letter-spacing:-0.02em;color:#fff;margin-bottom:2.3rem;}
.divider{height:1px;background:linear-gradient(90deg,var(--accent) 0%,transparent 55%);margin-bottom:2.3rem;}

/* ABOUT */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:start;}
.about-text{font-size:0.98rem;line-height:1.85;color:#94a3b8;}
.about-text p{margin-bottom:0.95rem;}
.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1.35rem;transition:border-color 0.2s;}
.stat-card:hover{border-color:var(--accent);}
.stat-num{font-family:var(--mono);font-size:1.85rem;font-weight:700;color:var(--accent);}
.stat-lbl{font-size:0.76rem;color:var(--muted);margin-top:0.2rem;}

/* SKILLS */
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1.2rem;}
.sk-group{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1.35rem;transition:transform 0.2s,border-color 0.2s;}
.sk-group:hover{transform:translateY(-3px);border-color:var(--accent2);}
.sk-title{font-family:var(--mono);font-size:0.7rem;color:var(--accent2);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.85rem;}
.sk-tags{display:flex;flex-wrap:wrap;gap:0.42rem;}
.sk-tag{background:rgba(0,229,255,0.06);border:1px solid rgba(0,229,255,0.14);color:#94a3b8;font-size:0.74rem;padding:0.22rem 0.62rem;border-radius:3px;font-family:var(--mono);}

/* EXPERIENCE */
.timeline{position:relative;padding-left:2rem;}
.timeline::before{content:'';position:absolute;left:0;top:0.5rem;bottom:0;width:2px;background:var(--border);}
.tl-item{position:relative;margin-bottom:2.6rem;}
.tl-dot{position:absolute;left:-2.42rem;top:0.42rem;width:11px;height:11px;border-radius:50%;background:var(--accent);border:2px solid var(--bg);box-shadow:0 0 10px rgba(0,229,255,0.5);}
.tl-head{display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.4rem;}
.tl-role{font-size:1.02rem;font-weight:600;color:#fff;}
.tl-date{font-family:var(--mono);font-size:0.74rem;color:var(--accent);}
.tl-org{font-size:0.86rem;color:var(--accent2);margin:0.2rem 0 0.6rem;}
.tl-pts{padding-left:1.15rem;}
.tl-pts li{font-size:0.86rem;color:#94a3b8;line-height:1.72;margin-bottom:0.28rem;}

/* PROJECTS */
.proj-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.35rem;}
.proj-card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1.75rem;transition:transform 0.25s,border-color 0.25s,box-shadow 0.25s;display:flex;flex-direction:column;}
.proj-card:hover{transform:translateY(-5px);border-color:var(--accent);box-shadow:0 12px 34px rgba(0,229,255,0.07);}
.proj-badge{display:inline-block;font-family:var(--mono);font-size:0.64rem;color:var(--accent2);background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.22);padding:0.17rem 0.52rem;border-radius:3px;margin-bottom:0.85rem;letter-spacing:0.07em;text-transform:uppercase;}
.proj-title{font-size:1.07rem;font-weight:600;color:#fff;margin-bottom:0.6rem;}
.proj-desc{font-size:0.84rem;color:#94a3b8;line-height:1.72;flex:1;margin-bottom:1.05rem;}
.proj-stack{display:flex;flex-wrap:wrap;gap:0.36rem;}
.st-tag{background:rgba(0,229,255,0.04);border:1px solid rgba(0,229,255,0.11);color:#64748b;font-size:0.68rem;padding:0.17rem 0.48rem;border-radius:3px;font-family:var(--mono);}

/* CERTIFICATIONS */
.cert-cat{margin-bottom:2.4rem;}
.cert-cat-title{font-family:var(--mono);font-size:0.7rem;color:var(--accent2);letter-spacing:0.14em;text-transform:uppercase;margin-bottom:1rem;padding-bottom:0.45rem;border-bottom:1px solid var(--border);}
.cert-row{display:flex;flex-wrap:wrap;gap:0.78rem;}
.cert-btn{
display:inline-flex;align-items:center;gap:0.45rem;
padding:0.58rem 1.1rem;background:var(--surface);
border:1px solid var(--border);border-radius:6px;
color:var(--text);text-decoration:none;font-size:0.83rem;
transition:border-color 0.2s,color 0.2s,background 0.2s;
}
.cert-btn:hover{border-color:var(--accent);color:var(--accent);background:rgba(0,229,255,0.04);}

/* COMPETITIONS */
.comp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1.1rem;}
.comp-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1.2rem 1.4rem;display:flex;align-items:flex-start;gap:0.85rem;transition:border-color 0.2s;}
.comp-card:hover{border-color:var(--accent2);}
.comp-icon{font-size:1.4rem;flex-shrink:0;margin-top:0.08rem;}
.comp-title{font-size:0.9rem;font-weight:600;color:#fff;margin-bottom:0.16rem;}
.comp-sub{font-size:0.76rem;color:var(--muted);}

/* EVENTS */
.ev-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1.2rem;}
.ev-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1.45rem;transition:transform 0.2s,border-color 0.2s;display:flex;flex-direction:column;gap:0.75rem;}
.ev-card:hover{transform:translateY(-3px);border-color:var(--accent);}
.ev-title{font-size:0.97rem;font-weight:600;color:#fff;}
.ev-role{font-family:var(--mono);font-size:0.7rem;color:var(--accent);letter-spacing:0.05em;text-transform:uppercase;}
.ev-btn{
display:inline-flex;align-items:center;gap:0.4rem;
padding:0.48rem 0.95rem;margin-top:auto;
background:transparent;border:1px solid var(--border);
border-radius:5px;color:var(--muted);
text-decoration:none;font-family:var(--mono);font-size:0.7rem;
transition:border-color 0.2s,color 0.2s;cursor:pointer;
}
.ev-btn:hover{border-color:var(--accent2);color:var(--accent2);}

/* CONTACT */
.contact-box{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:2.8rem;text-align:center;max-width:640px;margin:0 auto;}
.c-title{font-size:1.65rem;font-weight:700;color:#fff;margin-bottom:0.75rem;}
.c-sub{color:var(--muted);margin-bottom:2.1rem;line-height:1.72;font-size:0.93rem;}
.c-links{display:flex;justify-content:center;gap:0.85rem;flex-wrap:wrap;}
.c-link{
display:inline-flex;align-items:center;gap:0.5rem;
padding:0.65rem 1.3rem;border:1px solid var(--border);
border-radius:6px;color:var(--text);text-decoration:none;
font-family:var(--mono);font-size:0.76rem;
transition:border-color 0.2s,color 0.2s,background 0.2s;
}
.c-link:hover{border-color:var(--accent);color:var(--accent);background:rgba(0,229,255,0.04);}

/* FOOTER */
.footer{padding:1.7rem 3.5rem;text-align:center;border-top:1px solid var(--border);font-family:var(--mono);font-size:0.7rem;color:var(--muted);}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
<div class="nav-logo">DP//</div>
<ul class="nav-links">
<li><a onclick="document.getElementById('about').scrollIntoView({behavior:'smooth'})">About</a></li>
<li><a onclick="document.getElementById('skills').scrollIntoView({behavior:'smooth'})">Skills</a></li>
<li><a onclick="document.getElementById('experience').scrollIntoView({behavior:'smooth'})">Experience</a></li>
<li><a onclick="document.getElementById('projects').scrollIntoView({behavior:'smooth'})">Projects</a></li>
<li><a onclick="document.getElementById('certifications').scrollIntoView({behavior:'smooth'})">Certifications</a></li>
<li><a onclick="document.getElementById('competitions').scrollIntoView({behavior:'smooth'})">Competitions</a></li>
<li><a onclick="document.getElementById('events').scrollIntoView({behavior:'smooth'})">Events</a></li>
<li><a onclick="document.getElementById('contact').scrollIntoView({behavior:'smooth'})">Contact</a></li>
</ul>
</nav>

<!-- HERO -->
<section id="hero" class="hero">
<div class="hero-grid">
<div>
<div class="hero-tag">// ECE &nbsp;·&nbsp; Embedded Systems &nbsp;·&nbsp; AI/ML</div>
<h1 class="hero-name">Dhairya<br>Panchal</h1>
<p class="hero-role">
Engineering the intersection of <span>silicon</span> and <span>intelligence</span>.<br>
Building Edge AI systems, custom RTOS kernels,<br>and intelligent embedded applications.
</p>
<div class="hero-btns">
<a class="btn-p" href="mailto:panchaldhairya1314@gmail.com">Get in Touch</a>
<a class="btn-o" href="https://github.com/BareMetalBits" target="_blank">GitHub →</a>
</div>
</div>
<div>
<div class="photo-wrap">
<div class="photo-ring"></div>
<div class="photo-inner">
<div class="p-icon">🧑‍💻</div>
<div class="p-hint">Replace with<br>your photo</div>
</div>
</div>
</div>
</div>
</section>

<!-- ABOUT -->
<div class="s-alt" id="about">
<div class="s-wrap">
<div class="s-label">// About</div>
<h2 class="s-title">Who I Am</h2>
<div class="divider"></div>
<div class="about-grid">
<div class="about-text">
<p>I'm a B.Tech Electronics &amp; Communication Engineering student at <strong style="color:#e2e8f0;">Dharmsinh Desai University</strong>, driven by a passion for building systems where hardware meets intelligence.</p>
<p>My work spans low-level firmware and custom RTOS development (C, ARM Assembly, Cortex-M4), all the way up to deploying deep learning models on constrained edge hardware using TensorFlow, PyTorch, and CUDA.</p>
<p>I believe the most exciting problems in tech live at the boundary between embedded systems and AI — and that's exactly where I like to build.</p>
<p>Outside the lab, I play Trinity College London certified Electronic Keyboard and do 3D animation with Blender Studio.</p>
</div>
<div class="stat-grid">
<div class="stat-card"><div class="stat-num">8+</div><div class="stat-lbl">Projects Built</div></div>
<div class="stat-card"><div class="stat-num">2</div><div class="stat-lbl">Internships</div></div>
<div class="stat-card"><div class="stat-num">3</div><div class="stat-lbl">Competitions</div></div>
<div class="stat-card"><div class="stat-num">14+</div><div class="stat-lbl">Certifications</div></div>
</div>
</div>
</div>
</div>

<!-- SKILLS -->
<div style="background:var(--bg);" id="skills">
<div class="s-wrap">
<div class="s-label">// Skills</div>
<h2 class="s-title">Technical Expertise</h2>
<div class="divider"></div>
<div class="skills-grid">
<div class="sk-group">
<div class="sk-title">Programming Languages</div>
<div class="sk-tags">
<span class="sk-tag">C</span><span class="sk-tag">C++</span><span class="sk-tag">Python</span>
<span class="sk-tag">ARM Assembly</span><span class="sk-tag">8051 Assembly</span><span class="sk-tag">8086 Assembly</span>
</div>
</div>
<div class="sk-group">
<div class="sk-title">AI / ML Frameworks</div>
<div class="sk-tags">
<span class="sk-tag">TensorFlow</span><span class="sk-tag">PyTorch</span><span class="sk-tag">CUDA</span>
<span class="sk-tag">Ollama</span><span class="sk-tag">LangChain</span><span class="sk-tag">OpenCV</span>
</div>
</div>
<div class="sk-group">
<div class="sk-title">Hardware &amp; MCUs</div>
<div class="sk-tags">
<span class="sk-tag">STM32</span><span class="sk-tag">Nordic NRF54</span><span class="sk-tag">ARM Cortex-M4</span>
<span class="sk-tag">Raspberry Pi</span><span class="sk-tag">ESP32</span><span class="sk-tag">Arduino</span>
</div>
</div>
<div class="sk-group">
<div class="sk-title">IDEs &amp; Tools</div>
<div class="sk-tags">
<span class="sk-tag">ARM Keil</span><span class="sk-tag">STM32CubeIDE</span><span class="sk-tag">Nordic SDK</span>
<span class="sk-tag">Proteus</span><span class="sk-tag">Multisim</span>
</div>
</div>
<div class="sk-group">
<div class="sk-title">Other</div>
<div class="sk-tags">
<span class="sk-tag">3D Animation (Blender)</span><span class="sk-tag">RTOS Development</span>
<span class="sk-tag">Firmware OTA</span><span class="sk-tag">Electronic Keyboard</span>
</div>
</div>
</div>
</div>
</div>

<!-- EXPERIENCE -->
<div class="s-alt" id="experience">
<div class="s-wrap">
<div class="s-label">// Experience</div>
<h2 class="s-title">Work Experience</h2>
<div class="divider"></div>
<div class="timeline">
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-head">
<div class="tl-role">Summer Intern — Embedded Systems</div>
<div class="tl-date">May 2026 – Jun 2026</div>
</div>
<div class="tl-org">Semconix Tech Solutions · Gandhinagar, India</div>
<ul class="tl-pts">
<li>Developed an Over-The-Air (OTA) firmware update protocol for Nordic NRF54 series MCUs.</li>
<li>Gained expertise in low-level firmware development and wireless communication protocols.</li>
</ul>
</div>
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-head">
<div class="tl-role">Senior Associate</div>
<div class="tl-date">Aug 2025 – Jul 2026</div>
</div>
<div class="tl-org">SPECTRUM DDU · Dharmsinh Desai University, Nadiad</div>
<ul class="tl-pts">
<li>Spearheaded SpecteQ 2026 — a 1.5-month robotics event fostering hands-on learning across DDU.</li>
<li>Organised workshops covering Robotics, AI/ML, 6G Communications, and Raspberry Pi.</li>
</ul>
</div>
<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-head">
<div class="tl-role">Internship Trainee — Embedded Systems &amp; ML</div>
<div class="tl-date">Apr 2025 – Jun 2025</div>
</div>
<div class="tl-org">Pantech.AI · Remote, Ahmedabad</div>
<ul class="tl-pts">
<li>Built a plant disease identification system using image analysis and deep learning techniques.</li>
<li>Completed structured modules in Computer Vision, RTOS, IoT, and Embedded C.</li>
</ul>
</div>
</div>
</div>
</div>

<!-- PROJECTS -->
<div style="background:var(--bg);" id="projects">
<div class="s-wrap">
<div class="s-label">// Projects</div>
<h2 class="s-title">What I've Built</h2>
<div class="divider"></div>
<div class="proj-grid">

<div class="proj-card">
<span class="proj-badge">DL · Minor Research Project</span>
<div class="proj-title">Monocular Depth Estimation for Visually Impaired</div>
<div class="proj-desc">Custom Transformer-based approach for Monocular Depth Estimation on edge hardware to assist visually impaired individuals with real-time spatial awareness without cloud connectivity.</div>
<div class="proj-stack"><span class="st-tag">Transformers</span><span class="st-tag">PyTorch</span><span class="st-tag">TFLite</span><span class="st-tag">Edge Deployment</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">Embedded · Minor Research Project</span>
<div class="proj-title">Edge RTOS</div>
<div class="proj-desc">Custom RTOS kernel for Cortex-M4 MCUs enabling real-time edge ML inferencing with minimized scheduling overhead. Implements preemptive scheduling, memory management, and IPC from scratch.</div>
<div class="proj-stack"><span class="st-tag">C</span><span class="st-tag">ARM Assembly</span><span class="st-tag">Cortex-M4</span><span class="st-tag">RTOS</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">Robotics · SSIP Cell DDU</span>
<div class="proj-title">Multi-Purpose 3-Fingered Gripper</div>
<div class="proj-desc">Designed a 3-fingered robotic gripper with adaptive multi-purpose grasping, integrating servo actuation and embedded control for precise manipulation tasks in unstructured environments.</div>
<div class="proj-stack"><span class="st-tag">STM32</span><span class="st-tag">Servo Control</span><span class="st-tag">Embedded C</span><span class="st-tag">Kinematics</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">AI/ML · SSIP Cell DDU</span>
<div class="proj-title">Smart Healthcare Companion</div>
<div class="proj-desc">AI-powered smart healthcare companion leveraging embedded systems and ML for patient monitoring and intelligent health assistance, combining sensor fusion with on-device inference.</div>
<div class="proj-stack"><span class="st-tag">TFLite</span><span class="st-tag">Raspberry Pi</span><span class="st-tag">Sensor Fusion</span><span class="st-tag">Python</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">Gen AI · DU Hacks 5.0</span>
<div class="proj-title">RAG-based Local Research Assistant</div>
<div class="proj-desc">Token-optimised Retrieval Augmented Generation (RAG) based local research assistant for maximised context retention. Runs entirely offline using local LLMs via Ollama — no internet required.</div>
<div class="proj-stack"><span class="st-tag">LangChain</span><span class="st-tag">Ollama</span><span class="st-tag">RAG</span><span class="st-tag">FAISS</span><span class="st-tag">Python</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">Edge AI · Minor Research Project</span>
<div class="proj-title">Industrial Vision Intelligence System</div>
<div class="proj-desc">Integrates robotics, control systems, and deep learning (1D/2D CNN) with embedded edge computing for real-time signal and image processing in industrial environments — fully cloud independent.</div>
<div class="proj-stack"><span class="st-tag">CNN</span><span class="st-tag">PyTorch</span><span class="st-tag">Edge Computing</span><span class="st-tag">C++</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">Digital Design · ECP</span>
<div class="proj-title">4-Bit Microprocessor</div>
<div class="proj-desc">Designed and implemented a custom 4-bit microprocessor capable of arithmetic and logical operations, with an on-board programmable timer/counter — built from scratch to deepen understanding of computer architecture.</div>
<div class="proj-stack"><span class="st-tag">Digital Logic</span><span class="st-tag">Proteus</span><span class="st-tag">Computer Architecture</span><span class="st-tag">Timer/Counter</span></div>
</div>

<div class="proj-card">
<span class="proj-badge">IoT · Edge Systems</span>
<div class="proj-title">Independent Edge IoT Telemetry Ecosystem</div>
<div class="proj-desc">Shifts both data translation and web-hosting tasks directly onto edge silicon, transforming the system into an independent hardware appliance — eliminating cloud/internet dependency for maximum reliability and minimal downtime under fault.</div>
<div class="proj-stack"><span class="st-tag">ESP32</span><span class="st-tag">Edge Web Server</span><span class="st-tag">MQTT</span><span class="st-tag">C/C++</span><span class="st-tag">IoT</span></div>
</div>

</div>
</div>
</div>

<!-- CERTIFICATIONS -->
<div class="s-alt" id="certifications">
<div class="s-wrap">
<div class="s-label">// Certifications</div>
<h2 class="s-title">Certifications &amp; Training</h2>
<div class="divider"></div>

<div class="cert-cat">
<div class="cert-cat-title">NPTEL</div>
<div class="cert-row">
<!-- REPLACE href="#" with your Google Drive link for each certificate -->
<a class="cert-btn" href="#" target="_blank">📄 Digital Circuits</a>
<a class="cert-btn" href="#" target="_blank">📄 Analog Circuits</a>
<a class="cert-btn" href="#" target="_blank">📄 8051 Architecture &amp; Debugging</a>
</div>
</div>

<div class="cert-cat">
<div class="cert-cat-title">Spectrum DDU</div>
<div class="cert-row">
<a class="cert-btn" href="#" target="_blank">📄 AI/ML &amp; Raspberry Pi</a>
<a class="cert-btn" href="#" target="_blank">📄 Introduction to Robotics</a>
</div>
</div>

<div class="cert-cat">
<div class="cert-cat-title">NELIT</div>
<div class="cert-row">
<a class="cert-btn" href="#" target="_blank">📄 Embedded for Beginners</a>
</div>
</div>

<div class="cert-cat">
<div class="cert-cat-title">Robolearn</div>
<div class="cert-row">
<a class="cert-btn" href="#" target="_blank">📄 Autonomous Vehicle Development</a>
</div>
</div>

<div class="cert-cat">
<div class="cert-cat-title">Pantech.AI</div>
<div class="cert-row">
<a class="cert-btn" href="#" target="_blank">📄 Embedded Systems Design</a>
<a class="cert-btn" href="#" target="_blank">📄 Embedded System Design using ARM Cortex M4</a>
<a class="cert-btn" href="#" target="_blank">📄 RTOS</a>
<a class="cert-btn" href="#" target="_blank">📄 Computer Vision &amp; Machine Learning</a>
<a class="cert-btn" href="#" target="_blank">📄 Autonomous Systems</a>
</div>
</div>

</div>
</div>

<!-- COMPETITIONS -->
<div style="background:var(--bg);" id="competitions">
<div class="s-wrap">
<div class="s-label">// Competitions</div>
<h2 class="s-title">Competitions</h2>
<div class="divider"></div>
<div class="comp-grid">
<div class="comp-card">
<div class="comp-icon">🤖</div>
<div>
<div class="comp-title">Robocon 2025</div>
<div class="comp-sub">Basketball Playing Robot</div>
</div>
</div>
<div class="comp-card">
<div class="comp-icon">🥋</div>
<div>
<div class="comp-title">Robocon 2026</div>
<div class="comp-sub">Kung-Fu Robot</div>
</div>
</div>
<div class="comp-card">
<div class="comp-icon">🧠</div>
<div>
<div class="comp-title">DU Hacks 5.0</div>
<div class="comp-sub">Retrieval Augmented Generation(RAG) based Local Research Assistant</div>
</div>
</div>
<div class="comp-card">
<div class="comp-icon">🌊</div>
<div>
<div class="comp-title">Gujcost Robofest 5.0</div>
<div class="comp-sub">Autonomous Underwater Vehicle</div>
</div>
</div>
</div>
</div>
</div>


<!-- HOSTED / COORDINATED EVENTS -->
<div class="s-alt" id="events">
<div class="s-wrap">
<div class="s-label">// Events</div>
<h2 class="s-title">Hosted &amp; Coordinated</h2>
<div class="divider"></div>
<div class="ev-grid">

<div class="ev-card">
<div class="ev-title">SpecteQ 2026</div>
<div class="ev-role">Lead Coordinator &amp; Presenter</div>
<!-- REPLACE href="#" with your Google Drive link -->
<a class="ev-btn" href="#" target="_blank">↗ View Details</a>
</div>

<div class="ev-card">
<div class="ev-title">Eureka 4.0</div>
<div class="ev-role">Coordinator</div>
<a class="ev-btn" href="#" target="_blank">↗ View Details</a>
</div>

<div class="ev-card">
<div class="ev-title">AI/ML in 6G Communication</div>
<div class="ev-role">Coordinator</div>
<a class="ev-btn" href="#" target="_blank">↗ View Details</a>
</div>

<div class="ev-card">
<div class="ev-title">Advance Robotics</div>
<div class="ev-role">Coordinator &amp; Presenter</div>
<a class="ev-btn" href="#" target="_blank">↗ View Details</a>
</div>

</div>
</div>
</div>

<!-- CONTACT -->
<div style="background:var(--bg);" id="contact">
<div class="s-wrap">
<div class="s-label">// Contact</div>
<h2 class="s-title">Let's Connect</h2>
<div class="divider"></div>
<div class="contact-box">
<div class="c-title">Open to Opportunities</div>
<div class="c-sub">
I'm actively looking for research roles, internships, and projects at the<br>
intersection of embedded systems, robotics, and edge AI.<br>
Let's build something meaningful.
</div>
<div class="c-links">
<a class="c-link" href="mailto:panchaldhairya1314@gmail.com">✉&nbsp; Email Me</a>
<a class="c-link" href="https://github.com/BareMetalBits" target="_blank">⌥&nbsp; GitHub</a>
<a class="c-link" href="https://www.linkedin.com/in/dhairya-panchal-950a46285/" target="_blank">↗&nbsp; LinkedIn</a>
<a class="c-link" href="tel:+917600732550">☏&nbsp; Call Me</a>
</div>
</div>
</div>
</div>

<!-- FOOTER -->
<div class="footer">
<p>Dhairya Panchal &nbsp;·&nbsp; ECE @ Dharmsinh Desai University &nbsp;·&nbsp; Built with Streamlit</p>
</div>

</body>
</html>"""

# Adjust height if any section is clipped — increase the value below
components.html(HTML, height=8200, scrolling=False)