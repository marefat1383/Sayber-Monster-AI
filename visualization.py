import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
from PIL import Image
def generate_visualizations(audio_path: str):
    """
    Generates a matplotlib figure containing the Waveform and Mel-Spectrogram.
    Returns the matplotlib figure.
    """
    # Load audio (first 30 seconds only to save time)
    y, sr = librosa.load(audio_path, duration=30.0)
    
    fig, ax = plt.subplots(nrows=2, figsize=(10, 6), gridspec_kw={'height_ratios': [1, 2]})
    
    # 1. Waveform
    librosa.display.waveshow(y, sr=sr, ax=ax[0], alpha=0.6, color='blue')
    ax[0].set_title('Audio Waveform', color='black')
    ax[0].set_ylabel('Amplitude')
    
    # 2. Mel-Spectrogram
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', ax=ax[1], cmap='magma')
    ax[1].set_title('Mel-frequency spectrogram', color='black')
    fig.colorbar(img, ax=ax[1], format="%+2.0f dB")
    
    plt.tight_layout()
    return fig

def generate_image_visualizations(image_path: str):
    """
    Generates a matplotlib figure containing mock noise and channel analysis for images.
    Returns the matplotlib figure.
    """
    img = Image.open(image_path).convert('RGB')
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    
    # 1. Original Image Resized
    ax[0].imshow(img)
    ax[0].set_title('Original Media', color='black')
    ax[0].axis('off')
    
    # 2. Mock Error Level Analysis (Noise Space)
    img_array = np.array(img)
    noise = np.random.normal(scale=10.0, size=img_array.shape).astype(np.uint8)
    mock_ela = np.clip(img_array - noise, 0, 255)
    
    ax[1].imshow(mock_ela)
    ax[1].set_title('Mock Error Level Analysis', color='black')
    ax[1].axis('off')
    
    plt.tight_layout()
    return fig
