import re

def count_adverbs(sentence):
    result = re.findall(r'\b\w+ly\b', sentence)
    return len(result)


sentence_1 = "She ran hurriedly towards the stadium."
sentence_2 = "Ilya ran hurriedly towards the stadium."
sentence_3 = "She ate the lasagna heartily and noisily."

print(count_adverbs(sentence_3))