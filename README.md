# 📈 StartuPredict – AI-powered startup profit predictor  

---

## 🔍 Project Goal 
StartuPredict is a machine learning-based web app that predicts a startup's profit based on its **R&D spend, Administration costs, Marketing spend, and Location**. It helps entrepreneurs and analysts make **data-driven decisions** with ease.  

---

## 📖 Overview  
This project uses a **linear regression model** trained on a startup dataset to predict the estimated profit. The app is built with **Streamlit** for an interactive and user-friendly interface.  

---

## 🔄 Project Workflow  

### **1️⃣ Data Preprocessing**  
- Handled missing values and removed inconsistencies.  
- Converted categorical variables (States) into dummy variables for better compatibility with the regression model.  
- Normalized numerical values where necessary.  
- Split data into **80% training** and **20% testing** sets using `train_test_split`.

### **2️⃣ Model Building**  
- Built and trained a **Multiple Linear Regression (MLR)** model using `scikit-learn`.  
- Stored the trained model in `model.pkl` using `pickle` for easy deployment.  

### **3️⃣ Evaluation Metrics**  
- **R² Score:** ~0.94, indicating strong correlation between predicted and actual values.  
- **Mean Squared Error (MSE):** Low, ensuring minimal error in predictions.  
- **Adjusted R²:** Verified the reliability of the model with multiple input features.

### **4️⃣ Deployment**  
- Developed a clean **Streamlit** app for interactive predictions.
- Predictions are generated in **real-time** with clear output formatting.  

---

## 🛠 Tech Stack  
- **Programming Language:** Python 3  
- **Libraries Used:**  
  - **Streamlit** – Interactive web interface  
  - **Pandas** – Data manipulation and analysis  
  - **NumPy** – Numerical computations  
  - **Matplotlib** – Data visualization  
  - **Scikit-learn** – Machine learning and evaluation  
  - **Pickle** – Saving and loading the trained model  

---

## ✨ Features  
- Predict startup profits quickly with just a few inputs.  
- Simple and clean Streamlit interface for ease of use.  
- Real-time prediction powered by **Multiple Linear Regression**.  
- Beginner-friendly implementation and easy to customize.  

---

## 🔮 Future Enhancements  
- Integrate advanced models like **Random Forest** or **XGBoost** for improved accuracy.  
- Add visual dashboards for profit analysis.  
- Build an API for external integrations.  
- Deploy with Docker for scalability and portability.  

---

## 📌 How to Run Locally  

```
git clone https://github.com/yourusername/StartuPredict.git
cd StartuPredict
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀
