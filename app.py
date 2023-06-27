import os
import PyPDF2
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the pdf
pdf_file_path = os.getenv('PDF_FILE_PATH')
pdf_reader = PyPDF2.PdfReader(pdf_file_path)

# Read the content
content = ""
for page in pdf_reader.pages:
    content += page.extract_text()

# Setup OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define your prompt
prompt = content + "\nGiven the above, generate an itinerary for a visitor."

# Use the OpenAI API
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant. Today is 6/26/23. Generate an itinerary foe 6/31/23. Speak like geoffrey chaucer."},
        {"role": "user", "content": prompt},
    ]
)

# Print the generated schedule
print(response['choices'][0]['message']['content'])
