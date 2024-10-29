# Crypto AI Agent

This project is an AI-powered agent that can:

Fetch real-time cryptocurrency prices using the CoinGecko API.

Translate text to English using Google Translate API.

Maintain conversational flow using the LLaMA 3.1 8B model from Together AI.

---

## **Features**
### Fetch Cryptocurrency Prices

Query prices for Bitcoin or any other cryptocurrency in USD.

Example:
You: price bitcoin

Agent: Bitcoin price is $29,000 USD.

### Translate Text

Translate any text to English.

Example:
You: translate: Hola

Agent: Hello

---

## Setup Instructions

### Prerequisites

Python 3.8+

Together AI API Key

### Installation
#### Clone the Repository:

git clone https://github.com/prathikrvs163/crypto_agent.git

cd crypto_agent

### Create a Virtual Environment (Optional):

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies:

pip install -r requirements.txt

### Set the API Key:

Open llama_agent.py.

Replace "your-together-api-key" with your Together AI API key.

### Run the Application:

python main.py

### Example Usage
Welcome to the Crypto AI Agent! Ask about any cryptocurrency prices or request translations.

You: price ethereum

Agent: Ethereum price is $1,800 USD.

You: translate: Bonjour

Agent: Hello

You: exit
Goodbye!

### Assumptions and Limitations

If no cryptocurrency is mentioned, the agent assumes the user is asking for Bitcoin.
All responses are in English, even if the input is in another language.
Prices are cached for 5 minutes to reduce API calls.

### License
This project is licensed under the MIT License.


