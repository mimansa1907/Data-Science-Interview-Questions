# Convolutional Neural Networks

## Basics of CNN

### What is a Convolutional Neural Network(CNN or ConvNet)? List different layer of a CNN.
Covolutional Neural Network are a special type of Neural Network that work effectively for image data. It converts a spatial data to some meaningful classifyable output. A basic convolutional network is made of stack of distinct types of layers. They are:
1. Input Layer - It holds all the values of an input vector exteded along distinct dimensions. For example in images, it holds pixel values of the image for width, height and channel size(depth)
2. Conv Layer -  This layer consists of learnable filters, each filter has smaller dimensions are compared to images but posses same depth at the input. These filter are responsible for learning different features of the input images.  
3. Relu Layer - 
4. Pooling Layer - 
5. Fully Connected Layer -


### What are filter in CNN layers?
Filters are small spatial learnable matrices that are applied to input by convolution operation. They are used for detecting distinct aspects of images like edges, corners or textures. As the number of layers increase in a CNN layer, high level filters learn more complex features of the images. The values or weights of the filter matrix are learned during training time via backpropagation and gradient descent that minimizes loss function.


### What is translation invaraince and tranlsation equivaraince?
Translation invariance -  If a certain property of an object does not change with it's positional shift , i.e either left or right, up or down it is called as translation invaraince.

Translation Equivaraince - Consider a function f and g, both are said to be transilational equivariant if f(g(x)) = g(f(x)). In case of computer vision, if an image is first translated and given to CNN or first given to CNN then translated both will give the same output.

### What makes CNN translation invaraint?
The main reason that a CNN achieves translation invariance is because of convolutional and max pooling layers. The convolutional network reduces image to it's feature at the respective positions. Max pool layers takes these features , outputting the max of the grid making the positional information of features irrelevant, as we are selecting only those cells in the grid that have maximum information. When an image travels deeper into the network , due to compound effect of multiple max pool layers, the positional informtation becomes irrelevant to a great extent.

### Why invaraince is not needed in semantic segmentation? Explain significance of positional information.


### What is pooling in CNN layers? Also explain different pooling types available?
In pooling one convolves the features-maps after cnn layers with filter such that the feature map is downsampled by certain factor. along length and breadth dimension. There are different types of pooling, the most common in average and max pooling. Consider a 2 x 2 max pooling filter with stride of 2, when such filter is glided over an image it will store the max of 4 image grid cells into one cell, doing similar acroos the image. This way only highly relevant feature information is passed to the further layers in the CNN network. Similarly in average pooling the average of image covered by the filter is taken and put to a single cell. General filter size of 2x2 with stride 2 or 3x3 filter with stride 2 is considered. Taking too large filter for pooling can be destructive in the sense that it will result in too much information loss.

