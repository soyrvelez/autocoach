import requests
from bs4 import BeautifulSoup
import openai
import os


# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def fetch_and_parse(url):
    """
    Fetches HTML content from a given URL and parses it using BeautifulSoup.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        main_content = soup.get_text(separator="\n", strip=True)
        return main_content
    else:
        print(f"Failed to fetch URL: {url}")
        return ""

def generate_learning_strategies(text):
    try:
        response = openai.completions.create(
            model="text-davinci-003",  # or the latest available model
            prompt=f"Given the following content, provide three strategies to help understand or solve the problem:\n\n{text}",
            max_tokens=150,
            n=1,
            stop=["\n"]
        )
        print('SRATEGIES ----->', response.choices[0].text.strip())
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
