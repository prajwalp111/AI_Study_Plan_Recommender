import pandas as pd
import datetime
import random

def generate_schedule(subjects, hours_per_day, target_date, priority_subjects, days_off):
    today = datetime.date.today()
    delta_days = (target_date - today).days
    schedule = []

    for i in range(delta_days + 1):
        day = today + datetime.timedelta(days=i)
        if day.strftime("%A") in days_off:
            continue
        for hour in range(hours_per_day):
            subject = random.choice(priority_subjects or subjects)
            schedule.append({
                "Date": day.strftime("%Y-%m-%d"),
                "Hour Slot": hour + 1,
                "Subject": subject
            })
    return pd.DataFrame(schedule)
