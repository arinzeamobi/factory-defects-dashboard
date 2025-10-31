# Factory Defects & Yield Analysis

**Portfolio Project** | Data Analyst

---

## Project Overview

Analyzed 6 months of manufacturing data (5,400 records) to identify defect patterns, calculate yield metrics, and provide actionable insights for quality improvement across 3 production lines.

**Key Finding:** Misalignment defects account for 31% of all quality issues, and Line 2 consistently underperforms with 99.68% yield vs. 99.71% target.

---

## Tools & Technologies

- **Excel** - Pivot tables, calculated fields, data visualization
- **Power BI** - Interactive dashboard with KPIs and slicers
- **Python** (pandas, matplotlib) - Automated analysis and reporting
- **SQL** (DuckDB) - Database queries and aggregations

---

## Project Structure

```
/factory-analytics/
├── factory_defects_6mo.csv          # Raw data (5,400 records)
├── Defects_Yield_Excel.xlsx         # Excel analysis with 3 pivots + charts
├── Factory_Dashboard.pbix           # Power BI interactive dashboard
├── analysis_starter.py              # Python automation script
├── sql_queries.md                   # SQL queries with results
├── daily_yield_plot.png             # Yield trend visualization
├── pivot_defects_by_line.csv        # Exported pivot table
└── README.md                        # This file
```

---

## Analysis Deliverables

### 1. Excel Analysis
**3 Pivot Tables:**
- Defect count by type (sorted descending)
- Defect count by line × shift (matrix)
- Daily yield % with calculated field

**2 Charts:**
- Bar chart: Top 5 defect types
- Line chart: Yield % trend over time

### 2. Power BI Dashboard
**Interactive one-page dashboard featuring:**
- KPI cards: Yield %, Total Scrap Cost, Total Defects
- Bar chart: Defects by type
- Line chart: Yield % over time
- Matrix: Line × Shift breakdown
- Slicers: Line, Product, Shift (for filtering)

### 3. Python Analysis
**Automated reporting script that:**
- Calculates KPIs (Total Defects: 19,882 | Total Produced: 6,492,565 | Yield: 99.69%)
- Generates daily yield trend visualization
- Creates pivot table exports for further analysis

### 4. SQL Queries
**3 business queries:**
- Top defects by type (Misalignment: 6,153)
- Yield % per production line (L3: 99.71%, L1: 99.69%, L2: 99.68%)
- Scrap cost by month and product (Widget-B trending upward)

---

## Key Insights

### Quality Issues
- **Misalignment** is the #1 defect type (6,153 occurrences, 31% of total)
- **Scratch** is second (4,778 occurrences, 24% of total)
- Combined, these two issues account for 55% of all defects

### Production Line Performance
- **Line 3** achieves best yield at 99.71%
- **Line 2** consistently underperforms at 99.68% - may need maintenance review
- All lines maintain >99.6% yield, meeting quality standards

### Cost Analysis
- **Widget-B** shows increasing scrap costs (May: $6,786 → Sept: $6,858)
- Total scrap cost: $102,010 over 6-month period
- Average daily scrap: $567

### Recommendations
1. **Immediate:** Investigate root cause of misalignment defects (31% of issues)
2. **Short-term:** Review Line 2 processes and equipment maintenance schedules
3. **Long-term:** Implement preventive maintenance for Widget-B production to reduce rising scrap costs

---

## Technical Skills Demonstrated

✅ **Data Analysis:** Aggregation, grouping, calculated metrics  
✅ **Data Visualization:** Charts, dashboards, trend analysis  
✅ **Excel:** Pivot tables, formulas, conditional formatting  
✅ **Power BI:** DAX measures, interactive filtering, dashboard design  
✅ **Python:** pandas (data manipulation), matplotlib (visualization)  
✅ **SQL:** Joins, aggregations, window functions, filtering  
✅ **Business Intelligence:** KPI development, actionable insights

---

## How to Use This Project

### Excel File
- Open `Defects_Yield_Excel.xlsx`
- Review pivot tables in separate sheets
- Charts are embedded with data

### Power BI Dashboard
- Open `Factory_Dashboard.pbix` in Power BI Desktop
- Use slicers to filter by Line, Product, or Shift
- Hover over visuals for detailed tooltips

### Python Script
- Requires: Python 3.x, pandas, matplotlib
- Run: `python analysis_starter.py`
- Outputs: Console KPIs, chart PNG, pivot CSV

### SQL Queries
- Open `sql_queries.md` for documented queries
- Can be run in any SQL database (DuckDB, PostgreSQL, MySQL, etc.)
- Includes business context and insights

---

## About This Project

**Created by:** Arinze Amobi  
**Date:** October 2025  
**Purpose:** Entry-level data analyst portfolio demonstration  
**Dataset:** Synthetic manufacturing data (6 months, 3 lines, 2 shifts, 3 products, 5 defect types)

---

## Contact

*LinkedIn:** https://www.linkedin.com/in/arinze-amobi101
**GitHub:** https://github.com/arinzeamobi
**Email:** ArinzeAmobi@yahoo.com 
**Portfolio:** https://github.com/arinzeamobi/factory-defects-dashboard

---


*This project demonstrates end-to-end analytical capabilities from data exploration through actionable business recommendations.*
