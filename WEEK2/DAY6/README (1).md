# GenAI Fundamentals: AI vs ML vs DL vs GenAI + LLM Basics

Today's task checklist:

- [ ] Read sections 1 to 4 (concepts)
- [ ] Submit the one-page comparison note (Section 1)
- [ ] Run `tokenizer_demo.py` and screenshot a web tokenizer (Section 6)
- [ ] Run `llm.py` with Groq and save the response and token usage (Section 7)

---

## 1. One-Page Comparison Note: AI vs ML vs DL vs GenAI

**They are nested, like Russian dolls:**

```
AI  (any machine doing tasks that need "intelligence")
 └── ML  (AI that learns patterns from data instead of hand-written rules)
      └── DL  (ML using many-layered neural networks)
           └── GenAI  (DL models that CREATE new content: text, images, code, audio)
```

| | **AI** | **ML** | **DL** | **GenAI** |
|---|---|---|---|---|
| **One-line meaning** | Machines imitating human intelligence | Machines learning from data | ML with deep neural networks | DL that generates new content |
| **How it works** | Rules, search, logic, or learning | Algorithms find patterns in data (features chosen by humans) | Neural networks learn features automatically from raw data | Learns the distribution of data, then samples new outputs (e.g. predicts next token) |
| **Data needed** | Can be none (rule-based) | Small to medium | Large | Very large (internet scale) |
| **Output** | Decision or action | Prediction or label | Prediction or label | New text, image, audio, code |
| **Real examples** | Chess engine, rule-based chatbot, route planning in Google Maps | Spam filter, house price prediction, loan default model (Scikit-Learn) | Face unlock, YOLO object detection, speech recognition | ChatGPT, Claude, Gemini, DALL-E, Midjourney, GitHub Copilot |
| **Typical tools** | Prolog, expert systems, A* search | Scikit-Learn, XGBoost | PyTorch, TensorFlow | Transformers, LangChain, LLM APIs |

**Key differences in plain words**

1. **AI vs ML:** A thermostat with "if temp > 30 then cool" is AI but not ML. A model that learns your habits from data is ML.
2. **ML vs DL:** In ML you often engineer features (e.g. "word count" for spam). In DL the network discovers features itself (e.g. edges, then shapes, then faces).
3. **DL vs GenAI:** A DL classifier says "this is a cat". A GenAI model draws a new cat or writes a poem about one.

**Example that connects all four (fruit spoilage project style):**
- *AI:* the whole system that decides "discard or keep this fruit".
- *ML:* a Random Forest on NIR sensor readings to predict spoilage.
- *DL:* a CNN/YOLO on camera images to detect rot.
- *GenAI:* an LLM that reads the result and writes a plain-language report for a shopkeeper.

---

## 2. What is AI, ML, Deep Learning, GenAI (more detail)

### Artificial Intelligence
- **Narrow AI (what exists today):** good at one task (translation, recommendation).
- **AGI (hypothetical):** human-level across all tasks.

### Machine Learning: three types
| Type | Idea | Example |
|---|---|---|
| Supervised | Learn from labelled data | Email → spam/not spam |
| Unsupervised | Find structure in unlabelled data | Customer segmentation (K-Means) |
| Reinforcement | Learn by reward and penalty | Game-playing agents, RLHF for LLMs |

### Deep Learning
Neural networks with many layers. Main architectures:
- **CNN:** images (YOLO)
- **RNN/LSTM:** sequences (older NLP)
- **Transformer:** modern language models and more

### Generative AI
Model families: **LLMs** (text), **diffusion models** (images), **GANs**, **multimodal models** (text + image + audio).

---

## 3. AI Applications and Use Cases

| Domain | Use cases |
|---|---|
| Healthcare | X-ray/scan analysis, drug discovery, clinical note summarisation |
| Finance | Fraud detection, credit scoring, budgeting assistants (like Money Mentor) |
| Retail/E-commerce | Recommendations, demand forecasting, support chatbots |
| Agriculture | Crop disease detection, fruit quality grading |
| Manufacturing | Defect detection, predictive maintenance on sensors |
| Education | Personalised tutoring, auto-grading |
| Software | Code completion, test generation, bug explanation |
| Customer support | RAG chatbots over company documents |
| Content | Summaries, translation, marketing copy, image generation |
| Transport | Self-driving perception, route optimisation |

