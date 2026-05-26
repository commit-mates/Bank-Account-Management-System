# **1\. Introduction**

## **1.1 Purpose**

The purpose of this project is to develop a modern web-based Bank Account Management System using FastAPI, React JS, and PostgreSQL. The system will allow users to securely manage bank accounts and perform banking operations through a responsive web application.

The application will support:

* Creating and managing bank accounts  
* Depositing and withdrawing funds  
* Viewing account balances and account details  
* Maintaining transaction history  
* Persistent data storage using PostgreSQL  
* Secure REST API communication  
* Real-time frontend interaction using React  
* Input validation and exception handling

This project demonstrates:

* REST API development using FastAPI  
* Frontend development using React JS  
* PostgreSQL database integration  
* SQLAlchemy ORM implementation  
* Pydantic validation  
* CRUD operations  
* Error handling and security practices  
  ---

  ## **1.2 Scope**

The Bank Account Management System enables users to:

* Create Savings and Checking accounts  
* Deposit funds into accounts  
* Withdraw funds from accounts  
* View account balances  
* View account information  
* Maintain complete transaction history  
* Access banking operations through a web interface  
* Persist account and transaction data using PostgreSQL  
* Prevent invalid or unauthorized operations

The system is intended for:

* Educational and academic purposes  
* Backend and frontend development learning  
* Banking system simulation  
* REST API development practice  
* Database management implementation  
* Full-stack portfolio development  
  ---

  # **2\. System Overview**

The application follows a client-server architecture.

* React Frontend  
*        ↓  
* FastAPI Backend API  
*        ↓  
* Business Logic Layer  
*        ↓  
* SQLAlchemy ORM  
*        ↓  
* PostgreSQL Database


The frontend communicates with the backend through REST APIs.  
The backend processes business logic, validates requests, and interacts with PostgreSQL for persistent storage.

---

# **3\. Technology Stack**

| Component | Technology |
| ----- | ----- |
| Frontend | React JS |
| Backend Framework | FastAPI |
| Programming Language | Python |
| Database | PostgreSQL |
| API Documentation | Swagger UI |
| Version Control | Git/GitHub |

---

# **4\. Functional Requirements**

# **4.1 Authentication Module (Future Enhancement)**

## **Description**

Provides user authentication and authorization for secure banking operations.

## **Functionalities**

* User registration  
* User login  
* JWT authentication  
* Protected API routes  
* Session management

  ## **Possible Endpoints**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | /auth/register | Register user |
| POST | /auth/login | Login user |
| GET | /auth/profile | Get user profile |

  # **4.2 Account Management Module**

  ## **Description**

Manages customer bank account information and banking operations.

## **Account Entity**

| Attribute | Description |
| ----- | ----- |
| account\_id | Unique account ID |
| account\_number | Unique bank account number |
| account\_holder\_name | Name of account holder |
| account\_type | Savings / Checking |
| balance | Current account balance |
| created\_at | Account creation timestamp |

---

## **Functionalities**

* Create new accounts  
* Display account details  
* Update account information  
* Delete accounts  
* Check account balances  
* Retrieve all accounts  
  ---

  ## **API Endpoints**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | /accounts | Create account |
| GET | /accounts | Retrieve all accounts |
| GET | /accounts/{id} | Retrieve account by ID |
| PUT | /accounts/{id} | Update account |
| DELETE | /accounts/{id} | Delete account |

  ---

  # **4.3 Transaction Management Module**

  ## **Description**

Handles banking transactions including deposits and withdrawals.

## **Transaction Entity**

| Attribute | Description |
| ----- | ----- |
| transaction\_id | Unique transaction ID |
| account\_id | Linked account ID |
| transaction\_type | Deposit / Withdrawal |
| amount | Transaction amount |
| transaction\_time | Timestamp of transaction |
| status | Success / Failed |

---

## **Functionalities**

