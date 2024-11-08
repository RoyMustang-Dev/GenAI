# GenAI
This repo contains an in-depth study and implementation of all the commonly used Generative AI Techniques.

## Software And Tools Requirements

1. [GithubAccount](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/downloads)
4. [AnacondaPackage/JupyterNoteBook](https://www.anaconda.com/products/distribution)

## Creata a New Environment and Activate!!

```
conda create -p venv python==3.12 -y
conda activate venv/
```
<b>NOTE: Using Python ver 3.12 for better working with Gensim</b>

## Install all the Required Libraries!!

```
pip install -r requirements/text_preprocessing_requirements.txt
```
## Dataset Links
1. [Text Preprocessing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
2. [Feature Engineering Dataset](https://www.kaggle.com/datasets/khulasasndh/game-of-thrones-books)
3. [Project 1 - Text Classification Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

# Getting started with Generative AI!!

## `→ Understanding the Basics of Text Processing`
* Definition of Generative AI
* Created a Function that has multiple text processing functions
    - Step 1: Remove HTML tags
    - Step 2: Remove URLs
    - Step 3: Convert to lowercase
    - Step 4: Removing Punctuations
    - Step 5: Remove stopwords
    - Step 6: Replace chat words with full forms
    - Step 7: Remove/Handle emojis
* Using NLTK Word Tokenizer
* Using NLTK PorterStemmer
* Using NLTK WordNetLemmatizer 

## `→ Understanding the Feature Engineering`
* One-hot Encoding
* Bag of Words (CountVectorizer)
* TF-IDF
* Word2Vec
* Transformer based encoding

## `→ Project 1 - Text Classification using ML`
* Importing all the necessary Libraries
* Importing the Dataset
* Basic EDA & Splitting the Data into smaller Batches
* Applying the basic Text Preprocessing
* Train-test Split
* Modeling
    - Bag of Words (Count Vectorizer)
    - GaussianNB
    - Random Forest Classifier (RFC)
    - CountVectorizer with RFC
    - CountVectorizer with Ngrams & RFC
    - TF-IDF Vectorizer with RFC

## `→ Large Language Models (LLMs)`
* Introduction (in Notes)
* Propmt Engineering
    - Zero Shot Learning
    - Few Shot Learning
* Transformer Architecture (in Notes)
    - Encoder based LLMs
    - Decoder based LLms
    - Encoder-Decoder based LLMs
    - Google Research Paper: "Attention Is All You Need"
    - Encoder Architecture:
        - Self-Attention: Single Head, Multi Head
        - Positional Encoding
        - Add & Normalization: kind of Residual Layer (ResNet) feature
        - Feed Forward Neural Network
        - Inputs are given all at once (meaing Parallely)
    - Decoder Architecture:
        - Same as Encoder architecture
        - Has one extra layer: Encoder-Decoder Attention
        - Outputs are generated one-by-one
    - Linear Layer
    - Activation Layer: Softmax() is prominently used as an activation function
* How is ChatGPT trained
    - Uses an LLM: like gpt-3.5 or gpt-4, etc.
    - It is then trained in Several different steps:
        - Generative pre-training
        - Supervised fine-tuning
        - Reinforcement learning from human feedback (RLHF)
* Huggingface Platform
    - Introduction
    - Pipelines
    - NLP tasks
    - Tokenization
    - Datasets & Spaces
    - Fine-tuning LLMs
    - Project 2

# Happy Coding!!!