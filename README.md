#  Resume Analyzer using NLP

##  Overview

This project is a **Resume Analyzer** built using basic Natural Language Processing (NLP) and Machine Learning techniques.

It compares multiple resumes with a given job description and calculates a **match score (%)** for each resume. Based on this score, the system ranks candidates from most suitable to least suitable.

This helps automate the resume screening process and saves time compared to manual evaluation.

---

##  Features

* Analyze multiple resumes at once
* Compare resumes with a job description
* Generate match percentage
* Rank resumes automatically
* Display results in a bar graph

---

##  Concepts Used

* Text preprocessing (cleaning text)
* TF-IDF (Term Frequency–Inverse Document Frequency)
* Cosine Similarity
* Basic skill matching

---

##  Project Structure

```
resume_analyzer/
│
├── data/
│   ├── job_description.txt
│   ├── resume1.txt
│   ├── resume2.txt
│   ├── resume3.txt
│
├── src/
│   └── model.py
│
├── README.md
```

---

##  Requirements

Make sure you have **Python installed (3.x)**.

Install required libraries using:

```
pip install scikit-learn matplotlib
```

---

##  How to Run the Project

### Step 1: Navigate to project folder

Open terminal and go to your project folder:

```
cd path_to_resume_analyzer
```

---

### Step 2: Run the program

```
python src/model.py
```

---

##  Output

After running the program:

* You will see **resume ranking in terminal**, for example:

```
Resume Ranking:

resume3.txt -> 85.20%
resume1.txt -> 78.50%
resume2.txt -> 30.10%
```

* A **bar graph** will open showing match percentages visually.

---

##  How It Works

1. The program reads all resumes and the job description
2. It cleans the text (removes symbols, converts to lowercase)
3. It converts text into numbers using TF-IDF
4. It compares resumes with job description using cosine similarity
5. It also checks important skills (like Python, ML, etc.)
6. It combines both scores and ranks resumes

---

##  Adding Your Own Data

To test with your own data:

1. Replace content in:

   * `data/job_description.txt`
   * `data/resume1.txt`, `resume2.txt`, etc.

2. Keep file names starting with:

```
resume
```

3. Run the program again

---

##  Limitations

* Works only with `.txt` files
* Uses simple keyword-based skill matching
* Not suitable for very complex resumes

---

##  Future Improvements

* Support PDF resumes
* Add GUI or web interface
* Use advanced NLP models
* Highlight matched keywords

---

##  Author

This project was developed as part of an AIML course to demonstrate practical use of machine learning in real-world problems.

---

##  Conclusion

This project shows how basic NLP techniques can be used to build a simple and effective resume screening system. It is easy to understand, implement, and extend for future improvements.
