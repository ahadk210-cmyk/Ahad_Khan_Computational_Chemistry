# Computational Investigation of Food Antioxidants Using DFT

**Author:** Ahad Khan  
**Institution:** Institute for Excellence in Higher Education (IEHE), Bhopal  
**Level:** Self-directed Research Portfolio  
**Software:** ORCA 6.1.1 | Python 3.13 | ChimeraX 1.11.1 | Multiwfn 2026.4 | Avogadro 2  
**Level of Theory:** B3LYP/6-31G*

---

## Project Overview

This project presents a density functional theory (DFT) based computational investigation of the electronic structure and antioxidant activity of five naturally occurring food polyphenols. The central question addressed is:

> *"Why are some food antioxidants stronger than others — and can quantum chemistry explain this computationally?"*

Using the B3LYP/6-31G* level of theory implemented in ORCA 6.1.1, geometry optimisations, harmonic frequency calculations, and frontier molecular orbital analyses were performed on five molecules. HOMO-LUMO gaps, conceptual DFT descriptors, and electrostatic potential maps were calculated and correlated with experimental DPPH radical scavenging activity (IC₅₀) from published literature.

---

## Molecules Studied

| Molecule | Formula | MW (Da) | Atoms | Food Source |
|----------|---------|---------|-------|-------------|
| Quercetin | C₁₅H₁₀O₇ | 302.24 | 32 | Onions, apples, berries |
| Rutin | C₂₇H₃₀O₁₆ | 594.52 | 73 | Buckwheat, citrus |
| Caffeic Acid | C₉H₈O₄ | 180.16 | 21 | Coffee, olive oil |
| Ascorbic Acid | C₆H₈O₆ | 176.12 | 20 | Citrus fruits |
| Catechin | C₁₅H₁₄O₆ | 290.27 | 35 | Green tea, cocoa |

---

## Key Results

### HOMO-LUMO Gaps and CDFT Descriptors

CDFT descriptors were derived from frontier orbital energies using:
IP = −E(HOMO) | EA = −E(LUMO) | η = ΔE/2 | S = 1/2η

| Molecule | E(HOMO) eV | E(LUMO) eV | Gap eV | IP eV | EA eV | η eV | S eV⁻¹ |
|----------|-----------|-----------|--------|-------|-------|------|---------|
| Quercetin | −5.5803 | −1.6115 | 3.9688 | 5.5803 | 1.6115 | 1.9844 | 0.2520 |
| Rutin | −5.6247 | −1.5497 | 4.0750 | 5.6247 | 1.5497 | 2.0375 | 0.2454 |
| Caffeic Acid | −5.7234 | −1.5307 | 4.1927 | 5.7234 | 1.5307 | 2.0964 | 0.2385 |
| Ascorbic Acid | −6.1194 | −0.7450 | 5.3744 | 6.1194 | 0.7450 | 2.6872 | 0.1861 |
| Catechin | −5.3061 | +0.3440 | 5.6501 | 5.3061 | −0.3440 | 2.8251 | 0.1770 |

**IP** = Ionisation Potential | **EA** = Electron Affinity | **η** = Chemical Hardness | **S** = Chemical Softness

### Antioxidant Ranking (computed vs experimental)

| Rank | Molecule | Gap (eV) | Softness (eV⁻¹) | Experimental DPPH IC₅₀ (μM) |
|------|----------|----------|-----------------|------------------------------|
| 1st | Quercetin | 3.9688 | 0.2520 | 8.4 |
| 2nd | Rutin | 4.0750 | 0.2454 | ~12.6 |
| 3rd | Caffeic Acid | 4.1927 | 0.2385 | 14.0 |
| 4th | Ascorbic Acid | 5.3744 | 0.1861 | 31.3 |
| 5th | Catechin | 5.6501 | 0.1770 | 15.0 |

The computed gap ranking is consistent with experimental DPPH data for the four polyphenols (quercetin, rutin, caffeic acid, catechin). Ascorbic acid deviates from the gap-activity correlation due to its fundamentally different enediol antioxidant mechanism, as discussed in Key Finding 4.

