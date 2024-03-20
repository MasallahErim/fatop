from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
def analysis_sentence(sentences):
    return  sentiment_pipeline(sentences)