# Computational Investigation of Food Antioxidants Using DFT

**Author:** Ahad Khan  
**Institution:** Institute of Excellence in Higher Education (IEHE), Bhopal  
**Level:** Undergraduate Research Portfolio  
**Software:** ORCA 6.1.1 | Python 3.13 | ChimeraX | Multiwfn | Avogadro 2  
**Level of Theory:** B3LYP/6-31G*

---

## Project Overview

This project presents a density functional theory (DFT) based computational investigation of the electronic structure and antioxidant activity of four naturally occurring food polyphenols. The central question addressed is:

> *"Why are some food antioxidants stronger than others — and can quantum chemistry explain this computationally?"*

Using the B3LYP/6-31G* level of theory implemented in ORCA 6.1.1, geometry optimisations and frequency calculations were performed on four molecules. HOMO-LUMO gaps, conceptual DFT descriptors, and electrostatic potential maps were calculated and correlated with experimental DPPH radical scavenging activity (IC₅₀) from published literature.

---

## Molecules Studied

| Molecule | Formula | MW (Da) | Atoms | Food Source |
|----------|---------|---------|-------|-------------|
| Quercetin | C₁₅H₁₀O₇ | 302.24 | 32 | Onions, apples, berries |
| Caffeic Acid | C₉H₈O₄ | 180.16 | 21 | Coffee, olive oil |
| Ascorbic Acid | C₆H₈O₆ | 176.12 | 20 | Citrus fruits |
| Catechin | C₁₅H₁₄O₆ | 290.27 | 35 | Green tea, cocoa |

---

## Key Results

### HOMO-LUMO Gaps and CDFT Descriptors

| Molecule | E(HOMO) eV | E(LUMO) eV | Gap eV | IP eV | EA eV | η eV | S eV⁻¹ |
|----------|-----------|-----------|--------|-------|-------|------|---------|
| Quercetin | −5.5803 | −1.6115 | 3.9688 | 5.5803 | 1.6115 | 1.9844 | 0.2520 |
| Caffeic Acid | −5.7234 | −1.5307 | 4.1927 | 5.7234 | 1.5307 | 2.0964 | 0.2385 |
| Ascorbic Acid | −6.1194 | −0.7450 | 5.3744 | 6.1194 | 0.7450 | 2.6872 | 0.1861 |
| Catechin | −5.3061 | +0.3440 | 5.6501 | 5.3061 | −0.3440 | 2.8251 | 0.1770 |

**IP** = Ionisation Potential | **EA** = Electron Affinity | **η** = Chemical Hardness | **S** = Chemical Softness

### Antioxidant Ranking (computed vs experimental)

| Rank | Molecule | Gap (eV) | Experimental IC₅₀ (μM) |
|------|----------|----------|------------------------|
| 1st | Quercetin | 3.9688 | 8.4 |
| 2nd | Caffeic Acid | 4.1927 | 14.0 |
| 3rd | Ascorbic Acid | 5.3744 | 31.3 |
| 4th | Catechin | 5.6501 | 15.0 |

Computational ranking is consistent with experimental DPPH data — smaller HOMO-LUMO gap correlates with stronger radical-scavenging activity.

---

## Repository Structure

Ahad_Khan_Computational_Chemistry/
│
├── Quercetin/
│ ├── Quercetin.inp # ORCA input file
│ ├── Quercetin_v3.out # ORCA output file
│ ├── Quercetin.eldens.cube # Electron density grid
│ ├── Quercetin.esp.cube # ESP grid
│ ├── Quercetin_ESP.png # ESP map image
│ ├── Quercetin_HOMO.png # HOMO orbital image
│ └── Quercetin_LUMO.png # LUMO orbital image
│
├── Catechin/
│ └── [same structure]
│
├── Caffeic Acid/
│ └── [same structure]
│
├── Ascorbic Acid/
│ └── [same structure]
│
└── Python_Analysis/
├── Project1_Analysis.py # Complete analysis script
├── Plot1_HOMO_LUMO_Gap.png # Bar chart of gaps
├── Plot2_Chemical_Softness.png # Softness comparison
├── Plot3_Orbital_Energies.png # HOMO/LUMO energy levels
└── Plot4_Gap_vs_IC50.png # Correlation plot

---

## Methodology

