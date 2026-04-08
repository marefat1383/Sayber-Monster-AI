import streamlit as st

TRANSLATIONS = {
    "en": {
        "app_title": "🛡️ DeepFake Shield Lite",
        "app_subtitle": "Professional Deepfake Audio & Video Analyzer",
        "welcome_msg": "Welcome to **DeepFake Shield Lite**, an offline-ready MVP designed to detect AI-generated and manipulated media rapidly.\n\n#### What does this app do?\n* **Audio & Video Support**: Upload `.wav`, `.mp3`, or `.mp4` files. Our engine automatically extracts and processes the audio track.\n* **Instant Spectrogram Analysis**: Visualizes audio signals using `librosa` to hunt for synthetic frequency artifacts.\n* **Mock Risk Detection**: Scores the authenticity of the media and provides actionable security recommendations.\n* **Local Auditing**: All analysis runs are persistently saved to a local database for review.\n\n**⬅️ Select 'Analysis' from the sidebar to begin.**",
        "mock_engine_note": "Note: This MVP uses a deterministic Mock AI engine for reliable offline demonstrations.",
        "analysis_title": "🔍 Analyze Media",
        "analysis_desc": "Upload a file below to run the DeepFake Shield extraction and detection engine.",
        "uploader_label": "Choose an audio, video, or image file",
        "viz_title_image": "### 🖼️ Image Analysis Visualizations",
        "viz_generating_image": "Generating Noise Space and Channel Analysis...",
        "processing_upload": "Processing file upload...",
        "upload_success": "File '{0}' uploaded successfully!",
        "extracting_audio": "Extracting audio format (if necessary)...",
        "viz_title": "### 📊 Audio Analysis Visualizations",
        "viz_generating": "Generating spectrogram and waveform...",
        "viz_fail": "Could not generate advanced visualizations: {0}",
        "engine_title": "### 🤖 Detection Engine Results",
        "engine_analyzing": "Analyzing artifacts with Mock Engine...",
        "ai_prob_score": "AI Probability Score",
        "sec_rec_title": "#### Security Recommendations",
        
        "hist_title": "📜 Scan History",
        "hist_desc": "View a persistent log of dynamically evaluated media.",
        "hist_empty": "No recorded scans yet. Upload a file in the Analysis tab!",
        "hist_dl_btn": "Download Audit Log as CSV",
        
        "bench_title": "📈 Model Performance & Benchmarks",
        "bench_desc": "In an MVP, it's critical to provide transparency on the underlying theoretical model's capabilities. These metrics represent performance on standard datasets like **ASVspoof 2021**.",
        "bench_acc": "Overall Accuracy",
        "bench_eer": "Equal Error Rate (EER)",
        "bench_f1": "F1 Score",
        "bench_metrics_explained": "### Key Evaluation Metrics Explained\n- **Equal Error Rate (EER)**: The threshold where the False Acceptance Rate (FAR) and False Rejection Rate (FRR) are equal. A lower EER indicates a better, more robust system.\n- **Accuracy**: The overall percentage of correctly classified genuine and synthetic audio clips.\n- **F1 Score**: The harmonic mean of precision and recall. Critical for deeply unbalanced datasets where synthetic clips might outnumber genuine ones.",
        "bench_confusion": "### Simulated Confusion Matrix",
        
        # Labels and Recs
        "Likely Authentic": "Likely Authentic",
        "Suspicious": "Suspicious",
        "Likely AI-Generated": "Likely AI-Generated",
        "rec_auth_1": "Media appears natural.",
        "rec_auth_2": "No immediate threat detected.",
        "rec_auth_3": "Standard verification processes apply.",
        "rec_susp_1": "Audio contains possible synthetic artifacts.",
        "rec_susp_2": "Verify the source of the media.",
        "rec_susp_3": "Do not authorize financial transactions based on this audio alone.",
        "rec_fake_1": "High probability of AI generation detected.",
        "rec_fake_2": "Establish a trusted family safe word and hang up.",
        "rec_fake_3": "Do not share this media publicly.",
        "rec_fake_4": "Block the sender if received from an unknown number."
    },
    "tr": {
        "app_title": "🛡️ DeepFake Kalkanı Lite",
        "app_subtitle": "Profesyonel Deepfake Ses ve Video Analizörü",
        "welcome_msg": "Yapay zeka ile üretilmiş medyaları tespit etmek için tasarlanmış **DeepFake Kalkanı Lite** MVP'sine hoş geldiniz.\n\n#### Bu uygulama ne yapar?\n* **Ses ve Video Desteği**: `.wav`, `.mp3` veya `.mp4` dosyaları yükleyin. Motorumuz ses parçasını otomatik olarak çıkarır ve işler.\n* **Anında Spektrogram Analizi**: Sentetik frekans kalıntılarını avlamak için ses sinyallerini görselleştirir.\n* **Sahte Risk Tespiti**: Medyanın gerçekliğini puanlar ve güvenlik önerileri sunar.\n* **Yerel Denetim**: Tüm analiz çalışmaları incelenmek üzere yerel bir veritabanına kalıcı olarak kaydedilir.\n\n**⬅️ Başlamak için kenar çubuğundan 'Analysis' (Analiz) seçeneğini seçin.**",
        "mock_engine_note": "Not: Bu MVP, çevrimdışı demolar için deterministik bir Sahte Yapay Zeka motoru kullanır.",
        "analysis_title": "🔍 Medya Analizi",
        "analysis_desc": "Derin Sahte Kalkanı'nı çalıştırmak için aşağıya bir dosya yükleyin.",
        "uploader_label": "Bir ses, video veya görüntü dosyası seçin",
        "viz_title_image": "### 🖼️ Görüntü Analizi Görselleştirmeleri",
        "viz_generating_image": "Gürültü Uzayı ve Kanal Analizi Oluşturuluyor...",
        "processing_upload": "Dosya yükleme işleniyor...",
        "upload_success": "'{0}' dosyası başarıyla yüklendi!",
        "extracting_audio": "Ses formatı çıkarılıyor (gerekirse)...",
        "viz_title": "### 📊 Ses Analizi Görselleştirmeleri",
        "viz_generating": "Spektrogram ve dalga formu oluşturuluyor...",
        "viz_fail": "Gelişmiş görselleştirmeler oluşturulamadı: {0}",
        "engine_title": "### 🤖 Tespit Motoru Sonuçları",
        "engine_analyzing": "Yapay Zeka Motoru ile analiz ediliyor...",
        "ai_prob_score": "Yapay Zeka Olasılık Puanı",
        "sec_rec_title": "#### Güvenlik Önerileri",
        
        "hist_title": "📜 Tarama Geçmişi",
        "hist_desc": "Dinamik olarak değerlendirilen medyanın kalıcı günlüğünü görüntüleyin.",
        "hist_empty": "Henüz kaydedilmiş tarama yok. Analiz sekmesinde bir dosya yükleyin!",
        "hist_dl_btn": "Günlüğü CSV Olarak İndir",
        
        "bench_title": "📈 Model Performansı ve Metrikler",
        "bench_desc": "Bu metrikler **ASVspoof 2021** gibi standart veri kümelerindeki performansı temsil eder.",
        "bench_acc": "Genel Doğruluk",
        "bench_eer": "Eşit Hata Oranı (EER)",
        "bench_f1": "F1 Skoru",
        "bench_metrics_explained": "### Temel Değerlendirme Metrikleri Açıklandı\n- **Eşit Hata Oranı (EER)**: Daha düşük EER daha sağlam bir sistem sağlar.\n- **Doğruluk**: Doğru sınıflandırılmış kliplerin genel yüzdesi.\n- **F1 Skoru**: Hassasiyet ve geri çağırmanın harmonik ortalaması.",
        "bench_confusion": "### Simüle Edilmiş Karışıklık Matrisi",
        
        "Likely Authentic": "Büyük İhtimalle Gerçek",
        "Suspicious": "Şüpheli",
        "Likely AI-Generated": "Yapay Zeka Üretimi",
        "rec_auth_1": "Medya doğal görünüyor.",
        "rec_auth_2": "Acil bir tehdit tespit edilmedi.",
        "rec_auth_3": "Standart doğrulama süreci geçerlidir.",
        "rec_susp_1": "Ses olası sentetik kalıntılar içeriyor.",
        "rec_susp_2": "Medyanın kaynağını doğrulayın.",
        "rec_susp_3": "Yalnızca sese dayanarak finansal işlem yapmayın.",
        "rec_fake_1": "Yüksek ihtimalle AI tespiti yapıldı.",
        "rec_fake_2": "Güvenilir bir aile iletişim şifresi belirleyin.",
        "rec_fake_3": "Bu medyayı herkese açık olarak paylaşmayın.",
        "rec_fake_4": "Gerekirse numarayı engelleyin."
    },
    "fa": {
        "app_title": "🛡️ سپر فیک لایت",
        "app_subtitle": "تحلیلگر حرفه‌ای فایل‌های صوتی و ویدیویی",
        "welcome_msg": "به **سپر فیک لایت** خوش آمدید. ابزاری برای بررسی سریع رسانه‌های تولید شده توسط هوش مصنوعی.\n\n#### این برنامه چه می‌کند؟\n* **پشتیبانی صوتی و تصویری**: فایل‌های `.wav`, `.mp3` یا `.mp4` را آپلود کنید...\n* **تحلیل فوری اسپکتروگرام**: فرکانس‌های صوتی را بررسی می‌کند.\n* **تشخیص ریسک آزمایشی**: اعتبار رسانه را ارزیابی کرده و توصیه‌های امنیتی ارائه می‌دهد.\n* **ذخیره محلی**: تمام بررسی‌ها به‌طور ماندگار ذخیره می‌شوند.\n\n**⬅️ برای شروع، از منوی کناری 'تحلیل' را انتخاب کنید.**",
        "mock_engine_note": "توجه: این نسخه برای دموی آفلاین از موتور شبیه‌ساز AI استفاده می‌کند.",
        "analysis_title": "🔍 تحلیل رسانه",
        "analysis_desc": "فایلی را برای اجرای موتور دیپ‌فیک آپلود کنید.",
        "uploader_label": "یک فایل صوتی، تصویری یا عکس انتخاب کنید",
        "viz_title_image": "### 🖼️ تجسم تحلیل تصویر",
        "viz_generating_image": "در حال تولید فضای نویز و تحلیل کانال...",
        "processing_upload": "در حال پردازش...",
        "upload_success": "فایل '{0}' آپلود شد!",
        "extracting_audio": "در حال استخراج صوت...",
        "viz_title": "### 📊 تجسم تحلیل صوتی",
        "viz_generating": "در حال تولید طیف‌سنج و شکل موج...",
        "viz_fail": "طیف سنج ایجاد نشد: {0}",
        "engine_title": "### 🤖 نتایج تشخیص",
        "engine_analyzing": "در حال تحلیل اثرات AI...",
        "ai_prob_score": "احتمال هوش مصنوعی",
        "sec_rec_title": "#### توصیه‌های امنیتی",
        
        "hist_title": "📜 تاریخچه اسکن",
        "hist_desc": "گزارش رسانه‌های ارزیابی شده را مشاهده کنید.",
        "hist_empty": "سجل خالی است. فایلی آپلود کنید!",
        "hist_dl_btn": "دانلود گزارش CSV",
        
        "bench_title": "📈 عملکرد مدل",
        "bench_desc": "این معیارها عملکرد روی دیتاست‌های стандард مانند **ASVspoof 2021** را نشان می‌دهند.",
        "bench_acc": "دقت کلی",
        "bench_eer": "نرخ خطای برابر (EER)",
        "bench_f1": "امتیاز F1",
        "bench_metrics_explained": "### توضیح معیارها\n- **نرخ خطای برابر (EER)**: آستانه‌ای که در آن نرخ اشتباه برابر است.\n- **دقت (Accuracy)**: درصد کلیپ‌های صوتی که به درستی دسته‌بندی شده‌اند.\n- **امتیاز F1**: میانگین هارمونیک دقت.",
        "bench_confusion": "### ماتریس سردرگمی",
        
        "Likely Authentic": "احتمالاً واقعی",
        "Suspicious": "مشکوک",
        "Likely AI-Generated": "ساخته شده با AI",
        "rec_auth_1": "رسانه طبیعی به نظر می‌رسد.",
        "rec_auth_2": "تهدید فوری یافت نشد.",
        "rec_auth_3": "تایید هویت معمول کافی است.",
        "rec_susp_1": "صدا شامل دستکاری است.",
        "rec_susp_2": "منبع را تایید کنید.",
        "rec_susp_3": "تراکنش مالی را تأیید نکنید.",
        "rec_fake_1": "رسانه توسط هوش مصنوعی ساخته شده.",
        "rec_fake_2": "تلفن را قطع کنید.",
        "rec_fake_3": "این رسانه را منتشر نکنید.",
        "rec_fake_4": "فرستنده را مسدود کنید."
    },
    "zh": {
        "app_title": "🛡️ 伪造检测盾 Lite",
        "app_subtitle": "深度伪造音视频分析仪",
        "welcome_msg": "欢迎使用 **DeepFake Shield Lite**，这是一款快速检测AI生成媒体的离线MVP。\n\n#### 本应用功能说明\n* **音视频支持**：上传 `.wav`、`.mp3` 或 `.mp4` 文件以自动提取并处理音频序列。\n* **即时频谱仪**：可视化音频信号以定位合成频率异常。\n* **检测反馈**：为您的媒体文件评分并提供安全提示。\n* **本地审计**：所有扫描动作都会保留在本地以供审计。\n\n**⬅️ 请在左侧选择 'Analysis'（分析功能）开始。**",
        "mock_engine_note": "注：本系统因本地演示原因，正使用离线AI模拟引擎。",
        "analysis_title": "🔍 媒体分析",
        "analysis_desc": "在下方拖拽文件以侦测AI内容。",
        "uploader_label": "请选择音频、视频或图像",
        "viz_title_image": "### 🖼️ 图像分析可视化",
        "viz_generating_image": "提取噪声特征图...",
        "processing_upload": "正在读取文件...",
        "upload_success": "文件 '{0}' 已成功上传！",
        "extracting_audio": "正在提取音频轨道...",
        "viz_title": "### 📊 分析可视化",
        "viz_generating": "渲染声纹...请稍后",
        "viz_fail": "无法生成视图：{0}",
        "engine_title": "### 🤖 AI检测结果",
        "engine_analyzing": "模型判定中...",
        "ai_prob_score": "AI伪造概率",
        "sec_rec_title": "#### 应对建议",
        
        "hist_title": "📜 扫描历史记录",
        "hist_desc": "在此处检索您验证过的目标。",
        "hist_empty": "您的记录尚为空，请先前往分析功能上传。",
        "hist_dl_btn": "导出审计志 (.csv)",
        
        "bench_title": "📈 模型基准测试数据",
        "bench_desc": "这证明了检测引擎在公开标准数据集 **ASVspoof 2021** 中的强大表现。",
        "bench_acc": "综合准确度",
        "bench_eer": "等错误率 (EER)",
        "bench_f1": "F1 综合分数",
        "bench_metrics_explained": "### 参数释意\n- **等错误率 (EER)**：指系统接收错误与拒绝错误相同时候的阈值。越低表现越稳定。\n- **综合准确度**：正确分类真实与伪造数据点的比例。\n- **F1 综合分数**：精准率和召回率结合的参考标准。",
        "bench_confusion": "### 模拟混淆矩阵",
        
        "Likely Authentic": "极可能为真实内容",
        "Suspicious": "可疑片段",
        "Likely AI-Generated": "AI生成伪造",
        "rec_auth_1": "信号呈现自然排列。",
        "rec_auth_2": "暂未检测出威胁行为。",
        "rec_auth_3": "正常信任即可。",
        "rec_susp_1": "出现断续可疑频段。",
        "rec_susp_2": "谨慎核对发件方身份。",
        "rec_susp_3": "切勿立即进行金钱交易操作。",
        "rec_fake_1": "强烈检测出被AI修改特征。",
        "rec_fake_2": "务必直接使用暗号核对并立即挂断。",
        "rec_fake_3": "禁止随意转发以此引发误解。",
        "rec_fake_4": "如防诈骗，请立刻拉黑未知号码。"
    }
}

def get_text(lang, key, *args):
    text = TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)
    if args:
        return text.format(*args)
    return text

def inject_rtl_if_needed(lang):
    if lang == "fa":
        st.markdown(
            """
            <style>
            body, .stApp {
                direction: rtl;
                text-align: right;
            }
            .stMarkdown, .stText, h1, h2, h3, h4, h5, h6, label, .stMetric, .stDataFrame {
                direction: rtl;
                text-align: right;
                font-family: inherit;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
