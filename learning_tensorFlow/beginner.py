#!/usr/bin/env python3
'''
beginner tensorflow project
'''
# tensorflow
import tensorflow as tf

# helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# print(f'Type of train images: {type(train_images)}')
# print(f'Type of train labels: {type(train_labels)}')
# print(f'train images shape: {train_images.shape}')
# print(f'first element of train images: {train_images[0]}')
# print(f'length of train_labels: {len(train_labels)}')

# print(f'Type of test images: {type(test_images)}')
# print(f'first element of test images: {test_images[0]}')
# print(f'Type of test labels: {type(test_labels)}')
# print(f'test images shape: {test_images.shape}')
# print(f'length of train_labels: {len(test_labels)}')

# # '''
# # display the first image in train_images GUI
# # '''
# # plt.figure()
# # plt.imshow(train_images[0])
# # plt.colorbar()
# # plt.grid(False)
# # plt.show()

# # train_images = train_images / 255.0
# # test_images = test_images / 255.0

# # plt.figure(figsize=(10,10))
# # for i in range(25):
# #     plt.subplot(5, 5, i+1)
# #     plt.xticks([])
# #     plt.yticks([])
# #     plt.grid(False)
# #     plt.imshow(train_images[i], cmap=plt.cm.binary)
# #     plt.xlabel(class_names[train_labels[i]])
# # plt.show()

'''
build the model

layer is the basic building block of neural network
'''

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

'''
compile the model
'''
model.compile(
    optimizer = 'adam', 
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

'''
feed data to the model
'''

model.fit(train_images, train_labels, epochs=10)

'''
evaluate accuracy
'''
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
print(f'\nTest Accuracy: {test_acc}, Test loss: {test_loss}')

'''
make predictions
'''
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

print(f'first image predictions on all 10 labels: {predictions[0]}')
print(f'highest confidence value of first test image: {np.argmax(predictions[0])}')


i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()