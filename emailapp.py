import streamlit as st
import urllib.parse
from ml_backend import ml_backend  # Import the ml_backend class

# Token estimation function
def estimate_tokens(character_count):
    """
    Estimate the number of tokens based on character count.
    Approximation: 1 token ≈ 4 characters. Adding a buffer for safety.
    """
    return max(1, int(character_count / 4.0) + 50)  # Add a generous buffer to prevent truncation

# App title and introduction
st.set_page_config(page_title="Email Generator App", page_icon="📧", layout="centered")
st.title("📧 Interactive Email Generator App")
st.markdown("**Powered by OpenAI GPT-3.5**")

st.markdown("""
Welcome to the **Email Generator App**!  
This tool helps you craft professional, concise, and well-written emails in seconds.

### 🌟 Why Use This App?
- **Boost Productivity:** Let AI handle the writing, so you can focus on what matters.
- **Stress-Free Communication:** Never worry about finding the right words again.
- **Customizable Outputs:** Easily tailor emails to fit any tone or style.

---
""")

# Initialize the ml_backend class with your OpenAI API key
backend = ml_backend(api_key="your-openai-api-key")  # Replace with your actual API key

# Sidebar for settings
st.sidebar.header("⚙️ Settings")
character_limit = st.sidebar.slider("Character Limit", min_value=64, max_value=750, value=213, step=10)
st.sidebar.text("Set the maximum email length.")

if character_limit < 150:
    st.sidebar.warning("Setting a very low character limit may result in truncated emails.")

# Main form for input
st.markdown("### ✍️ Describe Your Email")

with st.form(key="email_form"):
    prompt = st.text_area(
        "What is the purpose of your email?",
        height=100,
        placeholder="e.g., Follow-up on my application status, Request for scheduling a meeting, or Ask for project feedback"
    )
    extra_details = st.text_area(
        "Provide additional details (optional)",
        height=100,
        placeholder="e.g., I submitted my application on October 10, 2024. I am particularly excited about your team's work on AI innovations."
    )

    st.markdown("Click **Generate Email** to create a tailored email based on your input.")
    submit_button = st.form_submit_button(label="Generate Email ✨")

    if submit_button:
        if not prompt.strip():
            st.error("Please provide a description for the email.")
        else:
            with st.spinner("Generating your email..."):
                # Estimate tokens based on character limit
                max_tokens = estimate_tokens(character_limit)

                # Combine prompt and extra details for generation
                combined_prompt = f"{prompt.strip()} {extra_details.strip()}" if extra_details.strip() else prompt.strip()

                # Generate the email content
                output = backend.generate_email(combined_prompt, max_tokens=max_tokens)

                # Check if the output seems incomplete
                if output and output[-1] not in ".!?":
                    output += "\n\n(Note: Please review and finalize this email for completeness.)"

            # Display the generated email
            st.markdown("### 📝 Generated Email:")
            st.markdown(f"**Subject:** Inquiry Regarding {prompt.strip().capitalize()}")  # Dynamic subject
            st.text_area("Email Content", output.strip(), height=300)  # Cleaned output

            # Provide a link to send the email via Gmail
            st.markdown("---")
            st.markdown("### 📤 Send Your Email")
            st.write("If you're happy with the email, click the link below to send it via Gmail:")

            # Properly encode the email content for the Gmail link
            subject = f"Inquiry Regarding {prompt.strip().capitalize()}"
            body = output.strip()
            encoded_subject = urllib.parse.quote(subject)
            encoded_body = urllib.parse.quote(body)

            # Generate the Gmail link
            url = f"https://mail.google.com/mail/?view=cm&fs=1&to=&su={encoded_subject}&body={encoded_body}"

            # Add the clickable link
            st.markdown(f"[Click here to send the email ✉️]({url})")



# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Srinija Vaibhavi Boggavarapu")

