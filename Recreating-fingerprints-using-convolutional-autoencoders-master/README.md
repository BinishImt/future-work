# Recreating Fingerprints Using Convolutional Autoencoders

Build a Neural network that is capable of recreating or reconstructing fingerprint images.

<img src= "Images/cover.gif">

## Problem Statement

Collecting fingerprints dataset by using Autoencoders recreating fingerprints

## Architecture

<img src= "Images/Architecture.PNG">

## Explanation

The dataset that I’m using is the FVC2002 fingerprint dataset. It consists of 4 different sensor fingerprints namely Low-cost Optical Sensor, Low-cost Capacitive Sensor, Optical Sensor and Synthetic Generator, each sensor having varying image sizes. The dataset has 320 images, 80 images per sensor.

Download dataset: http://bias.csr.unibo.it/fvc2002/databases.asp

#### Training Dataset

<img src= "Images/Train_dataset.png">

#### Tranning Model

<img src= "Images/Model_tranning.png">

## Output
Finally, you can see that the validation loss and the training loss both are in sync. It shows that your model is not overfitting: the validation loss is decreasing and not increasing, plotted graph on 'Training Loss' and 'Validation Loss'

##### Plot

<img src= "Images/Plot.png">

##### Recreated Fingerprints

<img src= "Images/Output_recreated_images.png">

## Blog

Please read this medium blog for more information - https://towardsdatascience.com/recreating-fingerprints-using-convolutional-autoencoders-5c576e479d4f
