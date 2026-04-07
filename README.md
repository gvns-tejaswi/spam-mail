## 🏗️ Project Description: Spam Detection System

This project implements a robust **Spam Mail Classifier** leveraging the **Multinomial Naive Bayes (MNB)** algorithm. By analyzing the frequency of terms within a dataset of emails, the model identifies linguistic patterns and "trigger words" to accurately distinguish between legitimate correspondence (Ham) and unsolicited or malicious content (Spam).



### 🧪 How it Works: The MNB Approach
The core of this system is built on the probabilistic foundation of Bayes' Theorem, specifically optimized for discrete feature counts (text data).

* **Feature Extraction:** The system utilizes **Tokenization** and **Stop-word Removal** to clean the raw email text. It then applies **Count Vectorization** to transform the text into a "Bag of Words" model, representing each email as a frequency distribution of terms.
* **The Multinomial Advantage:** Unlike standard classifiers, MNB accounts for the **frequency of occurrence**. If a spam-heavy word like "Limited" or "Claim" appears multiple times, the model increases the spam-probability weight proportionally.
* **Laplace Smoothing:** To handle "Zero Probability" issues (when the model encounters a word it hasn't seen during training), we implement **Alpha Smoothing** ($\alpha = 1$) to ensure the classifier remains stable and functional.



### 🚀 Key Features
* **High Efficiency:** MNB provides near-instant classification, making it suitable for real-time mail filtering.
* **Scalability:** Designed to handle large datasets of text without significant computational overhead.
* **Accuracy Metrics:** Evaluated using **Precision**, **Recall**, and **F1-Score** to ensure that "False Positives" (legitimate mail being marked as spam) are minimized.

---

### 🛠️ Tech Stack
* **Language:** Python
* **Library:** Scikit-Learn (specifically `MultinomialNB`)
* **Data Processing:** Pandas, NumPy
* **Text Processing:** NLTK / CountVectorizer
