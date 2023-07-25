# Automated Web Testing with Selenium, Docker Compose, Selenium Grid
This repository demonstrates how to perform automated web testing using Selenium WebDriver and Docker. The project includes sample test scenarios written in Python and organized using the Page Object Model (POM). The tests can be executed on various browsers, including Chrome, Firefox, and Edge, and can also be run in headless mode.

## Getting Started

1. **Install Python:** Ensure you have Python installed on your local machine.

2. **Setup Virtual Environment:** Create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
3. Install Dependencies: Install the required packages using pip:
```bash
pip install -r requirements.txt
```
4. Execute Tests Locally: To run the test scenarios locally, use the following command:
```bash
python -m pytest
```
## Running Tests with Docker
**Install Docker:** Ensure you have Docker installed on your machine.

**Build Docker Image:** Build the Docker image with the following command:

```bash
docker-compose build
```
**Execute Tests with Docker:** Run the tests using Docker Compose:
```bash
docker-compose up
```

## Customizing Test Execution
To select a specific browser for test execution, use the --browser flag with pytest. For example:
```bash
pytest --browser firefox
```
To run tests in headless mode, add the --headless flag:
```bash
pytest --headless
```

To retry failed tests, the RETRY_COUNT and RETRY_DELAY variables in the conftest.py file can be adjusted.

### Page Object Model (POM)
The test scenarios are organized using the Page Object Model (POM) design pattern. The pages directory contains page objects for different web pages, and the tests directory contains test scripts that utilize these page objects. This approach ensures cleaner and more maintainable code.

### Contributing
Contributions are welcome! If you find any issues or have improvements to suggest, please create a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Special thanks to the Selenium and Docker communities for providing the tools that make this project possible.

Feel free to contact me if you have any questions or need further assistance! Happy testing!
