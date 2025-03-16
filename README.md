# EAI6020 - End-to-End Machine Learning Pipeline

## **Project Overview**
This project demonstrates the development, training, and deployment of a machine learning model using a **Random Forest Classifier**. The objective is to predict target classes based on structured numerical input data. The model has been deployed using **FastAPI**, allowing real-time predictions through a REST API.

### **Key Features of This Project**
- **Data Preprocessing**: Handling missing values, feature encoding, and scaling.
- **Model Selection**: Comparison of Logistic Regression, Random Forest, and XGBoost models.
- **Hyperparameter Tuning**: Optimized Random Forest model using GridSearchCV.
- **Evaluation**: Model tested using accuracy, precision, recall, and F1-score.
- **Deployment**: API created using FastAPI to serve predictions.

## **Files in This Repository**
- `main.py` - FastAPI application for model deployment
- `test_request.py` - Python script to test the API
- `best_rf_model.pkl` - Trained Random Forest model
- `EAI6020_Report.pdf` - Final report for submission
- `requirements.txt` - Dependencies list
- `README.md` - Instructions to run the project

## **How to Run This Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/EAI6020-ML-Pipeline.git
cd EAI6020-ML-Pipeline
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Start FastAPI Server**
```bash
python -m uvicorn main:app --reload
```

### **4. Access API Documentation**
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Root Endpoint:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### **5. Test API Using Python Script**
Run `test_request.py`:

```bash
python test_request.py
```


## **Evaluation Metrics and Model Performance**

| **Model**          | **Accuracy** | **Precision** | **Recall** | **F1 Score** |
|-------------------|------------|-------------|---------|-----------|
| **Logistic Regression** | 85.2% | 81.1% | 80.0% | 80.5% |
| **Random Forest**       | 77.5% | 69.1% | 74.6% | 71.8% |
| **XGBoost**            | 82.6% | 75.9% | 80.0% | 77.9% |

After hyperparameter tuning, the **Random Forest model improved to 80.7% accuracy**, balancing precision and recall effectively.

## **Challenges Faced and Solutions**

| **Challenges** | **Solutions Implemented** |
|---------------|---------------------------|
| **Uvicorn Not Recognized** | Used `python -m uvicorn` to launch FastAPI. |
| **Pickle File Not Loading** | Verified file path and reloaded using `rb` mode. |
| **Missing Values in Data** | Applied imputation techniques before model training. |
| **API Deployment Issues** | Ensured proper installation and environment setup. |

## **Conclusion**
This project successfully trained, optimized, and deployed a Random Forest model using FastAPI. The API allows real-time model inference and can be easily extended for various machine learning applications.

