from datasets import load_dataset
import matplotlib.pyplot as plt

dataset = load_dataset('ashraq/esc50')
dataset


dados = dataset['train']
primeira_linha = dados[0]
primeira_linha


primeiras_linhas = dados.select(range(10))
for linha in primeiras_linhas:
    print(linha)
    print('-----')


idx_dados = 1
linha = dados[idx_dados]

plt.subplots(figsize=(30, 4))
plt.plot(linha['audio']['array'])
plt.suptitle(linha['category'])

print(f"Quantidade de dados: {linha['audio']['array'].shape}")

plt.show()