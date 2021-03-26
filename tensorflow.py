# Configurações iniciais para fazer o tensorflow rodar corretamente com a GPU
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


# Ler imagens de uma pasta
import tensorflow as tf

IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
imgs_path = 'um_diretório_acima_do_das_imagens'

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    imgs_path,
    label_mode=None,
    seed=50,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE)
  
# Layer a ser adicionado no modelo para deixar o valor dos píxels entre [-1, 1]  
# layers.experimental.preprocessing.Rescaling(1./127.5, offset=-1)
