# Auto Intel - 汽車供應鏈情報追蹤

## 專案狀態：🔵 初始建立 (2026-04-14)

專案剛完成初始建立，尚未進入自動化階段。

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **股價抓取** | 追蹤公司股票，Yahoo Finance | 🔲 待建立 |
| **新聞爬蟲** | 涵蓋 28 家公司 + 1 檔 ETF | 🔲 待建立 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | ✅ 從模板複製 |
| **報告生成** | 每日報告、7 日報告 | ✅ 從模板複製 |
| **前端** | D3.js Dashboard、供應鏈圖、事件時間軸 | ✅ 從模板複製 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 🔲 待設定 |

---

## 追蹤範圍

### 公司 (28 家 + 1 檔 ETF)

**上游 - 鋼鐵/輪胎/材料** (9 家)
- 日本製鐵(5401.T)、POSCO(005490.KS)、ArcelorMittal(MT NYSE)
- 普利司通(5108.T)、正新(2105.TW)、建大(2106.TW)
- 福耀玻璃(600660.SS)、Saint-Gobain(SGO.PA)、3M(MMM NYSE)

**中游 - 汽車零件** (8 家)
- 電裝(6902.T)、Continental(CON.DE)、Aptiv(APTV NYSE)
- Magna(MGA NYSE)、現代摩比斯(012330.KS)、Valeo(FR.PA)
- 和大(1536.TW)、東陽(1319.TW)

**下游 - 車廠/經銷** (11 家 + 1 ETF)
- 豐田(7203.T)、福斯(VOW3.DE)、GM(NYSE)、Ford(NYSE)
- 現代(005380.KS)、比亞迪(1211.HK)、Tesla(TSLA NASDAQ)
- Stellantis(STLA NYSE)、本田(7267.T)
- 裕隆(2201.TW)、和泰(2207.TW)
- CARZ ETF(NASDAQ)

### 主題 (configs/topics.yml)

- 汽車銷量 (auto_sales)
- 電動車滲透率 (ev_penetration)
- 零件價格 (parts_price)
- 庫存天數 (inventory_days)
- 汽車關稅與貿易 (auto_tariff_trade)
- 財報 (earnings)
- 展望 (guidance)

---

## 標準流程

```
fetch_news.py
    │
    ├─→ data/raw/{date}/news.jsonl    (原始抓取資料)
    │
    └─→ enrich_event.py
            │
            └─→ data/events/{date}.jsonl  (標準格式，唯一資料源)
                    │
            ┌───────┴───────────────┐
            │                       │
      sync_to_frontend.py     generate_metrics.py
            │                       │
            │                 data/metrics/{date}.json
            │                       │
            │                 generate_7d_report.py
            │                       │
            │                 reports/7d/{date}.json
            │                       │
      site/data/events.json   site/data/reports/7d/{date}.json
```

### 執行順序

1. `fetch_news.py` - 抓取所有公司新聞，輸出到 `data/raw/`
2. `enrich_event.py` - 標註事件，輸出到 `data/events/`（**唯一資料源**）
3. `generate_metrics.py` - 計算每日指標
4. `generate_7d_report.py` - 生成 7 日報告
5. `sync_to_frontend.py` - 同步事件到前端
6. `update_baselines.py` - 更新歷史基準線（最後執行）

**重要**：
- `data/events/*.jsonl` 是唯一的事件資料源
- 前端的 `site/data/events.json` 由 `sync_to_frontend.py` 生成
- 不要直接寫入 `site/data/events.json`

---

## 資料夾結構

```
auto-intel/
├── lib/                        # 規則引擎
│   ├── __init__.py
│   ├── matcher.py              # 關鍵字匹配
│   ├── sentiment.py            # 情緒分析
│   ├── scorer.py               # 重要性評分
│   └── anomaly.py              # 異常偵測
│
├── scripts/                    # 執行腳本
│   ├── fetch_news.py           # 整合抓取
│   ├── fetch_stocks.py         # 股價抓取
│   ├── enrich_event.py         # 事件標註
│   ├── generate_metrics.py     # 每日指標
│   ├── detect_anomalies.py     # 異常偵測
│   ├── generate_daily.py       # 每日報告
│   ├── generate_7d_report.py   # 7 日報告
│   ├── sync_to_frontend.py     # 同步事件到前端
│   └── update_baselines.py     # 更新基準線
│
├── configs/                    # 設定檔
│   ├── companies.yml           # 28 家公司 + 上下游關係
│   ├── topics.yml              # 主題 + 關鍵字
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   └── anomaly_rules.yml       # 異常偵測規則
│
├── fetchers/                   # 公司新聞爬蟲（待建立）
│
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務數據
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
│
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
│
├── site/
│   ├── index.html              # D3.js Dashboard
│   └── data/                   # 前端資料
│
└── CLAUDE.md
```

---

## 快速啟動

```bash
cd repos/auto-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 6231 -d site

# 瀏覽器開啟
open http://localhost:6231
```

---

## 故障排除

### 常見問題

1. **GitHub Actions 失敗**
   - 檢查 `gh run view <run-id> --log-failed`
   - 常見原因：網站結構變更、API 限制

2. **爬蟲抓不到資料**
   - 檢查目標網站是否改版
   - 更新 `fetchers/` 對應的爬蟲

3. **前端資料未更新**
   - 確認 `sync_to_frontend.py` 有執行
   - 檢查 `site/data/events.json` 時間戳
