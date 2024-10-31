import streamlit as st

# Initialize session state for selected name if not already set
if "selected_name" not in st.session_state:
    st.session_state.selected_name = None
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default to the homepage

# Sidebar dropdown for selecting a user
st.sidebar.title("Select a Portfolio")
names = ["Alice", "Bob", "Charlie", "David", "Evelyn", "Frank", "Grace", "Hannah", "Isaac", "Julia"]

# Dropdown to select a name
selected_name = st.sidebar.selectbox("Choose a name", ["Select..."] + names)

# Set the selected name and switch to the portfolio page if a name is chosen
if selected_name != "Select...":
    st.session_state.selected_name = selected_name
    st.session_state.page = "portfolio"
else:
    st.session_state.page = "home"

# Homepage content
def display_homepage():
    st.title("Multi-Agent AI Financial Newsletter 💲🤑")
    st.write(
        "An AI-powered financial newsletter that delivers personalized, real-time insights and summaries, leveraging memory and retrieval to keep users informed and engaged."
    )
    st.button("Get Newsletter")

# Portfolio page content with mock file upload and chat input
def display_portfolio():
    st.title(f"{st.session_state.selected_name}'s Portfolio")
    st.write(f"Welcome to {st.session_state.selected_name}'s personalized financial insights page!")

    # File upload for RAG (mock)
    uploaded_file = st.file_uploader("Upload a CSV file for RAG (Retrieval-Augmented Generation)", type="csv")
    if uploaded_file:
        st.write("**CSV file uploaded successfully!**")

    # Chat input for asking about the portfolio (mock)
    st.write("### Ask about the Portfolio")
    user_question = st.text_input("Type your question here")
    if user_question:
        st.write("**Answer:** This is where the response would appear.")

# Display the appropriate page based on the session state
if st.session_state.page == "home":
    display_homepage()
elif st.session_state.page == "portfolio":
    display_portfolio()
