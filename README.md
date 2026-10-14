# FoodCare-KE Data Portal
### Community food-security analytics · Kenya · 2020–present

I founded FoodCare-KE, a youth-led social enterprise, and built its data side: survey collection (KoBoToolbox / Google Forms), a validation and KPI pipeline in Python, and Power BI / Excel reporting for food security, youth agribusiness outreach and nutrition programmes.

Community data is not published. `pipeline/demo_kpis.py` shows the pipeline on **synthetic survey rows**.

## Run the demo
```bash
pip install -r requirements.txt
python pipeline/demo_kpis.py
```
It rejects rows with invalid food-group flags, computes a household dietary diversity score (12 food groups) and reports mean score and the share of low-diversity households by quarter and sub-county.

## What it tracks
| Area | Examples |
|---|---|
| Food security | Dietary diversity score, share of households below a threshold |
| Youth agribusiness | Farmers trained, crops grown, cohort income change |
| Outreach | Households reached, events, partner organisations |

## Limitations
- The demo's data is invented; the diversity threshold (≤4 groups) is an illustrative choice
- No cohort tracking or dashboard files are published yet

`Python` `pandas` `Power BI` `Excel` `KoBoToolbox`
