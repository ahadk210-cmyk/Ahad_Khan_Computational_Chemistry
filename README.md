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
