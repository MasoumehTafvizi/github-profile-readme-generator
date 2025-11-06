import streamlit as st
from pathlib import Path

from github_profile import generate_readme_profile


# Add project root to sys.path, so that we can import modules from src
# This is needed because streamlit cloud is running streamlit_app.py
# from the root directory.

st.title("Github Profile :rainbow[README] Generator")
kwargs = {}

# Personal Info
st.header("😎 Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name")
    last_name = col2.text_input("Last Name")
    kwargs['name'] = f"{first_name} {last_name}"
    kwargs['gmail'] = st.text_input("Gmail")
  

# Education
st.header(" 🎓 Education")
with st.expander("Education"):
    col1, col2 = st.columns(2)
    kwargs['degree'] = col1.text_input("Degree")
    kwargs['university_name'] = col2.text_input("University Name")
    kwargs['university_city'] = col1.text_input("University City")
    kwargs['university_country'] = col2.text_input("University Country")
    kwargs['university_url'] = st.text_input("University Website URL", placeholder="https://www.university.edu")
    if kwargs['university_url']:
        kwargs['university_name_url'] = kwargs['university_name']
        kwargs['university_name'] = ""
    else:
        kwargs['university_name_url'] = ""


# status
st.header(" 💼 Current Status")
with st.expander("Current Status"):
    kwargs['learnings'] = st.text_area("What are you currently learning?")
    
    stats = {}
    def display_input_row(index):
        stats[index] = st.text_input(f"Status {index + 1}", key=index)
        st.button('Remove', key=f'remove_{index}', on_click=decrease_rows, args=(index,))

    if 'rows' not in st.session_state:
        st.session_state['rows'] = 0

    def increase_rows():
        st.session_state['rows'] += 1
    def decrease_rows(index):
        st.session_state['rows'] -= 1
        stats.pop(index)

    st.button('Add more', on_click=increase_rows)

    for i in range(st.session_state['rows']):
        display_input_row(i)
    
  
# Technical Skills
st.header(" 💻 Technical Skills")
with st.expander("Technical Skills"):
    kwargs['skills'] = st.text_area("List your technical skills",placeholder="e.g. \n- Programming Languages: C, PYTHON, Java, JavaScript, HTML, CSS, Bash\n- Web Development: Flask, Django, React, Node.js\n- Databases: MySQL, PostgreSQL, MongoDB\n- Cloud Platforms: AWS, GCP, Azure",)
    
    
# Tech Stack
st.header(" 🔧 Tech Stack")
with st.expander("Tech Stack"):
    kwargs['tech_stack'] = st.text_area("List your tech stack (no big letters, separated by commas)", placeholder="javascript,vue,mysql")


# Social Media
st.header(" 📱 Social Media")
with st.expander("Social Media"):
    st.markdown("Enter your social media usernames (not links):")
    col1, col2 = st.columns(2)
    kwargs['github'] = col1.text_input("GitHub Username")
    kwargs['linkedin'] = col2.text_input("LinkedIn Username")
    kwargs['twitter'] = col1.text_input("Twitter Handle")
    kwargs['facebook'] = col2.text_input("Facebook Username")
    kwargs['instagram'] = col1.text_input("Instagram Handle")
    kwargs['youtube'] = col2.text_input("YouTube Channel")
    kwargs['website'] = col1.text_input("Website URL", placeholder="https://www.yourwebsite.com")
    kwargs['discord'] = col2.text_input("Discord Username")

if kwargs.get('github') or kwargs.get('linkedin') or kwargs.get('twitter') or kwargs.get('facebook') or kwargs.get('instagram') or kwargs.get('youtube') or kwargs.get('blog') or kwargs.get('discord') or kwargs.get('gmail'):
    kwargs['social_media'] = "here are my social media links:\n"
    
    

# Select Theme
st.header("🎨 Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox("Select Theme:", themes)
st.markdown(f"Selected Theme: **{theme}**")


# Generate README
st.header("🚀 Generate README")
generated = st.button("Generate")
profile = generate_readme_profile( theme, **kwargs)
if generated:
    st.markdown("Copy the code below and paste it in your 'README.md' file")
    st.code(profile)


