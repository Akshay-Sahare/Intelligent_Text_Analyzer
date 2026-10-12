# Intelligent Text Analyzer & Sentiment Tracker

An automated text manipulation and optimization program written in Core Python. It parses multi-line user inputs, processes them into distinct tokens, cleans structural punctuation marks, and extracts linguistic metrics like length density and text polarity (Positive/Negative/Neutral).

## Technical Framework
- **String Tokenization:** Utilizes Python's advanced string formatting tools (`.split()`, `.strip()`, `.lower()`) to perform text cleansing.
- **Sentiment Scoring Matrix:** Implements conditional mapping against customized positive/negative arrays to benchmark input moods.
- **Edge-Case Validation:** Prevents syntax leakage or null execution crashes by testing inputs against blank strings or un-spaced parameters.

## Execution
Run the program natively via terminal commands:
```bash
python text_analytics.py
```
