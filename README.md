Phishing URL Detection using Machine Learning

This project uses machine learning to identify whether a given URL is Safe or Phishing.  
It extracts important features from URLs (like length, HTTPS, suspicious words, dots, hyphens, etc.)  
and uses a Random Forest model to classify them.

The aim of this project is to help users avoid fake or malicious websites by quickly checking URLs.


 About the Project

Phishing attacks are increasing every year. Many people accidentally click on fake banking or login pages.  
This project is a simple and lightweight tool that lets users check if a URL is suspicious.

I built this project as part of my BSc IT (Second Year) work to learn machine learning, data cleaning,  
feature engineering, and real-world model evaluation.



 Features

 Extracts meaningful URL characteristics  
 Detects phishing patterns  
 Machine learning model (Random Forest)  
 Simple prediction script  
 Beginner-friendly code structure  
 Fast and accurate  
 Easy for anyone to use  



 Project Structure

│── dataset.csv                # Raw dataset (URLs + labels) │── processed_dataset.csv      # Features extracted from URLs │── extract_features.py        # Converts URL into numeric features │── train_model.py             # Trains the ML model │── predict_url.py             # Checks if a URL is Safe/Phishing │── phishing_model.pkl         # Saved trained model │── README.md                  # Project documentation



 How the Project Works

1. Load dataset containing URLs and their labels (safe or phishing)  
2. Extract features using extract_features.py  
3. Train the model using train_model.py  
4. Save the model 
5. Predict URL safety using predict_url.py

The model learns real patterns from phishing URLs — such as suspicious words  
("verify", "login", "free", etc.), very long URLs, presence of IP addresses, and more.



 Technologies Used

- Python
- Pandas
- Scikit-Learn
- Regex
- Joblib
- VS Code
- Git & GitHub (for version control)



 How to Run This Project on Your Computer

 1. Clone the project

git clone https://github.com/<your-username>/<your-repository>.git

2. Create virtual environment

python -m venv venv venv\Scripts\activate

3. Install dependencies

pip install pandas scikit-learn joblib

 4. Train the model

python train_model.py

5. Predict a URL

python predict_url.py

Enter any URL and the program will tell you:

⚠ Phishing or ✅ Safe

Model Accuracy

The Random Forest model trained on the dataset achieved high accuracy 
(depending on dataset size).  
In my case, accuracy reached 100% on the test data used.

Future Improvements

- Add a web UI (Flask / React)  
- Add more features (URL entropy, abnormal domain patterns)  
- Use a larger dataset from Kaggle  
- Deploy on cloud  
- Add Chrome extension support  


Thank You for Checking Out My Project!
