# 🏦 Banking Simulation System (Python)

A desktop-based Banking Simulation Application developed using **Python**, **Tkinter**, and **SQLite**.  
This project simulates real-world banking operations with secure authentication and OTP-based verification.
it runs with internet connection and also you need to replace app password of your gmail account in EmailHandler.py file.

---

## 🚀 Features

- 🆕 **New Account Creation**
  - Auto-generated Account Number & Password
  - Email notification with credentials
  - Input validation (Email, Mobile, Aadhaar)

- 🔐 **User Authentication**
  - Secure login using Account Number & Password
  - Forgot password feature with OTP verification

- 💼 **Account Management**
  - View account details (balance, email, Aadhaar, open date)
  - Update personal information
  - Upload and update profile picture

- 💰 **Banking Operations**
  - Deposit money
  - Withdraw money with OTP verification
  - Transfer money between accounts using OTP
  - Real-time balance updates

- 🔔 **Email & Security**
  - OTP sent via email for sensitive operations
  - Email alerts for account creation and transactions

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – GUI development
- **SQLite** – Database
- **SMTP / Gmail API** – Email & OTP service
- **Pillow (PIL)** – Image handling
- **Regex** – Input validation

---

## 📂 Project Structure

├── project01.py # Main application & GUI
├── TableCreator.py # Database & table creation
├── Generator.py # Password & OTP generator
├── EmailHandler.py # Email & OTP handling
├── mybank.sqlite # SQLite database (auto-created)

