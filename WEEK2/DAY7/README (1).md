# Day 7: Prompting Techniques (Zero-shot, One-shot, Few-shot, CoT)

## The Task Used for Every Prompt

> **Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.**

I use this single task for all five prompts, so that the **only thing that changes is the prompting technique**.
Every prompt also asks for the **same output format**, so the answers can be compared fairly.

**Why this task?** It is open-ended enough that answers can differ in structure, depth and accuracy, and it connects to Day 6 (tokens, embeddings, how GPT/Claude/Gemini work).

---

## 1. The Four Techniques in One Table

| Technique | What you give the model | Strength | Weakness | Use when |
|---|---|---|---|---|
| **Zero-shot** | Instruction only, no examples | Shortest, cheapest, fastest | Format and style may drift | Simple, well-known tasks |
| **One-shot** | Instruction + **1** example | Shows the style cheaply | One example can be copied too closely | You need a specific format |
| **Few-shot** | Instruction + **2 to 5** examples | Most consistent format and tone | Longer prompt = more input tokens | Format must be reliable, or the task is unusual |
| **Chain-of-Thought (CoT)** | Ask the model to reason step by step before answering | Helps multi-step reasoning, maths, logic | More output tokens, slower; little gain on simple explanations | Reasoning or calculation tasks |
| **Few-shot + CoT** (combined) | Examples that **include the reasoning** | Format **and** reasoning guided | Longest and most expensive prompt | Hard tasks where you need both |

> You asked for zero-shot, one-shot, few-shot and CoT in 5 prompts, so the 5th prompt combines few-shot with CoT.

---

## 2. Shared Output Format (used in all 5 prompts)

```text
Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer
```

## 3. Fair-Test Settings

| Setting | Value |
|---|---|
| Same task | Yes (above) |
| Same model | `gemini-2.5-flash` (or `claude-haiku-5-5`), one model for all prompts |
| Same temperature | `0.3` |
| Same max output tokens | `2048` |
| Runs per prompt | 1 (repeat 2 to 3 times for more reliable results) |

---

## 4. The 5 Prompts

### Prompt 1: Zero-shot
Instruction only. No example.

```text
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.

Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer
```

### Prompt 2: One-shot
One example (RAG) on a **different topic**, so the model learns the style but cannot copy the content.

```text
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.

Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer

Here is one example of the expected style on a different topic:

Topic: Retrieval-Augmented Generation (RAG)
1. Definition: RAG is a design where an LLM first retrieves relevant documents and then uses them to write a grounded answer.
2. Core components:
- Document loader and chunker: splits source files into small pieces
- Embedding model: converts chunks and questions into vectors
- Vector database (e.g. FAISS): finds the chunks nearest to the question
- Prompt builder: puts the retrieved chunks and the question into one prompt
- LLM: writes the final answer using that context
3. How an input becomes an output:
Step 1 - The question is converted into an embedding vector.
Step 2 - The vector database returns the top matching chunks.
Step 3 - The chunks and the question are combined into one prompt.
Step 4 - The LLM generates an answer grounded in those chunks.
4. Analogy: An open-book exam. The student (LLM) looks up the right pages (retrieval) before writing the answer.
5. Interview question: Why use RAG instead of fine-tuning to add company knowledge?
Model answer: RAG adds knowledge at query time, is cheap to update (just re-index the documents) and can cite its sources, while fine-tuning mainly changes behaviour and style.

Now do the same for this task:
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.
```

### Prompt 3: Few-shot
Three examples (RAG, CNN, Vector database), all on different topics.

