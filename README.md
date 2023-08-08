# Camera Light Streaks Detection and Noise Filtering

# abstract
This study is motivated by the application of data mining techniques to address issues caused by light streaks in images due to camera hardware anomalies. While modern camera lenses can capture vivid images in low-light environments, adjustments such as ISO, aperture, or shutter speed are often required. Nowadays, data mining and machine learning methods are applied in software to complement hardware limitations. This paper introduces methods of image preprocessing and light detection.

As part of the process to eliminate light noise, two major aspects are focused on:

Dimensionality reduction to handle high-resolution photos.
Image segmentation to distinguish light from the background elements (e.g., buildings, ceiling, streets).
In the dimension reduction phase, the use of autoencoders proves effective not only for reducing dimensions but also for denoising light streak artifacts. While the initial autoencoder used a bottleneck layer size of 128, a modification in the third phase reduces the bottleneck layer size to 16. This change aims to determine if a smaller bottleneck layer can adequately reconstruct images. The autoencoder is then employed to denoise images and identify optimal autoencoder structures.

Different autoencoder structures are compared, and the most effective one is selected for further analysis. Furthermore, a comparison is made with the variational autoencoder (VAE). The primary tools used in this study are Python TensorFlow, and the construction of autoencoders, denoise autoencoders (DAEs), and VAEs involves convolutional neural networks (CNNs).

It is important to note that while data slicing or stacking in neural networks can lead to information loss, CNNs are capable of retaining the spatial information of input images.
