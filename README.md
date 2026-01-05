# 🖼️ Local Photo Reviver

**Local Photo Reviver** is a fully local AI tool that restores, colorizes, and animates old photos.
It brings historical images back to life — without uploading them to the cloud.

> Privacy-first · Modular · Open-source · GPU-accelerated

---

## ✨ Features

- 🧩 Old photo restoration (damage, blur, noise)
- 🎨 Automatic colorization with realistic tones
- 🎞️ Photo animation
  - Face micro-motion (blink, smile)
  - 2.5D depth parallax
- 🖥️ Fully local inference (no cloud, no upload)
- 🔌 Modular pipeline (easy to swap models)
- 😊 Simple & Interactive GUI (thanks to Gradio)

---

## 📐 Pipeline Overview

Input Photo  
↓  
Preprocessing  
↓  
Restoration  
↓  
Colorization  
↓  
Animation  
↓  
Image / Video Output

---

## 🛠️ Installation

```bash
git clone https://github.com/yourname/local-photo-reviver.git
cd local-photo-reviver
conda env create -f environment.yml
conda activate photo-reviver
```

## 🚀 Quick Start (CLI)

```bash
python src/cli.py \
  --input examples/input/old_photo.jpg \
  --restore \
  --colorize \
  --animate parallax
```

Outputs will be saved to `outputs/`.

## 😊 Graphical User Interface (GUI)

For an easier, more interactive experience, you can use the Gradio-powered GUI.

```bash
python src/gui.py
```

This will launch a local web server. Open your browser and navigate to the URL provided in the terminal (usually `http://127.0.0.1:7860`) to use the interface.

<!-- TODO: Add a screenshot of the GUI here -->

**[GUI Screenshot Placeholder]**

## 📦 Building the Executable

You can build a single `.exe` file for Windows that contains the entire application.

1. Make sure you have `pyinstaller` installed (`pip install pyinstaller`).
2. Run the build command from the project root:

```bash
pyinstaller --name LocalPhotoReviver --onefile --windowed --add-data "src;src" src/gui.py
```

3. The final executable will be located in the `dist/` directory.

> **Note**: Building an executable with complex ML libraries can be tricky. You may need to create a custom `.spec` file to ensure all dependencies and data files are correctly bundled.

## 📂 Project Structure

- `src/pipeline/` — core AI pipeline
- `src/animation/` — animation generation
- `models/` — model placeholders & download instructions
- `notebooks/` — demo notebooks
- `configs/` — pipeline configs

## 🧪 Demo Notebook

Check `notebooks/demo_local_photo_reviver.ipynb` for a step-by-step walkthrough.

## 🧠 Roadmap

- Project structure & pipeline design
- Integrate old photo restoration model
- Integrate colorization model
- Depth-based photo animation
- Face animation module
- Web UI

## ⚠️ Disclaimer

This project is for research and educational purposes.
Please respect privacy and historical accuracy.

---

## 📜 License

MIT License