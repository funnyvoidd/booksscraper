# 🚀 Modular Scraping System

A production-style Python scraping framework designed for fast adaptation to any website.

---

## 💡 What this project does

This is not a single scraper — it is a **scraping engine**.

It allows you to:
- build scrapers for any website quickly
- reuse core logic
- plug in custom parsers
- export data in structured formats
- control everything via YAML config

---

## ⚙️ Features

- Config-driven architecture
- Plugin-based parsers
- Modular exporters (CSV ready, extendable)
- Pagination support
- Clean separation of concerns
- Ready for real-world scraping tasks

---

## ▶️ Run

```bash
python -m src.main
```

## 📊 Example output

- 📄 Page 1 scraped (20 items)
- 📄 Page 2 scraped (20 items)

- ✅ SCRAPING COMPLETED SUCCESSFULLY
- 📦 Total items scraped: 120
- 💾 Output file: data/output.csv
- ⏱ Time: 4.1s

## 🔌 Add new website
1. Create parser in src/parsers/
2. Add config entry
3. Run engine

No changes in core required.

## 🧠 Use cases
* e-commerce scraping
* price monitoring
* lead generation
* data pipelines
* research automation

## 🚀 Why this is useful
Instead of writing scrapers from scratch every time,
you reuse one engine for all projects.