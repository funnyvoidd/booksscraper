# 🚀 Modular Scraping System (Freelance Ready)

A lightweight, config-driven Python scraping framework for fast development of custom scrapers.

---

## 💡 What this project does

This system allows you to:

- scrape paginated websites
- plug in custom parsers per site
- export data to CSV (extensible to JSON/DB)
- configure scraping via YAML (no code changes needed)
- reuse the same engine for different projects

---

## ⚙️ Architecture

- **Engine** → controls scraping workflow  
- **Parsers** → extract data from HTML  
- **Exporters** → save data (CSV, extendable)  
- **Config system** → controls behavior without code changes  

---

## ▶️ How to run

```bash
python -m src.main
```

## 📦 Output
### After execution:
Data saved to file (defined in config)
scraping summary printed in terminal.

Example:
```bash
==================================================
✅ SCRAPING COMPLETED SUCCESSFULLY
📦 Total items scraped: 1200
💾 Results saved to: data/output.csv
==================================================
```

## 🔌 Adding new website

1. Create a new parser in ```
src/parsers/```
2. Update config.yaml
3. Run the system

No changes to engine required.

## 🧠 Use cases

- e-commerce data collection
- price monitoring
- lead generation
- research datasets
- automation pipelines