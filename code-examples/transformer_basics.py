from transformers import AutoModelForCausalLM, AutoTokenizer

# Load a pre-trained transformer model and tokenizer
model_name = "gpt2"  # You can replace with other models like 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example input text
input_text = "Transformers are"

# Tokenize the input
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text using the model
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the output text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(f"🔍 Input: {input_text}")
print(f"📝 Generated Text: {generated_text}")
