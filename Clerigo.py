
import streamlit as st
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Kristian Clerigo | Student Portfolio",
    page_icon="⚙️",
    layout="wide"
)

# Image directory
IMAGE_FOLDER = Path(__file__).parent / "images"

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("MY PORTFOLIO")
st.sidebar.caption("Student | Mechanical Engineering")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Personal Information",
        "Education",
        "Interests & Fitness"
    ]
)

st.sidebar.divider()
st.sidebar.write("Created by Kristian Emmanuel A. Clerigo")

# ==========================================
# MAIN HEADER
# ==========================================

st.header("Kristian Emmanuel A. Clerigo")
st.caption("Bachelor of Science in Mechanical Engineering")
st.divider()

# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.title("Welcome to My Portfolio! 👋")

    col1, col2 = st.columns([1, 2])

    with col1:
        profile = IMAGE_FOLDER / "profile.jpg"

        if profile.exists():
            st.image(
                str(profile),
                caption="Kristian Emmanuel A. Clerigo",
                use_container_width=True
            )
        else:
            st.warning("Profile picture not found.")

    with col2:
        st.subheader("Hello! I'm Kristian.")

        st.write("""
        I am a Mechanical Engineering student who is interested
        in technology, engineering, and personal development.

        This portfolio introduces who I am, my educational
        background, and the activities that I enjoy.
        """)

        st.info("Explore the sidebar to learn more about me!")

    st.divider()

    st.subheader("A Little About Me")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Field of Study", "Engineering")

    with col2:
        st.metric("University", "NEMSU")

    with col3:
        st.metric("Main Interest", "Fitness")

    st.divider()

    st.subheader("About This Application")

    st.write("""
    This web application was developed using Python and Streamlit.
    It demonstrates the use of text elements, images, navigation,
    columns, and interactive components.
    """)

# ==========================================
# PERSONAL INFORMATION
# ==========================================

elif page == "Personal Information":

    st.title("Personal Information")

    profile = IMAGE_FOLDER / "profile.jpg"

    col1, col2 = st.columns([1, 2])

    with col1:
        if profile.exists():
            st.image(str(profile), use_container_width=True)
        else:
            st.warning("Profile picture not found.")

    with col2:
        st.subheader("Basic Information")

        st.write("**Full Name:** Kristian Emmanuel A. Clerigo")
        st.write("**Course:** BS Mechanical Engineering")
        st.write("**University:** North Eastern Mindanao State University")
        st.write("**Academic Level:** College Student")

    st.divider()

    st.subheader("Personal Introduction")

    st.write("""
    I am a college student currently pursuing Mechanical Engineering.
    I enjoy learning new things, exploring technology, and developing
    skills that can help me in my academic and personal life.

    I also value physical fitness and enjoy going to the gym as part
    of my interest in maintaining an active lifestyle.
    """)

# ==========================================
# EDUCATION
# ==========================================

elif page == "Education":

    st.title("Educational Background")

    st.subheader("College Education")

    st.write("### North Eastern Mindanao State University")

    st.markdown(
        "[Visit the official NEMSU website](https://www.nemsu.edu.ph/)"
    )

    st.write("**Degree:** Bachelor of Science in Mechanical Engineering")

    st.write("""
    I am currently pursuing a degree in Mechanical Engineering.
    This field involves the study of machines, mechanical systems,
    engineering principles, and technology.
    """)

    engineering = IMAGE_FOLDER / "engineering.jpg"

    if engineering.exists():
        st.image(
            str(engineering),
            caption="Mechanical Engineering and Technology",
            use_container_width=True
        )
    else:
        st.info("Add engineering.jpg to your images folder.")

    st.divider()

    st.subheader("Senior High School")

    st.write("**School:** Bislig City National High School")
    st.write("**Strand:** Accountancy, Business, and Management (ABM)")

    st.write("""
    My senior high school experience helped me develop
    communication, research, and problem-solving skills.
    """)

# ==========================================
# INTERESTS AND FITNESS
# ==========================================

elif page == "Interests & Fitness":

    st.title("My Interests and Fitness Journey 🏋️")

    st.write("""
    One of my interests is going to the gym. I enjoy learning about
    fitness, strength training, and different exercises that help
    improve physical strength and endurance.
    """)

    hobbies = IMAGE_FOLDER / "hobbies.jpg"

    if hobbies.exists():
        st.image(
            str(hobbies),
            caption="Fitness and Personal Development",
            use_container_width=True
        )
    else:
        st.info("Add hobbies.jpg to your images folder.")

    st.divider()

    st.subheader("My Fitness Interests")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💪 Strength Training")

        st.write("""
        Learning about resistance exercises and building
        strength through movements such as:
        """)

        st.write("""
        - Bench Press
        - Squats
        - Deadlifts
        - Pull-ups
        - Shoulder Press
        """)

    with col2:
        st.markdown("### 🏃 Cardiovascular Exercise")

        st.write("""
        Improving endurance and staying active through:
        """)

        st.write("""
        - Jogging
        - Walking
        - Cycling
        - Jump Rope
        - Treadmill Workouts
        """)

    st.divider()

    st.subheader("My Fitness Goals")

    st.write("""
    - Improve my overall physical strength.
    - Develop better endurance and stamina.
    - Learn proper exercise techniques.
    - Maintain consistency in working out.
    - Improve discipline and self-confidence.
    """)

    st.divider()

    st.subheader("My Personal Fitness Philosophy")

    st.info("""
    Progress takes time. Consistency, discipline, proper recovery,
    and patience are important parts of building a healthier lifestyle.
    """)

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "© 2026 Kristian Emmanuel A. Clerigo | "
    "Created with Python and Streamlit"
)


