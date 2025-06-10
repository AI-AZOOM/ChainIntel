import requests
import os

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_KEY}",
    "Content-Type": "application/json"
}
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

def generate_wallet_summary(wallet, token_count):
    prompt = f"Analyze Solana wallet {wallet} holding {token_count} tokens. Summarize behavior and activity."
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
    }
    res = requests.post(ENDPOINT, headers=HEADERS, json=payload)
    return res.json().get("choices", [{}])[0].get("message", {}).get("content", "AI summary unavailable.")

def generate_token_summary(token_metadata):
    symbol = token_metadata.get("symbol", "Unknown")
    holders = token_metadata.get("holders", "N/A")
    prompt = f"Give a short overview of token {symbol} on Solana with {holders} holders."
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
    }
    res = requests.post(ENDPOINT, headers=HEADERS, json=payload)
    return res.json().get("choices", [{}])[0].get("message", {}).get("content", "AI summary unavailable.")