### Explain advantages and disadvantages of pooling.
[src](https://towardsdatascience.com/pooling-layers-for-convolutional-neural-networks-cnn-6cf2480668e2)
**Advantages**
Reduce Overfitting — Pooling keeps the key information in each feature map thereby reducing noise and aiding in curtailing the risk of overfitting. Its a form of feature selection.
Computational Efficiency — Reducing dimensionality means fewer operations, rendering the result more computationally efficient.
Invariance — Pooling recognises features in the image even if they are subject to translation, rotation, or scale. This is useful if we only care about if a feature is present and not where it is such as classification tasks. If say we are trying to detect a cat and in one image it is slightly translated on the image, then pooling neurons will still be active as its looking at a region. This means pooling can create translation, rotation and scale invariance to the network.

**Disadvantages**
Loss of Information — By reducing the dimensionality of the feature map, naturally there will some information loss during this process that could be useful. Pooling is inherently quite destructive.
Hyperparamter Tuning — Pooling layers introduce more hyperparameters to the CNN, therefore making the tuning process more time consuming.
Smoothing — Similar to loss of information, but through consolidating the features we may lose some fine grain details about an image.
Invariance Undesirable — Invariance is not always wanted for certain computer vision tasks such as semantic segmentation.

### What is stride in CNN layers? Also explain what happens on changing it's size?
Stride refers to the number of pixels by which a filter is moved over the image for convolutional. The main purposes of having stride is to increase computational speed and dimension reduction. For example if the stride is 2, this means the filter is moved over the image by jumping 2 pixel columns, this results is reduced size feature map. If stride size is increasese, there occurs information loss as some pixels are missed by the filter.

### What is feature extractions and feature map in CNN?
Feature extraction refers to the process of identifying meaningful patterns in the raw input data. For this learnable filter of a specific size is used to convolve over the image, extracting distinct pattern in input data. The output of the convolution operation is a know as feature map or activation map.


### Does the size of the feature map always reduce upon applying the filters? Explain why or why not.
Yes, feature map reduces in size based on the stride and pooling layers used at the end of conv layer. To presereve size of input we have to pad images such that the size reduction by stride or pooling layers doesn't change.

### What are effects of stride, filter, pooling layers and padding on size of feature map?
Stride:
1. Increase size: Increases computation efficiency, help in dimension reduction, leads to information loss.
2. Decrease size: Less information loss

Filter:
1. Decrease filter size: 

Pooling layer:

Padding:

### Why the number of filters increase as we go deeper into the CNN network?
[src](https://datascience.stackexchange.com/questions/55545/in-cnn-why-do-we-increase-the-number-of-filters-in-deeper-convolution-layers-fo)
The higher the number of filters, the higher the number of abstractions that your Network is able to extract from image data. The reason why the number of filters is generally ascending is that at the input layer the Network receives raw pixel data. Raw data are always noisy, and this is especially true for image data.

Because of this, we let CNNs extract first some relevant information from noisy, "dirty" raw pixel data. Once the useful features have been extracted, then we make the CNN elaborate more complex abstractions on it.

That is why the number of filters usually increases as the Network gets deeper, even though it doesn't necessarily have to be like that.

### How to calculate size of feature map?
1. Passing through Convolutional layer = (W-F+2P)/(S+1)
2. Passing through Pooling layer = (W-F)/(S+1)

### How can we prevent size reduction of image across consecutive layers of a CNN? // Explain padding and it's type
Padding is used to preserve spatial information of image after convolution on feature map. For this extra pixels are added along border of the image. There are two types of paddings:
1. Valid - No extra pixels are added, the feature map after convolutional layer is 
2. Same - Extra pixels are added on the border , such that size of feature map in same as input image.

### What is Flattening layer in CNN?
### Why do we add FCC layers at the end of CNN layers?
### State different classification functions used for binary and multi-class classification? Explain each of them.
Sigmoid, Softmax
### How does basic training of a CNN works? How are weights of the filter calculated?
### Why do we prefer Convolutional Neural networks (CNN) over Artificial Neural networks (ANN) for image data as input?
### Briefly explain the two major steps of CNN i.e, Feature Learning and Classification.
### How to capture corner information more efficiently in a CNN?
### Explain the significance of “Parameter Sharing” how it reduces number of parameters and “Sparsity of connections” in CNN.
### How CNN layer helps in dimensionality reduction?
### List different applications of CNN. (Object detection, segmentation, key-point)
### What is sequence to sequence learning in CNN?
### What is the purpose of data preprocessing in Computer Vision?

## CNN Model Tuning
### What is Batch Normalization?
### What is Drop-out layer?
### Explain relevance of augumentation in training
### What is transfer-learning?
### What is fine-tuning?
### What is Vanishing Gradient?
### How can be solve problem of vanishing gradients? (Deep Residual learning)  and other methods
Mainly occurs with sigmoid or tanh type activation function. Both brings output to a very small space[0-1].
How to recognize it:
1. Check changes in loss- if it is not changing then VG occured.
2. Weights - Plot graph, epoch vs value graph.

5 ways to resolve Vanishing Gradient
1. Reduce model complexity - try using shallow network
2. Using ReLu activation function - but might cause dying relu, came leaky relu
3. Proper weight intialization -Glorait, Xavier
4. Batch Normalization
5. Residual Network

## What happens if we initialize all the neiron weigths to 0?
1. Symmetry problem, all neuron learn similar features.
2. No gradient flow for neirons with relu, leading to dead neurons
3. Inefficent learning due to uniform gradient

## Exploding gradients
1. occurs in rnn

### What are different methods of regularization in CNN?
1. Layer dropout
2. Increase data size
3. L1-L2 for weight
4. Augumentation
5. Early stopping
6. Batch Normalization
7. Gradient clipping

### What are loss functions used in CNN?
### Can you explain the concept of backpropagation and its role in training deep neural networks?
### What is mean squared error (MSE), and how is it used in evaluating regression models in Computer Vision?




## Objection Detecetion, Segmentation and Tuning
### What is object detection and object locaization>
### What is instance segmentation?
### What is object localiztion?
### How does gradient descent works?
### Describe the process of image segmentation.
### What is the purpose of edge detection in Computer Vision?
### What is object detection, and how is it different from object recognition?
### What is the purpose of Non-Maximum Suppression (NMS) in object detection?
### How does image classification differ from image segmentation?
### What are the advantages and disadvantages of using CNNs for image classification?
### Can you explain how data imbalance can affect the performance of a Computer Vision model?
### What are some common techniques for reducing overfitting in deep learning models?
1. Regularization - Dropout
2. Add more data
3. Data Augumentation
4. Early stopping
5. Cross-validation

### What are some common metrics used for evaluating object detection algorithms?

### How does the concept of batch normalization help in training deep neural networks?
Help in tackling internal-covariate shift.

Adv.
1. Helps in achieving covergence faster
2. Creates stabilized training -> can have wider range of hyperparameter
3. Can act as a regularuzation - increases randomness in newtork
4. Reduce effects of weight intialization as contour is circle.

Working:
1. Always applied on Mini-Batch GD
2. Apply in layer by layer basis
z11 -> zn11 -> g(zn11) -> a11

zn11 = (z11 - U)/sigma ## Whyy??? As it may not be always necessary to have normalization
Zn11 = gamma*Zn11 + beta [gamma=1,beta=0] ## Learnable params
every neuron has it's own gamma and beta param

We track U and sigma while training , take their exponentially weigted average to find normalization  og input in testing.

### Exponentially weigthed moving average,
EWMA(t) = beta*EWMA(t-1) + (1-beta)theta(t) ## [0-1]





### What are some challenges associated with real-time object detection?
### Can you explain the concept of semantic segmentation?
### How does depth estimation work in Computer Vision?
### What are some common metrics used for evaluating object detection algorithms?

Can you explain the concept of image denoising?
Describe the concept of histogram equalization and its applications in image processing.
What is optical character recognition (OCR), and how is it implemented in Computer Vision?
Describe the concept of image stitching and its applications.
Can you explain the concept of image pyramid in Computer Vision?
Describe the concept of image inpainting.
Describe the concept of image super-resolution.
What are some emerging trends in Computer Vision research and applications?

Object detection algorithms?
1. Multi-stage detector
2. Single-stage detector






# Popular CNN Architecture


### List some predefined neural acrhitectures that combat vanishing gradients.


### 

# Autoencoders

### What are autoencoders?

### List few application of autoencoders.





## References
https://www.youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF
https://github.com/cs231n/cs231n.github.io/blob/master/convolutional-networks.md#overview
https://www.analyticsvidhya.com/blog/2021/05/20-questions-to-test-your-skills-on-cnn-convolutional-neural-networks/
https://climbtheladder.com/convolutional-neural-network-int erview-questions/
https://github.com/masmahbubalom/InterviewQuestions/tree/main

