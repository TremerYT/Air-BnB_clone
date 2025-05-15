# AirBnB Clone Project

## Description
The AirBnB Clone project is a simplified version of the AirBnB platform. It is a command-line interface (CLI) application that allows users to manage objects such as users, places, and amenities. This project is part of a larger project to build a full web application, including a front-end and back-end.

The goal of this project is to understand the fundamentals of higher-level programming, including object-oriented programming, file storage, and working collaboratively as a team using GitHub.

---

## Command Interpreter

The command interpreter is the core of this project. It allows users to interact with the application via a command-line interface to create, retrieve, update, and delete objects.

### How to Start It
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Air-BnB_clone.git
    cd Air-BnB_clone
    ```
2. Make the command interpreter executable:
    ```bash
    chmod +x console.py
    ```
3. Run the command interpreter:
    ```bash
    ./console.py
    ```

### How to Use It
The command interpreter supports the following commands:
- `create <class_name>`: Creates a new instance of a class.
- `show <class_name> <id>`: Displays the string representation of an instance.
- `destroy <class_name> <id>`: Deletes an instance.
- `all [<class_name>]`: Displays all instances or all instances of a specific class.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Updates an instance's attributes.

### Examples
1. Create a new user:
    ```bash
    (hbnb) create User
    ```
    Output:
    ```
    1234-5678-9012
    ```

2. Show a user:
    ```bash
    (hbnb) show User 1234-5678-9012
    ```
    Output:
    ```
    [User] (1234-5678-9012) {'id': '1234-5678-9012'}
    ```

3. Update a user:
    ```bash
    (hbnb) update User 1234-5678-9012 name "John Doe"
    ```

4. Delete a user:
    ```bash
    (hbnb) destroy User 1234-5678-9012
    ```

---

## AUTHORS File
The repository includes an `AUTHORS` file at the root, listing all contributors to the project. The format follows the structure of Docker's AUTHORS page, with each contributor's name and email address.

---

## Collaboration
To ensure smooth collaboration, the team uses branches and pull requests on GitHub. Each feature or bug fix is developed in a separate branch and merged into the main branch via a pull request after review. This workflow helps maintain code quality and organization.