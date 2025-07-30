# 🎨 BGR_trackbars

A simple interactive OpenCV application for understanding how colors are formed using the BGR (Blue, Green, Red) color model. The tool provides real-time color formation using trackbars, allowing users to experiment with different color combinations visually.

---

## 📌 What This Project Does

- Uses OpenCV trackbars to control individual **B**, **G**, and **R** channels.
- Displays the resulting color in real-time on a black image window.
- Includes a binary **ON/OFF switch** trackbar that determines whether the color is visible or not.
- Demonstrates OpenCV's default use of **BGR** instead of the conventional RGB model.

---

## 🧠 Why 0 to 255?

Each color channel (Blue, Green, Red) in OpenCV is 8-bit, meaning it supports values from **0 to 255**:
- `0` → No intensity (dark)
- `255` → Full intensity (brightest)
This range forms the foundation of most color images, where each pixel is represented by a BGR tuple.

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/BGR_trackbars.git
cd BGR_trackbars
```
Change the directory

```bash
cd BGR_trackbars
```

### 2. Install Requirements (in terminal)

Only **OpenCV** and **NumPy** are required:

```bash
pip install opencv-python numpy
```

### 3. Run the Code

```bash
python BGR_trackbar.py
```

### 4. Use the interface

* Adjust the **Blue**, **Green**, and **Red** sliders to create your desired color.
* Use the **ON/OFF switch** to toggle color visibility.
* Press the **Esc key** to exit the window.

---

## 🧩 Key features

* How OpenCV handles color channels (BGR vs RGB)
* Real-time GUI interaction using `createTrackbar`
* Basic NumPy image manipulation
* Binary logic control with GUI elements

