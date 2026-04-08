import streamlit as st
from utils.database import get_history
from utils.i18n import get_text as t, inject_rtl_if_needed

st.set_page_config(page_title="History", page_icon="📜", layout="wide")

lang = st.session_state.get('lang', 'en')
inject_rtl_if_needed(lang)

st.title(t(lang, "hist_title"))
st.markdown(t(lang, "hist_desc"))

df = get_history()

if df.empty:
    st.info(t(lang, "hist_empty"))
else:
    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=t(lang, "hist_dl_btn"),
        data=csv,
        file_name='deepfake_history.csv',
        mime='text/csv',
    )
