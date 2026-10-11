#!/usr/bin/env python3
"""Oracle mirror of engine.js for Vacuum math. Writes expected.json (with trailing newline)."""
import json, math

def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100

def article(n):
    s = str(int(n)) if isinstance(n, float) and n == int(n) else str(n)
    return "an" if s.startswith(("8", "11", "18")) else "a"

def jsnum(x):
    if isinstance(x, float) and x == int(x) and abs(x) < 1e15:
        return int(x)
    return x

def fmt(x):
    if isinstance(x, float) and x == int(x):
        return str(int(x))
    return repr(x) if isinstance(x, float) else str(x)

def binPlan(binL, perSessionL, sessionsWeek):
    if not (binL > 0) or not (perSessionL > 0) or not (sessionsWeek > 0):
        return {"error": "bin, pickup and pace must be positive"}
    sessions = r1(binL / perSessionL)
    emptiesYear = r1(sessionsWeek * 52 / sessions)
    return {"binL": jsnum(float(binL)), "perSessionL": jsnum(float(perSessionL)), "sessionsWeek": jsnum(float(sessionsWeek)),
            "sessions": jsnum(sessions), "emptiesYear": jsnum(emptiesYear)}

def bagPlan(bagL, perSessionL, sessionsWeek, bagPrice):
    if not (bagL > 0) or not (perSessionL > 0) or not (sessionsWeek > 0) or not (bagPrice > 0):
        return {"error": "bag, pickup, pace and price must be positive"}
    sessions = r1(bagL / perSessionL)
    bagsYear = r1(sessionsWeek * 52 / sessions)
    costYear = r2(bagsYear * bagPrice)
    return {"bagL": jsnum(float(bagL)), "perSessionL": jsnum(float(perSessionL)), "sessionsWeek": jsnum(float(sessionsWeek)),
            "bagPrice": jsnum(float(bagPrice)), "sessions": jsnum(sessions), "bagsYear": jsnum(bagsYear), "costYear": jsnum(costYear)}

def filterPlan(filterH, minSession, sessionsWeek, filterPrice):
    if not (filterH > 0) or not (minSession > 0) or not (sessionsWeek > 0) or not (filterPrice > 0):
        return {"error": "filter life, session length, pace and price must be positive"}
    hoursWeek = minSession * sessionsWeek / 60
    weeks = r1(filterH / hoursWeek)
    filtersYear = r1(52 / weeks)
    costYear = r2(filtersYear * filterPrice)
    return {"filterH": jsnum(float(filterH)), "minSession": jsnum(float(minSession)), "sessionsWeek": jsnum(float(sessionsWeek)),
            "filterPrice": jsnum(float(filterPrice)), "weeks": jsnum(weeks), "filtersYear": jsnum(filtersYear), "costYear": jsnum(costYear)}

def renderBin(r):
    return (article(r["binL"]) + " " + fmt(r["binL"]) + " L bin picking up a labeled " + fmt(r["perSessionL"]) + " liters a session fills after " + fmt(r["sessions"]) +
            " sessions - about " + fmt(r["emptiesYear"]) + " empties a year at " + fmt(r["sessionsWeek"]) + " sessions a week.")

def renderBag(r):
    return ("A labeled " + fmt(r["bagL"]) + " L bag at a labeled " + fmt(r["perSessionL"]) + " liters a session lasts " + fmt(r["sessions"]) +
            " sessions - about " + fmt(r["bagsYear"]) + " bags and " + fmt(r["costYear"]) + " a year at " + fmt(r["sessionsWeek"]) + " sessions a week.")

def renderFilter(r):
    return ("A labeled " + fmt(r["filterH"]) + "-hour filter at " + fmt(r["minSession"]) + " minutes a session, " + fmt(r["sessionsWeek"]) +
            " sessions a week, lasts about " + fmt(r["weeks"]) + " weeks - about " + fmt(r["filtersYear"]) + " filters and " + fmt(r["costYear"]) + " a year.")

CASES = []
CASES.append({"fn": "binPlan", "args": [0.8, 0.4, 2]})
CASES.append({"fn": "binPlan", "args": [1.5, 0.3, 3]})
CASES.append({"fn": "binPlan", "args": [0.5, 0.5, 1]})
CASES.append({"fn": "binPlan", "args": [2, 0.6, 4]})
CASES.append({"fn": "binPlan", "args": [8, 0.8, 2]})
CASES.append({"fn": "binPlan", "args": [1.2, 0.25, 6]})
CASES.append({"fn": "binPlan", "args": [0, 0.4, 2]})
CASES.append({"fn": "binPlan", "args": [0.8, 0, 2]})
CASES.append({"fn": "binPlan", "args": [0.8, 0.4, 0]})
CASES.append({"fn": "binPlan", "args": [0.6, 0.45, 5]})
CASES.append({"fn": "binPlan", "args": [3, 0.7, 2.5]})
CASES.append({"fn": "binPlan", "args": [11, 1, 1]})
CASES.append({"fn": "bagPlan", "args": [2, 0.4, 2, 3]})
CASES.append({"fn": "bagPlan", "args": [3.5, 0.5, 3, 4.5]})
CASES.append({"fn": "bagPlan", "args": [1.5, 0.3, 1, 2.25]})
CASES.append({"fn": "bagPlan", "args": [4, 0.8, 4, 6]})
CASES.append({"fn": "bagPlan", "args": [2.5, 0.6, 2, 1.5]})
CASES.append({"fn": "bagPlan", "args": [5, 0.7, 5, 8.99]})
CASES.append({"fn": "bagPlan", "args": [0, 0.4, 2, 3]})
CASES.append({"fn": "bagPlan", "args": [2, 0.4, 2, 0]})
CASES.append({"fn": "bagPlan", "args": [2, 0, 2, 3]})
CASES.append({"fn": "bagPlan", "args": [2, 0.4, 0, 3]})
CASES.append({"fn": "bagPlan", "args": [3, 0.45, 3.5, 5.5]})
CASES.append({"fn": "bagPlan", "args": [18, 1.2, 2, 7.25]})
CASES.append({"fn": "filterPlan", "args": [75, 20, 2, 12]})
CASES.append({"fn": "filterPlan", "args": [50, 30, 3, 9]})
CASES.append({"fn": "filterPlan", "args": [100, 15, 1, 15.5]})
CASES.append({"fn": "filterPlan", "args": [60, 45, 4, 22]})
CASES.append({"fn": "filterPlan", "args": [80, 25, 6, 6.75]})
CASES.append({"fn": "filterPlan", "args": [40, 60, 2, 30]})
CASES.append({"fn": "filterPlan", "args": [0, 20, 2, 12]})
CASES.append({"fn": "filterPlan", "args": [75, 0, 2, 12]})
CASES.append({"fn": "filterPlan", "args": [75, 20, 2, 0]})
CASES.append({"fn": "filterPlan", "args": [75, 20, 0, 12]})
CASES.append({"fn": "filterPlan", "args": [90, 12, 3, 18.5]})
CASES.append({"fn": "filterPlan", "args": [120, 90, 1, 45]})

out = []
for c in CASES:
    fn = {"binPlan": binPlan, "bagPlan": bagPlan, "filterPlan": filterPlan}[c["fn"]]
    r = fn(*c["args"])
    is_err = "error" in r
    if is_err:
        render = r["error"]
    else:
        render = {"binPlan": renderBin, "bagPlan": renderBag, "filterPlan": renderFilter}[c["fn"]](r)
    out.append({"fn": c["fn"], "args": c["args"], "result": r, "render": render, "isError": is_err})

with open("expected.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
    f.write("\n")
print("wrote", len(out), "cases")
