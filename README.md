![Python](https://img.shields.io/badge/python-3.8%2B-blue)

---

# ♟️ Chess960 SVG Generator

A simple Python utility that helps players set up **Fischer Random (Chess960)** positions quickly and accurately.  
Given a Chess960 starting position number, the script generates an **SVG file** that can be opened in any modern browser, making it easy to visualize and arrange pieces on a physical board.

---

## ✨ Purpose
The purpose of this script is to **bridge the gap between digital and physical play** in Chess960.  
Instead of manually deciphering piece placements from a number, you can instantly generate a clean, browser-viewable SVG diagram to guide your setup. Perfect for casual matches, tournaments, or training sessions.

---

## 📦 Dependencies
- [python-chess](https://python-chess.readthedocs.io/en/latest/)  
  Install via pip:
  ```bash
  pip install chess
  ```

---

## 🚀 Usage
1. Run the script:
   ```bash
   python generate960.py
   ```
2. Enter a Chess960 position number (0–959) when prompted.
3. The script will generate an SVG file (e.g., `svg_pos#.svg`).
4. Open the SVG in any browser to view the board setup.

---
<!--

## 🔮 Future Ideas
- Add support for generating PNG images alongside SVG.  
- Option to randomize a Chess960 position automatically.  
- Command-line arguments for faster usage (e.g., `python chess960_svg.py 518`).  

---
-->

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0) — see the [LICENSE](LICENSE) file for details.
---
this is note

