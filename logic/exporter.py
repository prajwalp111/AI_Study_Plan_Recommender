import streamlit as st
import pandas as pd
from io import BytesIO

def export_schedule(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Study Plan')
    st.download_button(label="📥 Download as Excel", data=output.getvalue(), file_name="study_plan.xlsx")
