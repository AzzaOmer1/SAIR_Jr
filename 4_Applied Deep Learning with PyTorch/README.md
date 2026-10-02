
# ⚡ Module 4: Applied Deep Learning with PyTorch

**From PyTorch Fundamentals to Production Deep Learning Systems**

> 📌 **Part of the [SAIR Jr. ML Engineering Track](../README.md)** — bottom-up, depth-first. We build the foundation that lasts years, not the framework of the month.

**📍 Location:** `4_Applied Deep Learning with PyTorch/`  
**🎯 Prerequisite:** [Module 3: Neural Networks from Scratch](../3_Neural%20Network%20from%20scratch/README.md)  
**➡️ Next Module:** [Module 5: GPT from Scratch](../5_GPT%20from%20scratch/README.md)

Welcome to **Module 4** of **SAIR** — your comprehensive journey into applied deep learning with PyTorch. This module bridges theory and practice, taking you from tensor operations all the way to modern architectures, with stops along the way for CNNs, YOLOv8, RNNs, LSTMs, and HuggingFace transformers.

---

## 🎯 Is This Module For You?

### ✅ **Complete this module if:**
- You've built neural networks from scratch and want to use production frameworks
- You're ready to work with real datasets, pretrained models, and modern architectures
- You want hands-on experience with computer vision, NLP, and transformers
- You're preparing for ML engineering roles that require PyTorch fluency

