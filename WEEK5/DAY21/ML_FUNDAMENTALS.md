# 1. Introduction to Machine Learning

## 1.1 What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence (AI) that enables machines to learn patterns from past data and predict/decide on future data, without being explicitly programmed for every rule.

**Traditional programming vs Machine Learning**

In the traditional way, we write explicit rules (if/else logic) for every scenario. For example, to detect spam emails traditionally:

```python
if "congratulations" in email or "won" in email or "prize" in email or "won" in email:
    flag = True
else:
    flag = False

if flag == True:
    print("Spam")
else:
    print("Not Spam")
```

The problem: we cannot write a fixed rule for every possible case. New spam patterns keep emerging, and the logic has to be rewritten or extended constantly.

In Machine Learning, instead of hand-writing rules, we give the machine **past data** (input + output) and let an ML algorithm learn the underlying pattern itself. Once trained, the model can predict outcomes for new, unseen inputs.

```python
# Simple non-ML example: pass/fail based on total of two subjects
T1 = int(input())
T2 = int(input())
if T1 >= 35 and T2 >= 35:
    print("Pass")
else:
    print("Fail")
```

```
Machine Learning way:
   Marks (Past Data) -> ML -> Input = 9 -> Predicts Pass/Fail
```

## 1.2 Why Machine Learning?

- We use ML whenever we have a **large amount of data** and the relationship between input and output is too complex to hand-code.
- We don't need to explicitly program the logic for every case — the model learns it by itself from data.
- In the traditional way, we cannot reuse the same logic for all scenarios; we would need to write or modify logic for every new condition. In ML, once trained, the same technique/model can be applied (or retrained) across many different cases/datasets.

## 1.3 Types of Machine Learning

### (1) Supervised Learning

**Definition:** A ML technique that learns the pattern from **labelled data** (data that has both input and known/correct output).

```
Past Data:  [Input, Output] -> Supervised Learning Algorithm (learns the pattern)
                                        |
                                        v
                              New Input -> Prediction (Output)
```

- Input columns are called **independent columns / features**.
- Output column is called the **dependent column / target**.

Two main categories of supervised learning:

- **Regression** — target/output column has continuous (numerical) values. E.g., house price prediction, weather prediction, exam score prediction.
- **Classification** — target/output column has categorical values. E.g., email spam detection (Spam / Not Spam), sentiment analysis (Positive / Negative / Neutral).

**Example — Weather Prediction / Email Spam Detection (concept):**
Email spam detection is traditionally done using keyword matching ("congratulations", "won", "prize" etc). With ML, we instead train a classification model on a labelled dataset of past emails (marked spam / not spam) so it learns the pattern itself.

### (2) Unsupervised Learning

**Definition:** A ML technique that learns the pattern from **unlabelled data** (only input, no output/target given).

```
Input -> Unsupervised Learning -> Output: Clusters
```

- **Clustering**: groups similar types of patterns/data points together.

**Example:** Given a set of unlabelled faces (happy/sad emojis mixed together, no labels), a clustering algorithm learns the pattern from the input alone and groups similar-looking data points into the same cluster (e.g., cluster of happy faces, cluster of sad faces) — without ever being told which is which.

**Example — Customer segmentation:**

| Age | Product price/day |
|---|---|
| 18 | 20L |
| 20 | 12L |
| 50 | 40L |
| 45 | 35L |

An unsupervised clustering algorithm can group this into, say, Cluster 1 (Age 18–20, lower price) and Cluster 2 (Age 45–50, higher price), purely based on similarity in the data — no labels were provided.

### (3) Semi-Supervised Learning

**Definition:** A ML technique that learns the pattern **mostly from unlabelled data and a little from labelled data**.

```
Unlabelled + a little Labelled data
        -> Based on the small labelled data, it learns the pattern of the output labels
        -> Then it labels all the remaining unlabelled data
        -> Train the model on this now-fully-labelled data
        -> Gives the best accuracy
```

Used for both regression and classification style problems. Example: house price prediction where only a few houses have known prices and most don't — the model learns from the few labelled examples, labels the rest, then trains on the complete dataset.

