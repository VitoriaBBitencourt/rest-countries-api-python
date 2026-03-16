# REST Countries API with Python

This project demonstrates how to use Python to retrieve and display country information using the REST Countries API.

The application allows the user to enter the name of a country and returns basic information such as capital, population, region, and languages.

---

## Project Overview

This project was created to practice working with APIs in Python.  
It sends HTTP requests to the REST Countries API and processes the JSON response to extract relevant information.

The goal is to understand how to:

- Send HTTP requests using Python
- Work with JSON data
- Access nested dictionaries and lists
- Structure a small Python application using functions

---

## Technologies Used

- Python
- Requests library
- REST Countries API

---

## Project Structure

```
country-api-test
│
├── main.py
├── requirements.txt
└── README.md

```

---

## How to Run the Project

1. Clone the repository

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the script

```bash
python main.py
```

4. Enter a country name when prompted.

  Example:

  ```
  Enter a country (or 'exit'): Brazil
  ```

  Example Output
  
  ```
  Country: Brazil
  Capital: Brasília
  Population: 213,421,037
  Region: Americas
  Languages: Portuguese
  ```

  API Used

  This project uses the REST Countries API:

  ```
  https://restcountries.com/
  ```

  Example endpoint:

  ```
  https://restcountries.com/v3.1/name/brazil
  ```

 --- 

## What I Practiced in This Project

- Working with APIs in Python

- Sending HTTP requests

- Handling API responses

- Parsing JSON data

- Accessing nested data structures

- Structuring Python code using functions



