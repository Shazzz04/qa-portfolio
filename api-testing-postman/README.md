# API Testing & Automation Project (Postman)

## 📌 Project Overview
This project demonstrates professional API testing and automation using **Postman**. It covers the full lifecycle of testing a RESTful API, including functional CRUD operations, data validation, and advanced security/error-handling scenarios.



## 🔧 Tools & Environment
* **Testing Tool:** Postman
* **Scripting:** JavaScript (Postman Sandbox)
* **Version Control:** GitHub
* **Mock API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com)

## ✅ Scope of Testing
The suite consists of **19 Test Cases** designed to validate the reliability and security of backend endpoints:

* **CRUD Validation:** Verified `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` methods.
* **Status Code Testing:** Ensured correct returns for `200 OK`, `201 Created`, `400 Bad Request`, and `404 Not Found`.
* **Response Validation:** * **Headers:** Validated `Content-Type` and `Charset`.
    * **Body:** Verified JSON structure and data types (String/Number).
    * **Performance:** Confirmed response times are consistently `< 1000ms`.
* **Negative & Security Testing:** * Testing behavior with **Missing Required Fields**.
    * Simulating **Unauthorized Access** (Missing/Invalid Tokens).
    * Handling **Malformed JSON** syntax.

## 📊 Test Execution Summary
| Category | Total Tests | Status |
| :--- | :--- | :--- |
| **Functional (CRUD)** | 10 | ✅ Pass |
| **Validation (Headers/Time)** | 4 | ✅ Pass |
| **Security & Error Handling** | 5 | ⚠️ 1 Pass / 4 Fail* |

> **Note on Security Results:** In cases TC_API_15, 16, and 17, the mock API bypassed security headers (returned `200 OK` instead of `401 Unauthorized` or `403 Forbidden`). In a real-world production environment, these would be documented as **critical security vulnerabilities**.



## 📁 Project Structure
* `API_Test_Suite.json`: The exported Postman collection containing all 19 tests and automation scripts.
* `README.md`: Project documentation and summary.
* `Execution_Screenshots/`: Evidence of passed test runs within the Postman console.

## 🚀 Instructions to Run
1. **Import** the `API_Test_Suite.json` into your Postman Workspace.
2. Ensure the request URL is set to `https://jsonplaceholder.typicode.com`.
3. Open the **Collection Runner** in Postman.
4. Click **Run Collection** to execute all automated tests and view the results in the console.

---
*This project showcases my ability to write automated test scripts in JavaScript to validate API responses instantly and demonstrates a "test-to-break" mindset by uncovering how systems handle bad data.*
