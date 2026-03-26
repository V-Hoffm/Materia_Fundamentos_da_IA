from transformers import pipeline

modelo = pipeline('fill-mask')
predicoes = modelo.predict('christmas is in <mask> of december')
print(predicoes)