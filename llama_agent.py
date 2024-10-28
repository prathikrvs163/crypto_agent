import requests

# Replace with your Together AI API key
TOGETHER_API_KEY = "YOUR API KEY"
TOGETHER_API_URL = "https://api.together.xyz/v1/llama3"

def call_llama(prompt):
    """Send a prompt to the LLaMA model and return the response."""
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
    payload = {"prompt": prompt, "max_tokens": 100}

    try:
        response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error communicating with LLaMA model: {str(e)}"
