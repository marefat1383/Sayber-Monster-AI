import streamlit as st
import os
from utils.media_processing import handle_upload, extract_audio_if_video
from utils.visualization import generate_visualizations, generate_image_visualizations
from utils.detection_api import predict_deepfake, get_security_recommendation_keys
from utils.database import save_scan
from utils.i18n import get_text as t, inject_rtl_if_needed

st.set_page_config(page_title="Analysis", page_icon="🔍", layout="wide")

lang = st.session_state.get('lang', 'en')
inject_rtl_if_needed(lang)

st.title(t(lang, "analysis_title"))
st.markdown(t(lang, "analysis_desc"))

uploaded_file = st.file_uploader(t(lang, "uploader_label"), type=["wav", "mp3", "mp4", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Handle Upload
    with st.spinner(t(lang, "processing_upload")):
        raw_path = handle_upload(uploaded_file)
        
    st.success(t(lang, "upload_success", uploaded_file.name))
    
    is_image = uploaded_file.name.lower().endswith(('.jpg', '.jpeg', '.png'))

    if is_image:
        st.image(raw_path)
        st.markdown(t(lang, "viz_title_image", t(lang, "viz_title")))
        with st.spinner(t(lang, "viz_generating_image", t(lang, "viz_generating"))):
            try:
                fig = generate_image_visualizations(raw_path)
                st.pyplot(fig)
            except Exception as e:
                st.warning(t(lang, "viz_fail", str(e)))
        target_path = raw_path
    else:
        # 2. Extract Audio
        with st.spinner(t(lang, "extracting_audio")):
            try:
                audio_path = extract_audio_if_video(raw_path)
                st.audio(audio_path)
            except Exception as e:
                st.error(str(e))
                st.stop()
                
        # 3. Visualization
        st.markdown(t(lang, "viz_title"))
        with st.spinner(t(lang, "viz_generating")):
            try:
                fig = generate_visualizations(audio_path)
                st.pyplot(fig)
            except Exception as e:
                st.warning(t(lang, "viz_fail", str(e)))
        target_path = audio_path
            
    # 4. Engine Analysis
    st.markdown(t(lang, "engine_title"))
    with st.spinner(t(lang, "engine_analyzing")):
        result = predict_deepfake(target_path, uploaded_file.name)
        
    score = result['confidence_fake']
    label_key = result['label_key']
    
    # Display String
    label_text = t(lang, label_key)
    
    # Save to history (saving English key for universal DB logic, but could save translated)
    save_scan(uploaded_file.name, score, label_text)
    
    # Display Result Cards
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if label_key == "Likely Authentic":
            st.success("✅ " + label_text)
        elif label_key == "Suspicious":
            st.warning("⚠️ " + label_text)
        else:
            st.error("🚨 " + label_text)
            
        st.metric(label=t(lang, "ai_prob_score"), value=f"{score}%")
        
    with col2:
        st.markdown(t(lang, "sec_rec_title"))
        recs_keys = get_security_recommendation_keys(label_key)
        for r_key in recs_keys:
            st.markdown(f"- {t(lang, r_key)}")
