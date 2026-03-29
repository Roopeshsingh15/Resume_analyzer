import os
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Clean Text Function

def clean_text(text):
    text = text.lower()                     
    text = re.sub(r'[^a-z\s]', '', text)    
    return text

# 2. Set Folder Path

base_path = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_path, "data")

# 3. Load Job Description

job_file = os.path.join(data_path, "job_description.txt")

with open(job_file, "r") as f:
    job_text = f.read()

job_text = clean_text(job_text)

# 4. Load Resumes

resume_texts = []
resume_names = []

files = os.listdir(data_path)

for file in files:
    if file.startswith("resume"):
        file_path = os.path.join(data_path, file)

        with open(file_path, "r") as f:
            text = f.read()

        text = clean_text(text)

        resume_texts.append(text)
        resume_names.append(file)

# 5. Convert Text to Numbers (TF-IDF)

documents = resume_texts + [job_text]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# 6. Compare Using Cosine Similarity

similarity = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])

# 7. Skill Matching

skills = ["python", "machine learning", "data", "analysis", "pandas", "numpy"]

def calculate_skill_score(text):
    count = 0
    for skill in skills:
        if skill in text:
            count = count + 1
    return count / len(skills)

# 8. Final Score Calculation

final_scores = []

for i in range(len(resume_texts)):
    sim_score = similarity[i][0]
    skill_score = calculate_skill_score(resume_texts[i])

    final_score = (0.7 * sim_score) + (0.3 * skill_score)
    final_scores.append(final_score)

# 9. Ranking

results = list(zip(resume_names, final_scores))

results.sort(key=lambda x: x[1], reverse=True)

print("\nResume Ranking:\n")
for name, score in results:
    print(name, "->", round(score * 100, 2), "%")


# 10. Graph

names = []
scores = []

for item in results:
    names.append(item[0])
    scores.append(item[1] * 100)

plt.bar(names, scores)
plt.xlabel("Resumes")
plt.ylabel("Match Percentage")
plt.title("Resume Ranking")
plt.show()