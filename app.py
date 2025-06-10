<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ChainIntel</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <header>
    <h1>ChainIntel</h1>
    <p>Solana Wallet & Token Intelligence Powered by AI</p>
    <nav>
      <a href="{{ url_for('scan_wallet_page') }}">Scan Wallet</a>
      <a href="{{ url_for('tokenintel_page') }}">Token Profiler</a>
      <a href="{{ url_for('roadmap_page') }}">Roadmap</a>
    </nav>
  </header>

  <main>
    <section>
      <h2>What is ChainIntel?</h2>
      <p>
        ChainIntel helps you investigate Solana wallets and token contracts using real-time data from Solscan and GPT-powered insights.
      </p>
      <p>
        Whether you're researching airdrops, whales, or tokens — ChainIntel saves you time and simplifies due diligence.
      </p>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 ChainIntel Labs</p>
  </footer>
</body>
</html>
