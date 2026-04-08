import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils.i18n import get_text as t, inject_rtl_if_needed

st.set_page_config(page_title="Benchmarks", page_icon="📈", layout="wide")

lang = st.session_state.get('lang', 'en')
inject_rtl_if_needed(lang)

st.title(t(lang, "bench_title"))
st.markdown(t(lang, "bench_desc"))

col1, col2, col3 = st.columns(3)
col1.metric(t(lang, "bench_acc"), "94.2%", "+1.2%")
col2.metric(t(lang, "bench_eer"), "3.1%", "-0.5%")
col3.metric(t(lang, "bench_f1"), "0.92")

st.markdown("---")

st.markdown(t(lang, "bench_metrics_explained"))

st.markdown(t(lang, "bench_confusion"))
# Generate a hardcoded / synthetic graph for the demo page
fig, ax = plt.subplots()
# Simplified visual representation of a confusion matrix
metrics_data = {
    'Actual Authentic': [450, 20],
    'Actual Fake': [35, 495]
}
df_cm = pd.DataFrame(metrics_data, index=['Predicted Authentic', 'Predicted Fake'])

cax = ax.matshow(df_cm, cmap='Blues')
fig.colorbar(cax)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['Actual Authentic', 'Actual Fake'])
ax.set_yticklabels(['Pred. Authentic', 'Pred. Fake'])

for (i, j), z in np.ndenumerate(df_cm.values):
    ax.text(j, i, '{:0.0f}'.format(z), ha='center', va='center')

st.pyplot(fig)
