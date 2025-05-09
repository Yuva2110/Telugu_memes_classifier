# 🧠 Multimodal Telugu Meme Classification

This project classifies Telugu memes as **Hate** or **Non-Hate** using a multimodal deep learning model that combines image and text understanding.

## 🔍 Overview

- **Vision Model:** CLIP (openai/clip-vit-base-patch32)
- **Text Model:** BERT (bert-base-multilingual-cased)
- **Fusion Strategy:** Concatenation of image + text embeddings followed by a linear classifier.
- **Input:** Telugu memes with image, text, and label (0: Non-Hate, 1: Hate)
- **Output:** Meme classification result with detailed evaluation metrics.

---

## 📁 Dataset Format

Your dataset must be in a JSON file (`final_data.json`) with the following structure:

```json
[
  {
    "img": "path/to/image1.jpg",
    "text": "some telugu or english text",
    "label": 1
  },
  ...
]
```

- `img`: Local path to image file
- `text`: Caption or meme text (in Telugu/English)
- `label`: 0 (Non-Hate), 1 (Hate)

---

## 🚀 Setup Instructions

### 1. Mount Google Drive

Ensure your dataset is in Google Drive (e.g., `/MyDrive/Dataset/final_data.json`).

### 2. Install Required Libraries

All dependencies are automatically installed in the notebook:

```python
!pip install transformers timm torchvision torch indic-nlp-library langdetect
```

---

##  How to Run

1. **Open the notebook in Google Colab.**

2. **Mount your Google Drive.**

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Set path to your dataset:**

   ```python
   data_path = "/content/drive/MyDrive/Dataset/final_data.json"
   ```

4. **Run all cells sequentially:**

   - Load and split dataset
   - Create Dataloaders
   - Build and train multimodal model
   - Validate and test model
   - View plots and confusion matrix

---

## Outputs

- Train/Validation Loss and Accuracy plots
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- Test Accuracy: 81.1%

---

## 🧠 Model Architecture

```text
   ┌────────────┐       ┌────────────────────┐
   │  Image     │       │ Text (Telugu/Eng)  │
   └────┬───────┘       └─────────┬──────────┘
        │                         │
   [CLIP Image Tower]     [Multilingual BERT]
        │                         │
        └────────────┬────────────┘
                     ▼
            Concatenated Embeddings
                     │
              Linear Classifier
                     ▼
           Output: Hate / Non-Hate
```

---

## 🧪 Evaluation

- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix (visual)

---

## Notes

- Ensure images in the JSON file are accessible in Colab.
- Works best with at least 1000 samples per class.
- Multilingual BERT handles Telugu-English mix well.

---

## Future Work

- Use a fusion transformer instead of simple concatenation
- Add attention between image and text
- Support other Indian languages