```text
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.

Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer

Here are three examples of the expected style on different topics:

Example 1
Topic: Retrieval-Augmented Generation (RAG)
1. Definition: RAG is a design where an LLM first retrieves relevant documents and then uses them to write a grounded answer.
2. Core components:
- Document loader and chunker: splits source files into small pieces
- Embedding model: converts chunks and questions into vectors
- Vector database (e.g. FAISS): finds the chunks nearest to the question
- Prompt builder: puts the retrieved chunks and the question into one prompt
- LLM: writes the final answer using that context
3. How an input becomes an output:
Step 1 - The question is converted into an embedding vector.
Step 2 - The vector database returns the top matching chunks.
Step 3 - The chunks and the question are combined into one prompt.
Step 4 - The LLM generates an answer grounded in those chunks.
4. Analogy: An open-book exam. The student (LLM) looks up the right pages (retrieval) before writing the answer.
5. Interview question: Why use RAG instead of fine-tuning to add company knowledge?
Model answer: RAG adds knowledge at query time, is cheap to update (just re-index the documents) and can cite its sources, while fine-tuning mainly changes behaviour and style.

Example 2
Topic: Convolutional Neural Network (CNN)
1. Definition: A CNN is a neural network that slides small filters over an image to detect visual patterns.
2. Core components:
- Convolution layers: filters that detect edges, textures and shapes
- Activation function (ReLU): adds non-linearity so the network can learn complex patterns
- Pooling layers: shrink the feature maps and keep the strongest signals
- Fully connected layers: combine the features to make a decision
- Output layer (softmax): gives a probability for each class
3. How an input becomes an output:
Step 1 - The image is fed in as a grid of pixel values.
Step 2 - Convolution and pooling layers extract features, from simple edges to complex shapes.
Step 3 - The features are flattened and passed to fully connected layers.
Step 4 - Softmax outputs the class probabilities.
4. Analogy: Identifying a friend in a crowd by first noticing simple clues (hair, glasses) and then combining them into a face.
5. Interview question: Why are CNNs better than plain fully connected networks for images?
Model answer: Filters share weights across the image, so a CNN needs far fewer parameters and can detect a pattern wherever it appears.

Example 3
Topic: Vector database
1. Definition: A vector database stores embeddings and quickly finds the ones most similar to a query vector.
2. Core components:
- Embeddings: vectors that represent the meaning of text or images
- Index (e.g. HNSW or IVF): a structure that makes nearest-neighbour search fast
- Similarity metric: cosine similarity or dot product to measure closeness
- Metadata store: keeps the original text and supports filtering
- Query API: accepts a vector and returns the top-k matches
3. How an input becomes an output:
Step 1 - Documents are embedded and stored in the index with their metadata.
Step 2 - The user query is embedded with the same model.
Step 3 - The index finds the top-k nearest vectors.
Step 4 - The matching text and metadata are returned.
4. Analogy: A library where books are shelved by topic similarity instead of alphabet, so similar books sit next to each other.
5. Interview question: When would you prefer cosine similarity over Euclidean distance?
Model answer: Cosine compares the direction of vectors and ignores their length, which suits text embeddings; Euclidean distance is affected by magnitude.

Now do the same for this task:
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.
```

### Prompt 4: Chain-of-Thought (CoT)
No examples. The model is told to reason in steps first, then give the final answer.

```text
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.

Think step by step before answering:
Step 1 - List what ChatGPT, Claude and Gemini have in common architecturally.
Step 2 - Note what differs between them, and what is not publicly known.
Step 3 - Decide the 5 most important components a fresher must know.
Write this thinking under the heading "Reasoning:". Then write the heading "Final Answer:" followed by the answer in this format:
Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer
```

### Prompt 5: Few-shot + CoT
One worked example that shows the **reasoning and the final answer**, then the real task.

```text
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.

First write your thinking under the heading "Reasoning:", then give the answer under the heading "Final Answer:" in this format:
Use exactly this format:
1. Definition: one line
2. Core components: exactly 5 bullet points
3. How an input becomes an output: numbered steps
4. Analogy: one real-life analogy
5. Interview question: one question with a model answer

Here is one worked example on a different topic:

Topic: Retrieval-Augmented Generation (RAG)
Reasoning: RAG has two stages, retrieval and generation. Retrieval needs a way to split documents, turn text into vectors and search them. Generation needs a prompt and an LLM. That gives five components in the order the data flows. The most common interview confusion is RAG versus fine-tuning, so the interview question should cover it.
Final Answer:
1. Definition: RAG is a design where an LLM first retrieves relevant documents and then uses them to write a grounded answer.
2. Core components:
- Document loader and chunker: splits source files into small pieces
- Embedding model: converts chunks and questions into vectors
- Vector database (e.g. FAISS): finds the chunks nearest to the question
- Prompt builder: puts the retrieved chunks and the question into one prompt
- LLM: writes the final answer using that context
3. How an input becomes an output:
Step 1 - The question is converted into an embedding vector.
Step 2 - The vector database returns the top matching chunks.
Step 3 - The chunks and the question are combined into one prompt.
Step 4 - The LLM generates an answer grounded in those chunks.
4. Analogy: An open-book exam. The student (LLM) looks up the right pages (retrieval) before writing the answer.
5. Interview question: Why use RAG instead of fine-tuning to add company knowledge?
Model answer: RAG adds knowledge at query time, is cheap to update (just re-index the documents) and can cite its sources, while fine-tuning mainly changes behaviour and style.

Now do the same for this task:
Explain the architecture behind modern LLM chatbots such as ChatGPT (GPT), Claude and Gemini for a fresher preparing for an AI/ML interview.
```

