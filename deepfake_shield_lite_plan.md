# DeepFake Shield Lite: 10-Day Operational Plan

## 📌 Project Overview
- **Duration**: 10 days
- **Daily Capacity**: 5 hours
- **Team Size**: 1 person (Solo Developer/Competitor)
- **Tech Stack**: Python, Streamlit, PyTorch/TensorFlow (API wrapper), Librosa, SQLite/JSON
- **Final Goal**: A professional, demonstrable, competition-ready Deepfake Audio/Video Analyzer MVP.

## ⏱️ Daily Rhythm Recommendation (5 Hours)
To maximize output, split your 5 hours into a strict schedule every day:
- **0:00 - 0:30 (30 mins)**: **Planning & Setup** - Read the day's objective, open docs, plan the architecture.
- **0:30 - 3:00 (2.5 hrs)**: **Deep Work / Coding** - Uninterrupted implementation of the day's core functionality. Put your phone away.
- **3:00 - 4:00 (1 hr)**: **Integration & UI** - Wire the backend logic into the Streamlit frontend. Make it visible.
- **4:00 - 4:45 (45 mins)**: **Testing & Edge Cases** - Try to break it. Fix bugs. Add error handling.
- **4:45 - 5:00 (15 mins)**: **Commit & Cleanup** - Document progress, push to GitHub, and set up for tomorrow.

---

## 📅 Day-by-Day Implementation Roadmap

### **Day 1: Project Skeleton & Basic UI**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Establish the foundation, repository, and basic Streamlit multipage layout. |
| **Concrete Tasks** | 1. Initialize Git repository & virtual environment.<br>2. Install `streamlit`, `pandas`.<br>3. Create sidebar navigation for: Home, Analysis, History, Benchmark.<br>4. Implement a drag-and-drop file uploader for `.wav`, `.mp3`, `.mp4`. |
| **Concrete Output** | A running Streamlit app where users can navigate pages and upload a file. The file is saved to a local `/tmp_uploads` folder. |
| **Prioritization** | **Must**: Upload widget & routing. **Should**: Basic UI text/titles. **Could**: Custom CSS styling. |
| **Risk Flags** | File size limits for uploads in Streamlit. |
| **Fallback Strategy** | Restrict uploads to <20MB for MVP and display early warning text if the file is larger. |
| **Definition of Done** | `streamlit run app.py` launches a multi-page app with successful, error-free file uploading. |

### **Day 2: Audio Extraction & Processing Base**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Handle media formats cleanly; extract audio from video. |
| **Concrete Tasks** | 1. Install `moviepy` and `pydub`.<br>2. Write logic: IF file is `.mp4`, use `moviepy` to extract `.wav`.<br>3. Add an interactive audio playback widget (`st.audio`) in the UI. |
| **Concrete Output** | Regardless of whether the user uploads video or audio, a `.wav` file is produced on disk and can be played back via the UI. |
| **Prioritization** | **Must**: MP4 to WAV extraction. **Should**: Duration validation (cut to 60s max). **Could**: UI spinner during extraction. |
| **Risk Flags** | `ffmpeg` system dependencies causing crashes. |
| **Fallback Strategy** | Drop video support temporarily; force users to upload ONLY audio files via a strict file uploader constraint. |
| **Definition of Done** | Uploading a 10s `.mp4` results in a fully playable 10s audio widget rendering in the Streamlit app. |

### **Day 3: Visualizations (Waveform & Spectrogram)**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Make the app look "scientific" and advanced through rich visualization. |
| **Concrete Tasks** | 1. Install `librosa` and `matplotlib` (or `plotly`).<br>2. Write function to generate a Waveform plot.<br>3. Write function to generate a Mel-Spectrogram plot.<br>4. Render both in Streamlit side-by-side using `st.columns()`. |
| **Concrete Output** | Two professional-looking charts appearing immediately after file upload and extraction. |
| **Prioritization** | **Must**: Static Matplotlib spectrogram. **Should**: Plotly interactive charts. **Could**: Overlay playhead tracking. |
| **Risk Flags** | Generating spectrograms for large files taking >15 seconds. |
| **Fallback Strategy** | Only process and plot the first 10 seconds of the uploaded audio. |
| **Definition of Done** | Uploading an audio file displays an accurate waveform and spectrogram without breaking layout. |