**1. Structure preparation**
3D molecular structures were downloaded from PubChem in SDF format and pre-optimised using molecular mechanics in Avogadro 2.

**2. DFT geometry optimisation**
Full geometry optimisation and harmonic frequency calculations were performed at the B3LYP/6-31G* level using ORCA 6.1.1 running inside WSL2/Ubuntu 24.04. The B3LYP hybrid functional was chosen for its well-established performance for organic molecules, and the 6-31G* basis set provides polarisation functions on heavy atoms at manageable computational cost.

**3. Electronic structure analysis**
HOMO and LUMO energies were extracted from ORCA output files. Conceptual DFT descriptors (IP, EA, chemical hardness, chemical softness) were calculated from frontier orbital energies using established formulas.

**4. ESP map generation**
Electron density and electrostatic potential cube files were generated using orca_plot and visualised in ChimeraX using the red-white-blue colour palette (range: −0.05 to +0.05 Hartree).

**5. Orbital visualisation**
HOMO and LUMO orbitals were rendered using Multiwfn with isovalue 0.050 after converting ORCA .gbw files to .molden format using orca_2mkl.

**6. Data analysis and plotting**
All data analysis and visualisation was performed in Python using matplotlib, numpy, and custom plotting scripts.

---

## Software and Tools

| Software | Version | Purpose |
|----------|---------|---------|
| ORCA | 6.1.1 | DFT calculations |
| Python | 3.13.9 | Data analysis and plotting |
| ChimeraX | 1.11.1 | ESP map visualisation |
| Multiwfn | 2026.4 | Orbital visualisation |
| Avogadro | 2 | Molecular building |
| WSL2/Ubuntu | 24.04 | Linux environment |

---

## Key Findings

1. **Quercetin** is the strongest antioxidant among the studied molecules, consistent with its smallest HOMO-LUMO gap (3.97 eV) and highest chemical softness (0.252 eV⁻¹), reflecting its extensively delocalized π-electron system across two aromatic rings.

2. **Caffeic acid** ranks second despite its small molecular size, due to extended conjugation through the vinyl chain connecting the catechol and carboxylate groups — a finding clearly supported by its delocalized HOMO orbital spanning the entire molecule.

3. **Ascorbic acid's** antioxidant mechanism differs fundamentally from the polyphenols — operating through enediol chemistry rather than π-electron donation — explaining its deviation from the HOMO-LUMO gap correlation.

4. **Catechin's** saturated C-ring prevents full conjugation across the molecule, resulting in the largest gap (5.65 eV) and most localised frontier orbitals among the series.

5. ESP maps visually confirm the numerical results — quercetin shows the most extensive electron-rich (red) surface coverage, directly visualising the sites available for radical scavenging.

---

## References

1. Neese, F. *Software update: The ORCA program system—Version 5.0.* WIREs Comput. Mol. Sci. 2022, 12, e1606.
2. Lu, T.; Chen, F. *Multiwfn: A multifunctional wavefunction analyzer.* J. Comput. Chem. 2012, 33, 580–592.
3. Pettersen, E.F. et al. *UCSF ChimeraX.* Protein Sci. 2021, 30, 70–82.
4. Becke, A.D. *Density-functional thermochemistry. III.* J. Chem. Phys. 1993, 98, 5648.
5. Lee, C.; Yang, W.; Parr, R.G. *Development of the Colle-Salvetti correlation-energy formula.* Phys. Rev. B 1988, 37, 785.
6. Parr, R.G.; Yang, W. *Density Functional Theory of Atoms and Molecules.* Oxford University Press, 1989.
7. Locatelli, M. et al. *EC50 estimation of antioxidant activity in DPPH assay.* Food Chemistry 2013, 138, 1478–1483.

---

## Notes

- Rutin (C₂₇H₃₀O₁₆, 73 atoms) was included in the study but its geometry optimisation is computationally intensive and ongoing. Results will be added upon completion.
- Quercetin exhibits a persistent low-frequency torsional imaginary mode (−185 cm⁻¹) associated with inter-ring OH rotation, consistent with its known conformational flexibility in literature. HOMO-LUMO analysis proceeds from the best available geometry.

---

*This project was developed as part of a computational chemistry portfolio in preparation for MSc applications in Chemistry.*
