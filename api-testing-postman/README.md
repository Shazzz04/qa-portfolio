# Intelligent Task Prioritization System – API Testing Suite

## 📌 Project Overview
**Author:** Shaza Faizer  
**Course:** Bachelors in Software Engineering (Edge Hill University)  
**Project Date:** Dec 15, 2025 – May 5, 2026

This repository contains a comprehensive API testing suite for an **Intelligent Task Prioritization System**. The project validates backend stability, data integrity, and security protocols using the JSONPlaceholder REST API as a mock production environment.



## 🔧 Tools & Technologies
* **Testing Tool:** Postman (Desktop & Web)
* **Automation:** JavaScript (Postman Sandbox)
* **Version Control:** GitHub
* **Environment:** [JSONPlaceholder API](https://jsonplaceholder.typicode.com)

## ✅ Scope of Testing
This suite covers the full lifecycle of API interactions, ensuring the prioritization system is robust against both user error and security threats.
* **CRUD Operations:** GET, POST, PUT, PATCH, DELETE.
* **Response Validation:** Status codes (200, 201, 400, 404), Headers, and Response Time.
* **Negative Scenarios:** Testing for missing fields, invalid data types, and non-existent endpoints.
* **Security Testing:** Authentication (401) and Authorization (403) handling.

## 📊 Test Coverage & Results
| Metric | Count |
| :--- | :--- |
| **Total Test Cases Executed** | 19 |
| **Passed** | 14 |
| **Failed/Identified Defects** | 5 (Security-related) |

### Key Findings
* **Critical Defect:** The API lacks strict authentication (Returned `200 OK` for requests with invalid/missing tokens in TC_API_15 & 16).
* **Performance:** All valid endpoints responded within **< 1000ms**.

## 📐 Prioritization Logic (Formula Derivation)
As part of the system design (Phase 3), the prioritization algorithm calculates task urgency using the following weighted formula:

$$P = (W_d \times D) + (W_i \times I)$$

Where:
* $P$ = Final Priority Score
* $W_d$ = Weight of the Deadline
* $W_i$ = Weight of Task Importance
* $D, I$ = Normalized data inputs

The API tests in this suite ensure that the data structures (`userId`, `id`, `title`, `body`) remain consistent to prevent calculation errors in the frontend.

## 📁 Project Files
* [**Postman Collection**](./API_Test_Suite.json) - Full JSON export of the 19 test cases.
* [**Test Case Document**](./Test_Case_Report.pdf) - Detailed spreadsheet of Expected vs. Actual results.
* **Bug Report** - Documented security flaws regarding token bypass.

## 🚀 How to Execute
1.  **Import:** Download the `.json` collection file and import it into Postman.
2.  **Environment:** Ensure the `baseUrl` is set to `https://jsonplaceholder.typicode.com`.
3.  **Run:** Open the Collection Runner and click **Run Collection** to see automated test results.

---
*This project is part of a Software Engineering degree program and demonstrates professional QA competency in API Automation.*
