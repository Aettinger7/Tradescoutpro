HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeScout Pro — {{ title }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-luxon"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-chart-financial"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; transition: background-color 0.3s, color 0.3s; }
        .theme-dark { background-color: #121212; color: #e0e0e0; }
        .theme-dark .table { --bs-table-bg: #1e1e1e; }
        .theme-dark .table-hover tbody tr:hover { background-color: #2d2d2d !important; }
        .coin-logo { width: 32px; height: 32px; margin-right: 10px; }
        .sparkline { width: 120px; height: 50px; }
        .change-positive { color: #00c853; }
        .change-negative { color: #ff1744; }
        .navbar { background-color: #1976d2; }
        .search-input { max-width: 300px; }
    </style>
</head>
<body class="theme-dark">
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand fw-bold" href="/">TradeScout Pro</a>
            <div class="d-flex align-items-center">
                <input type="text" id="searchInput" class="form-control me-3 search-input" placeholder="Search coin...">
                <button id="themeToggle" class="btn btn-outline-light"><i class="fas fa-moon"></i></button>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <h2 class="text-center mb-4">{{ title }}</h2>
        <div class="table-responsive">
            <table id="coinsTable" class="table table-hover align-middle">
                <thead class="table-light">
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Price</th>
                        <th>1h %</th>
                        <th>24h %</th>
                        <th>7d %</th>
                        <th>24h Volume</th>
                        <th>Market Cap</th>
                        <th>Last 7 Days Sparkline</th>
                    </tr>
                </thead>
                <tbody id="tableBody"></tbody>
            </table>
        </div>
        <p class="text-center text-muted mt-3">Last update: <span id="lastUpdate">{{ last_update }}</span> • Refreshes every 60s • Powered by CoinGecko</p>
    </div>

    <div class="modal fade" id="chartModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content theme-dark">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalTitle"></h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <canvas id="detailChart" height="400"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        let detailChart = null;

        function formatNumber(num) {
            if (!num) return '$0';
            if (num >= 1e9) return '$' + (num / 1e9).toFixed(2) + 'B';
            if (num >= 1e6) return '$' + (num / 1e6).toFixed(2) + 'M';
            return '$' + num.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 6});
        }

        function formatPercent(pct) {
            if (pct === null || pct === undefined || pct === 0) return '-';
            const cls = pct >= 0 ? 'change-positive' : 'change-negative';
            return `<span class="${cls}">${pct > 0 ? '+' : ''}${pct.toFixed(2)}%</span>`;
        }

        async function loadCoins() {
            try {
                const endpoint = "{{ '/api/trending' if is_trending else '/api/data' }}";
                const res = await fetch(endpoint);
                if (!res.ok) throw new Error("Network error");
                const json = await res.json();
                const data = json.data || [];

                const tbody = document.querySelector('#tableBody');
                tbody.innerHTML = '';

                data.forEach(coin => {
                    const row = document.createElement('tr');
                    row.style.cursor = 'pointer';
                    row.onclick = () => openModal(coin.id, coin.name, coin.symbol);

                    row.innerHTML = `
                        <td>${coin.rank}</td>
                        <td><img src="${coin.logo}" class="coin-logo rounded-circle" alt=""> ${coin.name} <small class="text-muted">${coin.symbol}</small></td>
                        <td>${formatNumber(coin.price)}</td>
                        <td>${formatPercent(coin.change_1h)}</td>
                        <td>${formatPercent(coin.change_24h)}</td>
                        <td>${formatPercent(coin.change_7d)}</td>
                        <td>${formatNumber(coin.volume_24h)}</td>
                        <td>${formatNumber(coin.market_cap)}</td>
                        <td><canvas class="sparkline" data-prices='${JSON.stringify(coin.sparkline_prices)}'></canvas></td>
                    `;
                    tbody.appendChild(row);
                });

                document.querySelectorAll('.sparkline').forEach(canvas => {
                    let prices = [];
                    try { prices = JSON.parse(canvas.dataset.prices); } catch(e) {}
                    if (prices.length < 2) return;
                    const isUp = prices[prices.length - 1] >= prices[0];
                    new Chart(canvas, {
                        type: 'line',
                        data: { datasets: [{ data: prices, borderColor: isUp ? '#00c853' : '#ff1744', tension: 0.4, pointRadius: 0, fill: false, borderWidth: 2 }] },
                        options: { scales: { x: { display: false }, y: { display: false } }, plugins: { legend: { display: false } }, responsive: true, maintainAspectRatio: false }
                    });
                });

                document.getElementById('lastUpdate').textContent = json.last_update || new Date().toUTCString();
            } catch (err) {
                console.error(err);
                document.querySelector('#tableBody').innerHTML = '<tr><td colspan="9" class="text-center text-danger">Failed to load data — check console (F12)</td></tr>';
            }
        }

        async function openModal(id, name, symbol) {
            document.getElementById('modalTitle').textContent = `${name} (${symbol}) — 30 Day Candlestick Chart`;
            try {
                const res = await fetch(`/api/coin_ohlc/${id}`);
                const rawData = await res.json();

                const candleData = rawData.map(d => ({
                    x: d[0],
                    o: d[1],
                    h: d[2],
                    l: d[3],
                    c: d[4]
                }));

                if (detailChart) detailChart.destroy();
                detailChart = new Chart(document.getElementById('detailChart'), {
                    type: 'candlestick',
                    data: {
                        datasets: [{
                            label: `${symbol.toUpperCase()} / USD`,
                            data: candleData
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });

                new bootstrap.Modal(document.getElementById('chartModal')).show();
            } catch (err) {
                alert('Could not load candlestick chart');
                console.error(err);
            }
        }

        document.getElementById('searchInput').addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            document.querySelectorAll('#coinsTable tbody tr').forEach(row => {
                row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
            });
        });

        document.getElementById('themeToggle').addEventListener('click', () => {
            document.body.classList.toggle('theme-dark');
            const isDark = document.body.classList.contains('theme-dark');
            const iconEl = document.querySelector('#themeToggle i');
            iconEl.classList.toggle('fa-moon', isDark);
            iconEl.classList.toggle('fa-sun', !isDark);
        });

        loadCoins();
        setInterval(loadCoins, 60000);
    </script>
</body>
</html>
'''
application = app  # Gunicorn sometimes looks for 'application' as fallback
