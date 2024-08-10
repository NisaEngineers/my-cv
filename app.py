from pathlib import Path
import os
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = "main.css"
resume_file = "assets/CV.pdf"
profile_pic = "new.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Web Resume | M Nur Uj Jaman Khan"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
NAME = "Mohammad Nur Uj Jaman Khan"
DESCRIPTION = """
**Full Stack, Data Scientist & Artificial Intelligence Researcher**.
"""
EMAIL = "tutorials.jaman@gmail.com"
SOCIAL_MEDIA = {
    "Upwork": "https://drive.google.com/file/d/1qAsWkYOOQ2NjGkkNa5ILCwhfzaF74_GY/view?usp=sharing",
    "Fiverr": "https://drive.google.com/file/d/1ciO8SfLqdR1ohM39wyaKzQnC1vjx1s0M/view?usp=sharing",
    "Freelancers": "https://www.freelancer.com/u/Jaman1310ai",
    "LinkedIn": "https://www.linkedin.com/in/jamankhan1310/",
}
PROJECTS = {
    "Camouflaged Object Detection and Re Camo": "https://github.com/DengPingFan/SINet/",
    "Autonomous Multipurpose Weapon System - Advance Computer Vision, Decision Model and Robotics (confidential)": "https://www.researchgate.net/profile/Mohammad-Khan-270",
    "Bengali Folklore and NLP": "https://arxiv.org/abs/2203.06607",
    "Audio processing with AI, Cloning Voice, Style Transfer, Music Generation": "https://github.com/NisaEngineers/RudiPRO_Drummer_Web",
    "Re-enhanced and fully restore the image with AI": "",
    "And Many More ....": " "
}
# --- SOCIAL MEDIA LOGOS ---
LOGOS = {
    "Upwork": "upwork.png",
    "Fiverr": "Fiverr_Logo.png",
    "Freelancers": "Freelancer_logo.png",
    "LinkedIn": "linkedin.png",
}



# --- LOAD CSS, PDF & PROFILE PIC ---
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
        file_name="CV.pdf",
        mime="application/octet-stream",
    )
    st.write("📫 tutorials.jaman@gmail.com")


# --- SOCIAL LINKS ---
#st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))

#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    #logo = Image.open(LOGOS[platform])
    #logo = logo.resize((50, 50))  # Ensure all logos are the same dimension
    #cols[index].image(logo)
    #cols[index].markdown(f"{platform}")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 5+ Years experience as a Data Scientist and AI developer
- ✔️ Strong hands-on experience and knowledge in Computer Vision and Natural Language Processing
- ✔️ Good understanding of core programming, embedded computing, and digital systems
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Very fast learner and ability to handle multi-tasking
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- **👩‍💻 Programming**: C, C++, Python 3, JavaScript, PHP, MySQL, Java
- **📊 Data Science Tools**: TensorFlow, PyTorch, Scikit-Learn, Transformers, keras, NumPy, Pandas, Matplotlib, Plotly, Seaborn
- **📚 Machine Learning Techniques**: Machine Learning, Deep Learning, Reinforcement Learning, Active Learning
- **🖼️ Computer Vision**: Advanced image restoration, camouflage object detection, stable diffusion, YOLO8, StyleGAN3, DALLE-E3
- **🗣️ NLP & LLM**: Natural Language Processing, Text to Speech/Speech to Text, Voice Clone, Text to Image/Video
- **🌐 Web Development**: Flask, Django, Laravel
- **🛠️ Development Environments**: Visual Studio Code, Anaconda Environment and Jupyter Notebook
"""
)






# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science and AI Engineering | Freelancer.com**")
st.write("17 Aug 2023 - Continuing")
st.write(
    """
