# Crypto AI Agent

This project implements an AI-powered agent that provides real-time cryptocurrency prices, handles language translation, and maintains conversational flow using the **LLaMA 3.1 8B model** from Together AI. It demonstrates API integrations, caching, and error handling.

---

## **Features**

1. **Fetch Cryptocurrency Prices**:  
   - Query Bitcoin or any other cryptocurrency price using **CoinGecko API**.
   - Example: `price bitcoin` or `price ethereum`.

2. **Language Translation**:  
   - Translate text to **English** using **Google Translate API**.
   - Example: `translate: Hola` → Response: "Hello"

3. **Conversational Flow with LLaMA**:  
   - Handles general queries using the LLaMA 3.1 8B model from **Together AI**.

4. **Error Handling & Caching**:  
   - Prices are cached for **5 minutes** to reduce API calls.
   - Handles network errors gracefully.

---


