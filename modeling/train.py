from modeling.dataloader import get_image_paths
import tensorflow as tf
import numpy
tf.keras.optimizers.RMSprop
# Parameters
BATCH_SIZE = 32
IMG_HEIGHT = 400
IMG_WIDTH = 400
RESERVE_VALIDATION = 0.2
# Shift and rotation is somewhat likely in our case (webcam might be moved or rotated slightly by accident)
# So we use small value as it's not common to happen
SHIFT_DELTA = 50
ROTATION_DELTA = 5
BRIGHTNESS_FACTOR_MIN = 0.1
# Unused augmentations
# zoom_range [x.x, 1.0]


df = get_image_paths()

# image data generator takes our images and applies data augmentation
# this makes the image data more suitable as input for the neural network
# it also generates more training data so we get more reliable results
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2)

numpy.random.seed(41)

train_data_gen = image_generator.flow_from_dataframe(df, x_col='path', y_col='label',
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     width_shift_range=[-SHIFT_DELTA, SHIFT_DELTA],
                                                     rotation_range=ROTATION_DELTA,
                                                     brightness_range=[BRIGHTNESS_FACTOR_MIN, 1.0],
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH), subset='training')

valid_data_gen = image_generator.flow_from_dataframe(df, x_col='path', y_col='label',
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     width_shift_range=[-SHIFT_DELTA, SHIFT_DELTA],
                                                     rotation_range=ROTATION_DELTA,
                                                     brightness_range=[BRIGHTNESS_FACTOR_MIN, 1.0],
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH), subset='validation')

# for x, y in valid_data_gen:
#     print(x)
#     print(y)

base_model = tf.keras.applications.MobileNetV2(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
                                               include_top=False,
                                               weights='imagenet')
# base_model.trainable = True
# for i, layer in enumerate(base_model.layers):
#     if i > 150:
#         layer.trainable = True
print(base_model.summary())
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(4, activation='softmax')
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy', 'categorical_crossentropy'])

model.fit(train_data_gen, epochs=100, validation_data=valid_data_gen)
