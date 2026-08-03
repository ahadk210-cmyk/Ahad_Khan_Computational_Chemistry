import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PROJECT 1 DATA — DFT Analysis of Food Antioxidants
# B3LYP/6-31G* level of theory — ALL 5 MOLECULES COMPLETE
# ============================================================

molecules = ['Quercetin', 'Rutin', 'Caffeic\nAcid', 'Ascorbic\nAcid', 'Catechin']
molecules_clean = ['Quercetin', 'Rutin', 'Caffeic Acid', 'Ascorbic Acid', 'Catechin']

# HOMO-LUMO gaps (eV)
gaps = [3.9688, 4.0750, 4.1927, 5.3744, 5.6501]

# HOMO energies (eV)
homo = [-5.5803, -5.6247, -5.7234, -6.1194, -5.3061]

# LUMO energies (eV)
lumo = [-1.6115, -1.5497, -1.5307, -0.7450, 0.3440]

# Chemical softness (eV-1)
softness = [0.2520, 0.2454, 0.2385, 0.1861, 0.1770]

# Experimental DPPH IC50 (μM) from literature
ic50 = [8.4, 12.6, 14.0, 31.3, 15.0]

# Colors for each molecule
colors = ['#2ecc71', '#9b59b6', '#e74c3c', '#3498db', '#f39c12']

# ============================================================
# PLOT 1 — HOMO-LUMO Gap Bar Chart
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(molecules, gaps, color=colors, edgecolor='black', linewidth=0.8)
ax.set_ylabel('HOMO-LUMO Gap (eV)', fontsize=13)
ax.set_title('HOMO-LUMO Energy Gap of Food Antioxidants\n(B3LYP/6-31G*, All 5 Molecules)', fontsize=14)
ax.set_ylim(0, 7)
for bar, val in zip(bars, gaps):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{val:.2f} eV', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.axhline(y=np.mean(gaps), color='gray', linestyle='--', linewidth=1.2,
           label=f'Mean gap = {np.mean(gaps):.2f} eV')
ax.legend(fontsize=11)
ax.tick_params(axis='x', labelsize=10)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot1_HOMO_LUMO_Gap.png', dpi=300)
plt.show()
print("Plot 1 saved!")

# ============================================================
# PLOT 2 — Chemical Softness Bar Chart
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(molecules, softness, color=colors, edgecolor='black', linewidth=0.8)
ax.set_ylabel('Chemical Softness S (eV\u207B\u00B9)', fontsize=13)
ax.set_title('Chemical Softness of Food Antioxidants\n(Higher = More Reactive = Stronger Antioxidant)', fontsize=14)
ax.set_ylim(0, 0.35)
for bar, val in zip(bars, softness):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.004,
            f'{val:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.tick_params(axis='x', labelsize=10)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot2_Chemical_Softness.png', dpi=300)
plt.show()
print("Plot 2 saved!")

# ============================================================
# PLOT 3 — HOMO and LUMO Energy Levels
# ============================================================
x = np.arange(len(molecules))
width = 0.35
fig, ax = plt.subplots(figsize=(11, 6))
bars1 = ax.bar(x - width/2, homo, width, label='HOMO', color='#3498db',
               edgecolor='black', linewidth=0.8)
bars2 = ax.bar(x + width/2, lumo, width, label='LUMO', color='#e74c3c',
               edgecolor='black', linewidth=0.8)
ax.set_ylabel('Orbital Energy (eV)', fontsize=13)
ax.set_title('HOMO and LUMO Orbital Energies\n(B3LYP/6-31G*, All 5 Molecules)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(molecules, fontsize=10)
ax.axhline(y=0, color='black', linewidth=1.0, linestyle='-')
ax.legend(fontsize=12)
for bar, val in zip(bars1, homo):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.2,
            f'{val:.2f}', ha='center', va='top', fontsize=8,
            color='white', fontweight='bold')
for bar, val in zip(bars2, lumo):
    offset = 0.15 if val >= 0 else -0.2
    va = 'bottom' if val >= 0 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + offset,
            f'{val:.2f}', ha='center', va=va, fontsize=8,
            color='white', fontweight='bold')
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot3_Orbital_Energies.png', dpi=300)
plt.show()
print("Plot 3 saved!")

# ============================================================
# PLOT 4 — Computed Gap vs Experimental DPPH IC50
# ============================================================
fig, ax = plt.subplots(figsize=(9, 6))
for i, mol in enumerate(molecules_clean):
    ax.scatter(gaps[i], ic50[i], color=colors[i], s=180, zorder=5,
               edgecolors='black', linewidth=0.8)
    ax.annotate(mol, (gaps[i], ic50[i]),
                textcoords='offset points', xytext=(8, 5), fontsize=10)
z = np.polyfit(gaps, ic50, 1)
p = np.poly1d(z)
x_line = np.linspace(min(gaps)-0.2, max(gaps)+0.2, 100)
ax.plot(x_line, p(x_line), 'k--', linewidth=1.2, alpha=0.7, label='Linear trend')
correlation = np.corrcoef(gaps, ic50)[0, 1]
r_squared = correlation**2
ax.text(0.05, 0.95, f'R\u00B2 = {r_squared:.3f}', transform=ax.transAxes,
        fontsize=13, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax.set_xlabel('HOMO-LUMO Gap (eV)', fontsize=13)
ax.set_ylabel('Experimental DPPH IC\u2085\u2080 (\u03BCM)', fontsize=13)
ax.set_title('Correlation: Computed HOMO-LUMO Gap vs\nExperimental DPPH Antioxidant Activity (5 Molecules)', fontsize=14)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot4_Gap_vs_IC50.png', dpi=300)
plt.show()
print("Plot 4 saved!")

# ============================================================
# PLOT 5 — Complete CDFT Descriptor Heatmap (NEW)
# ============================================================
import matplotlib.colors as mcolors

descriptors = ['Gap (eV)', 'IP (eV)', 'EA (eV)', 'Hardness η (eV)', 'Softness S (eV⁻¹)']
data = np.array([
    [3.9688, 5.5803, 1.6115, 1.9844, 0.2520],  # Quercetin
    [4.0750, 5.6247, 1.5497, 2.0375, 0.2454],  # Rutin
    [4.1927, 5.7234, 1.5307, 2.0964, 0.2385],  # Caffeic Acid
    [5.3744, 6.1194, 0.7450, 2.6872, 0.1861],  # Ascorbic Acid
    [5.6501, 5.3061,-0.3440, 2.8251, 0.1770],  # Catechin
])

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(data, cmap='RdYlGn_r', aspect='auto')
ax.set_xticks(range(len(descriptors)))
ax.set_xticklabels(descriptors, fontsize=11, rotation=15, ha='right')
ax.set_yticks(range(len(molecules_clean)))
ax.set_yticklabels(molecules_clean, fontsize=11)
for i in range(len(molecules_clean)):
    for j in range(len(descriptors)):
        ax.text(j, i, f'{data[i, j]:.3f}', ha='center', va='center',
                fontsize=10, fontweight='bold', color='black')
plt.colorbar(im, ax=ax, label='Value')
ax.set_title('CDFT Descriptor Heatmap — All 5 Food Antioxidants\n(B3LYP/6-31G*)', fontsize=14)
plt.tight_layout()
plt.savefig('D:\\Computational Projects\\Project 1\\Python_Analysis\\Plot5_CDFT_Heatmap.png', dpi=300)
plt.show()
print("Plot 5 saved!")

print("\nAll 5 plots generated and saved successfully!")
print("Project 1 — ALL 5 MOLECULES COMPLETE!")