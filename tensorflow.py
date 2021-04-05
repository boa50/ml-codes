### Configurações iniciais para fazer o tensorflow rodar corretamente com a GPU
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


### Ler imagens de uma pasta
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


### Salvar logs para serem usados pelo tensorboard
import tensorflow as tf
import datetime

log_dir = 'app/saves/logs/'
summary_writer = tf.summary.create_file_writer(
    log_dir + 'fit/' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

with summary_writer.as_default():
    tf.summary.scalar('gen_total_loss', gen_total_loss, step=epoch)
    tf.summary.scalar('gen_gan_loss', gen_gan_loss, step=epoch)
    tf.summary.scalar('gen_l1_loss', gen_l1_loss, step=epoch)
    tf.summary.scalar('disc_loss', disc_loss, step=epoch)
# Iniciar o tensorboard com o comando:
# $ tensorboard --logdir app/saves/logs/fit


### Criar um bloco de camada padrão
import tensorflow as tf

def downsample(filters, size, apply_batchnorm=True):
    initializer = tf.random_normal_initializer(0., 0.02)

    result = tf.keras.Sequential()
    result.add(tf.keras.layers.Conv2D(filters, size, strides=2, padding='same',
                                    kernel_initializer=initializer, use_bias=False))
    
    if apply_batchnorm:
        result.add(tf.keras.layers.BatchNormalization())
    
    result.add(tf.keras.layers.LeakyReLU())

    return result
