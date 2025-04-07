List of different **techniques** and **architectural patterns** commonly used with **LLMs (Large Language Models)** to enhance, optimize, or specialize their capabilities in real-world applications:

---

### 🔌 **Client/Serving Techniques**
These are methods to interact with LLMs via APIs or client setups:

1. **MCP Client (Multi-Chain Prompting)** – A way to manage and combine multiple prompts in a chain for more complex reasoning or tasks.
2. **LangChain** – A framework to chain prompts, memory, agents, and tools together around LLMs.
3. **LLM Client SDKs (e.g., OpenAI SDK, HuggingFace Transformers)** – Native clients to call LLM APIs easily.
4. **LLM-as-a-Service (e.g., DeepSeek, Claude, GPT-4 API)** – Access to hosted LLMs via API endpoints.
5. **WebLLM / Local LLM Clients** – Running LLMs on the edge (browser or local machine).

---

### 📚 **Data Augmentation Techniques**
Used to enhance the LLM’s knowledge or relevance:

6. **RAG (Retrieval-Augmented Generation)** – Combines LLM with external search/knowledge base to fetch relevant data before generation.
7. **FiD (Fusion-in-Decoder)** – Similar to RAG but fuses retrieved documents directly in the decoding phase.
8. **Memory-Augmented Models** – Incorporates short-term or long-term memory to retain context.
9. **Prompt Tuning / Soft Prompting** – Optimizing prompts using learnable vectors instead of plain text.

---

### 🧠 **Fine-Tuning & Training Techniques**
Used to adapt or specialize LLMs:

10. **Fine-Tuning (Full or Partial)** – Training the model on domain-specific data.
11. **LoRA (Low-Rank Adaptation)** – Efficient fine-tuning using low-rank matrices to reduce training cost.
12. **PEFT (Parameter-Efficient Fine-Tuning)** – Family of methods like LoRA, adapters, prefix-tuning.
13. **Instruction Tuning** – Fine-tuning LLMs on instruction-following tasks (e.g., FLAN, Alpaca).
14. **RLHF (Reinforcement Learning with Human Feedback)** – Fine-tuning models based on human preference data.

---

### 🕸️ **Architecture & Design Patterns**
For LLM-based systems:

15. **Agentic Workflows** – Use agents (LLM-based) to plan and execute tasks autonomously using tools (e.g., AutoGPT, LangGraph).
16. **Function Calling / Tool Use** – LLM calls external APIs/tools to augment capabilities.
17. **Multi-Agent Systems** – Several LLM agents collaborating or competing on tasks.
18. **Tree of Thought (ToT)** – Branching reasoning paths for more robust decision-making.
19. **Graph of Thought (GoT)** – Advanced version of ToT where reasoning paths form a graph.

---

### 🧾 **Prompt Engineering Techniques**
To control or guide LLM output:

20. **Zero-shot / Few-shot Prompting**
21. **Chain-of-Thought Prompting (CoT)** – Encourages the model to reason step by step.
22. **Self-Consistency** – Run multiple CoT paths and pick the most frequent answer.
23. **ReAct (Reason + Act)** – Encourages the LLM to reason before using external tools.
24. **Meta-Prompting** – Prompts that generate new prompts or strategies.

---

### 📦 **LLM Application Infrastructure**
To improve performance or UX:

25. **Caching (e.g., Redis for prompt-response caching)**
26. **Streaming Responses** – For real-time token-by-token output.
27. **Rate Limiting and Monitoring** – To handle traffic and errors effectively.
28. **Embeddings and Vector Stores (e.g., FAISS, Pinecone)** – For semantic search and similarity.
29. **Context Compression / Summarization** – Reducing previous context into summaries.

---