### 🚀 **Review and continue if you're experienced:**
- You've used PyTorch but want deeper coverage of CNNs, RNNs, and transformers
- You've trained models but want to master transfer learning and fine-tuning
- You want to add YOLOv8, HuggingFace, and model deployment to your toolkit

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![UV](https://img.shields.io/badge/UV-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

</div>

---

## 📚 Module Contents

### **1 — PyTorch Fundamentals**
📁 `1_PyTorch Fundemntals/`

| Notebook | Focus | Time |
|----------|-------|------|
| `1_Intro.ipynb` | Tensors, autograd, model building, training loops | 5–6 hrs |
| `2_DataLoader.ipynb` | Dataset classes, DataLoader optimization, performance | 4–5 hrs |
| `labs/lab_1.ipynb` | Tensors & autograd practice | 2–3 hrs |
| `labs/lab_2.ipynb` | Custom Dataset & DataLoader | 2–3 hrs |

---

### **2 — Computer Vision & CNNs**
📁 `2_Vision and CNN/`

| Notebook | Focus | Time |
|----------|-------|------|
| `3_CNN.ipynb` | Convolutional Neural Networks from scratch | 6–7 hrs |
| `4_Transfer_and_ResNet.ipynb` | Transfer learning, ResNet, pretrained models | 5–6 hrs |
| `5A_YOLO.ipynb` | YOLOv8 object detection | 4–5 hrs |
| `5B_Segment_Pose.ipynb` | Instance segmentation and pose estimation | 3–4 hrs |
| `5C_ViTs_and_Deploy.ipynb` | Vision Transformers and model deployment | 4–5 hrs |
| `labs/lab_3.ipynb` | CNN architecture practice | 2–3 hrs |
| `labs/lab_4.ipynb` | Transfer learning practice | 2–3 hrs |

**Production Demos** — `2_Vision and CNN/Demos/`

| Demo | Description |
|------|-------------|
| `demo_01_live_detection.py` | Real-time object detection with webcam |
| `demo_02_background_removal.py` | Background removal via segmentation |
| `demo_03_pose_estimation.py` | Human pose estimation in real-time |
| `demo_04_gesture_control.py` | Control applications with hand gestures |
| `demo_05_model_comparison.py` | Compare YOLOv8n/s/m performance |
| `demo_06_batch_processing.py` | Process multiple images efficiently |
| `demo_07_video_processing.py` | Object detection on video files |

```bash
cd '2_Vision and CNN/Demos'
uv pip install -r requirements.txt
uv run python run_demos.py
```

Pre-trained models in `2_Vision and CNN/`:
`yolov8n.pt` · `yolov8n-seg.pt` · `yolov8n-pose.pt` · `yolov8n.onnx`
`best_x.pt` · `best_yolo26n_100.pt` · `best_yolo26m_100.pt` · `yassir_best.pt`

---

### **3 — Sequence Modeling & NLP**
📁 `3_Sequence and NLP/`

| Notebook | Focus | Time |
|----------|-------|------|
| `6_Intro_to_Seq.ipynb` | RNNs, LSTMs, sequence modeling fundamentals | 5–6 hrs |
| `7_Seq_to_Seq.ipynb` | Sequence-to-sequence architectures | 4–5 hrs |
| `8A_HuggingFace_Ecosystem.ipynb` | Pipelines, tokenizers, models, datasets | 4–5 hrs |
| `8B_Hugging_Face_Finetuning.ipynb` | Fine-tuning pretrained transformers end to end | 5–6 hrs |

Saved models: `best_rnnclassifier.pt`, `best_lstmclassifier.pt`

Training data: `harry_potter_txt/` — books used for sequence modeling experiments

**Text Classification Pipeline** — `3_Sequence and NLP/Text Classification/`

A production-style NLP project demonstrating five approaches to text classification on the same dataset:

| Notebook | Approach |
|----------|----------|
| `notebooks/01_eda.ipynb` | Exploratory data analysis |
| `notebooks/02_feature_extraction.ipynb` | TF-IDF and classical ML features |
| `notebooks/03_embedding.ipynb` | Sentence embeddings pipeline |
| `notebooks/04_finetune.ipynb` | Full transformer fine-tuning |
| `notebooks/05_prompt.ipynb` | Zero-shot and prompt-based classification |

Fully modular — `src/` contains separate modules for data, training, evaluation, and inference.
Orchestrated by `run_pipeline.py`. Deployable app at `app/app.py`.

```bash
cd '3_Sequence and NLP/Text Classification'
uv pip install -r requirements.txt
uv run python run_pipeline.py
```

---

### **4 — Classification Hub**
📁 `Classification Hub/`

Five open-ended project notebooks — one per data modality.
**No steps. No guided cells.** A problem, a dataset, and a blank notebook.

| Project | Modality | Task |
|---------|----------|------|
| `Ex_1_Tabular_Classification.ipynb` | 📊 Tabular | Rice type classifier from grain measurements |
| `Ex_2_Image_Classification.ipynb` | 🖼️ Image (scratch) | Animal face classifier with a custom CNN |
| `Ex_3_Image_Classification_Pretrained.ipynb` | 🌿 Image (pretrained) | Bean leaf disease detector via transfer learning |
| `Ex_4_Audio_Classification.ipynb` | 🎵 Audio | Quran reciter identifier |
| `Ex_5_Text_Classification_Transformers.ipynb` | 📝 Text | Sarcasm detector with a fine-tuned transformer |

See `Classification Hub/README.md` for what each submission must include.

---

## 🗺️ Learning Pathway

### **Phase 1: Foundations** (Week 1–2)
1. `1_PyTorch Fundemntals/1_Intro.ipynb` — Tensors and autograd
2. Complete `labs/lab_1.ipynb`
3. `1_PyTorch Fundemntals/2_DataLoader.ipynb` — Data pipelines
4. Complete `labs/lab_2.ipynb`

### **Phase 2: Computer Vision** (Week 3–4)
1. `2_Vision and CNN/3_CNN.ipynb` — Build CNNs from scratch
2. Complete `labs/lab_3.ipynb`
3. `2_Vision and CNN/4_Transfer_and_ResNet.ipynb` — Transfer learning
4. Complete `labs/lab_4.ipynb`
5. `5A_YOLO.ipynb` → `5B_Segment_Pose.ipynb` → `5C_ViTs_and_Deploy.ipynb`
6. Run the Demos in `2_Vision and CNN/Demos/`

### **Phase 3: Sequence Modeling & NLP** (Week 5–6)
1. `3_Sequence and NLP/6_Intro_to_Seq.ipynb` — RNNs and LSTMs
2. `3_Sequence and NLP/7_Seq_to_Seq.ipynb` — Sequence-to-sequence
3. `3_Sequence and NLP/8A_HuggingFace_Ecosystem.ipynb` — The HuggingFace stack
4. `3_Sequence and NLP/8B_Hugging_Face_Finetuning.ipynb` — Fine-tuning
5. Explore the Text Classification production pipeline

### **Phase 4: Classification Hub** (Ongoing)
Work through all five projects independently. No guidance — just the problem brief and the dataset.

### **Phase 5: GPT from Scratch** → Module 5
Continue to `5_GPT from scratch/` — a standalone module dedicated to building a GPT-style language model end to end.

---

## 💡 Our Learning Philosophy

> **"Understand the tool, then use the tool at scale."**

After building neural networks from scratch in Module 3, this module teaches you to work with the **production frameworks** that industry uses every day. The point isn't to abandon fundamentals — it's to **layer framework fluency on top of the deep understanding you already have.**

**This is where you transition from framework user to ML engineer shipping real systems.**

---

## 🚀 Quick Start Guide

### **For Sequential Learners (Recommended):**
```bash
# 1. Start with PyTorch fundamentals
uv run jupyter notebook "1_PyTorch Fundemntals/1_Intro.ipynb"

# 2. Work through vision and CNNs
uv run jupyter notebook "2_Vision and CNN/3_CNN.ipynb"

# 3. Progress to sequence modeling
uv run jupyter notebook "3_Sequence and NLP/6_Intro_to_Seq.ipynb"

# 4. Finish with Classification Hub
uv run jupyter notebook "Classification Hub/Ex_1_Tabular_Classification.ipynb"
```

### **For Project-Focused Learners:**
```bash
# Start with Classification Hub to see the target
uv run jupyter notebook "Classification Hub/Ex_1_Tabular_Classification.ipynb"

# Refer back to lectures as needed for specific techniques
```

### **Run the Production Pipelines:**
```bash
# YOLOv8 demos
cd "2_Vision and CNN/Demos"
uv run python run_demos.py

# Text classification pipeline
cd "../../3_Sequence and NLP/Text Classification"
uv run python run_pipeline.py
```

> 💡 **First time here?** Run `uv sync` from the SAIR root first to install dependencies.

---

## 🎯 Learning Outcomes

After completing this module, you will be able to:

- **Build** neural networks from scratch using PyTorch
- **Design** efficient data pipelines with custom Datasets and DataLoaders
- **Train** CNNs for image classification
- **Deploy** YOLOv8 for detection, segmentation, and pose estimation
- **Build** sequence models with RNNs and LSTMs
- **Use** the HuggingFace ecosystem end to end
- **Fine-tune** pretrained transformers for downstream tasks
- **Apply** your skills independently across all five major data modalities

---

## 📂 Directory Structure

```
4_Applied Deep Learning with PyTorch/
│
├── 1_PyTorch Fundemntals/
│   ├── 1_Intro.ipynb
│   ├── 2_DataLoader.ipynb
│   └── labs/
│       ├── lab_1.ipynb
│       └── lab_2.ipynb
│
├── 2_Vision and CNN/
│   ├── 3_CNN.ipynb
│   ├── 4_Transfer_and_ResNet.ipynb
│   ├── 5A_YOLO.ipynb
│   ├── 5B_Segment_Pose.ipynb
│   ├── 5C_ViTs_and_Deploy.ipynb
│   ├── assets/
│   ├── data/                         # FashionMNIST, MNIST
│   ├── datasets/coco128/             # COCO128 dataset
│   ├── generated/                    # Notebook-generated outputs
│   ├── models/                       # Saved models
│   ├── labs/
│   │   ├── lab_3.ipynb
│   │   └── lab_4.ipynb
│   ├── Demos/                        # 7 production demos
│   │   ├── demo_01_live_detection.py
│   │   ├── demo_02_background_removal.py
│   │   ├── demo_03_pose_estimation.py
│   │   ├── demo_04_gesture_control.py
│   │   ├── demo_05_model_comparison.py
│   │   ├── demo_06_batch_processing.py
│   │   ├── demo_07_video_processing.py
│   │   ├── run_demos.py
│   │   ├── requirements.txt
│   │   └── README_DEMOS.md
│   ├── download_weights.py
│   ├── street.jpg
│   ├── coco128.yaml
│   ├── yolov8n.pt
│   ├── yolov8n-seg.pt
│   ├── yolov8n-pose.pt
│   ├── yolov8n.onnx
│   └── best_*.pt                     # Fine-tuned YOLO variants
│
├── 3_Sequence and NLP/
│   ├── 6_Intro_to_Seq.ipynb
│   ├── 7_Seq_to_Seq.ipynb
│   ├── 8A_HuggingFace_Ecosystem.ipynb
│   ├── 8B_Hugging_Face_Finetuning.ipynb
│   ├── assets/                       # rnn.png, lstm.png, rnns.png
│   ├── best_rnnclassifier.pt
│   ├── best_lstmclassifier.pt
│   ├── harry_potter_txt/             # Training corpus
│   └── Text Classification/          # Production NLP pipeline
│       ├── app/
│       ├── config.py
│       ├── models/
│       ├── notebooks/                # 5 approach notebooks
│       ├── src/                      # Modular source code
│       ├── run_pipeline.py
│       └── requirements.txt
│
├── Classification Hub/               # 5 open-ended projects
│   ├── Ex_1_Tabular_Classification.ipynb
│   ├── Ex_2_Image_Classification.ipynb
│   ├── Ex_3_Image_Classification_Pretrained.ipynb
│   ├── Ex_4_Audio_Classification.ipynb
│   ├── Ex_5_Text_Classification_Transformers.ipynb
│   └── README.md
│
├── data/                             # Shared datasets
│   ├── cifar-10-batches-py/
│   ├── cifar-10-python.tar.gz
│   ├── FashionMNIST/
│   ├── imdb/
│   └── MNIST/
│
├── datasets/coco128/                 # COCO128 images + labels
├── detection_output/                 # Sample detection results
├── lab_assignments/                  # Student submissions
│   ├── abdelhadi_osama/
│   ├── Eithar_Ismail/
│   └── ibrahim_alhafiz/
│
├── papers/                           # Foundational papers
│   ├── AlexNet_paper.pdf
│   └── ResNet_paper.pdf
│
├── coco128.yaml
├── coco128_dataset.yaml
├── yolov8n.pt
├── yolov8n-seg.pt
├── yolov8n-pose.pt
├── yolov8n.onnx
└── README.md
```

---

## 👥 Student Lab Submissions

Real submissions from SAIR learners — see how different students approach the same labs:

| Student | Contains |
|---------|----------|
| **abdelhadi_osama** | lab_1 → lab_4 + classification_hub |
| **Eithar_Ismail** | lab_1 → lab_4 + Lab_5 + CNN notebooks |
| **ibrahim_alhafiz** | lab_1 → lab_4 + classification_hub |

Browse `lab_assignments/[student_name]/` for working examples of each lab.

---

## 🔧 Installation & Setup with UV

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to module
cd 'SAIR/4_Applied Deep Learning with PyTorch'

# Create virtual environment
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Core dependencies
uv pip install torch torchvision torchaudio
uv pip install jupyter matplotlib numpy pandas tqdm

# For NLP and HuggingFace
uv pip install transformers datasets accelerate

# For YOLOv8 demos
cd '2_Vision and CNN/Demos'
uv pip install -r requirements.txt

# For the Text Classification pipeline
cd '../../3_Sequence and NLP/Text Classification'
uv pip install -r requirements.txt

# Launch Jupyter
cd ../..
uv run jupyter notebook
```

### **UV Commands Cheat Sheet**

| Command | Purpose |
|---------|---------|
| `uv venv` | Create virtual environment |
| `uv pip install <package>` | Install a package |
| `uv pip install -r requirements.txt` | Install from requirements file |
| `uv pip list` | List installed packages |
| `uv pip freeze > requirements.txt` | Generate requirements file |
| `uv pip uninstall <package>` | Remove a package |
| `uv cache clean` | Clean uv cache |
| `uv run <script>` | Run script inside the venv |

---

## 💻 Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| GPU VRAM | 4 GB (T4 on Colab) | 8 GB+ |
| RAM | 8 GB | 16 GB |
| Disk Space | 5 GB (pretrained models) | 10 GB |
| CUDA Version | 11.8+ | 12.x |

> **No GPU?** Use [Google Colab](https://colab.research.google.com/) with a free T4 GPU. All notebooks work on Colab.  
> Check GPU availability: `python -c "import torch; print(torch.cuda.is_available())"`

---

## 🔧 Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `CUDA out of memory` | Batch size too large | Halve the batch size; use `torch.cuda.empty_cache()` |
| `RuntimeError: Expected all tensors on the same device` | Mixing CPU and GPU tensors | Add `.to(device)` to all inputs and the model |
| YOLOv8 demo crashes with no webcam | No camera attached | Use `demo_06_batch_processing.py` instead |
| HuggingFace download hangs | Network issue or rate limit | Set `HF_HUB_OFFLINE=1` if models are already cached |
| Training loss not decreasing | Learning rate too high/low | Try `lr=1e-3` for Adam as a safe starting point |
| `UserWarning: No positive samples` | Class imbalance in mini-batch | Shuffle data and increase batch size |

---

## 🤝 Get Help & Connect

Stuck on a notebook? Confused by a YOLO output? Need help with HuggingFace?

[![Telegram](https://img.shields.io/badge/Telegram-Join_SAIR_Community-blue?logo=telegram)](https://t.me/+jPPlO6ZFDbtlYzU0)

Join our community for:
- 🖼️ Help with CNN architectures and vision tasks
- 📝 NLP and transformer fine-tuning guidance
- 🚀 Code reviews for your Classification Hub projects
- 🎯 Feedback on your Text Classification pipeline
- 📚 Study groups focused on modern deep learning

---

## 🎯 Ready for Your Next Step?

### **Starting PyTorch?**
→ Begin with [`1_PyTorch Fundemntals/1_Intro.ipynb`](1_PyTorch%20Fundemntals/1_Intro.ipynb)

### **Ready for vision?**
→ Continue with [`2_Vision and CNN/3_CNN.ipynb`](2_Vision%20and%20CNN/3_CNN.ipynb)

### **Ready for NLP?**
→ Explore [`3_Sequence and NLP/6_Intro_to_Seq.ipynb`](3_Sequence%20and%20NLP/6_Intro_to_Seq.ipynb)

### **Ready for open-ended projects?**
→ Dive into [`Classification Hub/`](Classification%20Hub/)

### **Ready to advance?**
→ Continue to [Module 5: GPT from Scratch](../5_GPT%20from%20scratch/README.md)

---

## 📚 Additional Resources

- [PyTorch Official Tutorials](https://pytorch.org/tutorials/)
- [HuggingFace Documentation](https://huggingface.co/docs)
- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [CNN Explainer](https://poloclub.github.io/cnn-explainer/)
- [Papers with Code](https://paperswithcode.com/)

> *"From tensors to production — understanding every layer of the stack."*

**Happy Learning with UV! 🚀⚡**

---

**🔜 Next Step:** [Module 5: GPT from Scratch](../5_GPT%20from%20scratch/README.md)