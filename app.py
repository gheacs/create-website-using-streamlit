import streamlit as st

def run():
    st.set_page_config(
        page_title="Welcome to Ghea's Page",
        page_icon="👋",
    )

    st.write("# Welcome to My Page! 👋")
    
    # List of projects
    projects = [
        {"name": "Tidy-Teddy Cleaning Companion", "url": "https://sites.google.com/uw.edu/yourcleaningcompanion/homepage"},
        {"name": "Simple Wearable Device", "url": "https://github.com/gheacs/SimpleWearableDevice"},
        {"name": "Other Projects", "url": "https://github.com/gheacs"}
    ]
        
    selected_project = st.sidebar.selectbox("Select a cool project:", projects)

    # Display the selected project's name and provide a link
    if selected_project:
        st.sidebar.markdown(f"Selected Project: [{selected_project['name']}]({selected_project['url']})")

    st.markdown(
        """
        This website is part of the TECHIN510 Lab Assignment. If you want to know more about me
        **👈 Select a cool project from the sidebar** 
        ### About
        - Ghea Chrestella Suyono 
        - My lifelong dream is to retire early and open an animal shelter
        - Linkedin [Linkedin Profile](https://www.linkedin.com/in/suyonoghea/) """)

    st.markdown(
      """
        ### Education
        - Grad (ongoing) in Ms Technology Innovation - University of Washington
        - Undergrad in Banking and Finance - University of London

        ### Work Experience
        - Payment Experience Lead - Gojek Tokopedia
        - Loan PM - SeaGroup, SeaBank
        - PMO, COO Office - SeaGroup
        - Corporate Relationship Manager - OCBC Bank
        - Management Associate - OCBC Bank

        ### Hobbies and Interests
        Crime Series! I highly recommend listening to 'RottenMango' by Stephanie Soo 

        ### Life At The Moment
        """)
    st.image('/workspaces/lab1/picture.jpg', caption="It's been 8 years and now I'm back to school")
    st.image('/workspaces/lab1/picture2.jpg', caption='The only reason I can survive my quarters')
    st.image('/workspaces/lab1/picture3.jpg', caption="Meet Jason! the highest rent-free household expense")
    st.image('/workspaces/lab1/picture4.jpg', caption="With Jason's spare human")

if __name__ == "__main__":
    run()