---

## 5. How to Run (llm.ipynb)

1. Put `llm.ipynb` in your `day7` folder (replace your existing one, or copy its cells into it).
2. Create a `.env` file in the same folder:
   ```
   GEMINI_API_KEY=your-key-here
   ```
   and add `.env` to `.gitignore`.
3. Open the notebook in VS Code, select a Python kernel, and **Run All**.
4. The notebook will:
   - send all 5 prompts to the LLM with identical settings,
   - show each answer,
   - run automatic checks (format, coverage) and record tokens and time,
   - let you add manual scores,
   - print the best technique and save `results.csv`, `results.md` and `responses/*.md`.
5. Paste the table from `results.md` into Section 7 below.

---

## 6. How I Judge "Best"

**A. Automatic checks (15 points)**

| Check | Points |
|---|---|
| All 5 required sections present | 5 |
| Core components has exactly 5 bullets | 1 |
| Mentions ChatGPT/GPT, Claude and Gemini | 1 |
| Key concepts covered (transformer, attention, token, embedding, pre-training, fine-tuning, alignment/RLHF, next-token prediction) | 8 |

**B. Manual rubric (15 points)**: Accuracy, Clarity and Depth, each scored 1 to 5 after reading the answers.

**C. Cost and speed (not scored, used as a tie-breaker):** input tokens, output tokens, seconds.

**Final score** = average of A and B (or A alone if B is not filled yet).

---

## 7. Results (fill after running the notebook)

| Technique | final(15) | auto(15) | manual(15) | input tokens | output tokens | seconds |
|---|---|---|---|---|---|---|
| 1. Zero-shot | | | | | | |
| 2. One-shot | | | | | | |
| 3. Few-shot | | | | | | |
| 4. Chain-of-Thought | | | | | | |
| 5. Few-shot + CoT | | | | | | |

### Observations (write 1 to 2 lines each)

- **Format following:** which prompts matched the 5-section format exactly?
- **Content quality:** which answers were most accurate and specific?
- **Hallucination:** did any answer state exact details about closed models that are not public?
- **Cost:** how many more input tokens did few-shot use compared with zero-shot? How many more output tokens did CoT use?

### Conclusion

> **Best performing technique:** ______________________
> **Why:** ______________________
> **Best value for money (quality per token):** ______________________

---

## 8. What to Expect (hypothesis to test, not a result)

These are common patterns, so you can check whether your run agrees:

- **Few-shot and one-shot** usually follow the required format most closely, because the examples show exactly what to copy.
- **Zero-shot** on a modern model often gives a good answer too, with small format slips (extra headings, 4 or 6 bullets).
- **CoT** mainly adds length. For an *explanation* task there is usually little quality gain, and some newer models already reason internally. CoT helps most on **multi-step reasoning or maths**.
- **Few-shot + CoT** is the most expensive in tokens, and only worth it if it clearly beats few-shot alone.

If your results differ, that is a valid finding. Write down why.

---

## 9. Limitations (mention these in your conclusion)

- **One run per prompt:** LLM outputs vary, so repeat the run to confirm the winner.
- **One task and one model:** the best technique can change for other tasks or models.
- **Automatic checks measure format and keywords, not truth:** that is why the manual accuracy score matters.
- **LLM-as-judge is biased** toward its own style, so use it only as a second opinion.

---

## 10. Quick Interview Q&A

**What is zero-shot prompting?**
Giving only the instruction, with no examples.

**What is few-shot prompting?**
Giving a few input-output examples in the prompt so the model copies the pattern. The model's weights are not changed; this is "in-context learning".

**What is Chain-of-Thought?**
Asking the model to show intermediate reasoning steps before the final answer, which improves multi-step reasoning.

**Few-shot vs fine-tuning?**
Few-shot only changes the prompt for that request and needs no training. Fine-tuning updates model weights and suits large, stable, repeated needs.

**Downside of few-shot?**
More input tokens (cost and context window), and a model may copy the examples too literally.

**When does CoT not help?**
Simple factual or formatting tasks, and with models that already reason internally.

**How do you evaluate prompts fairly?**
Fix the model, temperature and task; use the same output format; combine automatic checks with human scoring; repeat the runs.
