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

<b>NOTE: Some of the codes are written in Google Colab Notebooks, this will be mention in filename itself by "_colab".</b>

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
### 1. Introduction (in Notes)
### 2. Propmt Engineering
* Zero Shot Learning
* Few Shot Learning
### 3. Transformer Architecture (in Notes)
* The Illustrated Transformer: [by Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
* Encoder based LLMs
* Decoder based LLms
* Encoder-Decoder based LLMs
* Google Research Paper: [<u>"Attention Is All You Need"</u>](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
* Encoder Architecture:
    - Self-Attention: Single Head, Multi Head
    - Positional Encoding
    - Add & Normalization: kind of Residual Layer (ResNet) feature
    - Feed Forward Neural Network
    - Inputs are given all at once (meaing Parallely)
* Decoder Architecture:
    - Same as Encoder architecture
    - Has one extra layer: Encoder-Decoder Attention
    - Outputs are generated one-by-one
* Linear Layer
* Activation Layer: Softmax() is prominently used as an activation function
### 4. How is ChatGPT trained
* Uses an LLM: like gpt-3.5 or gpt-4, etc.
* It is then trained in Several different steps:
    - Generative pre-training
    - Supervised fine-tuning
    - Reinforcement learning from human feedback (RLHF)
### 5. Huggingface Platform
* Introduction
* Huggingface Tasks
    - NLP Tasks
    - Computer Vision Tasks
    - Speech Processing Tasks
    - Multimodal Tasks
    - Other Tasks
* NLP tasks
    - Sentiment Analysis
    - Batch Sentiment Analysis
    - Text Generation
    - Question Answering
* Tokenization: AutoTokenizer
* Datasets & Spaces
    - Loading and preparing Dataset
    - Preprocessing the Data
    - Setting-up the Training Arguments
    - Initializing the Model
    - Training the Model
    - Evaluating the Model
    - Saving the Model
    - ArXiv data Summarization
* Fine-tuning LLMs
* Project 2
* Text to Image Generation
* Text to Speech Generation
### 6. OpenAI Platform
* Introduction
* ChatCompletion API
* Completion API
* Function Calling
* Project 3
* Fine Tuning Classification Model

## `→ Project 2 - Text Summarization using Huggingface`
* Installing/Upgrading the Necessary Libraries
* Importing the Libraries
* Tokenization
    - Initializing the Tokenizer and Model
    - Loading Dataset from Huggingface
    - Getting info about the dataset
    - Converting Dataset into Tokens (Features)
* Training
    - Using Data Collator - for batch loading the data
    - Setting the Training Arguments
    - Initializing the Trainer
    - Training
* Evaluating the Model
    - Using Rouge Metrics to evaluate the Text Summarization Model
    - Using the Huggingface doc's function to evaluate the model
* Saving the Model & Tokenizer
* Loading the Saved Model
* Predictions using the Loaded Model

## `→ Project 3 - Telegram ChatBot using OpenAI Platform`
* The main code for the project is in the `main.py` file
* The code uses the OpenAI Platform's ChatCompletion API to interact with the user
* To get the Telegra Bot Token
    - Open Telegram either on your phone or on the Laptop, and search for the "BotFather"
    - Follow the Steps to create the Bot
    - It will give you the Bot Token and the Bot Username, and the Bot instance. Type the following:
        - /start
        - /newbot
        - Name your Bot
        - Choose the Bot Username
        - This will generate the Bot Token
* The code in the `main.py` file has been implemented using the following steps:
    - Importing the necessary Libraries
    - Step 1: Load the Keys and Tokens
    - Step 2: Initialize the Class instance
    - Step 3: Initialize bot and dispatcher
    - Step 4: Define the function to handle the /start command
    - Step 5: Define the function to handle the /help command
    - Step 6: Define the function to clear the previous responses and context
    - Step 7: Define the function to handle the Users inputs and generate responses
    - Step 8: Call the Executor


# Happy Coding!!!