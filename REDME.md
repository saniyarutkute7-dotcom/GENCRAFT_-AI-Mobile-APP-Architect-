# 🤖 GENCRAFT — AI-Powered Mobile Application Architect

GENCRAFT is an AI-powered application development assistant built using **Python, Streamlit, and Generative AI**.

It helps students and beginner developers transform application ideas into structured app architectures and provides AI-powered tools for **prompt engineering, translation, chatbot assistance, privacy analysis, and AI evaluation**.

---

## ✨ Features

### 🏠 Home
Provides an introduction to GENCRAFT and explains the purpose of the application.

### 🏗️ App Architect
Generate a structured application architecture from a simple application idea.

It can provide:

- App Concept
- Target Users
- Main Features
- Mobile Screens
- User Flow
- Database Design
- Technology Stack
- API Requirements
- AI Features
- Security Considerations
- Future Improvements

### 🧪 Prompt Lab
Experiment with different prompt engineering techniques:

- Basic Prompt
- Role-Based Prompt
- Structured Prompt
- Advanced Prompt

Users can enter an application idea and generate an AI response using the selected prompting technique.

### 🌐 AI Translator
Translate text into different languages using Generative AI.

Supported languages include:

- English
- Hindi
- Marathi
- Kannada
- Gujarati
- Bengali
- Tamil
- Telugu
- Malayalam
- Punjabi
- Urdu
- Sanskrit
- French
- German
- Spanish
- Italian
- Portuguese
- Japanese
- Korean
- Chinese

### 🤖 AI Chatbot
An AI-powered assistant that can help with:

- Generative AI
- Python
- Java
- HTML, CSS and JavaScript
- DBMS and SQL
- Data Structures
- Operating Systems
- Computer Networks
- Power BI
- Artificial Intelligence
- Machine Learning
- Project development
- Coding errors and debugging

### 🔐 Privacy & Security
GENCRAFT includes privacy and security considerations when generating application architectures.

A **Clear** option is also provided to reset the application's Streamlit session state.

### 📊 AI Evaluation
Provides an evaluation of generated AI responses using metrics such as:

- Relevance
- Completeness
- Clarity
- Feasibility

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Groq API | Generative AI |
| LLM | AI-powered responses |
| HTML/CSS | Interface styling through Streamlit |
| GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
GENCRAFT_Project/
│
├── app.py
├── ai_engine.py
├── requirements.txt
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── venv/
```

> `venv/` and API credentials should not be uploaded to GitHub.

---

## 🔑 API Configuration

GENCRAFT uses the **Groq API** for Generative AI responses.

The API key should be stored securely and should **never be written directly inside the Python source code**.

For Streamlit secrets, create:

```text
.streamlit/secrets.toml
```

and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never publish your actual API key on GitHub.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd GENCRAFT_Project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start GENCRAFT using:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## ⚙️ AI Configuration

GENCRAFT supports different AI models through Groq, including the models configured in the application.

The application also provides controls for:

- AI model
- Response style
- Temperature
- Response length
- Reasoning level
- AI information display

---

## 🔒 Security

GENCRAFT follows basic security practices such as:

- Keeping API keys outside the main Python source code
- Using `.gitignore` to prevent sensitive files from being committed
- Avoiding hard-coded API credentials
- Providing privacy and security considerations for generated architectures

**Never upload your real API key to GitHub.**

---

## 🎯 Purpose of the Project

The main purpose of GENCRAFT is to demonstrate how **Generative AI can assist in application development**.

Instead of starting an application project from scratch, a user can provide a simple idea and use GENCRAFT to generate a structured development plan.

It is designed especially for **students and beginner developers** who want to understand application architecture and explore practical uses of Generative AI.

---

## 🚀 Future Improvements

Possible future enhancements include:

- User authentication
- Database integration
- Saving generated architectures
- Exporting architecture as PDF
- More AI models
- Voice input and output
- Advanced code generation
- Application prototype generation
- Cloud deployment
- Improved AI evaluation

---

## 👩‍💻 Project Developer

**Saniya Rutkute**

BCA Student  
Interested in Web Development, AI and Application Development.

---

## 📌 Project Status

**Version:** 1.0

**Status:** Educational / Academic Project

GENCRAFT is developed as a learning project to explore **Python, Streamlit, Generative AI, prompt engineering, and AI-powered application development**.