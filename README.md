
---

```markdown
# Offline-First AI Tutor for GCE Students  
**Group 11 – SEED Inc. Innovation Program**  
**Team Members:** Tayuh Favour (PM) • Nditafon Grace • Njomen Jeanson • Sale Aieshatou • Neba Stanislas 

---

## 🧠 Project Overview
The **Offline-First AI Tutor** is a web-based learning assistant built to support **Cameroon GCE students** who face poor internet connectivity and limited access to quality tutoring.  
The system uses **Lightweight LLMs** (via Ollama) and **Retrieval-Augmented Generation (RAG)** to provide curriculum-aligned, interactive explanations — even offline.

---

## 🎯 Problem Statement
Many students preparing for the **Cameroon GCE examinations** struggle due to:
- Unreliable or costly internet access.
- Limited access to qualified tutors.
- Lack of personalized study guidance and timely feedback.

This project bridges the **urban-rural educational gap** by delivering AI-driven learning support that runs on low-end devices and functions offline.

---

## 💡 Proposed Solution
A web-based **Offline-First AI Tutor** that:
- Uses an **Ollama-hosted local model** for subject-specific Q&A (Mathematics, Physics, Biology, etc.)
- Implements **RAG** using a locally indexed database of GCE past papers, marking guides, and textbooks.
- Works **offline-first**, syncing progress and updates whenever an internet connection is detected.
- Provides **personalized learning paths** with analytics, revision plans, and topic recommendations.

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Frontend** | Next.js | Web interface for students and teachers |
| **Backend** | FastAPI | Handles AI requests, RAG pipeline, and database communication |
| **AI Model** | Ollama (Phi / Mistral) + LangChain | Local lightweight LLM for explanations and RAG |
| **Database** | SQLite (offline), Supabase (cloud sync) | Store user data, progress, and GCE content |
| **Hosting / Deployment** | Render / Supabase Edge | For online sync and updates |

---

## ⚙️ Folder Structure

```

ai-tutor-gce/
├── frontend/                  # Next.js web app (student interface)
│   ├── components/
│   ├── pages/
│   ├── public/
│   └── utils/
├── backend/                   # FastAPI server and API endpoints
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── models/
│   └── requirements.txt
├── model/                     # Ollama integration, fine-tuning scripts
│   ├── load_model.py
│   └── rag_pipeline.py
├── data/                      # GCE dataset and past papers
│   ├── raw/
│   └── processed/
├── docs/                      # Documentation (SRS, diagrams, reports)
├── .gitignore
├── README.md
└── LICENSE

````

---

## 🔄 Collaboration Workflow

1. **Main branch:** Stable, production-ready code only.
2. **Feature branches:** Each team member works on their assigned branch.
   - Example:  
     - `frontend-grace` → UI/UX  
     - `backend-jeanson` → API & RAG integration  
     - `model-favour` → Ollama + LangChain setup  
     - `docs-group11` → Reports, diagrams, and SRS
3. Pull Requests → Code Reviews → Merge to `main`

### 🧩 Branch Naming Convention
| Branch Type | Format | Example |
|--------------|--------|----------|
| Frontend | `frontend-<name>` | `frontend-grace` |
| Backend | `backend-<name>` | `backend-jeanson` |
| AI Model | `model-<name>` | `model-favour` |
| Documentation | `docs-<name>` | `docs-group11` |

---

## 🧪 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/ai-tutor-gce.git
cd ai-tutor-gce
````

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 3️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4️⃣ Model Setup (Ollama)

Install Ollama locally:
[https://ollama.ai/download](https://ollama.ai/download)

Then pull a lightweight model:

```bash
ollama pull phi
```

Run it:

```bash
ollama run phi
```

---

## 📅 Project Timeline (3 Weeks)

| Week   | Milestone                    | Deliverable                           |
| ------ | ---------------------------- | ------------------------------------- |
| Week 1 | Requirement analysis & setup | SRS, folder structure, diagrams       |
| Week 2 | Core development             | Frontend + Backend + AI integration   |
| Week 3 | Testing & refinement         | Final demo, documentation, submission |

---

## 👥 Roles and Responsibilities

| Member             | Role                           | Responsibility                                   |
| ------------------ | ------------------------------ | ------------------------------------------------ |
| **Tayuh Favour**   | Project Manager / AI Developer | Lead dev workflow, model integration, review PRs |
| **Nditafon Grace** | Frontend Developer             | Build student dashboard, UI design               |
| **Njomen Jeanson** | Backend Engineer               | Build APIs, manage RAG, connect DBs              |

---

## 📦 Collaboration Tools

| Tool                   | Purpose                              |
| ---------------------- | ------------------------------------ |
| **GitHub**             | Version control & code collaboration |
| **Trello**             | Project management (3-week roadmap)  |
| **Google Docs**        | Shared notes & reports               |
| **Draw.io**            | Diagrams and architecture design     |
| **Supabase Dashboard** | Cloud database management            |

---

## 🧩 Contribution Guide

1. Create a branch for your task.
2. Make your changes, commit often with clear messages.
3. Push your branch and open a **Pull Request**.
4. Tag the PM for review.
5. Wait for approval and merge.

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

## 📧 Contact

**SEED Inc. – Nurturing the Next Generation of Tech Talent**
Center Bolt, Mile 4, Bamenda, Cameroon
📩 Email: [info@innovatewithseed.com](mailto:info@innovatewithseed.com) | ☎️ +237 680 468 606
🌐 [Facebook](https://facebook.com/SEED) | [Instagram](https://instagram.com/innovators237) | [LinkedIn](https://linkedin.com/company/seed-inc)

---