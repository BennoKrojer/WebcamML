from modeling.dataloader import get_image_paths
import tensorflow as tf
from PIL import Image
import config

df = get_image_paths()

image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WIDTH = 224
train_data_gen = image_generator.flow_from_dataframe(df, x_col='path', y_col='label',
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     class_mode='raw',
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH))

base_model = tf.keras.applications.MobileNetV2(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
                                               include_top=False,
                                               weights='imagenet')

base_model.trainable = True
print(base_model.summary())
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1)
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

model.compile(loss='mse',
              optimizer=optimizer,
              metrics=['mae', 'mse'])

model.fit(train_data_gen, epochs=2)

example = Image.open(config.images/'2020-06-20_12-45-00.jpg')
array = tf.keras.preprocessing.image.img_to_array(example)

model(example)