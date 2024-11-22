import openai
import os
class ml_backend:
    def __init__(self, api_key=None):
        """
        Initialize the ml_backend class with the OpenAI API key.

        Args:
            api_key (str): Your OpenAI API key. If not provided, it defaults to the environment variable OPENAI_API_KEY.
        """
        if api_key:
            openai.api_key = api_key
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")


    def generate_email(self, prompt, max_tokens=150):
        """
        Generate an email using OpenAI's GPT-3.5-turbo or GPT-4 model.

        Args:
            prompt (str): The main content or request for the email.
            start (str): The initial text or starting point of the email.

        Returns:
            str: The generated email content.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" if needed
                messages=[
                    {"role": "system", "content": "You are a professional email writer."},
                    {"role": "user", "content": prompt.strip()}
                ],
                max_tokens=max_tokens,
                temperature=0.7
            )
            # Extract the email content from the response
            email_content = response['choices'][0]['message']['content'].strip()
            return email_content

        except openai.error.OpenAIError as e:
            # Handle OpenAI API errors gracefully
            return f"An error occurred: {e}"

        except Exception as e:
            # Catch any other errors
            return f"An unexpected error occurred: {e}"

 
