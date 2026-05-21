from transformers import pipeline

classifier = pipeline(
"text-classification",
model="g25ait2131/mlops-assign2"
)

text = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

result = classifier(text)

print(result)