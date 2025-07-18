# 📰 Fake News Detector Chrome Extension

**Identify and avoid fake news in real-time.**
A Chrome Extension powered by NLP and machine learning that classifies news articles as **Fake** or **Legitimate** while you browse.

---

## 🚀 Project Overview

The **Fake News Detector** is a Chrome extension developed to combat the spread of misinformation online. Using natural language processing (NLP) and machine learning techniques, the extension analyzes the content of news articles in real time and flags them accordingly.

Built with a lightweight Flask backend and a user-friendly browser interface, the tool integrates seamlessly into your browsing experience to ensure the content you consume is credible.

---

## 🔍 Features

* ✅ **Real-Time Detection**
  Instantly analyze the news content you're reading with just a click.

* 🧠 **High Accuracy**
  Achieves **92% accuracy** using a Support Vector Machine (SVM) trained on a labeled news dataset.

* 📊 **Content Analysis**
  Uses **TF-IDF Vectorization** for text representation and **NLTK** for preprocessing.

* 🖥️ **User-Friendly Interface**
  Minimal, intuitive interface built with Flask for fast and efficient user interaction.

---

## 🛠️ Tech Stack

| Component                | Technology                                     |
| ------------------------ | ---------------------------------------------- |
| **Programming Language** | Python                                         |
| **Frontend**             | Flask (rendered as the Chrome Extension popup) |
| **NLP Toolkit**          | NLTK                                           |
| **Vectorization**        | TF-IDF                                         |
| **Model**                | Support Vector Machine (SVM)                   |

---

## 🧪 How It Works

1. **Preprocessing**
   News text is cleaned using NLTK — removing stopwords, punctuation, and applying tokenization.

2. **Vectorization**
   Cleaned text is converted into numerical features using **TF-IDF**.

3. **Classification**
   A trained **SVM classifier** analyzes the vectorized input and predicts if the news is *Fake* or *Legitimate*.

4. **Display**
   Results are displayed instantly in the Chrome extension popup.

---

## 🔧 Installation & Setup

### Prerequisites

* Google Chrome
* Python 3.8+
* `pip` for package installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Fake-News-Detection.git
cd Fake-News-Detection
```

### 2. Set Up the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Start the Flask Backend

```bash
python app.py
```

### 5. Load Chrome Extension

1. Open **Chrome** → `chrome://extensions/`
2. Enable **Developer Mode**
3. Click **"Load unpacked"**
4. Select the `/extension` folder from the cloned repo

---

## 🧪 Example

| **Input**                                                       | **Prediction**    |
| --------------------------------------------------------------- | ----------------- |
| *"The Earth is flat and NASA faked the moon landing."*          | ❌ Fake News       |
| *"The Prime Minister announced a new healthcare policy today."* | ✅ Legitimate News |

---

## 📂 Project Structure

```
Fake-News-Detection/
├── extension/              # Chrome extension UI and scripts
│   ├── popup.html
│   ├── popup.js
│   └── manifest.json
├── model/
│   ├── svm_model.pkl       # Trained SVM model
│   └── tfidf_vectorizer.pkl
├── app.py                  # Flask backend for prediction
├── preprocess.py           # Text cleaning and NLP pipeline
├── requirements.txt
└── README.md
```

---

## 📈 Accuracy

* Model: **SVM Classifier**
* Vectorizer: **TF-IDF**
* Dataset: Balanced dataset of fake and real news articles
* Accuracy Achieved: **92%**

