def optimize_schedule(df, weak_subjects):
    if not weak_subjects:
        return df
    df['Priority'] = df['Subject'].apply(lambda s: 1 if s in weak_subjects else 0)
    return df.sort_values(by=['Date', 'Priority'], ascending=[True, False]).reset_index(drop=True)