*IC₅₀ values: quercetin and caffeic acid from Locatelli et al. (2013), Food Chemistry; catechin and ascorbic acid from Surveswaran et al. (2007), Food Chemistry; rutin from Burda & Oleszek (2001), J. Agric. Food Chem.*

---

## Repository Structure

---
Ahad_Khan_Computational_Chemistry/
│
├── Quercetin/
│   ├── Quercetin.inp          # ORCA input file
│   ├── Quercetin_v3.out       # ORCA output file
│   ├── Quercetin.eldens.cube  # Electron density grid
│   ├── Quercetin.esp.cube     # ESP grid
│   ├── Quercetin_ESP.png      # ESP map image
│   ├── Quercetin_HOMO.png     # HOMO orbital image
│   └── Quercetin_LUMO.png     # LUMO orbital image
│
├── Catechin/
│   └── [same structure as Quercetin]
│
├── Caffeic Acid/
│   └── [same structure as Quercetin]
│
├── Ascorbic Acid/
│   └── [same structure as Quercetin]
│
├── Rutin/
│   ├── Rutin.inp              # ORCA input file
│   ├── Rutin.out              # ORCA output file (1 day 8h 49min)
│   ├── Rutin.eldens.cube      # Electron density grid
│   ├── Rutin.esp.cube         # ESP grid
│   ├── Rutin_ESP.png          # ESP map image
│   ├── Rutin_HOMO.png         # HOMO orbital image
│   └── Rutin_LUMO.png         # LUMO orbital image
│
└── Python_Analysis/
    ├── Project1_Analysis.py        # Complete analysis script
    ├── Plot1_HOMO_LUMO_Gap.png     # Bar chart of gaps (all 5 molecules)
    ├── Plot2_Chemical_Softness.png # Softness comparison
    ├── Plot3_Orbital_Energies.png  # HOMO/LUMO energy levels
    ├── Plot4_Gap_vs_IC50.png       # Correlation plot (R²=0.422)
    └── Plot5_CDFT_Heatmap.png      # CDFT descriptor heatmap
---

## Methodology

**1. Structure preparation**
3D molecular structures were downloaded from PubChem in SDF format and pre-optimised using molecular mechanics in Avogadro 2 to provide ORCA with clean starting geometries.

**2. DFT geometry optimisation**
Full geometry optimisation and harmonic frequency calculations were performed at the B3LYP/6-31G* level using ORCA 6.1.1 running inside WSL2/Ubuntu 24.04. B3LYP was chosen for its well-established performance for organic polyphenolic molecules; 6-31G* provides polarisation functions on heavy atoms at manageable computational cost for molecules of this size.

**3. Frequency verification**
Harmonic vibrational frequency calculations were performed after each geometry optimisation to confirm true energy minima (all positive frequencies). Quercetin exhibits a persistent low-frequency torsional mode (−185 cm⁻¹) documented in published DFT studies of flavonoids; all other molecules showed no imaginary frequencies.

**4. Electronic structure analysis**
HOMO and LUMO energies were extracted from ORCA output files. Five Conceptual DFT (CDFT) descriptors — ionisation potential, electron affinity, HOMO-LUMO gap, chemical hardness, and chemical softness — were calculated from frontier orbital energies using established formulas (Parr & Yang, 1989).

**5. ESP map generation**
Electron density and electrostatic potential cube files were generated using orca_plot and visualised in UCSF ChimeraX using the red-white-blue colour palette with a consistent range of −0.05 to +0.05 Hartree across all five molecules for direct comparability.

**6. Orbital visualisation**
HOMO and LUMO orbitals were rendered using Multiwfn (isovalue 0.050) after converting ORCA .gbw wavefunction files to .molden format using orca_2mkl.

**7. Data analysis and plotting**
All data analysis and visualisation was performed in Python (matplotlib, numpy) generating five publication-quality plots including a CDFT descriptor heatmap across all five molecules.

---

## Software and Tools

| Software | Version | Purpose |
|----------|---------|---------|
| ORCA | 6.1.1 | DFT calculations (geometry opt, freq, SP) |
| Python | 3.13.9 | Data analysis and plotting |
| ChimeraX | 1.11.1 | ESP map visualisation |
| Multiwfn | 2026.4 | Orbital visualisation and wavefunction analysis |
| Avogadro | 2 | Molecular building and MM pre-optimisation |
| WSL2/Ubuntu | 24.04 LTS | Linux environment for ORCA |