### **Day 4: API Integration / Mock Engine**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Connect the ML detection core (via external API or mock). |
| **Concrete Tasks** | 1. Setup API keys (e.g., Hugging Face Inference API).<br>2. Build a Python request wrapper to send the `.wav` file.<br>3. Parse JSON response into a confidence score (0-100%).<br>4. Create a realistic "Mock API" toggle for testing while offline. |
| **Concrete Output** | A backend function that takes a filepath and returns a dictionary: `{"confidence_fake": 82.5, "processing_time_ms": 120}`. |
| **Prioritization** | **Must**: Working Python function returning a score. **Should**: Error handling for timeouts. **Could**: Webhooks/Async loading. |
| **Risk Flags** | Third-party API goes down, limits rate, or rejects format. |
| **Fallback Strategy** | Use the Mock Engine mode. Base the mock score on file metadata (e.g., if filename contains "fake", return 85%; else 12%) so the demo is predictable. |
| **Definition of Done** | The UI successfully simulates or performs a network call, displaying the raw JSON/score below the visualization. |

### **Day 5: Results Engine & UI Logic**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Translate numbers into human-readable actionable intelligence. |
| **Concrete Tasks** | 1. Build logic tree: <30% = Likely Authentic (Green), 30-70% = Suspicious (Yellow), >70% = Likely AI-Generated (Red).<br>2. Map specific Security Recommendations to each tier.<br>3. Build prominent, colored UI metric cards using `st.metric()` or custom HTML/CSS via `st.markdown(unsafe_allow_html=True)`. |
| **Concrete Output** | A colored dashboard banner showing the outcome, the exact score, and a bulleted list of next steps. |
| **Prioritization** | **Must**: 3-tier classification. **Should**: Custom colored Streamlit alerts (`st.warning`, `st.error`). **Could**: Downloadable PDF report. |
| **Risk Flags** | UI feeling bare or uninteresting. |
| **Fallback Strategy** | Heavy reliance on Streamlit native components (expander, alerts, metrics) to make it look clean without custom CSS. |
| **Definition of Done** | Uploading different files reliably triggers the correct Green/Yellow/Red UI state and distinct recommendations. |

### **Day 6: History & Database Pipeline**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Add persistence to prove it is a real application. |
| **Concrete Tasks** | 1. Implement a lightweight local database (SQLite via `sqlalchemy` or just a `history.json` file).<br>2. Save: Timestamp, Filename, Score, Final Label, Duration.<br>3. Populate the "History" page using `st.dataframe()`. |
| **Concrete Output** | A styled, sortable dataframe on the History tab that remembers sessions. |
| **Prioritization** | **Must**: JSON file storage + Dataframe display. **Should**: SQLite Implementation. **Could**: Delete/Clear History button. |
| **Risk Flags** | State persistence issues if Streamlit reloads aggressively. |
| **Fallback Strategy** | Use `st.session_state` to store history temporarily, informing judges it's purely an in-memory MVP limitation. |
| **Definition of Done** | Closing the browser and reopening it still shows the files evaluated 5 minutes ago on the History page. |

### **Day 7: Benchmarks & Evaluations Page**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Add technical credibility to the project. |
| **Concrete Tasks** | 1. Create a static dataset performance summary.<br>2. Add charts (ROC Curve, Confusion Matrix) using dummy or pre-computed data from a known dataset (e.g., ASVspoof 2021).<br>3. Explain the metrics (What is EER? What is F1?) using clean typography. |
| **Concrete Output** | A robustly documented page that explains *how good* the theoretical model is, aimed at technical judges. |
| **Prioritization** | **Must**: 3 key metrics displayed (Accuracy, EER, F1). **Should**: Interactive charts of the model's performance. **Could**: Live test against a known directory of 10 files. |
| **Risk Flags** | Spending too much time fighting plotting libraries. |
| **Fallback Strategy** | Render high-quality screenshots of charts generated in a Jupyter Notebook instead of coding them directly in Streamlit. |
| **Definition of Done** | Benchmark page is fully populated with charts and scientific explanations. |

### **Day 8: UI/UX Refinement & Polish**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Elevate the app from a "script" to a "product". |
| **Concrete Tasks** | 1. Add `st.spinner("Analyzing audio frequencies...")` during loads.<br>2. Implement `st.snow()` or `st.balloons()` for non-threat results.<br>3. Create a welcoming hero section on the Home page (App logo, description).<br>4. Add tooltips (`help="x"`) to all complex terms. |
| **Concrete Output** | A visually cohesive application with zero unhandled python errors visible to the user. |
| **Prioritization** | **Must**: Spinners and error handling. **Should**: Good margins and tooltips. **Could**: Custom Dark/Light mode toggles. |
| **Risk Flags** | Breaking core functionality while doing CSS hacks. |
| **Fallback Strategy** | Use Streamlit's `.streamlit/config.toml` to change primary colors safely without HTML injection. |
| **Definition of Done** | You can confidently navigate the app clicking randomly, and it handles everything gracefully. |

