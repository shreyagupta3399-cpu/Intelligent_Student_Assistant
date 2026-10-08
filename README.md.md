# AI-Based Intelligent Student Assistant

## Project Overview

The AI-Based Intelligent Student Assistant is an educational application designed to help students analyze their academic performance and receive personalized study guidance.

The project combines basic student utilities with Artificial Intelligence and Machine Learning to predict student performance based on academic factors.

## Problem Statement

Students often have information such as marks, attendance, assignment scores, and previous exam performance, but they may find it difficult to analyze these factors together.

This project uses a Machine Learning model to predict the student's performance level and provide an appropriate study recommendation.

## Objectives

- Calculate student marks and percentage.
- Calculate attendance percentage.
- Provide study planning suggestions.
- Predict student performance using Machine Learning.
- Provide personalized recommendations based on the prediction.
- Demonstrate fundamental AI/ML concepts.

## AI/ML Concepts Used

The project demonstrates the following concepts:

- Supervised Machine Learning
- Classification
- Decision Tree Classifier
- Training and Testing Data
- Feature Selection
- Model Prediction
- Accuracy Evaluation
- AI-based Recommendation

## Machine Learning Model

A *Decision Tree Classifier* is used for student performance prediction.

### Input Features

The model uses:

1. Study Hours
2. Attendance Percentage
3. Assignment Score
4. Previous Exam Score

### Output

The model predicts the student's performance as:

- LOW
- MEDIUM
- HIGH

## Project Workflow

Student Data
↓
Study Hours + Attendance + Assignment Score + Previous Exam Score
↓
Machine Learning Model
↓
Decision Tree Classifier
↓
Performance Prediction
↓
Personalized Study Recommendation

## Existing Features

### 1. Marks Calculator

Calculates total marks and percentage based on marks entered by the student.

### 2. Attendance Calculator

Calculates attendance percentage and checks whether the student has achieved the 75% attendance requirement.

### 3. Study Planner

Provides study suggestions based on the number of hours available for studying.

### 4. AI Performance Prediction

Uses a trained Decision Tree Machine Learning model to predict the student's performance level.

### 5. AI-Based Recommendation

Provides a recommendation according to the predicted performance level.

## Technologies Used

- Python
- Scikit-learn
- Decision Tree Algorithm
- Machine Learning

## How to Run

Install the required library:

```bash
pip install -r requirements.txt