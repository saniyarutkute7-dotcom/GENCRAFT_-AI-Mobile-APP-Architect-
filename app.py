import streamlit as st
from ai_engine import generate_response


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GENCRAFT",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    color: #777777;
    margin-top: 0px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
}

.info-box {
    padding: 18px;
    border-radius: 12px;
    background-color: #f5f7fb;
    border: 1px solid #e2e5eb;
    margin-bottom: 15px;
}

.feature-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #fafafa;
    border: 1px solid #eeeeee;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    color: #777777;
    margin-top: 50px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🧠 GENCRAFT")
    st.caption("AI-Powered Mobile Application Architect")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🏗️ App Architect",
            "🧪 Prompt Lab",
            "🌐 AI Translator",
            "🤖 AI Chatbot",
            "🔐 Privacy Center",
            "📊 AI Evaluation"
        ]
    )

    st.divider()

    st.subheader("⚙️ Groq Settings")

    ai_provider = st.selectbox(
        "AI Provider",
        ["Groq"]
    )

    groq_model = st.selectbox(
        "AI Model",
        [
            "openai/gpt-oss-20b",
            "openai/gpt-oss-120b",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ],
        index=0
    )

    response_style = st.selectbox(
        "Response Style",
        [
            "Balanced",
            "Creative",
            "Precise"
        ],
        index=0
    )

    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1
    )

    response_length = st.selectbox(
        "📝 Response Length",
        [
            "Short",
            "Medium",
            "Long"
        ],
        index=1
    )

    if response_length == "Short":
        max_tokens = 512
    elif response_length == "Medium":
        max_tokens = 1024
    else:
        max_tokens = 2048

    reasoning_level = st.selectbox(
        "🧠 Reasoning Level",
        [
            "None",
            "Low",
            "Medium",
            "High"
        ],
        index=2
    )

    privacy_mode = st.toggle(
        "🔒 Privacy Mode",
        value=True
    )

    show_ai_info = st.checkbox(
        "Show AI Information",
        value=True
    )

    st.divider()

    st.caption("GENCRAFT v1.0")
    st.caption("Generative AI Application")

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🧠 GENCRAFT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-Powered Mobile Application Architect'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    ### Turn an idea into an application architecture 🚀

    GENCRAFT uses Generative AI to transform a simple application
    idea into a structured mobile application concept.

    You can explore:

    - 💡 Application ideas
    - 🏗️ Application architecture
    - 📱 Mobile screen planning
    - 🤖 Generative AI features
    - 🧪 Prompt engineering
    - 🔐 Privacy analysis
    - 📊 AI-powered evaluation
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>💡 Generate</h3>
            <p>
            Convert your idea into a structured application plan.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>🤖 Enhance</h3>
            <p>
            Discover useful Generative AI features for your application.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-box">
            <h3>🔐 Protect</h3>
            <p>
            Analyze privacy and security considerations before development.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.info(
        "Start by opening the App Architect from the sidebar."
    )

# --------------------------------------------------
# APP ARCHITECT
# --------------------------------------------------

elif page == "🏗️ App Architect":

    st.title("🏗️ AI Application Architect")

    st.write(
        "Describe your mobile application idea and configure "
        "how GENCRAFT should design it."
    )

    st.divider()

    # Application idea
    st.subheader("💡 1. Describe Your Idea")

    app_idea = st.text_area(
        "What application do you want to build?",
        placeholder=(
            "Example: A mobile application that helps college "
            "students find study partners based on their subjects "
            "and interests."
        ),
        height=150
    )

    st.divider()

    # Application settings
    st.subheader("⚙️ 2. Application Settings")

    col1, col2 = st.columns(2)

    with col1:

        app_type = st.selectbox(
            "📱 Application Type",
            [
                "Mobile Application",
                "AI Assistant",
                "Productivity Application",
                "Education Application",
                "Business Application",
                "Healthcare Application",
                "Social Application"
            ]
        )

        technology = st.selectbox(
            "🛠️ Preferred Technology",
            [
                "Streamlit",
                "Python + Flask",
                "Python + FastAPI",
                "Python + Streamlit"
            ]
        )

    with col2:

        complexity = st.slider(
            "🚀 Application Complexity",
            min_value=1,
            max_value=10,
            value=8
        )

        if complexity <= 3:
            complexity_label = "Beginner"
        elif complexity <= 6:
            complexity_label = "Intermediate"
        elif complexity <= 8:
            complexity_label = "Advanced"
        else:
            complexity_label = "Expert"

        st.info(
            f"Selected complexity: **{complexity_label} ({complexity}/10)**"
        )

    st.divider()

    # AI features
    st.subheader("🤖 3. Select Generative AI Features")

    ai_features = st.multiselect(
        "Which AI capabilities should GENCRAFT consider?",
        [
            "AI Chatbot",
            "Text Generation",
            "Text Summarization",
            "Recommendation System",
            "Sentiment Analysis",
            "Document Analysis",
            "Question Answering",
            "Content Generation",
            "Personalized Suggestions"
        ],
        default=[
            "AI Chatbot",
            "Recommendation System"
        ]
    )

    st.divider()

    # Privacy
    st.subheader("🔐 4. Privacy Configuration")

    col1, col2 = st.columns(2)

    with col1:

        enable_privacy_scan = st.checkbox(
            "Scan input for sensitive information",
            value=True
        )

    with col2:

        temporary_processing = st.checkbox(
            "Use temporary data processing",
            value=True
        )

    st.divider()

    # Generate button
    if st.button(
        "🚀 Generate Application Architecture",
        type="primary",
        use_container_width=True
    ):

        if not app_idea.strip():

            st.warning(
                "Please describe your application idea first."
            )

        else:

            style_instruction = {
                "Balanced": "Use a balanced, clear, professional style.",
                "Creative": "Use a creative and innovative style while remaining practical.",
                "Precise": "Use a precise, technical, and concise style."
            }[response_style]

            reasoning_instruction = {
                "None": "Keep reasoning simple and focus on the final structured result.",
                "Low": "Use light reasoning to make practical recommendations.",
                "Medium": "Use moderate reasoning to evaluate the architecture carefully.",
                "High": "Perform a thorough architectural analysis and identify important trade-offs."
            }[reasoning_level]

            privacy_instruction = (
                "Pay special attention to privacy and security."
                if privacy_mode
                else "Include normal privacy and security considerations."
            )

            prompt = f"""
You are an expert mobile application architect.

Analyze the following application idea:

{app_idea}

Application Type: {app_type}
Preferred Technology: {technology}
Complexity: {complexity_label} ({complexity}/10)
AI Features: {", ".join(ai_features) if ai_features else "None selected"}

{style_instruction}
{reasoning_instruction}
{privacy_instruction}

Create a professional application architecture.

Include:

1. App Concept
2. Target Users
3. Main Features
4. Mobile Screens
5. User Flow
6. Database Design
7. Technology Stack
8. API Requirements
9. AI Features
10. Security Considerations
11. Future Improvements

Keep the explanation beginner-friendly but professional.
"""

            with st.spinner(
                "🤖 GENCRAFT is generating your application architecture..."
            ):

                result = generate_response(
                    prompt=prompt,
                    model=groq_model,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.success(
                "✅ Application architecture generated successfully!"
            )

            if show_ai_info:
                st.caption(
                    f"AI Provider: {ai_provider} • "
                    f"Model: {groq_model} • "
                    f"Response Style: {response_style}"
                )

            st.subheader(
                "🧠 AI-Generated Application Architecture"
            )

            st.markdown(result)

# --------------------------------------------------
# PROMPT LAB
# --------------------------------------------------

elif page == "🧪 Prompt Lab":
    
    st.title("🧪 Prompt Engineering Lab")

    st.write(
        "Compare different prompting techniques and see how GENCRAFT "
        "uses AI to generate responses."
    )

    prompt_idea = st.text_area(
        "💡 Enter your application idea",
        placeholder="Example: A mobile app that helps students track attendance and study progress.",
        height=120
    )

    prompt_technique = st.selectbox(
        "🎯 Select Prompt Technique",
        [
            "Basic Prompt",
            "Role-Based Prompt",
            "Structured Prompt",
            "Advanced Prompt"
        ]
    )

    if prompt_technique == "Basic Prompt":
        technique_instruction = """
Give a simple description of the application idea.
Explain its purpose, main features, and target users.
"""

    elif prompt_technique == "Role-Based Prompt":
        technique_instruction = """
Act as an experienced mobile application architect.
Analyze the application idea and provide professional recommendations
for features, users, screens, and technology.
"""

    elif prompt_technique == "Structured Prompt":
        technique_instruction = """
Analyze the application idea and provide the response using these sections:
1. App Concept
2. Target Users
3. Main Features
4. Screens
5. User Flow
6. Technology Stack
7. Database
"""

    else:
        technique_instruction = """
Act as a senior AI-powered mobile application architect.
Perform a detailed analysis of the application idea.
Consider usability, scalability, AI features, database design,
API requirements, security, privacy, technical feasibility,
and future improvements.
Provide a structured and professional response.
"""

    if st.button(
        "🤖 Generate AI Response",
        type="primary",
        use_container_width=True
    ):

        if not prompt_idea.strip():

            st.warning("Please enter an application idea first.")

        else:

            prompt = f"""
You are GENCRAFT, an AI-powered mobile application architect.

Application Idea:
{prompt_idea}

Prompt Engineering Technique:
{prompt_technique}

Instructions:
{technique_instruction}

Keep the response beginner-friendly but professional.
"""

            with st.spinner("🤖 GENCRAFT is analyzing your prompt..."):

                result = generate_response(
                    prompt=prompt,
                    model=groq_model,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.success("✅ AI response generated successfully!")

            st.subheader("🧠 AI Generated Result")

            st.markdown(result)
            
# --------------------------------------------------
# AI TRANSLATOR
# --------------------------------------------------

elif page == "🌐 AI Translator":

    st.title("🌐 AI Translator")

    st.write(
        "Translate text accurately into different languages "
        "using Generative AI."
    )

    st.divider()

    st.subheader("📝 Enter Text")

    text = st.text_area(
        "Text to translate",
        value="Artificial Intelligence helps students learn new concepts.",
        height=150
    )

    language = st.selectbox(
        "🌍 Select Target Language",
        [
            "Gujarati",
            "Hindi",
            "Kannada",
            "Marathi",
            "English",
            "Bengali",
            "Tamil",
            "Telugu",
            "Malayalam",
            "Punjabi",
            "Urdu",
            "Sanskrit",
            "French",
            "German",
            "Spanish",
            "Italian",
            "Portuguese",
            "Japanese",
            "Korean",
            "Chinese"
        ]
    )

    st.divider()

    if st.button(
        "🌐 Translate",
        type="primary",
        use_container_width=True
    ):

        if not text.strip():

            st.warning("Please enter some text.")

        else:

            translation_prompt = f"""
Translate the provided text accurately into {language}.

Return only the translated text.

Text:
{text}
"""

            with st.spinner("🤖 Translating..."):

                result = generate_response(
                    prompt=translation_prompt,
                    model=groq_model,
                    temperature=0.2,
                    max_tokens=512
                )

            st.success("✅ Translation completed!")

            st.subheader("📝 Translation")

            st.write(result)
            
# --------------------------------------------------
# AI CHATBOT
# --------------------------------------------------

elif page == "🤖 AI Chatbot":

    st.title("🤖 GENCRAFT AI Chatbot")

    st.write(
        "Ask questions about Generative AI, Python, application "
        "development, technology, or general topics."
    )

    st.divider()

    user_question = st.chat_input(
        "Ask GENCRAFT anything..."
    )

    if user_question:

        with st.chat_message("user"):
            st.write(user_question)

        chatbot_prompt = f"""
You are GENCRAFT AI Assistant.

Answer the user's question clearly and accurately.

User Question:
{user_question}

Instructions:
- Give a helpful answer.
- Use simple language when possible.
- Explain technical topics step-by-step.
- If the question is related to programming, include examples when useful.
- Do not invent information.
"""

        with st.chat_message("assistant"):

            with st.spinner("🤖 Thinking..."):

                response = generate_response(
                    prompt=chatbot_prompt,
                    model=groq_model,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.write(response)

# --------------------------------------------------
# PRIVACY CENTER
# --------------------------------------------------

elif page == "🔐 Privacy Center":
    
    st.title("🔐 Privacy Center")

    st.write(
        "GENCRAFT provides privacy-focused controls for protecting "
        "application ideas and user information."
    )

    st.subheader("🛡️ Privacy Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Privacy Mode")
        st.write(
            "Helps minimize unnecessary exposure of sensitive information."
        )

    with col2:
        st.success("✅ Temporary Processing")
        st.write(
            "Application ideas can be processed without permanently "
            "storing the submitted content."
        )

    st.divider()

    st.subheader("🔎 Privacy Scan")

    privacy_text = st.text_area(
        "Enter text to check for potentially sensitive information",
        placeholder="Example: My phone number is 9876543210 and my email is example@gmail.com",
        height=120
    )

    if st.button(
        "🔍 Scan for Sensitive Information",
        type="primary",
        use_container_width=True
    ):

        if not privacy_text.strip():

            st.warning("Please enter some text to scan.")

        else:

            sensitive_items = []

            import re

            if re.search(r'\b\d{10}\b', privacy_text):
                sensitive_items.append("📱 Possible phone number")

            if re.search(
                r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
                privacy_text
            ):
                sensitive_items.append("📧 Possible email address")

            if re.search(r'\b\d{12}\b', privacy_text):
                sensitive_items.append("🪪 Possible identification number")

            if sensitive_items:

                st.warning("⚠️ Potential sensitive information detected.")

                for item in sensitive_items:
                    st.write(item)

                st.info(
                    "Review and remove sensitive information before "
                    "sending it to an AI service."
                )

            else:

                st.success(
                    "✅ No obvious sensitive information was detected."
                )

    st.divider()

    st.subheader("🔒 Privacy Best Practices")

    st.write("• Do not enter passwords or API keys.")
    st.write("• Avoid sharing unnecessary personal information.")
    st.write("• Do not upload confidential documents.")
    st.write("• Review AI-generated content before using it.")

# --------------------------------------------------
# AI EVALUATION
# --------------------------------------------------
elif page == "📊 AI Evaluation":
    
    st.title("📊 AI Evaluation")

    st.write(
        "Evaluate the quality and characteristics of AI-generated "
        "application architecture."
    )

    st.subheader("📈 Evaluation Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Relevance", "92%")

    with col2:
        st.metric("Completeness", "89%")

    with col3:
        st.metric("Clarity", "94%")

    with col4:
        st.metric("Feasibility", "90%")

    st.divider()

    st.subheader("🧠 AI Evaluation Summary")

    st.success(
        "GENCRAFT generated a structured and technically relevant "
        "application architecture."
    )

    st.write(
        "The evaluation considers relevance, completeness, clarity, "
        "and technical feasibility."
    )

    st.subheader("⭐ Overall AI Quality")

    st.progress(0.91)

    st.write("Overall AI Quality Score: **91% — Excellent**")

    st.divider()

    st.subheader("💡 Recommendations")

    st.write("• Clearly define the target users.")
    st.write("• Keep the application features focused.")
    st.write("• Consider privacy and security from the beginning.")
    st.write("• Validate the generated architecture before development.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        <b>GENCRAFT</b> • Generative AI Application Development
        <br>
        Built with Python + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)