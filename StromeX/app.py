import streamlit as st
from pymongo import MongoClient
import os

# --- MONGODB CONNECTION ---
# It's recommended to use Streamlit's secrets management for sensitive data
# For local development, you can use an environment variable or hardcode it.
MONGO_URI = st.secrets.get("mongo_uri", "mongodb://localhost:27017/")

try:
    client = MongoClient(MONGO_URI)
    db = client['stromex_database']
    collection = db['contact_submissions']
    # Check if the connection is successful
    client.admin.command('ping')
    db_connection_success = True
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")
    db_connection_success = False

# --- HELPER FUNCTION TO LOAD HTML FILES ---
def render_html(page_path):
    """Reads and returns the content of an HTML file."""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h2 style='color: red; text-align: center;'>Error: {os.path.basename(page_path)} not found.</h2><p style='text-align: center;'>Please make sure the HTML file exists in the same directory as the script.</p>"
    except Exception as e:
        return f"<h2 style='color: red;'>An error occurred:</h2><p>{e}</p>"

# --- PAGE RENDERING FUNCTIONS ---

def index():
    """Renders the home page."""
    st.markdown(render_html('index.html'), unsafe_allow_html=True)

def contact():
    """Renders the contact page with a Streamlit form."""
    st.header("Contact Us")
    st.markdown("Have a question or want to work with us? Fill out the form below.")

    # Use st.form for submission handling
    with st.form(key='contact_form', clear_on_submit=True):
        st.subheader("Send us a Message")
        name = st.text_input("Full Name", placeholder="John Doe")
        email = st.text_input("Email Address", placeholder="you@example.com")
        contact_num = st.text_input("Contact Number", placeholder="+1 234 567 890")
        message = st.text_area("Your Message", placeholder="Your message here...")

        # Submit button
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not all([name, email, message]):
                st.warning("Please fill out all required fields (Name, Email, Message).")
            elif not db_connection_success:
                st.error("Cannot submit form. Database connection failed.")
            else:
                try:
                    # Store data in MongoDB
                    submission_data = {
                        'name': name,
                        'email': email,
                        'contact': contact_num,
                        'message': message
                    }
                    collection.insert_one(submission_data)
                    st.success("Thank you for your message! We will get back to you shortly.")
                    st.balloons()
                except Exception as e:
                    st.error(f"An error occurred while submitting the form: {e}")

    # You can still render the rest of your contact.html if it has other content
    # st.markdown(render_html('contact.html'), unsafe_allow_html=True)


def blog():
    """Renders the blog page."""
    st.markdown(render_html('Blog.html'), unsafe_allow_html=True)

def products():
    """Renders the products page."""
    st.markdown(render_html('Products.html'), unsafe_allow_html=True)

def services():
    """Renders the services page."""
    st.markdown(render_html('Services.html'), unsafe_allow_html=True)

def solution():
    """Renders the solutions page."""
    st.markdown(render_html('Solutions.html'), unsafe_allow_html=True)

def software_saas_applications():
    """Renders the software/SaaS page."""
    st.markdown(render_html('software-saas-applications.html'), unsafe_allow_html=True)

def audio_video_solutions():
    """Renders the audio/video solutions page."""
    st.markdown(render_html('audio-video-solutions.html'), unsafe_allow_html=True)

def end_user_computing():
    """Renders the end-user computing page."""
    st.markdown(render_html('end-user-computing.html'), unsafe_allow_html=True)

def data_center_infrastructure():
    """Renders the data center page."""
    st.markdown(render_html('data-center-infrastructure.html'), unsafe_allow_html=True)

def it_consulting_managed_services():
    """Renders the IT consulting page."""
    st.markdown(render_html('it-consulting-managed-services.html'), unsafe_allow_html=True)

def cloud_colocation_services():
    """Renders the cloud/colocation services page."""
    st.markdown(render_html('cloud-colocation-services.html'), unsafe_allow_html=True)


# --- MAIN APP ---
def main():
    """Main function to run the Streamlit app."""
    # Configure the page
    st.set_page_config(page_title="Stromex", layout="wide")

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", [
        "Home",
        "Products",
        "Services",
        "Solutions",
        "Blog",
        "Contact"
    ])

    # --- SUB-MENUS for services/solutions if desired ---
    if selection == "Services":
        service_selection = st.sidebar.selectbox("Our Services", [
            "All Services",
            "Software & SaaS Applications",
            "Audio & Video Solutions",
            "End User Computing",
            "Data Center Infrastructure",
            "IT Consulting & Managed Services",
            "Cloud & Colocation Services"
        ])

    # --- PAGE ROUTING ---
    if selection == "Home":
        index()
    elif selection == "Products":
        products()
    elif selection == "Services":
        if service_selection == "All Services":
            services()
        elif service_selection == "Software & SaaS Applications":
            software_saas_applications()
        elif service_selection == "Audio & Video Solutions":
            audio_video_solutions()
        elif service_selection == "End User Computing":
            end_user_computing()
        elif service_selection == "Data Center Infrastructure":
            data_center_infrastructure()
        elif service_selection == "IT Consulting & Managed Services":
            it_consulting_managed_services()
        elif service_selection == "Cloud & Colocation Services":
            cloud_colocation_services()
    elif selection == "Solutions":
        solution()
    elif selection == "Blog":
        blog()
    elif selection == "Contact":
        contact()


if __name__ == '__main__':
    main()

