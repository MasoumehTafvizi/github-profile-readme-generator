import streamlit as st
from pathlib import Path

from github_profile import generate_readme_profile
from sections import (add_social_accounts, add_stats, add_personal_info,
                           add_technical_skills, add_education, add_tech_stack)


# Add project root to sys.path, so that we can import modules from src
# This is needed because streamlit cloud is running streamlit_app.py
# from the root directory.

st.title("Github Profile :rainbow[README] Generator")
st.sidebar.image('src/assets/logo.jpeg', width=300)
st.sidebar.markdown('''
:bulb: Built by [Masoumeh Tafvizi](https://github.com/MasoumehTafvizi).
''')


'''
This app generates a Github profile readme file. To learn how to add a readme file to your Github profile, check out
[this](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).
You can customize it and use it in your Github profile.
- First, fill out the forms below.
- Then, go to **Code** tab to copy the code and paste it in your `README.md` file.

You can also change the theme of the readme file by selecting a theme from the dropdown below.
Themes are added by the community. If you want to add a theme, check out the [Github repo](https://github.com/hejazizo/github-profile-readme).
'''

'''\n\n'''
st.header('Personalize your Readme')


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    ':bust_in_silhouette: Profile Info',
    ':mortar_board: Education',
    ':briefcase: Status',
    ':computer: Technical Skills',
    ':wrench: Tech Stack',
    ':phone: Social Accounts'
])

kwargs = {}
kwargs = add_personal_info(tab1, **kwargs)
kwargs = add_education(tab2, **kwargs)
kwargs = add_stats(tab3, **kwargs)
kwargs = add_technical_skills(tab4, **kwargs)
kwargs = add_tech_stack(tab5, **kwargs)
kwargs = add_social_accounts(tab6, **kwargs)     


st.header('README.md Preview')
'''
- Select a theme from the dropdown below.
- Go to **Code** tab to copy the code and paste it in your `README.md` file.
- **Github extensions will not work in the preview.** You can only see them in the code and in your Github profile.
'''

# Select Theme
st.header("🎨 Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox("Select Theme:", themes)


# Generate README
st.header("🚀 Generate README")
generated = st.button("Generate")
profile = generate_readme_profile( theme, **kwargs)
if generated:
    tab1, tab2 = st.tabs(['Preview', 'Code'])
    with tab1:
        st.markdown('### Preview')
        tab1.markdown(profile, unsafe_allow_html=True)
    with tab2:
        st.markdown('Copy the code below and paste it in your README.md file')
        st.code(profile)