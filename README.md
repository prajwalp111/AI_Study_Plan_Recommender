Here’s the complete content for your README.md file. You can copy it into a file named README.md and include it in your project folder:

---

# 🧠 AI Study Plan Recommender – Digital Blinc Internship Project

This project is a Personalized Study Plan Generator built using Python and Streamlit. It creates optimized daily study schedules for students based on their goals, available hours, and subject preferences.

## 🚀 Features

* Collects user input: subjects, total days, hours per day, weak/priority subjects
* Distributes study time intelligently using weighted logic
* Dynamically generates a weekly/monthly plan
* Visualizes the schedule in tables
* Allows exporting the plan as an Excel file
* Streamlit-based user interface for easy interaction

## 🛠️ Tech Stack

* Python 3.8+
* Streamlit
* Pandas
* NumPy
* OpenPyXL (for Excel export)

## 🧩 Folder Structure

```
📁 study_plan_app/
├── main.py
├── logic/
│   ├── input_processing.py
│   ├── scheduler.py
│   └── exporter.py
├── assets/
│   └── style.css (optional)
├── README.md
└── requirements.txt
```

## 📦 Installation

1. Clone the repository or extract the zip:

   ```bash
   git clone https://github.com/yourusername/study-plan-ai.git
   cd study-plan-ai
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the App

Launch the Streamlit application:

```bash
streamlit run main.py
```

The app will open in your default browser. Input your subjects, goal duration, hours per day, and weak areas to get your personalized plan.

## 📤 Export Option

Click the "Export to Excel" button at the bottom of the app to download your study schedule.

## 🧪 Certification Notes

Before submission, ensure your app:

* Accepts valid inputs
* Generates accurate daily plans
* Respects priority subject preferences
* Is bug-free and passes UI review

## 📋 Preview : 

![Preview](https://github.com/prajwalp111/AI_Study_Plan_Recommender/blob/main/preview1.png?raw=true)

![Preview](https://github.com/prajwalp111/AI_Study_Plan_Recommender/blob/main/preview2.png?raw=true)

---

