# Ransomware Prediction in Bitcoin Transactions

This repository contains a machine learning project that predicts ransomware attacks in Bitcoin transactions. The project includes a trained model and a Streamlit-based web application for real-time prediction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [App Interface](#app-interface)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Bitcoin is a cryptocurrency used for transactions in blockchain technology. Ransomware attacks are emerging as a major source of malware in Bitcoin transactions. While many ransomware prediction techniques have been proposed, there is a need for more suitable approaches using machine learning techniques.

This project focuses on developing a machine learning model to predict specific types of ransomware attacks in Bitcoin transactions. The project includes a web application built with Streamlit for easy interaction and real-time predictions.

## Features
- **Machine Learning Model**: Trained on a dataset of Bitcoin transactions to detect ransomware attacks.
- **Streamlit Web App**: An interactive web application for real-time prediction of ransomware types.
- **User Input**: Users can input transaction details like year, day, length, weight, count, looped, neighbor, and income to predict the ransomware type.

## Installation

### Prerequisites
- Python 3.7 or above
- Anaconda (optional, for environment management)
- Required Python libraries:
  - pandas
  - numpy
  - scikit-learn
  - joblib
  - streamlit

### Steps to Install

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Ransomware-Prediction-Bitcoin-Transactions.git
    cd Ransomware-Prediction-Bitcoin-Transactions
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Usage
1. **Open the Streamlit app**: After running the app, a local URL will be provided, which you can open in your web browser.
2. **Enter transaction details**: Input the year, day, length, weight, count, looped, neighbor, and income values related to the Bitcoin transaction.
3. **Get prediction**: Click on the "Predict" button to see the predicted ransomware attack type.

## Model Details
The machine learning model used in this project was trained on a custom dataset of Bitcoin transactions. The model predicts six specific types of ransomware attacks:
- montrealCryptXXX
- montrealCryptoLocker
- paduaCryptoWall
- princetonCerber
- princetonLocky
- white

The dataset includes features such as year, day, length, weight, count, looped, neighbor, and income.

## App Interface
The web app interface allows users to input transaction details manually. After submitting the details, the app will display the predicted ransomware attack type based on the trained model.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Demo Video
https://github.com/user-attachments/assets/86cc7462-b5bb-49dd-9f02-6cbf50a2ec9f


