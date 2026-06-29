📘 Selenium Web Automation Framework - Week 3
📌 Project Overview

This project is a modular test automation framework built using Selenium WebDriver with Python and Pytest. It is part of a progressive learning assignment starting from Week 1 (Test Strategy), Week 2 (Test Script Development), and now Week 3 (Framework Design & Implementation).

The goal of this framework is to create a scalable, maintainable, and reusable automation structure using industry-standard practices such as the Page Object Model (POM), centralized configuration, and automated reporting.

🧱 Framework Architecture

The framework follows a layered structure:

tests/ → Test cases (test_home_page, test_search_movie, etc.)
pages/ → Page Object Models (HomePage, DetailPage, FavoritePage)
utils/ → WebDriver setup and helper utilities
config/ → Environment configuration (BASE_URL)
reports/ → Test execution reports (HTML)
⚙️ Key Features
Page Object Model (POM) design pattern
Centralized WebDriver management
Config-based environment setup (BASE_URL)
Reusable test components
Automated test execution using Pytest
HTML reporting using pytest-html
Stable synchronization using explicit waits
🧪 Test Scenarios Covered

The framework includes automated test cases for:

Home page load validation
Movie search functionality
Movie detail page navigation
Favorite movie feature validation
🚀 Setup & Installation

1. Clone or extract the project
   unzip week3-framework.zip
   cd week3-framework
2. Install dependencies
   pip install -r requirements.txt
   ▶️ How to Run Tests

Run all test cases using Pytest:

python -m pytest tests --html=reports/report.html

After execution, open the report:

reports/report.html
📦 Requirements
selenium
pytest
pytest-html
🧠 Design Principles

This framework follows key automation best practices:

Separation of concerns (test logic vs page logic)
Code reusability using Page Object Model
Maintainability through centralized configuration
Scalability for future test expansion
Readable and structured test design
📊 Reporting

Test execution results are generated in HTML format using pytest-html, providing:

Test execution status (PASS/FAIL)
Execution summary
Detailed test logs
📌 Future Improvements
Add logging system (log file tracking)
Integrate CI/CD pipeline (GitHub Actions)
Improve locator strategy (data-testid usage)
Add test data management layer
Implement parallel test execution
👨‍💻 Author

Automation Testing Project - Week 3
Built using Python, Selenium WebDriver, and Pytest

🔄 Continuous Integration (CI)

This project uses GitHub Actions for Continuous Integration (CI). Every push or pull request to the main branch will automatically trigger the test suite execution.

CI Workflow Steps:
Checkout repository
Setup Python environment
Install dependencies
Run Selenium test suite in headless mode
Generate HTML test report
CI Configuration File:
.github/workflows/ci.yml
How to Trigger CI:

Simply push changes to GitHub:

git add .
git commit -m "run ci pipeline"
git push origin main
Test Execution:

Tests run automatically using:

python -m pytest tests --html=reports/report.html
