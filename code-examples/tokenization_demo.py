from transformers import AutoTokenizer

# Choose a tokenizer (you can try different models)
model_name = "bert-base-uncased"  # You can also try "gpt2", "roberta-base", etc.
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Input text
text = "Transformers are revolutionizing NLP!"

# Tokenize the text
tokens = tokenizer.tokenize(text)
input_ids = tokenizer.convert_tokens_to_ids(tokens)

# Add special tokens (for models like BERT)
encoded_input = tokenizer(text, return_tensors="pt")

# Display results
print(f"🔍 Original Text: {text}")
print(f"🧩 Tokens: {tokens}")
print(f"🔢 Token IDs: {input_ids}")
print(f"📦 Model Input Format: {encoded_input}")

# Decoding back to text
decoded_text = tokenizer.decode(input_ids)
print(f"🔄 Decoded Text: {decoded_text}")
