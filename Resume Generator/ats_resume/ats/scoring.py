import spacy
from sklearn.feature_extraction.text import CountVectorizer

nlp = spacy.load("en_core_web_sm")

def calculate_ats_score(resume_text, job_desc):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = (vectors * vectors.T).A[0][1]

    score = min(100, int(similarity * 10))
    return score
