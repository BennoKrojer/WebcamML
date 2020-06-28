from modeling.dataloader import get_image_paths
import tensorflow as tf

df = get_image_paths()

# image data generator takes our images and applies data augmentation
# this makes the image data more suitable as input for the neural network
# it also generates more training data so we get more reliable results
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)


BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WIDTH = 224
# Shift and rotation is somewhat likely in our case (webcam might be moved or rotated slightly by accident)
# So we use small value as it's not common to happen
SHIFT_DELTA = 50
ROTATION_DELTA = 5
BRIGHTNESS_FACTOR_MIN = 0.1
# Unused augmentations
# zoom_range [x.x, 1.0]


train_data_gen = image_generator.flow_from_dataframe(df, x_col='path', y_col='label',
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     class_mode='raw',
                                                     width_shift_range=[-SHIFT_DELTA,SHIFT_DELTA],
                                                     rotation_range=ROTATION_DELTA,
                                                     brightness_range=[BRIGHTNESS_FACTOR_MIN,1.0],
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH))

base_model = tf.keras.applications.MobileNetV2(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
                                               include_top=False,
                                               weights='imagenet')

base_model.trainable = False
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

model.fit(train_data_gen, epochs=100)