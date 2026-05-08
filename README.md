# AI Agency Portal: Premium Motion & Geist UX

A high-end, cinematic AI Agency portal built with **Django**, **GSAP**, and the **Vercel Geist Design System**. This project transforms a standard agency interface into a professional "SaaS-grade" experience with fluid motion, interactive spotlight effects, and real-time AI capabilities.

![Version](https://img.shields.io/badge/version-2.1.0-blue.svg?style=flat-square)
![Stack](https://img.shields.io/badge/Stack-Django%20%7C%20GSAP%20%7C%20OpenAI-black.svg?style=flat-square)
![Design](https://img.shields.io/badge/Design-Geist-white.svg?style=flat-square)

---

## ✨ Key Features

### 🎬 Premium Motion Engine
- **Cinematic Reveals**: Word-by-word staggered entrance animations for hero sections.
- **Lenis Smooth Scroll**: High-performance, buttery-smooth scrolling across the entire dashboard.
- **ScrollTrigger Choreography**: Section entrance animations that build as the user explores.

### 🎨 Geist Design System
- **Spotlight Cards**: Interactive mouse-tracking highlight effects on agent cards.
- **Global Light Follow**: A subtle radial background light that tracks the cursor globally.
- **Glassmorphism**: Sticky headers and console containers with saturation and blur effects.
- **Adaptive Dark Mode**: "Dark-First" architecture with instant theme synchronization.

### 🧠 Intelligent Agency Features
- **Categorized AI Agents**: 10+ professional categories (Engineering, Design, Marketing, etc.).
- **Real-time Chat Console**: Fluid message entrance animations and "Magnetic" interaction buttons.
- **Context-Aware Prompts**: Every agent is pre-configured with specific domain expertise.

---

## 🚀 Tech Stack

- **Backend**: Python 3.x, Django 5.x
- **Frontend**: HTML5, Vanilla CSS (Geist Tokens), JavaScript (ES6+)
- **Motion**: GSAP (GreenSock), ScrollTrigger, Lenis (Smooth Scroll), SplitType
- **AI**: OpenAI GPT-4o Integration
- **Infrastructure**: Docker Ready, Render/Vercel Optimized

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ai-agency-portal
   ```

2. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory (only mandatory variable is NVIDIA_API_KEY):
   ```env
   NVIDIA_API_KEY=your_openai_key
   SECRET_KEY=your_secret_key (Optional: generated automatically if not set)
   DEBUG=False (Default is False for production)
   NVIDIA_MODEL=meta/llama-3.1-405b-instruct (Optional default)
   ```

4. **Initialize Database**
   ```bash
   python manage.py migrate
   python manage.py create_default_agents # Optional custom command
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

---

## 📐 Project Structure

```text
ai-agency-agents/
├── core/               # Project configuration
├── portal/             # Main application logic
│   ├── views.py        # AI Orchestration & UI Handlers
│   ├── models.py       # Agent & Category Definitions
│   └── templates/      # Premium Geist Templates
├── static/             # Assets & Motion Engine Scripts
├── .gitignore          # Production exclusions
└── README.md           # Documentation
```

---

## 🤝 Contributing

Contributions to the AI Agency Portal are welcome! Please follow the established Geist design tokens and GSAP motion patterns when submitting pull requests.

---

## 📄 License

MIT License - Copyright (c) 2026 AI Agency Portal
