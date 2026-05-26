# Collatz Structural Framework — Spiral Families, Fixed‑k Layers, and Global Dynamics

This repository contains all supplementary materials supporting the paper:

**“A Structural Theory of the Inverse Collatz Map:  
Spiral Families, Modular Geometry, Entropy Barriers, and Global Descent.”**

It includes interactive HTML visualizations, Python scripts, computational
notebooks, and high‑resolution figures used throughout the document.

---

## 📁 Repository Contents

### 🔷 1. Interactive HTML Visualizations
Located in `html/`.

These pages illustrate the geometric and modular structure of the inverse
Collatz map:

- **Spiral Family Explorer** — visualize the affine chain \(n \mapsto 4n+1\)
  and the unique family of every odd integer.
- **Collatz Galaxy** — digit‑color maps, modular residue overlays, and
  geometric spirals.
- **Fixed‑k Layers** — directed graphs showing inverse edges, same‑color
  connectivity, and absence of cycles.
- **Odd‑Only DAG Viewer** — interactive visualization of the odd‑only
  inverse Collatz graph.

All HTML files run locally in any modern browser.

---

### 🔷 2. Python Scripts
Located in `python/`.

These scripts implement the computational components of the theory:

- `1`  
  Compute the initial exponent \(k_0(m)\) for any odd child \(m\).

- `2`  
  Generate the full affine chain \(n_{t+1} = 4n_t + 1\) for any family.

- `3`  
  Determine valid odd children and classify them by modular constraints.

- `4`  
  Construct fixed‑\(k\) inverse layers and export them as graphs.

- `5`  
  Classify odd integers modulo \(10, 20, 100\) and identify family membership.

- `6`  
  Produce spiral, modular, and digit‑pattern visualizations.

All scripts are written in pure Python and require only standard libraries
(or optionally `matplotlib` for plotting).


---

### 🔷 4. Figures and Images
Located in `figures/`.

High‑resolution images used in the paper:

- Spiral family plots  
- Collatz Galaxy color maps  
- Fixed‑\(k\) directed graphs  
- Modular residue diagrams  
- Digit‑pattern visualizations  

---

## 📘 How to Use This Repository

### 🔹 Explore the HTML visualizations
Open any file in `html/` directly in your browser.

### 🔹 Run Python scripts
```bash
python python/generate_spiral_family.py

