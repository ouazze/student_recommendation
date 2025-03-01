# CNN-Based Student Recommendation System

## Description
This project involves training a Convolutional Neural Network (CNN) model to recommend subjects for students who are weak in specific areas. The goal is to suggest ways for students to improve their skills and develop the necessary competencies to increase their overall final score. The model is implemented using Flask, HTML, and CSS for the desktop platform.

### Key Features:
- **CNN Model**: A Convolutional Neural Network (CNN) is trained on student grades and performance data to provide personalized recommendations.
- **Web Platform**: A simple web interface built with Flask, HTML, and CSS to interact with the model and receive recommendations.
- **Multilingual Support**: The platform will provide recommendations in both Arabic and English to accommodate a wide range of students.

## Objective
The main objective of this project is to:
1. Train a CNN model to assess students' performance based on their grades.
2. Provide recommendations for subjects that students should focus on to improve their final scores.
3. Implement a user-friendly web platform for students to interact with the model and receive actionable insights.

## How it Works
1. **Data Input**: Students' grades are inputted into the system.
2. **Model Training**: The CNN model is trained using the data to predict the areas where the student needs to improve.
3. **Recommendations**: Based on the model’s output, students receive recommendations for subjects and resources to help them improve.
4. **Web Interface**: Students can access their personalized recommendations via a web interface built using Flask. The platform will provide suggestions in both Arabic and English.

## Tech Stack:
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Model**: Convolutional Neural Network (CNN)
- **Languages**: Python, HTML, CSS

## Requirements
- Python 3.10
- Flask
- TensorFlow/Keras (for CNN model)
- Other dependencies listed in `requirements.txt`

## Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/your-username/student-recommendation-system.git
cd student-recommendation-system
