from flask import Flask, render_template, request, jsonify
import sys, os

# Enable local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ai')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

from summary_engine import generate_wallet_summary, generate_token_summary
from solana_api import fetch_wallet_tokens, fetch_token_metadata

app = Flask(__name__)

# ========== PAGE ROUTES ==========

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan-wallet')
def scan_wallet_page():
    return render_template('scan_wallet.html')

@app.route('/tokenintel')
def tokenintel_page():
    return render_template('tokenintel.html')

@app.route('/roadmap')
def roadmap_page():
    return render_template('roadmap.html')

# ========== API ROUTES ==========

@app.route('/api/scan-wallet', methods=['POST'])
def scan_wallet():
    data = request.json
    wallet = data.get('wallet')
    if not wallet:
        return jsonify({'error': 'No wallet address provided'}), 400

    tokens = fetch_wallet_tokens(wallet)
    if not tokens:
        return jsonify({'error': 'Failed to fetch wallet data'}), 500

    summary = generate_wallet_summary(wallet, len(tokens))

    return jsonify({
        'wallet': wallet,
        'summary': summary,
        'tokens': tokens
    })

@app.route('/api/analyze-token', methods=['POST'])
def analyze_token():
    data = request.json
    token_address = data.get('token')
    if not token_address:
        return jsonify({'error': 'No token address provided'}), 400

    token_data = fetch_token_metadata(token_address)
    if not token_data:
        return jsonify({'error': 'Failed to fetch token data'}), 500

    summary = generate_token_summary(token_data)

    return jsonify({
        'token': token_address,
        'summary': summary,
        'data': token_data
    })

# ========== RUN ==========

if __name__ == '__main__':
    app.run(debug=True)