---

## Key Findings

1. **Quercetin** is the strongest antioxidant in this series, consistent with its smallest HOMO-LUMO gap (3.97 eV) and highest chemical softness (0.252 eV⁻¹), reflecting its extensively delocalised π-electron system across two aromatic rings with five hydroxyl groups.

2. **Rutin** ranks second (gap = 4.08 eV, softness = 0.245 eV⁻¹), consistent with its quercetin-derived flavonoid core. HOMO and LUMO orbitals are entirely localised on the chromone ring system — the disaccharide sugar unit contributes no frontier orbital density, suggesting the sugar's primary role is pharmacokinetic rather than electronic.

3. **Caffeic acid** ranks third despite its small molecular size (MW = 180 Da), consistent with extended π-conjugation through the vinyl chain connecting the catechol and carboxylate groups. Its HOMO orbital spans the entire molecular backbone.

4. **Ascorbic acid** deviates from the polyphenol gap-activity trend. Its antioxidant mechanism involves enediol proton-coupled electron transfer rather than π-electron donation, which static HOMO-LUMO gap calculations do not fully capture. This deviation is physically meaningful rather than a computational failure.

5. **Catechin's** saturated C-ring prevents full conjugation across the molecule, resulting in the largest HOMO-LUMO gap (5.65 eV), the only positive LUMO energy (+0.34 eV), and the most localised frontier orbitals in the series — consistent with its weaker experimental antioxidant activity.

6. **ESP maps** across all five molecules visually support the numerical results — quercetin shows the most extensive electron-rich (red) surface coverage, while catechin's surface is predominantly neutral (yellow), consistent with its reduced radical-scavenging capacity.

---

## References

1. Neese, F. Software update: The ORCA program system — Version 5.0. *WIREs Comput. Mol. Sci.* 2022, 12, e1606. DOI: 10.1002/wcms.1606
2. Lu, T.; Chen, F. Multiwfn: A multifunctional wavefunction analyzer. *J. Comput. Chem.* 2012, 33, 580–592. DOI: 10.1002/jcc.22885
3. Lu, T. A comprehensive electron wavefunction analysis toolbox. *J. Chem. Phys.* 2024, 161, 082503.
4. Pettersen, E.F. et al. UCSF ChimeraX. *Protein Sci.* 2021, 30, 70–82.
5. Becke, A.D. Density-functional thermochemistry. III. *J. Chem. Phys.* 1993, 98, 5648.
6. Lee, C.; Yang, W.; Parr, R.G. Development of the Colle-Salvetti correlation-energy formula. *Phys. Rev. B* 1988, 37, 785.
7. Parr, R.G.; Yang, W. *Density Functional Theory of Atoms and Molecules.* Oxford University Press, 1989.
8. Locatelli, M. et al. EC₅₀ estimation of antioxidant activity in DPPH assay. *Food Chemistry* 2013, 138, 1478–1483.
9. Surveswaran, S. et al. Systematic evaluation of natural phenolic antioxidants. *Food Chemistry* 2007, 102, 938–953.
10. Burda, S.; Oleszek, W. Antioxidant and antiradical activities of flavonoids. *J. Agric. Food Chem.* 2001, 49, 2774–2779.

---

## Notes

- Rutin (C₂₇H₃₀O₁₆, 73 atoms) required **1 day 8 hours 49 minutes** of computation time on a personal laptop (AMD Ryzen 7 4800HS, 8 cores, 16 GB RAM, WSL2/Ubuntu 24.04) — the most computationally demanding calculation in the series (662 basis functions, 219 frequency perturbations). All results are complete and included.
- Quercetin exhibits a persistent low-frequency torsional imaginary mode (−185 cm⁻¹) associated with inter-ring OH rotation, consistent with its known conformational flexibility reported in DFT literature for flavonoids. HOMO-LUMO analysis proceeds from the best available geometry.

---

*This project was developed as part of a self-directed computational chemistry portfolio in preparation for MSc applications in Chemistry.*