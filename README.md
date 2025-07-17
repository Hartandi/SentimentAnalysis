# SentimentAnalysis


This repository provides a simple Python program for loading a pre-trained
sentiment analysis model using the Hugging Face `transformers` library.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the example script to load the model and analyze sample sentences:

```bash
python sentiment_loader.py
```

The script will print out the predicted sentiment labels and their scores for
some example sentences. You can modify the examples in `sentiment_loader.py` or
use the returned pipeline object to analyze your own text.
