from transformers import pipeline


import torch
print(torch.cuda.is_available())  # Should return True


generator = pipeline(
    "text-generation", 
    model="distilgpt2", 
    device=0, 
    framework="pt", 
    torch_dtype="auto"  # It will use fp16 if supported
)

res = generator(
    "In this course we will teach you",
    max_length =30,
    num_return_sequences =2,
    truncation=True
)

print(res)