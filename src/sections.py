import urllib.parse

import streamlit as st

def add_personal_info(tab, **kwargs):
    """
    Add personal info to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        first_name = col1.text_input("First Name")
        last_name = col2.text_input("Last Name")
        kwargs['name'] = f"{first_name} {last_name}"
        
    return kwargs

def add_education(tab, **kwargs):
    """
    Add education info to tab.

    :param tab: Streamlit tab
    """
    with tab:
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
    return kwargs
    
def add_stats(tab, **kwargs):
    """
    Add current status to tab.

    :param tab: Streamlit tab
    """
    with tab:
        kwargs['learnings'] = st.text_area("What are you currently learning?", height=100, placeholder="e.g. Learning Data Structures and Algorithms in Python.")
        stats = {}
        def display_input_row(index):
            stats[index] = st.text_area(f"Status {index + 1}", key=index, height=100,)
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
            
    return kwargs

def add_technical_skills(tab, **kwargs):
    with tab:
        kwargs['skills'] = st.text_area("List your technical skills", height=300, placeholder="e.g. \n- Programming Languages: C, PYTHON, Java, JavaScript, HTML, CSS, Bash\n- Web Development: Flask, Django, React, Node.js\n- Databases: MySQL, PostgreSQL, MongoDB\n- Cloud Platforms: AWS, GCP, Azure", )
    
    return kwargs

def add_tech_stack(tab, **kwargs):
    with tab:
        st.write('''Add your skills. You can add any skills you want.
        **Just make sure to separate them with a new line.**
        ''')
        col1, col2 = st.columns(2)
        kwargs['tech_stack'] = col1.text_area('Skills:', height=300, key='skills', placeholder="e.g.\njavascript\npython\nreact\nnode.js")
        kwargs['tech_stack'] = kwargs['tech_stack'].split('\n')
        kwargs['tech_stack'] = filter(lambda x: x, kwargs['tech_stack'])
        kwargs['tech_stack'] = [f'{skill.lower()}' for skill in kwargs['tech_stack']]
        kwargs['tech_stack'] = ','.join(kwargs['tech_stack'])

    return kwargs

def add_social_accounts(tab, **kwargs):
    """
    Add social accounts to tab.

    :param tab: Streamlit tab
    """
    with tab:
        col1, col2 = st.columns(2)
        st.markdown("Enter your social media usernames (not links):")
        col1, col2 = st.columns(2)
        kwargs['github'] = col1.text_input("GitHub Username")
        kwargs['linkedin'] = col2.text_input("LinkedIn Username")
        kwargs['twitter'] = col1.text_input("Twitter Handle")
        kwargs['facebook'] = col2.text_input("Facebook Username")
        kwargs['instagram'] = col1.text_input("Instagram Handle")
        kwargs['youtube'] = col2.text_input("YouTube Channel")
        kwargs['gmail'] = col1.text_input("Gmail")
        kwargs['discord'] = col2.text_input("Discord Username")
        kwargs['website'] = st.text_input("Website URL", placeholder="https://www.yourwebsite.com")

    if kwargs.get('github') or kwargs.get('linkedin') or kwargs.get('twitter') or kwargs.get('facebook') or kwargs.get('instagram') or kwargs.get('youtube') or kwargs.get('blog') or kwargs.get('discord') or kwargs.get('gmail'):
        kwargs['social_media'] = "here are my social media links:\n"

    return kwargs


def add_extensions(tab, **kwargs):
    """
    Add extensions to tab.

    :param tab: Streamlit tab
    """
    with tab:
        st.write('''Add more to your profile. You can add Github stats, Github profile views, and more.''')
        kwargs['github'] = st.text_input('Github', 'hejazizo')
        if not kwargs['github']:
            st.warning('For extensions, you must enter your Github username.')
            kwargs['profile_views'] = None
            kwargs['github_stats'] = None
            return kwargs

        kwargs['github_stats'] = None
        if st.checkbox('Show Github Stats', value=True):
            kwargs['github_stats'] = kwargs['github']

        kwargs['profile_views'] = None
        if st.checkbox('Show Github Profile Views', value=True):
            kwargs['profile_views'] = kwargs['github']

    return kwargs