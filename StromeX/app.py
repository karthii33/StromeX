import streamlit as st
from pymongo import MongoClient

# MongoDB setup
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client['stromex_database']
collection = db['contact_submissions']

# Sidebar Navigation
pages = [
    "Home", "Contact", "Blog", "Products", "Services", "Solutions",
    "Software & SaaS Applications", "Audio & Video Solutions",
    "End-User Computing", "Data Center Infrastructure",
    "IT Consulting & Managed Services", "Cloud & Colocation Services"
]
page = st.sidebar.selectbox("Navigate", pages)

# Page Rendering
def show_home():
    st.title("Welcome to StromeX IT Solutions")
    st.write("Innovating for a Digital Future.")

def show_contact():
    st.title("Contact Us 📬")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        contact = st.text_input("Contact Number")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if name and email and contact and message:
                try:
                    result = collection.insert_one({
                        'name': name,
                        'email': email,
                        'contact': contact,
                        'message': message
                    })
                    st.success("✅ Your message has been submitted!")
                except Exception as e:
                    st.error(f"❌ Failed to submit: {e}")
            else:
                st.warning("Please fill out all fields.")

def show_blog():
    st.title("Blog 📝")
    st.write("Our latest insights, updates, and tech talk!")

def show_products():
    st.title("Products")
    st.write("Explore our range of innovative IT products.")

def show_services():
    st.title("Services")
    st.write("Professional services tailored for your business.")

def show_solutions():
    st.title("Solutions")
    st.write("End-to-end solutions for your IT needs.")

def show_software():
    st.title("Software & SaaS Applications")
    st.write("Cloud-native applications and productivity tools.")

def show_audio_video():
    st.title("Audio & Video Solutions")
    st.write("Unified communication and conferencing tools.")

def show_end_user():
    st.title("End-User Computing")
    st.write("Desktop, mobile, and workspace solutions.")

def show_data_center():
    st.title("Data Center Infrastructure")
    st.write("Scalable, secure, and efficient infrastructure.")

def show_it_consulting():
    st.title("IT Consulting & Managed Services")
    st.write("Optimize IT strategy and reduce downtime.")

def show_cloud_colocation():
    st.title("Cloud & Colocation Services")
    st.write("Hybrid cloud, storage, and colocation options.")

# Page Dispatcher
if page == "Home":
    show_home()
elif page == "Contact":
    show_contact()
elif page == "Blog":
    show_blog()
elif page == "Products":
    show_products()
elif page == "Services":
    show_services()
elif page == "Solutions":
    show_solutions()
elif page == "Software & SaaS Applications":
    show_software()
elif page == "Audio & Video Solutions":
    show_audio_video()
elif page == "End-User Computing":
    show_end_user()
elif page == "Data Center Infrastructure":
    show_data_center()
elif page == "IT Consulting & Managed Services":
    show_it_consulting()
elif page == "Cloud & Colocation Services":
    show_cloud_colocation()
