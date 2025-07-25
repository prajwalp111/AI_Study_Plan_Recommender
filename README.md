# 📚 AI-Powered Study Plan Recommender

An intelligent and customizable study planner built using **Streamlit**, designed to help you optimize your daily study schedule with support for weak subjects, preferred days off, and automatic break scheduling.

---

## 🚀 Features

- ✍️ Input any number of subjects
- ⏰ Customize study hours per day
- 📅 Set your target completion date
- 🧠 Prioritize weak subjects (they get **1 extra hour per day**)
- 💤 Auto-insert breaks (with adjustable count and duration)
- 🚫 Select preferred days off
- ⚙️ AI optimization for smarter scheduling
- 📥 Export your final plan as an Excel file

---

## 🗂️ Project Structure

```
AI_Study_Plan_Recommender/
├── main.py                # Streamlit UI and app logic
├── logic/
│   ├── scheduler.py       # Creates study schedule with breaks
│   ├── optimizer.py       # Optimizes schedule (weak subjects earlier)
│   ├── input_processing.py # Validates user inputs
│   └── exporter.py        # Exports schedule as Excel
├── requirements.txt       # Dependencies
└── README.md              # Project documentation (this file)
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/AI_Study_Plan_Recommender.git
cd AI_Study_Plan_Recommender
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> 🔁 If Excel export fails, also run:
```bash
pip install XlsxWriter
```

---

## 🧪 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

---

## 📤 Export Format

Exports your final plan as `study_plan.xlsx` using the format:

| Day     | Date       | Time       | Subject |
|---------|------------|------------|---------|
| Monday  | 2025-07-28 | 09:00–10:00| Math    |
|         |            | 10:00–10:15| Break   |
|         |            | 10:15–11:15| Physics |
| ...     | ...        | ...        | ...     |

---

## 📌 Notes

- Breaks are spaced automatically across your day.
- Only **1 extra hour per day** is guaranteed for weak subjects.
- Optimized schedule ensures weak subjects are not clustered.

---

## 🧾 Requirements

- Python 3.8+
- Streamlit
- Pandas
- XlsxWriter

---

## 📋 Preview : 

![Preview](https://github.com/prajwalp111/AI_Study_Plan_Recommender/blob/main/preview1.png)

![Preview](https://github.com/prajwalp111/AI_Study_Plan_Recommender/blob/main/preview2.png)

---
