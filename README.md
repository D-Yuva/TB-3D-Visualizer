# 🦠 TB 3D Visualizer

This project visualizes suspected Tuberculosis (TB)-infected regions in chest X-rays as a 3D volume using basic image processing and PyVista. The pipeline converts a 2D masked X-ray into a volumetric representation to help with exploratory visualizations.

---

## 📁 Project Structure


---

## 🚀 Features

- ✅ Automatically generates binary mask if one doesn't exist
- ✅ Applies mask to grayscale X-ray image
- ✅ Extrudes 2D masked image into a pseudo-3D volume
- ✅ Renders volume with lighting and opacity using PyVista

---

## 📦 Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt

Run main.py
