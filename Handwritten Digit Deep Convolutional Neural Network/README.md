# Handwritten Digit Deep Convolutional Neural Network
Recognition of handwritten digits from the MNIST dataset.

## Training and evaluation
The training and evalution of the model is done in the digitRecognition.ipynb file. This file also imports the dataset and saves the trained model to file called mnist_predictior.h5.

## Prediction
The predict.py file needs the mnist_predictor.h5 and number.png file to run using python 3.10. When run, the code will import the model from the mnist_predictor.h5 file and the handwritten digit from number.png and predict what the number is, returning probabilities for each output.
---
## Strengths and limitations
To improve this model, more data from the MNIST dataset could be used; more dropout layers could be added and the model could be trained for longer and; the size of the neural network could be made larger. 