- ► Highly accomplished Data Science and AI Engineering freelancer with 0.9 years of experience, boasting a remarkable 100% Success Rate, 6 diverse projects, and 108 hours of dedicated work. Consistently delivered exceptional results, earning a consistent 5-star rating.
- ► Expertise in X-ray image analysis for disease detection, leveraging AI-based segmentation techniques.
- ► Proficient in applying data science concepts to drive precision in various domains, such as communication technology and autonomous vehicles.
- ► Developed innovative NLP-powered solutions, like Document Copilot, for efficient document handling and content generation.
- ► Successfully implemented Federated Learning for precise wave beam detection in vehicle-to-infrastructure networks, enhancing communication systems.
- ► Developed AI-powered autonomous vehicle systems, enabling safe and efficient operations through machine learning algorithms.
- ► Created a revolutionary Document Copilot/Bot, utilizing NLP to generate high-quality content quickly and overcome writer's block.
- ► Collaborated with Langchain and Hugging Face to integrate large language models (LLMs) for tailored applications, enhancing flexibility and power.
- ► Contributed to the development of X-ray image analysis for disease detection, leveraging AI-based segmentation methods for accurate diagnosis and planning.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior AI Researcher and Full Stack Developer**")
st.write("18 Mar 2022 - Continuing")
st.write(
    """
- ► Highly skilled AI/ML engineer and developer with 2.2 years of experience in C++, Python, and Machine Learning Algorithms. Proven track record of delivering high-quality results with a 100% Job Success Rate, Top Rated, completing 40+ projects, and accumulating 427 hours of work. Maintained a stellar 4.8-star overall rating.
- ► Developed various AI/ML projects, including chatbots, language models, recommender systems, and computer vision applications. Proficient in frameworks like TensorFlow, LangChain, and ChatGPT.
- ► Utilized Python for a range of projects, from AI/ML development to web application development and algorithmic trading.
- ► Applied C++ expertise in projects related to fluid dynamics simulation and stochastic control.
- ► Developed a full-fledged computer vision Exercise & physio therapy tracker application for complex therapy movement with several detection methods like YOLO8 and mediapipe with speech-activated health monitoring system.
- ► Developed multiple chatbots, including one using ChatGPT, LangChain, Whisper, and Wolfarm Alpha.
- ► Successfully implemented Advanced Deep Learning models (BERT, ROBERTa, GPT2, T5) for NLP tasks.
- ► Demonstrated expertise in Computer Vision by extracting planar roof structures from aerial images and creating an AI that understands screenshots.
- ► Built a recommender system using Python and developed various web applications, including a personal trainer and symptom checker.
- ► Conducted algorithmic trading using ML and Jupyter Notebooks.
- ► Created voice clones and TTS solutions, including a virtual microphone for real-time speech-to-speech conversion.
- ► Contributed to diverse projects, such as stochastic control and forecasting using Kalman filters, and recompiling C++ code for fluid dynamics simulation.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Computer Programmer | Fiverr**")
st.write("22 August 2016 - Continuing")
st.write(
    """
- ► Established and highly skilled Level 2 Seller on Fiverr, boasting a remarkable 5-star rating and a 10 out of 10 Success Rate. With 5.3 years of expertise in Data Analysis, Programming, and Web Development, I have delivered exceptional results across various domains.
- ► Developed versatile bots, next-generation AI image generation, and engaging chatbots that interact with users and automate tasks.
- ► Expertise in advanced image restoration, innovative camouflage detection, stable diffusion, and StyleGAN3 image generation, showcasing ability to create realistic images and analyze visual data.
- ► Created Phi and Mistral-based advance Copilots, demonstrating exceptional language understanding and reasoning capabilities.
- ► Conducted dynamic sports analytics, incorporating data to analyze and improve athletic performance.
- ► Successfully applied programming skills to develop web applications, demonstrating proficiency in various programming languages.
- ► Developed innovative and versatile AI-powered solutions, including bots, image generation, and restoration technologies.
- ► Demonstrated expertise in computer vision, natural language processing, and data analysis, solving complex problems in entertainment, engineering, scientific research, and sports analytics.
- ► Created engaging chatbots, dynamic sports analytics, and realistic fluid simulations, showcasing the ability to adapt to diverse project requirements.
- ► Utilized cutting-edge models like Phi-2 and Mistral to create advanced Copilots, highlighting expertise in NLP and AI.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Full Stack Developer | Singularity Limited**")
st.write("1 Dec 2020 - 1 Mar 2023")
st.write(
    """
- ► Result-driven professional with 2.2 years of experience in Business Analysis, Database Application, and Recommendation Engine development. Proven track record of delivering impactful solutions that drive business growth, improve customer experiences, and enhance operational efficiency.
- ► Skilled in CDR analysis, e-commerce optimization, inventory control, and CRM strategy, with a focus on driving business growth and improving customer experiences.
- ► Proficient in developing and integrating database applications to streamline business operations and improve data management.
- ► Expertise in building app-based recommender systems using machine learning to provide personalized experiences for users.
- ► Conducted CDR analysis to provide valuable insights into call patterns, network usage, and customer behavior, resulting in improved productivity and enhanced customer service for telecommunications companies.
- ► Developed e-commerce optimization strategies to improve website design, product description, search engine ranking, and shopper experience, leading to increased traffic and conversions.
- ► Implemented inventory control systems to manage stock levels, monitor customer demand, and ensure timely delivery of products, resulting in reduced inventory costs and improved supply chain management.
- ► Designed and developed Facebook marketing automation strategies to streamline marketing tasks, target audience segments, and analyze performance metrics, resulting in improved engagement and conversion rates.
- ► Integrated ERP systems with other software applications and databases to facilitate data exchange and ensure synchronization across various business functions, resulting in improved operational efficiency and reduced costs.
- ► Created business web designs that effectively represented businesses online, incorporating user-friendly navigation, high-quality images, clear call-to-action buttons, and visually appealing layouts, resulting in improved online presence and customer engagement.
- ► Developed CRM strategies to manage and nurture customer relationships, provide personalized experiences, and build stronger relationships, resulting in improved customer satisfaction and loyalty.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Research Assistant | Bangladesh Agriculture University**")
st.write("Aug 2020 - Jul 2023")
st.write(
    """
- ► Designed and developed an IoT system for monitoring plant health and environmental conditions, predicting optimal harvesting times for maximum production.
- ► Built a deep learning-based plant disease detection system for prompt identification and treatment.
- ► Successfully deployed YOLO8 custom training for rice grain classification and counting, revolutionizing intelligent rice mills.
- ► Classified pumpkin flowers for male/female sorting, resulting in increased yields and sizes.
- ► Created a chatbot, "Farmers Mate", using Large Language Models (LLMs) to provide personalized assistance to farmers.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
projects = [
    "Camouflaged Object Detection and Re Camo",
    "Autonomous Multipurpose Weapon System - Advance Computer Vision, Decision Model and Robotics (confidential)",
    "Bengali Folklore and NLP", 
    "Audio processing with AI, Cloning Voice, Style Transfer, Music Generation",
    "Re-enhanced and fully restore the image with AI",
    "And Many More ...."
]
links = [
    "https://github.com/DengPingFan/SINet/",
    "https://www.researchgate.net/profile/Mohammad-Khan-270",
    "https://arxiv.org/abs/2203.06607",
    "https://github.com/NisaEngineers/RudiPRO_Drummer_Web",
    "",
    ""
]
for project, link in zip(projects, links):
    st.write(f"{project}")
