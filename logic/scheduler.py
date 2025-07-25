def generate_schedule(subjects, hours_per_day, target_date, priority_subjects, days_off, num_breaks, break_duration, start_hour):
    import datetime
    import pandas as pd
    import random

    today = datetime.date.today()
    delta_days = (target_date - today).days
    schedule = []

    study_block_minutes = 60
    break_block_minutes = break_duration

    for i in range(delta_days + 1):
        day = today + datetime.timedelta(days=i)
        if day.strftime("%A") in days_off:
            continue

        current_minutes = start_hour * 60  
        total_study_blocks = hours_per_day
        total_blocks = total_study_blocks + num_breaks

  
        break_positions = set()
        if num_breaks > 0 and total_study_blocks >= 2:
            interval = total_study_blocks // (num_breaks + 1)
            break_positions = {interval * (j + 1) + j for j in range(num_breaks)}

        study_blocks_done = 0
        block_index = 0
        while study_blocks_done < total_study_blocks + num_breaks:
            from_minutes = current_minutes
            if block_index in break_positions:
        
                current_minutes += break_block_minutes
                to_minutes = current_minutes
                label = "Break"
            else:
                current_minutes += study_block_minutes
                to_minutes = current_minutes
                if priority_subjects and study_blocks_done == 0:
                    label = random.choice(priority_subjects)
                else:
                    label = random.choice(subjects)
                study_blocks_done += 1

            from_time = datetime.time(from_minutes // 60, from_minutes % 60).strftime("%H:%M")
            to_time = datetime.time(to_minutes // 60, to_minutes % 60).strftime("%H:%M")

            schedule.append({
                "Day": day.strftime("%A") if block_index == 0 else "",
                "Date": day.strftime("%Y-%m-%d") if block_index == 0 else "",
                "Time": f"{from_time}–{to_time}",
                "Subject": label
            })

            block_index += 1

    return pd.DataFrame(schedule)
