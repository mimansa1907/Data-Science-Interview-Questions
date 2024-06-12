## State and explain loss functions used in deep learning for different use-case problems.
Use Case: Regression problem
1. Mean Square Error
Adv -  Easy to interpret, always differentiable, one local minima
Disadv - Error unit is squared, Not Robust to outliers

2. Mean Absoulte Error
Adv - Intuitive, robust to outliers, same unit as output
Disadv - Not differentiable, Need to calculate subgradients

3. Huber Loss (Combats effect of outliers), a combination of MSE or MAE
Adv - 
Disadv - 

Use Case: Classification problem
1. Binary Cross Entropy - Used for two classses
Output Activation must be sigmoid
Adv-  Differentiable
Disadv - Local Minima exists

2. Categorical Cross Entropy
Output Activation must be softmax
Adv - 
Disadv - 

3. Sparse Categorical
4. Hinge Loss

Use Case: Autoencoders
1. KL Diverengce

Use Case: GAN
1. Discrimanant loss
2. Min Max Loss


Use Case: Object Detection
1. Focal Loss
2. Jaccard loss
3. Dice Loss

## What is difference between loss function and cost function?
Loss function(error function) is calculated on a single training example.
Cost function is average sum of Loss function on entire batch of data.

## Different types of Gradient Decent
Most common way to optimize an algorithm. It is a way to minimize loss function.
all differ in the amount of data used for performing parameter update. There is a trade-off between accuracy of param update and time of param update.

1. Batch -  take entire dataset to make the update
2. Stochastic - We update param with each datapoint, after shuffling data. It takes more time than stochastic GD. Converges faster than Batch. Unstable loss reduction, this helps to move out of local minima, get approximate solution.Vectorization makes it faster
3. Mini Batch - Make small batches, in every epoch for each batch find loss and update param. Sme numbe rof batches and number of epochs.


## Why is batch_size given in multiple of 2?
To handle RAM effectively

## Why do we use optimizer in GD?

## What momentum does? And what is it?
Helps in navigating through non-convex functions
1. 

## State different feature selection methods use in python.
A. Supervised techniques
1. Filter based approach - Information gain, Chi-Square test, Fisher's Score, Missing value ratio
2. Wrapper-based approach - Forward selection, Backward selection, Exhauative Feature selection, Recursive feature elemenation
3. Embedded Approach - Regularization, Random forest approach

B. Unsupervised techniques - PCA, ICA, NMF, t-SNE, Autoencoder



