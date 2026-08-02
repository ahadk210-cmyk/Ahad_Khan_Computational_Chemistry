import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PROJECT 1 DATA — DFT Analysis of Food Antioxidants
# B3LYP/6-31G* level of theory
# ============================================================

molecules = ['Quercetin', 'Caffeic Acid', 'Ascorbic Acid', 'Catechin']

# HOMO-LUMO gaps (eV)
gaps = [3.9688, 4.1927, 5.3744, 5.6501]

# HOMO energies (eV)
homo = [-5.5803, -5.7234, -6.1194, -5.3061]

# LUMO energies (eV)
lumo = [-1.6115, -1.5307, -0.7450, 0.3440]

# Chemical softness (eV-1)
softness = [0.2520, 0.2385, 0.1861, 0.1770]

# Experimental DPPH IC50 (μM) from literature
ic50 = [8.4, 14.0, 31.3, 15.0]

# Colors for each molecule
colors = ['#2ecc71', '#e74c3c', '#3498db', '#f39c12']

# ============================================================
# PLOT 1 — HOMO-LUMO Gap Bar Chart
# ============================================================

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(molecules, gaps, color=colors, edgecolor='black', linewidth=0.8)
ax.set_ylabel('HOMO-LUMO Gap (eV)', fontsize=12)
ax.set_title('HOMO-LUMO Energy Gap of Food Antioxidants\n(B3LYP/6-31G*)', fontsize=13)
ax.set_ylim(0, 7)
for bar, val in zip(bars, gaps):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{val:.2f} eV', ha='center', va='bottom', fontsize=10)
ax.axhline(y=np.mean(gaps), color='gray', linestyle='--', linewidth=1, label=f'Mean gap = {np.mean(gaps):.2f} eV')
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot1_HOMO_LUMO_Gap.png', dpi=300)
plt.show()
print("Plot 1 saved!")

# ============================================================
# PLOT 2 — Chemical Softness Bar Chart
# ============================================================

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(molecules, softness, color=colors, edgecolor='black', linewidth=0.8)
ax.set_ylabel('Chemical Softness S (eV⁻¹)', fontsize=12)
ax.set_title('Chemical Softness of Food Antioxidants\n(Higher = More Reactive = Stronger Antioxidant)', fontsize=13)
ax.set_ylim(0, 0.35)
for bar, val in zip(bars, softness):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
            f'{val:.4f}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot2_Chemical_Softness.png', dpi=300)
plt.show()
print("Plot 2 saved!")

# ============================================================
# PLOT 3 — HOMO and LUMO Energy Levels
# ============================================================

x = np.arange(len(molecules))
width = 0.35
fig, ax = plt.subplots(figsize=(9, 6))
bars1 = ax.bar(x - width/2, homo, width, label='HOMO', color='#3498db', edgecolor='black', linewidth=0.8)
bars2 = ax.bar(x + width/2, lumo, width, label='LUMO', color='#e74c3c', edgecolor='black', linewidth=0.8)
ax.set_ylabel('Orbital Energy (eV)', fontsize=12)
ax.set_title('HOMO and LUMO Orbital Energies\n(B3LYP/6-31G*)', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(molecules, fontsize=10)
ax.axhline(y=0, color='black', linewidth=0.8, linestyle='-')
ax.legend(fontsize=11)
for bar, val in zip(bars1, homo):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.2,
            f'{val:.2f}', ha='center', va='top', fontsize=9, color='white', fontweight='bold')
for bar, val in zip(bars2, lumo):
    offset = 0.15 if val >= 0 else -0.2
    va = 'bottom' if val >= 0 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + offset,
            f'{val:.2f}', ha='center', va=va, fontsize=9, color='white', fontweight='bold')
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot3_Orbital_Energies.png', dpi=300)
plt.show()
print("Plot 3 saved!")

# ============================================================
# PLOT 4 — Computed Gap vs Experimental DPPH IC50
# ============================================================

fig, ax = plt.subplots(figsize=(8, 6))
for i, mol in enumerate(molecules):
    ax.scatter(gaps[i], ic50[i], color=colors[i], s=150, zorder=5, edgecolors='black', linewidth=0.8)
    ax.annotate(mol, (gaps[i], ic50[i]),
                textcoords='offset points', xytext=(8, 5), fontsize=10)

# Trend line
z = np.polyfit(gaps, ic50, 1)
p = np.poly1d(z)
x_line = np.linspace(min(gaps)-0.2, max(gaps)+0.2, 100)
ax.plot(x_line, p(x_line), 'k--', linewidth=1.2, alpha=0.7, label='Linear trend')

# R² value
correlation = np.corrcoef(gaps, ic50)[0, 1]
r_squared = correlation**2
ax.text(0.05, 0.95, f'R² = {r_squared:.3f}', transform=ax.transAxes,
        fontsize=12, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.set_xlabel('HOMO-LUMO Gap (eV)', fontsize=12)
ax.set_ylabel('Experimental DPPH IC₅₀ (μM)', fontsize=12)
ax.set_title('Correlation: Computed HOMO-LUMO Gap vs\nExperimental DPPH Antioxidant Activity', fontsize=13)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot4_Gap_vs_IC50.png', dpi=300)
plt.show()
print("Plot 4 saved!")

print("\nAll 4 plots generated and saved successfully!")