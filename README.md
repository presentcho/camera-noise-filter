# Camera Light Streaks Detection and Noise Filtering

This study is motivated by the application of data mining techniques to address issues caused by light streaks in images due to camera hardware anomalies. While modern camera lenses can capture vivid images in low-light environments, adjustments such as ISO, aperture, or shutter speed are often required. Nowadays, data mining and machine learning methods are applied in software to complement hardware limitations. This paper introduces methods of image preprocessing and light detection.

As part of the process to eliminate light noise, two major aspects are focused on:

1. Dimensionality reduction to handle high-resolution photos.
2. Image segmentation to distinguish light from the background elements (e.g., buildings, ceiling, streets).

## Methods
Principal Component Analysis (PCA) was used to compress images and handle the large dataset. Additionally, the K-means clustering method and Gaussian Mixture Model (GMM) were employed for image segmentation, and a comparison was made between these two methods.

For the noise filtering model, autoencoders and variational autoencoders (VAEs) were implemented. To enhance the model's performance, Gaussian noise was introduced to the images. The model was then trained using both the original images and the images with added Gaussian noise. Notably, a convolutional neural network (CNN) was utilized for denoising the images.

## Result
| Cat pics               | Dog pics               |
| ---------------------- | ---------------------- |
| ![1](img/test.png) | ![2](img/autoencoder.png) |