### (4) Reinforcement Learning

**Definition:** A ML technique that learns patterns by taking **actions** and receiving a **reward or penalty** based on the outcome.

**Example:** A ChatGPT-style feedback system — it takes feedback from the user (thumbs up/down, ratings) and, based on that feedback (reward/penalty), improves its performance over time.

### Difference: Supervised vs Unsupervised Learning

| Aspect | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Data | Learns the pattern from **labelled** data | Learns the pattern from **unlabelled** data |
| Algorithms used | Regression & Classification algorithms | Clustering algorithms |
| Example | Weather prediction, Email spam detection | Recommendation systems, customer segmentation |

## 1.4 Setting up the environment

```bash
pip install scikit-learn
pip install xgboost
```

---

## Interview Questions — Introduction to ML

**Q1. What is Machine Learning, in your own words?**
A: Machine Learning is a subset of AI that enables a system to learn patterns from historical (past) data and use that learned pattern to make predictions or decisions on new data, without being explicitly programmed with fixed rules for every scenario.

**Q2. How is Machine Learning different from traditional programming?**
A: In traditional programming, a developer writes explicit rules/logic (if-else conditions) to handle every case, and these rules must be manually updated whenever a new scenario appears. In Machine Learning, we instead provide historical input-output data, and the algorithm learns the underlying pattern/relationship itself. This learned pattern is then used to predict outputs for new, unseen inputs — without needing to hand-code separate logic for every case.

**Q3. Why do we need Machine Learning if traditional programming already works?**
A: Traditional programming becomes impractical when: (a) there is a large volume of data with complex, non-obvious relationships, (b) the rules would need to be rewritten or expanded constantly as new patterns emerge, and (c) the same fixed logic cannot generalize well across many varied cases. ML models learn directly from data and generalize better to new, unseen situations.

**Q4. What are the main types of Machine Learning? Explain briefly.**
A: 

- **Supervised Learning** — learns from labelled data (has both input and correct output); used for Regression (continuous target) and Classification (categorical target).
- **Unsupervised Learning** — learns from unlabelled data (only input); used for clustering/grouping similar data points.
- **Semi-Supervised Learning** — learns mostly from unlabelled data with a small amount of labelled data to guide the learning.
- **Reinforcement Learning** — learns by taking actions and receiving rewards or penalties, improving performance over time based on feedback.

**Q5. What is the difference between Regression and Classification?**
A: Regression is used when the target/output column has continuous numerical values (e.g., price, score, temperature). Classification is used when the target/output column has categorical/discrete values (e.g., spam/not spam, pass/fail).

**Q6. Give one real-world example each for Supervised, Unsupervised, and Reinforcement Learning.**
A:

- Supervised: Email spam detection (labelled as spam/not spam).
- Unsupervised: Customer segmentation based on age and spending, without predefined labels.
- Reinforcement: A recommendation or feedback system (like a chatbot) that improves based on user feedback (reward/penalty).

**Q7. What is labelled vs unlabelled data?**
A: Labelled data has both the input features and the known correct output/target value for each record (e.g., an email marked "spam" or "not spam"). Unlabelled data has only the input features, with no known output — the algorithm must find structure or patterns on its own.

**Q8. When would you use Semi-Supervised Learning instead of pure Supervised Learning?**
A: When labelling data is expensive, time-consuming, or impractical to do for the entire dataset, but a small labelled subset is available. Semi-supervised learning uses that small labelled portion to learn initial patterns, propagates labels to the remaining unlabelled data, and then trains the final model on the complete (now labelled) dataset.

**Q9. What is Clustering?**
A: Clustering is an unsupervised learning technique that groups similar data points together based on shared characteristics/patterns in the input data, without using any predefined output labels.

**Q10. How does Reinforcement Learning differ from Supervised Learning?**
A: Supervised learning learns from a fixed dataset of labelled input-output pairs provided upfront. Reinforcement learning learns dynamically by taking actions in an environment and receiving rewards or penalties as feedback, gradually improving its decision-making/policy over time based on that feedback rather than a static labelled dataset.