### **Day 9: Cloud Deployment Preparation**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Put the app on the internet. |
| **Concrete Tasks** | 1. Create a pristine `requirements.txt`.<br>2. Deploy via Streamlit Community Cloud (easiest) or Render/Heroku.<br>3. Configure any API Secrets securely in the cloud environment (do not hardcode). |
| **Concrete Output** | A public `https://deepfake-shield-lite.streamlit.app` link that works on mobile and desktop. |
| **Prioritization** | **Must**: Public web link. **Should**: Custom subdomain name. **Could**: Dockerfile for generic hosting. |
| **Risk Flags** | Deployment failures due to `moviepy`/`librosa` requiring system C-libraries like `libsndfile` or `ffmpeg`. |
| **Fallback Strategy** | Add a `packages.txt` for Debian dependencies (Streamlit Cloud supports this) OR abandon cloud deployment and screen-record a pristine local execution demo. |
| **Definition of Done** | App is accessible via the internet on a smartphone. |

### **Day 10: Demo Script, Sourcing & Rehearsal**
| Category | Details |
| :--- | :--- |
| **Daily Objective** | Construct a flawless narrative and rehearse the presentation. |
| **Concrete Tasks** | 1. Source 3 distinct test files (details below).<br>2. Write a step-by-step click script.<br>3. Screen record a backup video of the perfect demo (in case live demo fails).<br>4. Rehearse the 2-minute pitch out loud 5 times. |
| **Concrete Output** | A rehearsed pitch, an emergency backup MP4, and a folder of perfectly curated sample media. |
| **Definition of Done** | You can execute the demo in under 3 minutes while speaking clearly without referencing notes. |

---

## 🎬 Demo Scenario & Asset Sourcing (Day 10)

To blow away the judges, you need a smooth, engaging narrative. Do not use random files—curate a story.

### 🗂️ Sourcing Your Media Assets
You need exactly 3 files stored in a folder on your desktop named `Demo_Assets`:
1. **`authentic_speech.wav` (The Baseline)**
   - **Source**: Record yourself reading a paragraph on your phone's voice memo app.
   - **Why**: Proves the system doesn't just flag everything as fake.
2. **`obvious_fake_biden.mp4` (The Hook/Video Test)**
   - **Source**: Go to YouTube, search "AI Biden speech parody" or use [Civitai Audio](https://civitai.com/models) or TikTok. Use a free online YouTube-to-MP4 converter.
   - **Why**: Proves your tool can strip audio from a video and detect public-figure deepfakes.
3. **`sophisticated_scam.wav` (The Threat)**
   - **Source**: Create a free account on [ElevenLabs](https://elevenlabs.io/). Type: *"Hey mom, it's me. I lost my phone and I'm using a friend's. I urgently need you to Zelle me $500."* Generate audio using a normal sounding voice.
   - **Why**: Demonstrates real-world application protecting against financial scams targeting ordinary people.

### 🎤 The 3-Minute Demo Script

**[0:00-0:30] The Intro:**
> "Hi, I built DeepFake Shield Lite. AI voice cloning is now cheap and weaponized for scams and misinformation. I built a platform that allows anyone to immediately verify the authenticity of media. Let's look at a real-world scenario."

**[0:30-1:15] The Video Extraction Demo:**
> *(Upload `obvious_fake_biden.mp4`)*
> "Here is a video circulating online. My system immediately extracts the audio, generates a visual spectrogram to analyze frequency artifacts invisible to the human ear..."
> *(Point to the spectrogram/waveform loading)*
> "...and flags it as a *Likely AI-Generated* deepfake with 94% confidence, recommending we do not share the clip."

**[1:15-2:00] The Personal Scam Demo:**
> *(Upload `sophisticated_scam.wav`)*
> "But it's not just politicians. Scammers now clone family members' voices. If someone receives this voicemail—*(play 3 seconds of the audio)*—our system instantly analyzes it and flags it as Suspicious. We provide direct security recommendations: 'Establish a trusted family safe word and hang up.'"

**[2:00-2:30] The Wrap-up:**
> *(Click over to the History and Benchmark pages)*
> "All analyses are persisted in a local database for security audits. On the backend, we are benchmarking against the ASVspoof dataset with a 92% F1 score. DeepFake Shield Lite is fast, secure, and ready to scale. Thank you."

---

## 🚨 Golden Rules for the Solo Competitor
1. **Never build from scratch if an API exists**: You only have 5 hours a day. Use Hugging Face models (`speechbrain/fake-speech-detection` or similar) via their free API.
2. **Mocking is acceptable in MVPs**: If the Hugging Face API rate-limits you during the hackathon, *flip the switch to your Mock API*. Judges care about the architecture and the idea workflow more than a perfectly tuned zero-shot model you had 10 days to train.
3. **Always have a backup video**: On presentation day, APIs fail, WiFi drops, and dependencies break. Your Day 10 screen recording is your absolute insurance policy.
