import math, json

# --- Measured input from AEI (release 2025-02-10, automation_vs_augmentation.csv) ---
modes = {"directive":22.563272409918948, "feedback loop":12.036303266190515,
         "learning":18.917648061953294, "none":2.9013020624347967,
         "task iteration":25.47648663831153, "validation":2.314220367546746}
automation = modes["directive"] + modes["feedback loop"]          # AEI "automation"
augmentation = modes["learning"] + modes["task iteration"] + modes["validation"]
a_econ = automation / (automation + augmentation)                  # share among classified
print(f"AEI automation share (economy-wide, classified) a = {a_econ:.3f}")
print(f"  automation={automation:.1f}%  augmentation={augmentation:.1f}%")

# --- JT calibration ---
psiL, gY0, sigma, n = 0.5, 3.0, 0.2, 1.0
def phi(x0): return (psiL + x0/(1-sigma))/gY0
def regime(p):
    if p < 0.99: return f"semi-endogenous (g~{p*n/(1-p):.0f}%/yr)"
    if p <= 1.01: return "knife-edge"
    return f"explosive (~{1/((p-1)*(gY0/100)):.0f} yr horizon)"

# --- Level-1 flows pipeline:  x0 = -ln(1 - a*pi) flow ~ a * dpi  ---
# a   = within-AI automation share (measured; computing skews higher, API~0.77)
# dpi = annual rise in AI penetration of the sector's task volume (ASSUMPTION)
def x0_of(a, dpi):  # annual automation rate, %/yr
    return -math.log(1 - a*dpi) * 100

print("\n  a     dpi    x0(%/yr)   Phi    regime")
rows=[]
for label,a,dpi in [("low",0.43,0.05),("base",0.45,0.08),("high",0.77,0.15)]:
    x0=x0_of(a,dpi); p=phi(x0)
    rows.append((label,a,dpi,x0,p))
    print(f"  {a:.2f}  {dpi:.2f}   {x0:5.2f}     {p:.2f}   {regime(p)}  [{label}]")

base=[r for r in rows if r[0]=="base"][0]
print(f"\nBASE -> x0 = {base[3]:.1f}%/yr, Phi = {base[4]:.2f}")
print(f"JT anchors: pbs x0=2.0 Phi={phi(2.0):.2f} | computers x0=5.2 Phi={phi(5.2):.2f}")