* Deposit funds  
* Withdraw funds  
* Validate transactions  
* Maintain transaction history  
* Prevent insufficient balance withdrawals  
* Store transaction logs  
  ---

  ## **API Endpoints**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | /transactions/deposit | Deposit funds |
| POST | /transactions/withdraw | Withdraw funds |
| GET | /transactions/{account\_id} | Retrieve transaction history |

  ---

  # **4.4 Frontend User Interface Module**

  ## **Description**

Provides responsive user interaction through a web-based interface using React JS.

## **Frontend Pages**

| Page | Description |
| ----- | ----- |
| Dashboard | System overview |
| Create Account | Create bank accounts |
| Account Details | Display account information |
| Deposit Page | Deposit funds |
| Withdraw Page | Withdraw funds |
| Transaction History | Display transaction records |
| Error Page | Handle invalid routes |

---

## **Frontend Features**

* Responsive user interface  
* Form validation  
* Dynamic account display  
* API integration using Axios  
* Real-time transaction updates  
* Error notifications and alerts  
  ---

  # **4.5 Database Module**

  ## **Description**

Stores account and transaction data persistently using PostgreSQL.

---

## **Database Tables**

# **1\. accounts**

## **Purpose**

Stores customer bank account information.

| Column | Type |
| ----- | ----- |
| account\_id | SERIAL PRIMARY KEY |
| account\_number | VARCHAR(20) UNIQUE |
| account\_holder\_name | VARCHAR(100) |
| account\_type | VARCHAR(20) |
| balance | NUMERIC(12,2) |
| created\_at | TIMESTAMP |

---

# **2\. transactions**

## **Purpose**

Stores all banking transaction records.

| Column | Type |
| ----- | ----- |
| transaction\_id | SERIAL PRIMARY KEY |
| account\_id | INTEGER |
| transaction\_type | VARCHAR(20) |
| amount | NUMERIC(12,2) |
| transaction\_time | TIMESTAMP |
| status | VARCHAR(20) |

---

# **3\. system\_logs**

## **Purpose**

Tracks system activities and application errors.

| Column | Type |
| ----- | ----- |
| log\_id | SERIAL PRIMARY KEY |
| action | VARCHAR(100) |
| status | VARCHAR(20) |
| log\_time | TIMESTAMP |
| details | TEXT |

---

# **5\. Non-Functional Requirements**

## **5.1 Performance**

* API requests should execute efficiently.  
* Database queries should execute with minimal delay.  
* Frontend pages should load quickly.  
* Transactions should process in real time.  
  ---

  ## **5.2 Reliability**

* Account and transaction data must persist between executions.  
* Transactions must execute accurately.  
* Failed database operations should rollback automatically.  
* APIs should handle errors gracefully.  
  ---

  ## **5.3 Maintainability**

* Modular code structure  
* Reusable services and components  
* Separation of concerns  
* Easy debugging and testing  
* Organized frontend and backend architecture  
  ---

  ## **5.4 Security**

* Validate all user inputs  
* Prevent invalid database operations  
* Secure API endpoints  
* Implement JWT authentication in future versions  
* Prevent unauthorized account manipulation  
  ---

  # **6\. Input Validation Requirements**

| Validation | Rule |
| ----- | ----- |
| Empty fields | Not allowed |
| Account number | Must be unique |
| Deposit amount | Must be positive |
| Withdrawal amount | Must be positive |
| Balance validation | Insufficient funds not allowed |
| Account type | Must be valid |
| Numeric fields | Numeric validation required |
| API request body | Must follow schema validation |

  ---

  # **7\. Error Handling Requirements**

The system should handle the following scenarios:

| Error Type | Handling |
| ----- | ----- |
| Invalid input | Display validation warning |
| Database connection failure | Show server error |
| Insufficient funds | Prevent withdrawal |
| Invalid account number | Show error message |
| SQL execution failure | Rollback transaction |
| Duplicate account number | Prevent duplicate creation |
| Invalid API route | Return 404 response |
| Unauthorized request | Return authentication error |