**GenAI-specific patterns used in industry:** chatbots, RAG (answer from your documents), summarisation, extraction (invoice → JSON), classification via prompts, code assistants, agents (LLM + tools).

---

## 4. LLM Fundamentals

### 4.1 Tokens
LLMs do not read characters or words. They read **tokens**: chunks of text (whole words, parts of words, punctuation, spaces).

- Rule of thumb for English: **1 token ≈ 4 characters ≈ 0.75 words**.
- Each token maps to an integer **token ID**.
- Common words are often 1 token. Rare words split: `"unbelievability"` might become `un` + `believ` + `ability`.
- **Non-English text (Kannada, Hindi, Tamil) usually needs more tokens** per word, so it costs more and fills the context window faster.
- Pricing and limits are all in tokens (input tokens + output tokens).

**Why subwords?** A fixed word list can't cover every word, and characters make sequences too long. Subwords (BPE, SentencePiece) are the compromise.

### 4.2 Embeddings
An **embedding** is a list of numbers (a vector) representing the meaning of a token or text.

- Similar meanings → vectors close together (`king` is near `queen`; `bank` near `money`).
- Closeness is measured by **cosine similarity**.
- Inside an LLM, every token ID is first converted to an embedding.
- **Separate embedding models** turn whole sentences/documents into vectors for search. This is the base of **RAG**: embed documents → store in a vector DB (FAISS) → embed the question → retrieve nearest chunks → give them to the LLM.

### 4.3 Context Window
The **maximum number of tokens the model can handle in one request**: your prompt + history + documents + the answer it writes.

- If you exceed it, the request fails or old content is dropped.
- Bigger window = can read longer documents, but costs more and long contexts can reduce accuracy ("lost in the middle").
- LLMs are **stateless**: the "memory" in a chat app is just the app re-sending earlier messages each time.

### 4.4 Other settings you will see in APIs
| Setting | Meaning |
|---|---|
| `temperature` | Randomness. Low (0 to 0.3) = focused and repeatable; high (0.8+) = creative |
| `max_tokens` | Cap on output length |
| `top_p` | Sample only from the most likely tokens that add up to probability p |
| system prompt | Instruction that sets the model's role and rules |

---

## 5. How GPT, Claude, Gemini, DeepSeek Work

### The shared core: Transformer, trained to predict the next token
All of them are built on the **Transformer** architecture (Google, 2017, "Attention Is All You Need").

**Step by step, what happens when you send a prompt:**

1. **Tokenise:** text → token IDs.
2. **Embed:** IDs → vectors (plus position information so word order matters).
3. **Transformer layers:** each layer uses **self-attention**, where every token looks at every other token to decide what matters ("it" → which noun?), followed by a feed-forward network. Dozens of layers are stacked.
4. **Output probabilities:** the model gives a probability for every possible next token.
5. **Pick one token** (influenced by temperature), append it, and **repeat** until done. The answer is generated one token at a time.

### How they are trained (3 stages)
| Stage | What happens |
|---|---|
| 1. **Pre-training** | Predict the next token over huge text/code corpora. Gives broad knowledge and language skill. Most expensive stage. |
| 2. **Fine-tuning (instruction tuning)** | Train on example question-and-answer pairs so the model follows instructions instead of just continuing text. |
| 3. **Alignment** | Use human or AI feedback (RLHF and similar methods) so answers are helpful, honest and safer. |

### Differences between the four families

