# Homework 10
### Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

### Documentation of 5 Resolved Errors
1. [Change Schema to fix the issue](https://github.com/vinaykath/Assignment10/issues/1)
2. [Update Error Codes for Specific Tests](https://github.com/vinaykath/Assignment10/issues/2)
3. [Enable Role Assignment During User Registration in /register Route ](https://github.com/vinaykath/Assignment10/issues/3)
4. [Update login_request_data Parameter to Use 'User' Instead of 'Email](https://github.com/vinaykath/Assignment10/issues/4)
5. [Update user_api Test Cases to Return Correct Response for Assertions ](https://github.com/vinaykath/Assignment10/issues/5)

### Installation Instructions
Follow these steps to set up the project on your local machine:

1. clone the Repository
    ```sh
    git clone git@github.com:vinaykath/Assignment10.git
    ```
2. Create and Activate a Virtual Environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install Requirements
    ```sh
    pip install -r requirements.txt
    ```
4. Run Tests Locally
    ```sh
    pytest
    ```
5. Start Docker

6. Start the App with Docker Compose
    ```sh
    docker-compose up --build
    ```
7. View OpenAPI Spec Documentation
    ```sh
    Go to http://localhost/docs to view the OpenAPI specification documentation.
    ```

### Learning Experience:
This assignment gave me a thorough look at user authentication, focusing on username and password validation. By solving specific issues, I learned about ensuring data integrity and security. I improved my skills in navigating code, finding vulnerabilities, and implementing strong solutions. This experience likely increased my understanding of security practices, data validation, and the importance of testing.

I faced challenges in coordinating changes and communicating solutions. Discussing impacts and aligning on approaches were key parts of the collaboration. Writing pytests helped me create comprehensive test cases to check my code.

Overall, this assignment deepened my technical skills in authentication and taught me about the teamwork needed to implement security measures. Through solving problems and testing, I gained a better grasp of both the technical and collaborative sides of software development.

