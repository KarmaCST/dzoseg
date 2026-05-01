# dzoseg 🇧🇹

[![PyPI version](https://img.shields.io/pypi/v/dzoseg.svg)](https://pypi.org/project/dzoseg/)
![License](https://img.shields.io/github/license/KarmaCST/dzoseg)

`dzoseg` is a lightweight Python library for Dzongkha Tokenizer. It offers a hybrid approach, allowing users to choose between high-performance AI subword tokenization (using SentencePiece) and traditional Tseg-based segmentation.

## 🚀 Features
* **Subword Segmentation:** Uses a pre-trained **Unigram** model with a 32,000 vocabulary size for deep learning applications.
* **Tseg Segmentation:** A rule-based approach to split text into syllables based on the traditional Dzongkha Tseg (་).
* **Byte-Fallback:** Automatically handles non-Dzongkha characters (English, numbers, etc.) without crashing.

## 📦 Installation

```bash
pip install dzoseg

🛠 Usage
1. Subword (AI-Based) Segmentation
This method is recommended for Machine Learning tasks like machine translation or sentiment analysis.

from dzoseg import DzongkhaTokenizer

# Initialize the segmenter
ds = DzongkhaTokenizer()

text = "འབྲུག་རྒྱལ་གཞུང་གཙུག་ལག་སློབ་སྡེའི་འོག་ལུ་ཡོད་པའི་ཚན་རིག་དང་འཕྲུལ་རིག་མཐོ་རིམ་སློབ་གྲྭའི་གློག་རིག་དང་འཕྲུལ་རིག་ལས་ཁུངས།"

# Get subword tokens
tokens = ds.segment_subwords(text)
print(f"Subwords: {tokens}")

# Expected Output: 
# Subwords: [' འབྲུག་', 'རྒྱལ་གཞུང་', 'གཙུག་ལག་སློབ་སྡེ', 'འི་', 'འོག་ལུ་ཡོད་པའི་', 'ཚན་རིག་', 'དང་', 'འཕྲུལ་རིག་', 'མཐོ་རིམ་སློབ་གྲྭ', 'འི་', 'གློག་རིག་', 'དང་', 'འཕྲུལ་རིག་', 'ལས་ཁུངས།']

2. Tseg-based Segmentation
This method splits the text strictly based on the Dzongkha syllable delimiter (Tseg).

# Get syllable-level tokens
syllables = ds.segment_tseg(text)
print(f"Syllables: {syllables}")

# Expected Output: 
# Syllables: ['འབྲུག','རྒྱལ','གཞུང', 'ཙུག', 'ལག', 'སློབ', 'སྡེའི', 'འོག', 'ལུ', 'ཡོད', 'པའི', 'ཚན', 'རིག', 'དང', 'འཕྲུལ', 'རིག', 'མཐོ', 'རིམ', 'སློབ', 'གྲྭའི', 'གློག', 'རིག', 'དང', 'འཕྲུལ', 'རིག', 'ལས', 'ཁུངས།']

📊 Model Details
Model Type: Unigram (SentencePiece)
Vocabulary Size: 32,000
Character Coverage: 100%
Training Data: Cleaned Dzongkha Web & Literary Corpus

📜 License
This project is licensed under the MIT License.
Maintained by: Karma Wangchuk
Contact: karma.cst@rub.edu.bt
