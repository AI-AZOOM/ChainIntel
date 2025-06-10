function scanWallet() {
  const wallet = document.getElementById('walletInput').value;
  fetch('/api/scan-wallet', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ wallet })
  })
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById('result');
      if (data.error) return div.innerText = "❌ " + data.error;
      div.innerText = data.summary;
    })
    .catch(err => alert('Request failed: ' + err));
}

function analyzeToken() {
  const token = document.getElementById('tokenInput').value;
  fetch('/api/analyze-token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ token })
  })
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById('tokenResult');
      if (data.error) return div.innerText = "❌ " + data.error;
      div.innerText = data.summary;
    })
    .catch(err => alert('Request failed: ' + err));
}
