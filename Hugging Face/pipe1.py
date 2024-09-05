from transformers import pipeline

classifier = pipeline("sentiment-analysis", device=0)

res  = classifier("I am not a fan of hugging face")

print(res)