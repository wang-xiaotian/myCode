#!/usr/bin/env python3
'''
beginner tensorflow project
https://www.tensorflow.org/tutorials/keras/classification

What is a tensor? 
it is a vector or a matrix of n-dimensions(ranks) that represents all types of data
https://www.youtube.com/watch?v=f5liqUk0ZTw

1. Define the training data
2. Define a neural network model
3. Configure the learning process
4. Train the model
5. Evaluate model
6. Predictions
'''
# tensorflow library 2.0
import tensorflow as tf

# helper libraries
import numpy as np
import matplotlib.pyplot as plt

# tensorflow 1.0 vs 2.0
print(tf.__version__)

# label a image by one of the class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# training data from keras learning dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

'''
build the model:
layer is the basic building block of neural network
The Sequential class is used to define a linear stack of network layers
https://www.kdnuggets.com/2018/06/keras-4-step-workflow.html
'''
def buildModel():
    try:
        # TODO: more in details
        # configure model; sequential, functional or others
        # only the first layer of the model requires the input dimension to be explicitly stated; the following layers are able to infer from the previous linear stacked layer
        # flatten = np.reshape()
        # dense layer https://www.youtube.com/watch?v=ohgONsuoxVs https://medium.com/@hunterheidenreich/understanding-keras-dense-layers-2abadff9b990
        
        # TODO: what each layer does? how do the parameters affect the model?
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28,28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
            #tf.keras.layers.Dense(10)
        ])
        # batch size is None as it is not set. Batch size is usually set during training phase
        print(model.summary())

        ''' configure the learning process '''
        # compile the model
        # optimizers use different algorithms: SGD RMSprop, Adam, Adadelta, Adagrad, Adamax, Nadam and Ftrl
        # loss: https://keras.io/api/losses/ The purpose of loss functions is to compute the quantity that a model should seek to minimize during training
        # 
        # metrics: A metric is a function that is used to judge the performance of your model.
        model.compile(
            optimizer = 'adam', 
            loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
        )

        ''' feed data to the model; tensorFlow 1.0 need to use Session() '''
        # the number of passes of the entire training dataset the machine learning algorithm has completed
        model.fit(train_images, train_labels, epochs=10)
        return model
    except:
        print('Bad happened in buildModel')

'''
evaluate accuracy
'''
def modelEvaluation(model):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
    print(f'\nTest Accuracy: {test_acc}, Test loss: {test_loss}')

'''
make predictions
'''
def makePredictions(model, sample):
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

    predictions = probability_model.predict(sample)

    print(f'first image predictions on all 10 labels: {predictions[0]}')
    print(f'highest confidence value of first test image: {np.argmax(predictions[0])}')
    # print detail and large image for 1 st test image
    plot_value_array(1, predictions[0], test_labels)
    _ = plt.xticks(range(10), class_names, rotation=45)
    return predictions

'''helper method to plot a individual image'''
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

'''helper method to arrange images'''
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

def plotAll(predictions):
    i = 0
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions[i],  test_labels)
    plt.show()

    # Plot the first 15 test images, their predicted labels, and the true labels.
    # Color correct predictions in blue and incorrect predictions in red.
    num_rows = 5
    num_cols = 4
    num_images = num_rows*num_cols
    plt.figure(figsize=(2*2*num_cols, 2*num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2*num_cols, 2*i+1)
        plot_image(i, predictions[i], test_labels, test_images)
        plt.subplot(num_rows, 2*num_cols, 2*i+2)
        plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()
    plt.show()

'''
how does sample data look like?
'''
def displaySampleData(train_images, train_labels, test_images, test_labels):
    print(f'Type of train images: {type(train_images)}')
    print(f'Type of train labels: {type(train_labels)}')
    print(f'train images shape: {train_images.shape}')
    print(f'first element of train images:\n{train_images[0]}')
    print(f'length of train_labels:\n{len(train_labels)}')
    

    # display the first image in train_images GUI
    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()

    print(f'Type of test images: {type(test_images)}')
    print(f'first element of test images: {test_images[0]}')
    print(f'Type of test labels: {type(test_labels)}')
    print(f'test images shape: {test_images.shape}')
    print(f'length of train_labels: {len(test_labels)}')

    # display the first image in test_images GUI
    plt.figure()
    plt.imshow(test_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()


def main():
    displaySampleData(train_images, train_labels, test_images, test_labels)
    model = buildModel()
    modelEvaluation(model)
    predictions = makePredictions(model, test_images)
    plotAll(predictions)

if __name__ == "__main__":
    main()
