# Student Manager App

A simple and user-friendly app for managing student information, written in Python.

## Features

- Adding, editing, and deleting student records
- Storing and retrieving student information such as name, major, class, GPA, date of birth, gender, hometown, and address
- Sorting and filtering student records based on various criteria
- Exporting student information to a CSV file

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following software installed on your system:

- [Python](https://www.python.org/downloads/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) library
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/) library
- [pandas](https://pandas.pydata.org/) library
- [XAMPP](https://www.apachefriends.org/download.html)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Asa-Nguyen/App_Student_Manager.git
```

2. Install the required libraries using pip:
```bash
pip install tkinter pymysql pandas
```

3. Start the XAMPP control panel and start the Apache and MySQL services

4. Open a web browser and navigate to `http://localhost/phpmyadmin`

5. Create a database named `student_manager`

6. Create a table named `data` with the following columns:

- `Id`: VARCHAR(255)
- `Name`: VARCHAR(255)
- `Major`: VARCHAR(255)
- `Class`: VARCHAR(255)
- `GPA`: VARCHAR(255)
- `Birth`: VARCHAR(255)
- `Gender`: VARCHAR(255)
- `Hometown`: VARCHAR(255)
- `Address`: VARCHAR(255)

7. Update the database connection information in the `database.py` file

8. Run the app using the command line:
```bash
python main.py
```

## Built With

- Python
- Tkinter
- PyMySQL
- pandas
- XAMPP

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Author

- Asa Nguyen

## License

This project is licensed under the [MIT License](https://github.com/Asa-Nguyen/App_Student_Manager/blob/main/LICENSE).

