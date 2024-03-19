# Hate Speech and Offensive Language Detection

## Overview
This project aims to perform sentiment analysis on Twitter data to classify tweets into categories of hate speech, offensive language, or neither. The project utilizes machine learning techniques and natural language processing (NLP) to analyze and classify the sentiment expressed in tweets.

## Table of Contents
- [Project Overview](#overview)
- [Project Structure](#structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Preprocessing](#preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
- `data_input/`: Contains the datasets used for training and evaluation.
- `notebooks/`: Jupyter notebooks for data exploration, preprocessing, model training, and evaluation.
- `src/`: Source code for preprocessing, model training, and evaluation.
- `models/`: Saved trained models.
- `results/`: Results and evaluation metrics.

## Dependencies
- Python 3.x
- Jupyter Notebook (for running the notebooks)
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- NLTK
- TensorFlow or PyTorch (for deep learning models)
- [IMBLEARN](https://github.com/scikit-learn-contrib/imbalanced-learn) (for handling class imbalance)
- fastAPI
- pydantic

## Installation
1. Clone the repository:
https://github.com/abhinowo/LanguageDet.git
2. Install dependencies:
pip install -r requirements.txt


## Usage
1. Navigate to the `notebooks/` directory and run the Jupyter notebooks for data exploration, preprocessing, model training, and evaluation.

## Data
- The datasets used in this project can be found in the `data_input/` directory.
- The main dataset contains labeled tweets with categories of hate speech, offensive language, or neither.
- Additional data preprocessing may be required, such as removing noise,  and addressing class imbalance.

## Preprocessing
- Text preprocessing techniques are applied to clean and tokenize the tweets, including removing special characters, URLs, usernames, and extra spaces.
- Stopwords are removed, and words are lemmatized or stemmed to normalize the text data.

## Model Training
- Various machine learning and deep learning models are trained on the preprocessed data, including logistic regression, decision trees, random forests, support vector machines, and neural networks.
- Hyperparameter tuning and model selection techniques are employed to optimize performance.

## Evaluation
- Models are evaluated using appropriate evaluation metrics such as accuracy, precision, recall, F1-score, and confusion matrices.
- Techniques for handling class imbalance are applied and evaluated, such as oversampling (SMOTE), undersampling, and cost-sensitive learning.

## Results
- Evaluation results are saved in the `model/` directory.
- Comparative analysis of different models and techniques is provided to identify the best-performing approach.

## Future Work
- Integration of real-time data streaming and sentiment analysis for live monitoring of social media platforms.
- Deployment of the trained model as a web application or API for broader usage.

## Contributing
Contributions to the project are welcome! Feel free to submit bug reports, feature requests, or pull requests.
