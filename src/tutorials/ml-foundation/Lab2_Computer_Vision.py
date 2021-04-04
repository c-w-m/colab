import tensorflow as tf

print("tensorflow version: {}".format(tf.__version__))

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (
    test_images, test_labels) = mnist.load_data()

"""
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])
"""

# Normalize Data (gray scale is 0-255)
training_images = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("test_loss: {}".format(test_loss))
print("test_acc: {}".format(test_acc))

classifications = model.predict(test_images)

# Exploration Exercise
# Exercise 1:
print(classifications[0])

print(test_labels[0])