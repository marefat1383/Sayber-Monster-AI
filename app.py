import streamlit as st
from utils.database import init_db
from utils.i18n import get_text as t, inject_rtl_if_needed

init_db()

st.set_page_config(
    page_title="DeepFake Shield Lite",
    page_icon="🛡️",
    layout="wide"
)

# Sidebar mapping
LANGUAGE_MAP = {
    "en": "English",
    "tr": "Türkçe",
    "fa": "فارسی",
    "zh": "中文"
}
REVERSE_MAP = {v: k for k, v in LANGUAGE_MAP.items()}

if 'lang' not in st.session_state:
    st.session_state['lang'] = 'en'

lang_choice = st.sidebar.selectbox(
    "Language / Dil / زبان / 语言", 
    options=list(LANGUAGE_MAP.values()), 
    index=list(LANGUAGE_MAP.keys()).index(st.session_state['lang'])
)

st.session_state['lang'] = REVERSE_MAP[lang_choice]
lang = st.session_state['lang']
inject_rtl_if_needed(lang)

st.title(t(lang, "app_title"))
st.markdown(f"### {t(lang, 'app_subtitle')}")

st.markdown(t(lang, "welcome_msg"))
st.info(t(lang, "mock_engine_note"))
