# Regularization
# Activation Function
https://www.v7labs.com/blog/neural-networks-activation-functions

# Why should acitvation function be zero centered?
In this case the gradient output always remains poisitive or negative, this implies mpre number of epochs are needed for convergence, making training slower. Hence we needed zero-centered activations if possible so that we get convergence in shorter time. They make sure that mean of activation functiom remains around 0.When activation is not zero, we normalize data to provide such case.

# Dimension Reduction - PCA, t-SNE


# How to initialize weights in a Neural Network?

# What should we consider while selecting activation functions?
- Vanishing gradient and Exploding gradient

# Parametric and Non-Parametric ML models
# Loss Function

# Gradient Descent
# Liner Regression - Restrictions for dataset
# Logistic Regression
# Support Vector Machine

# Data Distribution

# Homoscadescity and Heteroscadescity


# Decision Tree
Learning Type - Supervised

Model Type - Non parametric

Problem Type - Regression and Classification

Basic working - 
1. It is a basic tree structure, which has a root, parent nodes, child nodes and leaf nodes.
2. Each node represents a condition on any particular feature, it is responsible for diving the data into further subset, each branch represents one possible outcome of that condition,each leaf node presents a classification label or a regression value.
It is basically a kind of separation of datapoints from the subset based on different conditions on distinct features. Each node and it's further branches are created based on a particular criteria which involves monitoring gini impurity or entropy or information gain or MSE to validate the split for a considered condition and feature.
**Criteria**
1. CART(Classification and Regression Tree) - uses gini index
2. ID3 (Iterative Dichotomiser 3) - Entropy function and Information gain


Data application scenarios
1. Non-linear relationship
2. Heterogeneous Data - When data has both catergorical and numerical data
3. When dataset has outliers
4. High Varaince data - Bagging boosting techniques that use DT are useful
5. Handles missing values - either by ignoring them or distributing datapoints with misiing values through distinct strategies

Hyperparameters
- Minimum number of samples per leaf
- Max depth
- Minimum sample splits
- Max Features
- splitter - best or random
- criteria 
- ccp_alpha


Overfitting handle
- By managing hyperparams
- Cost complexity pruning 

Advantages -
1. Does not put any constraint on data distribution
2. Gives intuitive understanding of the dataset
3. Inference time is very small
4. Missing values are ignorable to some extent

Disadvantages - 
1. Unstable prone to small changes in data - not robust
2. Overfitting

# Numbers of nodes in a decision tree and depth of decision tree
Depth(d) - longest path from root from leaf in a tree
Nodes - 2^(d+1) - 1 

# What pruning? State and explain its types.[https://blog.dailydoseofds.com/p/decision-trees-always-overfit-heres]
1. Cost complexity pruning (Weak Link Pruning)
Cost (C) : Number of misclassifications
Complexity (C) : Number of nodes
Tree Score : Error + alpha*T (T are terminal nodes)

a. Pre pruning -  applying max depth criteria or any other hyperparameter
b. Post pruning - First split full and create complete DT, then start pruning. Suitable for small datasets


# What can be criteria to keep max_depth and min_samples per leaf?



# Random Forest
Basic working - 

Data application scenarios - 

Hyperparameter - 


# Bagging
Basic working - 

Data application scenarios - 

Hyperparameter - 


# Boosting
Basic working - 

Data application scenarios - 

Hyperparameter - 


# Extreme Gradient Boosting
Basic working - 

Data application scenarios - 

Hyperparameter - 


# ANOVA test

# Hypothesis testing

# VIF, AIC, BIC
# Type 1 and Type 2 errors
# Z-test, T-test, P-value
# What are Parquet Files?
# GRU, RNN
# Outlier Detection
# A/B tests in online machine learning

# Regularization - L1 and L2

# How to handle skewed data?

# In what cases are missing values ignoreable?

# Explain bais and variance trade-off

# State distinct Hyperparameter tuning techinques
1. Grid Search
2. Random Search
3. BAyesian Search

# Difference between hyperparameter tuning and parameter tuning
parameter tuning - means finding relevant values of weights and baises that responsible for making a our final model function
hyperparameter tuning - means finding relevant values of varaibles that deterimine training conditions.

# ROC AUC PRecision recall defs


# Define Entropy, Information Gain, Gini Impurity [Add image]

# Difference between categorical and sparse categorical entropy.

Categorical Cross-Entropy
Categorical Cross-Entropy is used when the true labels are provided in a one-hot encoded format. Each label is represented as a binary vector, where only the correct class is marked as 1 and the rest are 0.

Characteristics:
Input Format: One-hot encoded vectors for true labels.
Output: A single loss value that quantifies the difference between the predicted probability distribution and the one-hot encoded true labels.

Formula:
For a single sample, the categorical cross-entropy loss 
𝐿
L is calculated as:

𝐿=∑𝑖=1𝐶 𝑦𝑖log⁡(𝑦^𝑖)

where:
C is the number of classes.
𝑦𝑖 is the one-hot encoded true label (1 for the correct class, 0 otherwise).
𝑦^𝑖 is the predicted probability for class 𝑖


Sparse Categorical Cross-Entropy is used when the true labels are provided as integers, representing the class indices directly. This is a more compact representation compared to one-hot encoding, especially useful when the number of classes is large.

Characteristics:
Input Format: Integer class labels for true labels.
Output: A single loss value that quantifies the difference between the predicted probability distribution and the true class indices.
Formula:
For a single sample, the sparse categorical cross-entropy loss 
𝐿
L is calculated as:
𝐿=−log⁡(𝑦^𝑐)
where:
𝑦^𝑐  is the predicted probability for the true class 𝑐

# Why opt for softmax normalization instead of standard normalizaton/
Softmax normalization reacts to small and large variation/change differently but standard normalization does not differentiate the stimulus by intensity so longest the proportion is the same.

Another problem arises when there are negative values in the logits. In that case, you will end up with negative probabilities in the output. The Softmax is not affected with negative values because exponent of any value (positive or negative) is always a positive value.


# State distinct ways to handle outliers.

# When to normalize data and for for standard scaling?

