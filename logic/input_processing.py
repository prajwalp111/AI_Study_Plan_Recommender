import datetime

def validate_inputs(subjects, hours, target_date):
    errors = []
    if not subjects:
        errors.append("Subject list cannot be empty.")
    if hours <= 0:
        errors.append("Study hours must be greater than 0.")
    if target_date <= datetime.date.today():
        errors.append("Target date must be in the future.")
    return errors
