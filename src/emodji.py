from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from translator import translate


def emotionAnalysis(text):
    # Translate the text to English if it's not already
    text = translate(text)

    # Create a sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    # Scores are between -1 and 1 for negative, neutral and positive
    scores = analyzer.polarity_scores(text)
    return scores
