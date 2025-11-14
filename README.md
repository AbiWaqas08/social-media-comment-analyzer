Social Media Comment Analyzer

A Sentiment Analysis Web App that predicts whether a social media comment is 
Positive, Neutral, or Negative.
Built with **Machine Learning (Logistic Regression / Naive Bayes), deployed via FastAPI backend, and a Streamlit UI for interactive predictions.

---

 Features

* Clean and preprocess comments (lowercase, remove noise, stopwords, lemmatization).
* TF-IDF vectorization for ML model input.
* Fast ML models: Logistic Regression / Naive Bayes.
* REST API for predictions using **FastAPI**.
* Interactive **Streamlit frontend** for real-time sentiment analysis.
* Visualization of sentiment distribution in the dataset.

---

Project Structure

social-media-comment-analyzer/
│
├─ app.py                 # FastAPI backend
├─ streamlit_app.py       # Streamlit UI
├─ sentiment_model.pkl    # Trained ML model
├─ tfidf_vectorizer.pkl   # TF-IDF vectorizer
├─ label_encoder.pkl      # Label encoder
├─ youtube_comments.csv   # Dataset
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation


---

Installation

1. Clone this repository:


git clone https://github.com/yourusername/social-media-comment-analyzer.git
cd social-media-comment-analyzer


2. Create and activate virtual environment (optional but recommended):


python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:


pip install -r requirements.txt


 Running the App

Start FastAPI backend


uvicorn app:app --reload


The API runs at: `http://127.0.0.1:8000`

### Start Streamlit frontend

bash
streamlit run streamlit_app.py


Open the URL shown by Streamlit in your browser.

---

## Usage

* Enter a social media comment in the text area.
* Click **Analyze**.
* See predicted sentiment: Positive / Neutral / Negative.

---

## Dataset

* Dataset used: [YouTube Comments Sentiment Dataset](https://www.kaggle.com/datasets/andrewmvd/youtube-comments-sentiment-dataset)
* Preprocessing includes:

  * Lowercasing
  * Removing URLs, mentions, hashtags, emojis, punctuation
  * Stopword removal
  * Lemmatization

---

## Technologies

* Python 3.x
* Pandas, NumPy
* Scikit-learn (Logistic Regression / Naive Bayes, TF-IDF)
* NLTK (Stopwords, Lemmatizer)
* FastAPI (Backend API)
* Streamlit (Frontend UI)

---

## Future Improvements

* Use **BERT / DistilBERT** for deep learning-based sentiment analysis.
* Deploy app online (Heroku / Render / Streamlit Cloud).
* Support multiple languages for comments.
* Add batch prediction and CSV upload feature.



"# social-media-comment-analyzer" 
