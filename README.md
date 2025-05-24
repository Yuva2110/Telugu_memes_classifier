# Multimodal Classification of Telugu Memes  

**Detecting Vulgarity and Ethical Concerns in Regional Social Media Content**  

## Overview

This project addresses the classification of Telugu memes into **Vulgar**, and **Normal** categories using **multimodal deep learning**. It leverages **both image and text information** from memes, focusing on ethical AI for **regional content moderation**.

> Telugu is spoken by over 80 million people, yet remains underrepresented in AI research, particularly in content moderation and hate speech detection.

---

## Problem Statement

Design and evaluate a **deep learning-based multimodal classification system** to accurately detect **vulgar**, and **benign** content in Telugu memes. The system addresses:

- Telugu-English code-mixed language
- Cultural and regional context
- Visual-textual alignment in memes

---

## Objectives

- **Dataset Creation:** Scrape and annotate over 2000 Telugu memes  
Dataset link: https://drive.google.com/drive/folders/1XU9-GYbYfYtPPbV-qyaKdz4qKrJGkCf_?usp=sharing
- **Text Analysis:** Use `mBERT` and `IndicBERT` for code-mixed and native Telugu
- **Image Analysis:** Use `EfficientNetB7`, `ResNet50`, and `ViT` for visual understanding
- **Multimodal Fusion:** Combine vision and text via `ViT + BERT` and `CLIP + BERT (LoRA)`
- **Evaluation:** Compare models across precision, accuracy, and recall

---

## Dataset

- Source: Social media platforms (Facebook, Twitter, Instagram)
- Annotations: Manually labeled as **Hate**, **Vulgar**, or **Normal**
- Preprocessing:
  - OCR with Google Vision API
  - GPT-based cleaning of extracted text
  - Language detection and tokenization

### Split:

| Split      | Count |
| ---------- | ----- |
| Train      | ~1400 |
| Validation | 300   |
| Test       | 300   |

---

## Models Used

### Text-Only:

- `mBERT`: Best for code-mixed and informal Telugu
- `IndicBERT`: Best for Unicode-rich, typed Telugu

### Vision-Only:

- `EfficientNetB7`: Compound scaling architecture
- `ResNet50`: Deep CNN with residual connections

### Multimodal:

- `ViT + BERT`: Late fusion model using CLS token concat + MLP
- `CLIP + LoRA + BERT`: Contrastive learning with lightweight fine-tuning

---

## Performance

| Model                | Accuracy  | Vulgar Precision | Normal Precision | Highlights                           |
| -------------------- | --------- | ---------------- | ---------------- | ------------------------------------ |
| `mBERT`              | 76.2%     | 0.75             | 0.79             | Handles text but misses image cues   |
| `IndicBERT`          | 78.1%     | 0.77             | 0.80             | Strong on native Telugu              |
| `EfficientNetB7`     | 85.0%     | 0.83             | 0.86             | Strong visual understanding          |
| `ViT + BERT`         | 87.3%     | 0.84             | 0.90             | Fusion boosts accuracy               |
| `CLIP + LoRA + BERT` | **89.7%** | **0.86**         | **0.92**         | Best performance, efficient training |

---

## 🔬 Model Architecture

- **Text pipeline:** Tokenized text ➝ BERT ➝ CLS ➝ Classifier  
- **Image pipeline:** Image ➝ ViT or CLIP ➝ CLS ➝ Classifier  
- **Fusion:** `[CLS_image; CLS_text]` ➝ MLP ➝ Softmax

---

## Training Setup

- Loss Function: Cross-Entropy
- Optimizer: AdamW
- Frameworks: PyTorch, Transformers (HuggingFace)
- Fine-tuning: LoRA for CLIP (low-rank adaptation)

---

## Key Takeaways

- Multimodal approaches outperform unimodal ones
- LoRA allows efficient adaptation of CLIP to Telugu memes
- Combining BERT + Vision features bridges the semantic gap
- Strong potential for real-world moderation tools

---

## Future Work

- Fairness: Bias reduction and ethical model evaluation
- Multilingual Expansion: Tamil, Hindi, Kannada meme classification
- Deployment: Browser plugin or moderation bot
- Humor/Sarcasm Detection: Sentiment fusion module
- Unified Text Model: Combine IndicBERT and mBERT

---

## References

Key sources include:

- [CLIP: Radford et al., 2021]
- [mBERT & IndicBERT: Google & AI4Bharat]
- [ViT: Dosovitskiy et al., 2021]
- [Kiela et al., Hateful Memes Challenge, 2020]
- [Davidson et al., 2017 - Hate Speech on Twitter]

---

## Model Architecture

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
           Output: Vulgar / Normal
```

## Author

**Irigi Yuva Kumar**  
M.Tech, CSE Department  
NITK Surathkal  
Project Guide: Prof. (Dr.) P. Santhi Thilagam  

---

## License

This project is released under the [MIT License](LICENSE).
