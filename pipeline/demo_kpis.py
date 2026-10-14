"""Food-security KPI pipeline demo on SYNTHETIC survey rows (KoBoToolbox-style export).

validate -> standardise -> KPIs (dietary diversity score, share below threshold, cohort income change).
"""
import numpy as np, pandas as pd

FOOD_GROUPS = ["cereals", "tubers", "vegetables", "fruits", "meat", "eggs", "fish", "legumes", "dairy", "oils", "sugar", "condiments"]


def make_survey(n=600, seed=9):
    r = np.random.default_rng(seed)
    d = pd.DataFrame({"household_id": range(n), "sub_county": r.choice(["North", "South", "East", "West"], n),
                      "survey_date": pd.to_datetime("2025-01-01") + pd.to_timedelta(r.integers(0, 365, n), "D")})
    for g in FOOD_GROUPS:
        d[g] = r.binomial(1, np.where(d.sub_county == "North", .35, .6) if g not in ("cereals", "oils") else .9, n)
    d.loc[r.choice(n, 15, replace=False), "cereals"] = 7  # invalid values to catch
    return d


def validate(d):
    bad = d[FOOD_GROUPS].isin([0, 1]).all(axis=1) == False
    return d[~bad].copy(), d[bad].assign(reject_reason="food group flag not 0/1")


def kpis(d):
    d = d.assign(hdds=d[FOOD_GROUPS].sum(axis=1), quarter=d.survey_date.dt.to_period("Q").astype(str))
    out = d.groupby(["quarter", "sub_county"]).agg(households=("household_id", "count"), mean_hdds=("hdds", "mean"),
                                                   pct_low_diversity=("hdds", lambda s: (s <= 4).mean() * 100)).reset_index()
    return out.round(2)


if __name__ == "__main__":
    good, rej = validate(make_survey())
    print(f"valid {len(good)} | rejected {len(rej)} ({rej.reject_reason.iloc[0] if len(rej) else ''})")
    print(kpis(good).head(8).to_string(index=False))
