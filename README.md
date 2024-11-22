📧 Interactive Email Generator

Welcome to the Interactive Email Generator, a powerful application designed to craft professional, concise, and customized emails using the capabilities of OpenAI's GPT-3.5. This tool simplifies the process of email writing by allowing users to describe the purpose and provide additional context, generating tailored emails in seconds.

✨ Features

Boost Productivity: Generate professional emails effortlessly, saving time and mental energy.
Customizable Outputs: Provide details to tailor emails for specific purposes and audiences.
Streamlined Workflow: Easily copy or send generated emails through Gmail with a single click.
User-Friendly Interface: Intuitive layout with clear options and instructions.
Secure API Integration: The app securely integrates with OpenAI's GPT-3.5 API.
🚀 How It Works

Input Your Email Purpose:
Describe what you need the email to say (e.g., "Follow-up on my job application status").
Provide Additional Details (Optional):
Add context to customize the email further (e.g., "I submitted my application on October 10, 2024").
Generate the Email:
Click the "Generate Email" button to craft your email.
Review and Send:
Review the generated email, copy it, or send it directly via Gmail using the provided link.
🛠️ Installation

Requirements
Python 3.7 or higher
OpenAI API Key
Clone the Repository
git clone https://github.com/SrinijaVaibhavi/email-generator.git
cd email-generator
Install Dependencies
Create a virtual environment (optional but recommended) and install the required libraries:

python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
Set Up OpenAI API Key
Option 1: Environment Variables

Set the API key as an environment variable:

export OPENAI_API_KEY="your-api-key"

Option 2: Streamlit Secrets

Create a ~/.streamlit/secrets.toml file and add your API key:

[general]
OPENAI_API_KEY = "your-api-key"
⚙️ Running the App

Start the Streamlit app:

streamlit run emailapp.py
Open your browser 

📖 Usage Example

Input:
Email Purpose: Follow-up on my job application status.
Additional Details: I applied on October 10, 2024, and I’m eager to hear back about the Software Engineer position.
Output:
Subject: Inquiry Regarding Job Application Status
Email Content:

Dear Hiring Manager,

I hope this email finds you well. I am writing to follow up on the status of my application for the Software Engineer position at ABC Corp, which I submitted on October 10, 2024. I am very enthusiastic about the opportunity to potentially join your esteemed organization and would appreciate any updates or information regarding the progress of my application.

If there are any additional materials or documents needed from my end to further support my application, please let me know.

Thank you for your time and consideration. I look forward to your response.

Best regards,  
[Your Name]
📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

💡 Future Enhancements

Add multi-language support for generating emails in different languages.
Incorporate templates for common email types (e.g., meeting requests, reminders).
Enable integration with popular email services like Outlook.
📧 Contact

For questions, suggestions, or feedback, please reach out:

Email: srinijavaibhavi@hotmail.com
GitHub: rinijavaibhavi
Let me know if you'd like to tweak any section or add additional details! 😊