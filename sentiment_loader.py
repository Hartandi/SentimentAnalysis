from transformers import pipeline


def load_sentiment_model(model_name="distilbert-base-uncased-finetuned-sst-2-english"):
    """Load and return a sentiment analysis pipeline."""
    return pipeline("sentiment-analysis", model=model_name)


def main():
    model = load_sentiment_model()
    examples = [
        "I love this product!",
        "This is the worst experience I've ever had."
    ]
    results = model(examples)
    for text, result in zip(examples, results):
        print(f"{text} -> {result['label']} (score: {result['score']:.4f})")


if __name__ == "__main__":
    main()