| Model family | Company | Notable points |
|---|---|---|
| **GPT** | OpenAI | Decoder-only Transformer; started the ChatGPT wave; proprietary (weights not public); multimodal in newer versions |
| **Claude** | Anthropic | Transformer LLM; strong focus on safety and alignment (including a technique called Constitutional AI); known for coding and long-document work |
| **Gemini** | Google DeepMind | Built **multimodal from the start** (text, images, audio, video); very long context windows; tight Google ecosystem integration |
| **DeepSeek** | DeepSeek (China) | Open-weight models; uses **Mixture-of-Experts (MoE)**, where only part of the network activates per token, making it efficient; its R1 line focuses on reasoning trained with reinforcement learning |

> Caveat for interviews: companies do not publish full architecture details of their closed models. Say "based on public information", and don't claim exact parameter counts.

### Concepts that come up next
- **Prompt engineering:** write clear instructions, examples, and output format.
- **RAG:** retrieval plus generation, to reduce hallucination and use private data.
- **Hallucination:** confident but wrong output. The model predicts likely text, not verified facts.
- **Agents / tool use:** the LLM decides to call functions (search, database, calculator).
- **Fine-tuning vs RAG:** fine-tune to change *behaviour/style*; use RAG to add *knowledge*.

---

## 6. Tokenizer Visualisation (Task)

### Option A: Web tool (fastest, take a screenshot)
- OpenAI Tokenizer: https://platform.openai.com/tokenizer
- Tiktokenizer (shows token IDs, pick model): https://tiktokenizer.vercel.app

Paste these and compare token counts:
1. `Hello, I am learning Generative AI today.`
2. `Unbelievability is a rare word.`
3. `ನಾನು ಇಂದು ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಕಲಿಯುತ್ತಿದ್ದೇನೆ` (Kannada: see how many more tokens it needs)
4. `def add(a, b): return a + b` (code)

### Option B: Python script
Run `tokenizer_demo.py` (in this folder). It prints each token piece and its ID.

```bash
pip install tiktoken
python tokenizer_demo.py
```

**Write 3 observations in your note.** Example points to look for:
- Short common words are usually one token.
- Rare words are split into pieces.
- Spaces are often attached to the start of the next word.
- Non-English text uses many more tokens.

---

## 7. Call an LLM API (Task)

This example uses Groq's chat-completions API.

1. Create an API key at [console.groq.com/keys](https://console.groq.com/keys).
2. In PowerShell, set the key for the current terminal:

```powershell
$env:GROQ_API_KEY = "your-key-here"
.\DAY6.venv\Scripts\python.exe .\llm.py
```

Alternatively, add `GROQ_API_KEY=your-key-here` to a `.env` file in this
directory, then run the script. It prints the response, model name, input
tokens, output tokens, and total tokens reported by Groq.

### Understanding the token usage output
| Field | Meaning |
|---|---|
| Input / prompt tokens | Tokens in what you sent |
| Output / completion tokens | Tokens in the answer |
| Total | Input + output |

Try changing `PROMPT` in `llm.py` and compare the input and output token counts.

---

## 8. Credentials and privacy

Keep your Groq API key out of the source code and never commit `.env` to
GitHub. The API has usage limits; check your Groq console for current limits.

If a cloud API key is ever pushed, revoke it immediately in the provider's
console.

---

## 9. Quick Revision Q&A

**What is the relationship between AI, ML, DL, GenAI?**
AI is the broad goal. ML is AI that learns from data. DL is ML with deep neural networks. GenAI is DL that generates new content.

**What is a token?**
A chunk of text (word or subword) that the model reads; roughly 4 characters of English.

**What is an embedding?**
A vector of numbers capturing meaning; similar meanings sit close together.

**What is a context window?**
The maximum tokens (input plus output) a model can handle in one request.

**How does an LLM generate text?**
It predicts a probability for the next token, picks one, appends it, and repeats.

**Why do LLMs hallucinate?**
They generate statistically likely text and do not check facts.

**What does temperature do?**
Controls randomness of token selection: low is focused, high is creative.

**RAG vs fine-tuning?**
RAG adds external knowledge at query time; fine-tuning changes model behaviour by further training.

**Why do Indian-language prompts cost more?**
Tokenisers are mostly trained on English-heavy text, so these scripts split into more tokens.
