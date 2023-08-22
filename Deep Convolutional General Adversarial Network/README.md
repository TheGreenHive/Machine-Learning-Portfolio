### Important note!!!
The following was created by following a tutorial available [here](https://www.tensorflow.org/tutorials/generative/dcgan).
# Deep Convolution General Adversarial Network
## Purpose
The notebook named [fashion_generator.ipynb](https://github.com/TheGreenHive/Machine-Learning-Portfolio/blob/main/Deep%20Convolutional%20General%20Adversarial%20Network/fashion_generator.ipynb) trains on images using the fashion mnist dataset to create new original images using a Deep Convolution General Adversarial Network (DCGAN). The images at each epoch are available, and there is also a [dcgan.gif](https://github.com/TheGreenHive/Machine-Learning-Portfolio/blob/main/Deep%20Convolutional%20General%20Adversarial%20Network/dcgan.gif) file that shows the progression of the model as it trains.
## How it Works
The GAN works by using two models that work in tandem to create images. The generator model (the artist) creates images that it believes the discriminator model (the art critic) will classify as real. As these models both get better at the same speed, the images do as well. It is, however, difficult to get both the models to develop at the same speed so the hyperparameters must be tuned accordingly.
