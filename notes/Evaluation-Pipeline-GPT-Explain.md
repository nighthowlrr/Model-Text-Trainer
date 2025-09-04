### 🔹 What are the ground-truth summaries?

* The **summaries you already wrote yourself** (34 so far) are the **ground truth**.
* They represent your style, structure, and formatting.
* These are stored in your training dataset (`train.jsonl` as `"output"`).

---

### 🔹 How will it score output summaries?
The idea is to compare the model’s **predicted summary** against your **ground-truth summary** using text similarity metrics:

1. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**
   * Measures **overlap of n-grams** (e.g., words, phrases) between the model’s output and your reference.
   * Example:
     * Reference: `"Force the idea to work before rejecting it"`
     * Prediction: `"Try to make an idea work before discarding it"`
     * ROUGE would give a **high score** since many word sequences overlap.

2. **BLEU (Bilingual Evaluation Understudy)**
   * Measures how close the prediction is to the reference by looking at **precision of n-grams** (phrases in the prediction that appear in the reference).
   * It also applies a **brevity penalty** if the output is too short.

3. **Optional extras** (if you want later):
   * **BERTScore** → uses embeddings from BERT to check semantic similarity (not just word overlap).
   * **Human evaluation** → metrics never fully capture your writing style, so human spot-checking is still valuable.

---

### 🔹 Example Workflow
1. Split your 34 summaries into **train set (e.g., 28)** and **test set (e.g., 6)**.
2. Train LoRA on the train set.
3. Run inference on the test set transcripts → get predicted summaries.
4. Compare predicted summaries with your ground-truth summaries in the test set using ROUGE, BLEU, etc.
5. Report scores (e.g., ROUGE-L: 0.62, BLEU: 0.55).

---

✅ This gives you **numeric benchmarks** to track improvements as you fine-tune more or adjust prompts.
⚠️ But remember: these metrics can’t fully capture your exact **style** (Markdown formatting, “lesson-like” tone, etc.), so they’re indicators, not final judges.
