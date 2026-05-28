import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Dhairya Panchal | Portfolio",
    page_icon="⚡",
    layout="wide",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;700&display=swap');

/* ─ Reset & base ─ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

/* Streamlit chrome overrides */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
div[data-testid="stAppViewContainer"] { background: #0a0a0f; }

/* ─ CSS Variables ─ */
:root {
    --bg:       #0a0a0f;
    --surface:  #13131a;
    --border:   #1e1e2e;
    --accent:   #00e5ff;
    --accent2:  #7c3aed;
    --text:     #e2e8f0;
    --muted:    #64748b;
    --mono:     'Space Mono', monospace;
    --sans:     'DM Sans', sans-serif;
}

/* ─ Layout ─ */
.portfolio-wrap {
    font-family: var(--sans);
    color: var(--text);
    background: var(--bg);
    min-height: 100vh;
}

/* ─ Nav ─ */
.nav {
    position: sticky; top: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 4rem;
    background: rgba(10,10,15,0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { font-family: var(--mono); font-size: 1.1rem; color: var(--accent); font-weight: 700; }
.nav-links { display: flex; gap: 2rem; list-style: none; }
.nav-links a { 
    color: var(--muted); text-decoration: none; font-size: 0.85rem;
    letter-spacing: 0.08em; text-transform: uppercase;
    transition: color 0.2s;
}
.nav-links a:hover { color: var(--accent); }

/* ─ Hero ─ */
.hero {
    min-height: 92vh;
    display: flex; align-items: center;
    padding: 6rem 4rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background: 
        radial-gradient(ellipse 60% 60% at 80% 50%, rgba(124,58,237,0.12) 0%, transparent 70%),
        radial-gradient(ellipse 40% 50% at 10% 80%, rgba(0,229,255,0.08) 0%, transparent 60%);
    pointer-events: none;
}
.hero-grid {
    display: grid; grid-template-columns: 1fr auto;
    gap: 4rem; align-items: center;
    width: 100%; max-width: 1200px; margin: 0 auto;
    position: relative;
}
.hero-tag {
    font-family: var(--mono); font-size: 0.8rem;
    color: var(--accent); letter-spacing: 0.15em;
    text-transform: uppercase; margin-bottom: 1rem;
}
.hero-name {
    font-size: clamp(3rem, 6vw, 5.5rem);
    font-weight: 700; line-height: 1.05;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}
.hero-role {
    font-size: 1.25rem; color: var(--muted);
    font-weight: 300; margin-bottom: 2rem; line-height: 1.6;
}
.hero-role span { color: var(--accent); font-weight: 500; }
.hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary {
    padding: 0.75rem 2rem;
    background: var(--accent); color: #0a0a0f;
    font-family: var(--mono); font-size: 0.8rem;
    font-weight: 700; letter-spacing: 0.05em;
    text-decoration: none; border-radius: 4px;
    transition: transform 0.2s, box-shadow 0.2s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,229,255,0.3); }
.btn-outline {
    padding: 0.75rem 2rem;
    border: 1px solid var(--border); color: var(--text);
    font-family: var(--mono); font-size: 0.8rem;
    letter-spacing: 0.05em;
    text-decoration: none; border-radius: 4px;
    transition: border-color 0.2s, color 0.2s;
}
.btn-outline:hover { border-color: var(--accent); color: var(--accent); }

/* Photo placeholder */
.photo-wrap {
    width: 240px; height: 240px;
    border-radius: 50%;
    border: 2px solid var(--border);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    background: var(--surface);
    position: relative; overflow: hidden;
    flex-shrink: 0;
}
.photo-wrap::before {
    content: '';
    position: absolute; inset: -2px;
    border-radius: 50%;
    background: conic-gradient(var(--accent), var(--accent2), var(--accent));
    z-index: -1; animation: spin 6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.photo-inner {
    width: calc(100% - 4px); height: calc(100% - 4px);
    border-radius: 50%; background: var(--surface);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center; gap: 0.5rem;
}
.photo-icon { font-size: 3.5rem; }
.photo-hint { font-size: 0.7rem; color: var(--muted); font-family: var(--mono); text-align: center; padding: 0 1rem; }

/* ─ Sections ─ */
.section {
    padding: 6rem 4rem;
    max-width: 1200px; margin: 0 auto;
}
.section-label {
    font-family: var(--mono); font-size: 0.75rem;
    color: var(--accent); letter-spacing: 0.2em;
    text-transform: uppercase; margin-bottom: 0.75rem;
}
.section-title {
    font-size: 2.5rem; font-weight: 700;
    letter-spacing: -0.02em;
    color: #fff; margin-bottom: 3rem;
}
.divider {
    height: 1px;
    background: linear-gradient(90deg, var(--accent) 0%, transparent 60%);
    margin: 0 0 3rem;
}

/* ─ About ─ */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }
.about-text { font-size: 1.05rem; line-height: 1.8; color: #94a3b8; }
.about-text p { margin-bottom: 1rem; }
.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
.stat-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 1.5rem;
    transition: border-color 0.2s;
}
.stat-card:hover { border-color: var(--accent); }
.stat-num { font-family: var(--mono); font-size: 2rem; font-weight: 700; color: var(--accent); }
.stat-label { font-size: 0.8rem; color: var(--muted); margin-top: 0.25rem; }

/* ─ Skills ─ */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; }
.skill-group {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 1.5rem;
    transition: transform 0.2s, border-color 0.2s;
}
.skill-group:hover { transform: translateY(-3px); border-color: var(--accent2); }
.skill-group-title {
    font-family: var(--mono); font-size: 0.75rem;
    color: var(--accent2); letter-spacing: 0.1em;
    text-transform: uppercase; margin-bottom: 1rem;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.skill-tag {
    background: rgba(0,229,255,0.07); border: 1px solid rgba(0,229,255,0.15);
    color: #94a3b8; font-size: 0.78rem;
    padding: 0.3rem 0.75rem; border-radius: 4px;
    font-family: var(--mono);
}

/* ─ Experience ─ */
.timeline { position: relative; padding-left: 2rem; }
.timeline::before {
    content: ''; position: absolute;
    left: 0; top: 0.5rem; bottom: 0;
    width: 2px; background: var(--border);
}
.timeline-item { position: relative; margin-bottom: 3rem; }
.timeline-dot {
    position: absolute; left: -2.45rem; top: 0.4rem;
    width: 12px; height: 12px; border-radius: 50%;
    background: var(--accent); border: 2px solid var(--bg);
    box-shadow: 0 0 12px rgba(0,229,255,0.5);
}
.timeline-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; }
.timeline-role { font-size: 1.1rem; font-weight: 600; color: #fff; }
.timeline-date { font-family: var(--mono); font-size: 0.78rem; color: var(--accent); }
.timeline-org { font-size: 0.9rem; color: var(--accent2); margin: 0.25rem 0 0.75rem; }
.timeline-desc { font-size: 0.9rem; color: #94a3b8; line-height: 1.7; }
.timeline-desc li { margin-bottom: 0.35rem; margin-left: 1.2rem; }

/* ─ Projects ─ */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1.5rem; }
.project-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 10px; padding: 2rem;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
    display: flex; flex-direction: column;
}
.project-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent);
    box-shadow: 0 12px 40px rgba(0,229,255,0.08);
}
.project-badge {
    display: inline-block;
    font-family: var(--mono); font-size: 0.68rem;
    color: var(--accent2); background: rgba(124,58,237,0.12);
    border: 1px solid rgba(124,58,237,0.25);
    padding: 0.2rem 0.6rem; border-radius: 3px;
    margin-bottom: 1rem; letter-spacing: 0.08em;
    text-transform: uppercase;
}
.project-title { font-size: 1.15rem; font-weight: 600; color: #fff; margin-bottom: 0.75rem; }
.project-desc { font-size: 0.88rem; color: #94a3b8; line-height: 1.7; flex: 1; margin-bottom: 1.25rem; }
.project-stack { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.stack-tag {
    background: rgba(0,229,255,0.05); border: 1px solid rgba(0,229,255,0.12);
    color: #64748b; font-size: 0.72rem;
    padding: 0.2rem 0.55rem; border-radius: 3px;
    font-family: var(--mono);
}

/* ─ Achievements ─ */
.achieve-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; }
.achieve-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 1.25rem 1.5rem;
    display: flex; align-items: flex-start; gap: 1rem;
    transition: border-color 0.2s;
}
.achieve-card:hover { border-color: var(--accent2); }
.achieve-icon { font-size: 1.5rem; flex-shrink: 0; margin-top: 0.1rem; }
.achieve-title { font-size: 0.95rem; font-weight: 600; color: #fff; margin-bottom: 0.2rem; }
.achieve-sub { font-size: 0.8rem; color: var(--muted); }

/* ─ Contact ─ */
.contact-wrap {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 12px; padding: 3rem;
    text-align: center; max-width: 700px; margin: 0 auto;
}
.contact-title { font-size: 1.8rem; font-weight: 700; color: #fff; margin-bottom: 1rem; }
.contact-sub { color: var(--muted); margin-bottom: 2.5rem; line-height: 1.7; }
.contact-links { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; }
.contact-link {
    display: flex; align-items: center; gap: 0.6rem;
    padding: 0.75rem 1.5rem;
    border: 1px solid var(--border); border-radius: 6px;
    color: var(--text); text-decoration: none;
    font-family: var(--mono); font-size: 0.82rem;
    transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.contact-link:hover { border-color: var(--accent); color: var(--accent); background: rgba(0,229,255,0.05); }

/* ─ Footer ─ */
.footer {
    padding: 2rem 4rem; text-align: center;
    border-top: 1px solid var(--border);
    font-family: var(--mono); font-size: 0.75rem;
    color: var(--muted);
}

/* ─ Responsive ─ */
@media (max-width: 768px) {
    .hero { padding: 4rem 1.5rem; }
    .hero-grid { grid-template-columns: 1fr; }
    .photo-wrap { margin: 0 auto; }
    .nav { padding: 1rem 1.5rem; }
    .nav-links { gap: 1rem; }
    .section { padding: 4rem 1.5rem; }
    .about-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)


# ── Portfolio HTML ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="portfolio-wrap">

<!-- NAV -->
<nav class="nav">
  <div class="nav-logo">DP//</div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#contact">Contact</a></li>
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
        <a class="btn-primary" href="mailto:panchaldhairya1314@gmail.com">Get in Touch</a>
        <a class="btn-outline" href="https://github.com/BareMetalBits" target="_blank">GitHub →</a>
      </div>
    </div>
    <div>
      <div class="photo-wrap">
        <div class="photo-inner">
          <div class="photo-icon">🧑‍💻</div>
          <div class="photo-hint">Replace with your photo</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<div id="about" style="background: #0d0d14;">
<div class="section">
  <div class="section-label">// 01 &nbsp; about</div>
  <h2 class="section-title">Who I Am</h2>
  <div class="divider"></div>
  <div class="about-grid">
    <div class="about-text">
      <p>I'm a B.Tech Electronics & Communication Engineering student at <strong style="color:#e2e8f0;">Dharmsinh Desai University</strong>, driven by a passion for building systems where hardware meets intelligence.</p>
      <p>My work spans low-level firmware and custom RTOS development (C, ARM Assembly, Cortex-M4), all the way up to deploying deep learning models on constrained edge hardware using TensorFlow, PyTorch, and CUDA.</p>
      <p>I believe the most exciting problems in tech live at the boundary between embedded systems and AI — and that's exactly where I like to build.</p>
      <p>Outside the lab, I play Trinity College London certified Electronic Keyboard and do 3D animation with Blender.</p>
    </div>
    <div class="stat-grid">
      <div class="stat-card">
        <div class="stat-num">6+</div>
        <div class="stat-label">Projects Built</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">3</div>
        <div class="stat-label">Internships</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">4</div>
        <div class="stat-label">Competitions</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">10+</div>
        <div class="stat-label">Certifications</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- SKILLS -->
<div id="skills" style="background: #0a0a0f;">
<div class="section">
  <div class="section-label">// 02 &nbsp; skills</div>
  <h2 class="section-title">Technical Expertise</h2>
  <div class="divider"></div>
  <div class="skills-grid">
    <div class="skill-group">
      <div class="skill-group-title">Programming Languages</div>
      <div class="skill-tags">
        <span class="skill-tag">C</span><span class="skill-tag">C++</span>
        <span class="skill-tag">Python</span><span class="skill-tag">ARM Assembly</span>
        <span class="skill-tag">8051 Assembly</span><span class="skill-tag">8086 Assembly</span>
      </div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">AI / ML Frameworks</div>
      <div class="skill-tags">
        <span class="skill-tag">TensorFlow</span><span class="skill-tag">PyTorch</span>
        <span class="skill-tag">CUDA</span><span class="skill-tag">Ollama</span>
        <span class="skill-tag">LangChain</span><span class="skill-tag">OpenCV</span>
      </div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">Hardware & MCUs</div>
      <div class="skill-tags">
        <span class="skill-tag">STM32</span><span class="skill-tag">Nordic NRF54</span>
        <span class="skill-tag">ARM Cortex-M4</span><span class="skill-tag">Raspberry Pi</span>
        <span class="skill-tag">ESP32</span><span class="skill-tag">Arduino</span>
        <span class="skill-tag">8051</span>
      </div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">IDEs & Simulation</div>
      <div class="skill-tags">
        <span class="skill-tag">ARM Keil</span><span class="skill-tag">STM32CubeIDE</span>
        <span class="skill-tag">Nordic SDK</span><span class="skill-tag">Proteus</span>
        <span class="skill-tag">Multisim</span>
      </div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">Other Skills</div>
      <div class="skill-tags">
        <span class="skill-tag">3D Animation (Blender)</span>
        <span class="skill-tag">Electronic Keyboard</span>
        <span class="skill-tag">RTOS Development</span>
        <span class="skill-tag">Firmware OTA</span>
      </div>
    </div>
  </div>
</div>
</div>

<!-- EXPERIENCE -->
<div id="experience" style="background: #0d0d14;">
<div class="section">
  <div class="section-label">// 03 &nbsp; experience</div>
  <h2 class="section-title">Work Experience</h2>
  <div class="divider"></div>
  <div class="timeline">

    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-header">
        <div class="timeline-role">Summer Intern — Embedded Systems</div>
        <div class="timeline-date">May 2026 – Jun 2026</div>
      </div>
      <div class="timeline-org">Semconix Tech Solutions · Gandhinagar, India</div>
      <div class="timeline-desc">
        <ul>
          <li>Developed an Over-The-Air (OTA) firmware update protocol for Nordic NRF54 series MCUs.</li>
          <li>Gained hands-on expertise in low-level firmware development and wireless communication protocols.</li>
        </ul>
      </div>
    </div>

    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-header">
        <div class="timeline-role">Senior Associate</div>
        <div class="timeline-date">Aug 2025 – Jul 2026</div>
      </div>
      <div class="timeline-org">SPECTRUM DDU · Dharmsinh Desai University, Nadiad</div>
      <div class="timeline-desc">
        <ul>
          <li>Spearheaded SpecteQ, a 1.5-month robotics event fostering hands-on learning across DDU.</li>
          <li>Organized workshops covering robotics, AI/ML, and Raspberry Pi for university participants.</li>
        </ul>
      </div>
    </div>

    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-header">
        <div class="timeline-role">Internship Trainee — Embedded Systems & ML</div>
        <div class="timeline-date">Apr 2025 – Jun 2025</div>
      </div>
      <div class="timeline-org">Pantech.AI · Remote, Ahmedabad</div>
      <div class="timeline-desc">
        <ul>
          <li>Built a plant disease identification system using image analysis and deep learning techniques.</li>
          <li>Covered computer vision, RTOS, IoT, and embedded C across structured training modules.</li>
        </ul>
      </div>
    </div>

  </div>
</div>
</div>

<!-- PROJECTS -->
<div id="projects" style="background: #0a0a0f;">
<div class="section">
  <div class="section-label">// 04 &nbsp; projects</div>
  <h2 class="section-title">What I've Built</h2>
  <div class="divider"></div>
  <div class="projects-grid">

    <div class="project-card">
      <span class="project-badge">Robotics · SSIP Cell DDU</span>
      <div class="project-title">Multi-Purpose 3-Fingered Gripper</div>
      <div class="project-desc">Designed and developed a 3-fingered robotic gripper with adaptive multi-purpose grasping. Integrated servo actuation and embedded control for precise manipulation tasks in unstructured environments.</div>
      <div class="project-stack">
        <span class="stack-tag">STM32</span><span class="stack-tag">Servo Control</span>
        <span class="stack-tag">Embedded C</span><span class="stack-tag">Kinematics</span>
      </div>
    </div>

    <div class="project-card">
      <span class="project-badge">AI/ML · SSIP Cell DDU</span>
      <div class="project-title">Smart Healthcare Companion</div>
      <div class="project-desc">Built an AI-powered smart healthcare companion leveraging embedded systems and ML for patient monitoring and intelligent health assistance. Combines sensor fusion with on-device inference.</div>
      <div class="project-stack">
        <span class="stack-tag">TensorFlow Lite</span><span class="stack-tag">Raspberry Pi</span>
        <span class="stack-tag">Sensor Fusion</span><span class="stack-tag">Python</span>
      </div>
    </div>

    <div class="project-card">
      <span class="project-badge">NLP · DU Hacks 5.0</span>
      <div class="project-title">RAG-based Local Research Assistant</div>
      <div class="project-desc">Developed an efficient, token-optimized Retrieval Augmented Generation (RAG) based local research assistant for maximized context retention. Runs entirely offline with local LLMs via Ollama.</div>
      <div class="project-stack">
        <span class="stack-tag">LangChain</span><span class="stack-tag">Ollama</span>
        <span class="stack-tag">RAG</span><span class="stack-tag">Python</span><span class="stack-tag">FAISS</span>
      </div>
    </div>

    <div class="project-card">
      <span class="project-badge">Edge AI · Minor Research Project</span>
      <div class="project-title">Industrial Vision Intelligence System</div>
      <div class="project-desc">Integrates robotics, control systems, and deep learning (1D/2D CNN) with embedded edge computing for real-time signal and image processing in industrial environments — no cloud dependency.</div>
      <div class="project-stack">
        <span class="stack-tag">CNN</span><span class="stack-tag">Edge Computing</span>
        <span class="stack-tag">PyTorch</span><span class="stack-tag">C++</span>
      </div>
    </div>

    <div class="project-card">
      <span class="project-badge">Embedded · Minor Research Project</span>
      <div class="project-title">Edge RTOS</div>
      <div class="project-desc">Custom RTOS kernel for Cortex-M4 MCUs enabling real-time edge ML inferencing. Implements preemptive scheduling, memory management, and IPC primitives from scratch in C and ARM Assembly.</div>
      <div class="project-stack">
        <span class="stack-tag">C</span><span class="stack-tag">ARM Assembly</span>
        <span class="stack-tag">Cortex-M4</span><span class="stack-tag">RTOS</span>
      </div>
    </div>

    <div class="project-card">
      <span class="project-badge">DL · Minor Research Project</span>
      <div class="project-title">Monocular Depth Estimation for Visually Impaired</div>
      <div class="project-desc">Designed and deployed a custom Transformer-based approach for Monocular Depth Estimation on edge hardware to assist visually impaired individuals with real-time spatial awareness.</div>
      <div class="project-stack">
        <span class="stack-tag">Transformers</span><span class="stack-tag">PyTorch</span>
        <span class="stack-tag">Edge Deployment</span><span class="stack-tag">TFLite</span>
      </div>
    </div>

  </div>
</div>
</div>

<!-- ACHIEVEMENTS -->
<div id="achievements" style="background: #0d0d14;">
<div class="section">
  <div class="section-label">// 05 &nbsp; achievements</div>
  <h2 class="section-title">Competitions & Events</h2>
  <div class="divider"></div>
  <div class="achieve-grid">
    <div class="achieve-card">
      <div class="achieve-icon">🏆</div>
      <div>
        <div class="achieve-title">DUHacks 5.0</div>
        <div class="achieve-sub">RAG Based Local Research Assistant</div>
      </div>
    </div>
    <div class="achieve-card">
      <div class="achieve-icon">🤖</div>
      <div>
        <div class="achieve-title">Robocon 2025</div>
        <div class="achieve-sub">Basketball Playing Robot</div>
      </div>
    </div>
    <div class="achieve-card">
      <div class="achieve-icon">🥋</div>
      <div>
        <div class="achieve-title">Robocon 2026</div>
        <div class="achieve-sub">Kung-Fu Robot</div>
      </div>
    </div>
    <div class="achieve-card">
      <div class="achieve-icon">🌊</div>
      <div>
        <div class="achieve-title">Gujcost Robofest 5.0</div>
        <div class="achieve-sub">Autonomous Underwater Vehicle</div>
      </div>
    </div>
    <div class="achieve-card">
      <div class="achieve-icon">📜</div>
      <div>
        <div class="achieve-title">NPTEL Certified</div>
        <div class="achieve-sub">Analog & Digital Circuits · 8051 Architecture</div>
      </div>
    </div>
    <div class="achieve-card">
      <div class="achieve-icon">🎹</div>
      <div>
        <div class="achieve-title">Trinity College London</div>
        <div class="achieve-sub">Certified Electronic Keyboard</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- CONTACT -->
<div id="contact" style="background: #0a0a0f;">
<div class="section">
  <div class="section-label">// 06 &nbsp; contact</div>
  <h2 class="section-title">Let's Connect</h2>
  <div class="divider"></div>
  <div class="contact-wrap">
    <div class="contact-title">Open to Opportunities</div>
    <div class="contact-sub">
      I'm actively looking for research roles, internships, and projects at the intersection of embedded systems, robotics, and edge AI. Let's build something meaningful.
    </div>
    <div class="contact-links">
      <a class="contact-link" href="mailto:panchaldhairya1314@gmail.com">
        ✉ &nbsp; panchaldhairya1314@gmail.com
      </a>
      <a class="contact-link" href="https://github.com/BareMetalBits" target="_blank">
        ⌥ &nbsp; github.com/BareMetalBits
      </a>
      <a class="contact-link" href="https://www.linkedin.com/in/dhairya-panchal-950a46285/" target="_blank">
        ↗ &nbsp; LinkedIn
      </a>
      <a class="contact-link" href="tel:+917600732550">
        ☏ &nbsp; +91 7600732550
      </a>
    </div>
  </div>
</div>
</div>

<!-- FOOTER -->
<div class="footer">
  <p>Dhairya Panchal · ECE @ Dharmsinh Desai University</p>
</div>

</div>
""", unsafe_allow_html=True)