# ♻️ EcoFinds – Sustainable Second-Hand Marketplace

A web application built for the **Odoo x Paradox Hackathon** to promote conscious consumerism through the buying and selling of second-hand items. EcoFinds helps extend product lifecycles, reduce waste, and make sustainable choices easier for everyone.

---

## 🧠 Problem Statement

**EcoFinds – Empowering Sustainable Consumption through a Second-Hand Marketplace**

Create a user-friendly and engaging desktop + mobile-friendly platform that allows users to register, list pre-owned items, browse available listings, and manage carts and previous purchases.

---

## 🚀 Features Implemented

### 🔐 User Authentication
- Secure **signup and login** using email and password
- Basic profile setup and editing (username, email)

### 📦 Product Listings
- Create listings with:
  - Title
  - Description
  - Category
  - Price
  - Image placeholder
- View and manage own listings (CRUD)

### 🧭 Browsing & Discovery
- Browse all available products
- **Filter by category**
- **Search** products by keyword

### 🛒 Purchase Flow
- Add products to **cart**
- View **cart contents**
- Track **previous purchases**

---

## 💻 Tech Stack

| Technology      | Purpose                        |
|----------------|---------------------------------|
| **Flask**       | Backend framework               |
| **SQLite**      | Lightweight local DB            |
| **WTForms**     | Form handling                   |
| **Flask-Login** | Authentication & session mgmt   |
| **Jinja2**      | Templating engine               |
| **HTML/CSS**    | Frontend UI                     |

---

## 📸 Demo Video

🎥 **[Watch the Demo](https://drive.google.com/file/d/1K6Y1ODTk-z7hMlctHgXAsGMDNS0MNdEX/view?usp=drive_link)**  
> _(Click the link to see the full working flow of the application)_

---

## 🗂️ Project Structure

EcoFinds/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ └── forms.py
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ ├── product_list.html
│ ├── product_form.html
│ ├── product_detail.html
│ ├── cart.html
│ └── previous.html
├── Static/
│ └── style.css
├── instance/
│ └── ecofinds.db
├── run.py
├── init_db.py
├── requirements.txt
└── README.md


---

## 🛠️ Running the App Locally

### 1. Clone the Repository

git clone https://github.com/satyamsharma815/EcoFinds.git
cd
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python run.py

Visit <https://mediumspringgreen-marten-366046.hostingersite.com/>in your browser to use the application.

Team Details
Team Number: 237

Team Members:

Satyam Sharma (@satyamsharma815)

GitHub Repo: https://github.com/satyamsharma815/EcoFinds




🙌 Thank You!