---

# **8\. System Design**

# **8.1 Backend Architecture**

* Routes Layer  
*       ↓  
* Services Layer  
*       ↓  
* Database Layer  
*       ↓  
* PostgreSQL  
    
  ---

  # **8.2 Frontend Architecture**

* React Components  
*        ↓  
* Pages  
*        ↓  
* API Services  
*        ↓  
* FastAPI Backend  
    
  ---

  # **8.3 Backend Modules**

| Module | Responsibility |
| ----- | ----- |
| routes | API endpoints |
| services | Business logic |
| models | SQLAlchemy models |
| schemas | Pydantic validation |
| database | Database connection |
| utils | Validation and exceptions |

  ---

  # **9\. File Structure**

* bank-management-system/  
* │  
* ├── backend/  
* │   │  
* │   ├── app/  
* │   │   ├── main.py  
* │   │   ├── database.py  
* │   │   │  
* │   │   ├── models/  
* │   │   │   ├── account.py  
* │   │   │   ├── transaction.py  
* │   │   │  
* │   │   ├── schemas/  
* │   │   │   ├── account\_schema.py  
* │   │   │   ├── transaction\_schema.py  
* │   │   │  
* │   │   ├── routes/  
* │   │   │   ├── account\_routes.py  
* │   │   │   ├── transaction\_routes.py  
* │   │   │  
* │   │   ├── services/  
* │   │   │   ├── account\_service.py  
* │   │   │   ├── transaction\_service.py  
* │   │   │  
* │   │   ├── utils/  
* │   │   │   ├── validators.py  
* │   │   │   ├── exceptions.py  
* │   │  
* │   ├── requirements.txt  
* │  
* ├── frontend/  
* │   │  
* │   ├── src/  
* │   │   ├── components/  
* │   │   ├── pages/  
* │   │   ├── services/  
* │   │   ├── App.js  
* │   │  
* │   ├── package.json  
* │  
* ├── README.md  
    
  ---

  # **10\. Workflow**

  ## **Step 1**

User opens the React web application.

## **Step 2**

Frontend sends API requests to FastAPI backend.

## **Step 3**

Backend validates incoming request data.

## **Step 4**

Business logic processes banking operation.

## **Step 5**

SQLAlchemy interacts with PostgreSQL database.

## **Step 6**

Database updates account and transaction data.

## **Step 7**

Backend returns API response.

## **Step 8**

Frontend displays updated information to the user.

---

# **11\. API Design Overview**

## **Account APIs**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | /accounts | Create account |
| GET | /accounts | Get all accounts |
| GET | /accounts/{id} | Get account details |
| PUT | /accounts/{id} | Update account |
| DELETE | /accounts/{id} | Delete account |

---

## **Transaction APIs**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | /transactions/deposit | Deposit funds |
| POST | /transactions/withdraw | Withdraw funds |
| GET | /transactions/{account\_id} | View transaction history |

---

# **12\. Future Enhancements**

Possible future upgrades include:

* JWT authentication system  
* Role-based access control  
* Admin dashboard  
* Email/SMS transaction alerts  
* Interest calculation automation  
* Loan management system  
* ATM simulation  
* Mobile banking application  
* Docker containerization  
* CI/CD pipeline integration  
* Cloud deployment using AWS/Azure/GCP  
* REST API versioning  
* Redis caching  
* Microservice architecture  
  ---

  # **13\. Expected Outcomes**

The system should:

* Manage bank accounts efficiently  
* Perform secure deposits and withdrawals  
* Persist all data using PostgreSQL  
* Provide RESTful API architecture  
* Deliver responsive frontend interaction  
* Maintain accurate transaction history  
* Handle exceptions gracefully  
* Demonstrate modern full-stack development architecture  
* Provide scalable backend and frontend implementation  
* Serve as a portfolio-ready banking web application

