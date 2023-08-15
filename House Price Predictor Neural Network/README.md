# House Price Predictor Neural Network

## How to run
This directory contains two files, the csv file that contains the data for the house prices and the interactive python notebook that contains the model. The notebook has been pretrained, and to run it go to the bottom cell and enter in the desired inputs. 
*Note: the model is only trained on US house price data, therefore the output will be in US dollars and be based on the US house market.*

## Description

The data is read from the csv file and then split into testing and training sets. The data is then normalized. The model is then initialised with dense layers, as well as dropout layers to prevent overfitting. The model is trained to a maximum of 175 epochs, but early stopping is incorporated to prevent overfitting.
