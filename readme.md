![BCG-logo](chatbot_app/static/image/BCG-Logo-1.svg) 
# **Financial Chatbot**

A financial chatbot designed to provide insights from financial datasets. Built with **Flask** and **Pandas**, the chatbot answers financial questions such as revenue, profit margins, and other key financial metrics.

---

## 🚀 **Project Overview**

This chatbot enables users to:
- Ask financial questions about specific companies.
- Retrieve data such as **Total Revenue**, **Net Income**, **Profit Margin**, and more.
- Analyze financial datasets interactively.
- Summarize financial performance in a human-readable format.

The project leverages **Flask** for backend services and **Pandas** for data processing.

---

## 🛠️ **Technologies Used**

- **Python**: Backend processing and chatbot logic.
- **Flask**: Web framework for creating APIs.
- **Pandas**: Data analysis and processing.
- **HTML/CSS/JavaScript**: User interface and interactivity.
- **Vercel**: Deployment platform for serverless functions.

---

## ⚙️ **Setup Instructions**

### 📌 **1. Clone the Repository**
```bash
git clone https://github.com/Omedobi/financial-chatbot.git
cd financial-chatbot
```

### 📌 **2. Create a Virtual Environment**
```bash
python -m venv myenv
myenv\Scripts\activate     # On Windows
```

### 📌 **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 📌 **4. Run the Application Locally**
```bash
flask run
```

- Access the chatbot in your browser at: **https://bcg-financial-chatbot.vercel.app/**

---

## 🌐 **Deployment on Vercel**

### 📌 **1. Install Vercel CLI**
```bash
npm install -g vercel
```

### 📌 **2. Deploy to Vercel**
```bash
vercel --prod --yes
```

### 📌 **3. Configure `vercel.json`**
Ensure the following configuration is present:
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
}
```
---

## 💬 **Usage**

1. **Visit the Chatbot UI**  
   Open the application in your browser with `chatbot_app\static\image\BCG-Logo-1.svg`

2. **Ask a Question**  
   - Example Questions:
     - *What is the total revenue?*
     - *What is the net income?*
     - *What is the profit margin?*

3. **Receive Insights**  
   The chatbot will process your request and provide answers based on financial datasets.

---

## 📜 **License**

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute as per the license terms.

---

## 📧 **Contact**

- **Developer:** Erder 
- **Email:** ikennaomedobi@gmail.com  
- **GitHub:** [Your GitHub Profile](https://github.com/Omedobi)  

---

**Happy Chatting! 🚀💬**
