from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "my_.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Web Resume | M Nur Uj Jaman Khan"
PAGE_ICON = ":wave:"
NAME = "Mohammad Nur Uj Jaman Khan"
DESCRIPTION = """
Senior Data Scientist, Artificial Intelligence and Computer Vision Researcher.
"""
EMAIL = "tutorials.jaman@gmail.com"
SOCIAL_MEDIA = {
    "Upwork": "https://drive.google.com/file/d/1qAsWkYOOQ2NjGkkNa5ILCwhfzaF74_GY/view?usp=sharing",
    "Fiverr": "https://drive.google.com/file/d/1ciO8SfLqdR1ohM39wyaKzQnC1vjx1s0M/view?usp=sharing",
    "Freelancers": "https://www.freelancer.com/u/Jaman1310ai",
    "LinkedIn": "https://www.linkedin.com/in/jamankhan1310/",
}
PROJECTS = {
    "🏆 Camoflouged Object Detection and Re Camo ": "https://github.com/DengPingFan/SINet/",
    "🏆 Autonomus Multipurpose Weapon System - Advance Computer Vision, Desicion Model and Robotics (confidential)": "https://www.researchgate.net/profile/Mohammad-Khan-270",
    "🏆 Bengali Folklore and NLP": "https://arxiv.org/abs/2203.06607",
    "🏆 Audio processing with AI, Cloning Voice, Style Transfer, Music Generation": "https://github.com/NisaEngineers/RudiPRO_Drummer_Web",
    "🏆 Re enhanced and fully restore image with AI": "",
    "🏆 And Many More ....": ""
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3+ Years expereince as a Data Scientist and AI developer
- ✔️ Strong hands on experience and knowledge in Computer Vision and Natural Language Processing
- ✔️ Good understanding of core programming, embedded computing and digital systems
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Very fast learner and ability to handle multi tasking
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, javascript, C++, C#
- 📊 Data Science Tools: Plotly, Matplotlib, Pandas, OpenCV, Pillow, SeaBorn & More
- 📚 Model Generation: TensorFlow, PyTorch, Transformers,  Scikit Learn, Keras 
- 🗄️ Others Major Working Area: Web , Desktop and Mobile App devolopment (Django, Flask, Electron, PyQT5, Flutter, Kivy and More)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Python and Artificial Intelligence Developer | Upwork**")
st.write("02/2021 - Present")
st.write(
    """
- ► Top Rated and !00% Job Succes Rate
- ► The projects are from almost all field of AI and Data Science - natural language processing, computer vision, chatbot, trading bot, embedded robotics, etc
- ► Created Cutom and Improve Existing Model
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**AI and Bot Developer, C++ and Python | Fiverr**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Leve 2 Seller
- ► Made various bot for customer specification, simulation software for mechanical properties and solved many projects with C++ and python
- ► Scientific Computing and large project on computer vision has been done here
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Scientist and AI Engineering | Freelancers**")
st.write("01/2023 - present")
st.write(
    """
- ► Used federate learning on sensors based data and prediction
- ► Currently doing a large project on gpt-3.5-turbo, langchain, vector database (pinecone, chromadb and faiss) and other API integrated own dataset custom bot
- ► Overall 5 star Rating
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
