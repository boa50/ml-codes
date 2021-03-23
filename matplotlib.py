# Salva uma imagem gerada pelo matplotlib em disco
import matplotlib.pyplot as plt

plt.imshow(image, cmap='gray')
plt.savefig('nome_arquivo.png')
