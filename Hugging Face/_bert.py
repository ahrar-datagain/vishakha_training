import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Initialize the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

# Define the context and question
context = "BERT (Bidirectional Encoder Representations from Transformers) is a method of pre-training language representations. BERT can be fine-tuned for specific tasks, such as question answering, by adding an additional output layer."
question = "What does BERT stand for?"

# Tokenize the input
inputs = tokenizer.encode_plus(question, context, return_tensors='pt')

# Get the input IDs and attention masks
input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']

# Perform inference
with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)

# Extract the start and end positions of the answer
start_scores = outputs.start_logits
end_scores = outputs.end_logits

# Get the most likely start and end token indices
start_index = torch.argmax(start_scores)
end_index = torch.argmax(end_scores)

# Convert the token indices to answer text
answer_tokens = tokenizer.convert_ids_to_tokens(input_ids[0][start_index:end_index+1])
answer = tokenizer.convert_tokens_to_string(answer_tokens)

print(f"Question: {question}")
print(f"Answer: {answer}")
