# Salva uma imagem gerada pelo matplotlib em disco
import matplotlib.pyplot as plt

plt.imshow(image, cmap='gray')
plt.savefig('nome_arquivo.png')


# Cria um gif a partir de um conjunto de imagens salvas em disco
import glob
import imageio

anim_file = 'imagem_gerada.gif'

with imageio.get_writer(anim_file, mode='I') as writer:
  filenames = glob.glob('imagens_origem*.png')
  filenames = sorted(filenames)
  for filename in filenames:
    image = imageio.imread(filename)
    writer.append_data(image)
