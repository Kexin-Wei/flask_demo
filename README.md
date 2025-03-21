# Flask Demo

This is a simple Flask Demo.

## Requirement
- python 3.6 or later
- Flask `pip install flask`

## Running the Application

1. Clone the repository.

2. Run `python -m flask --app test.py run` in the terminal.

3. Open your web browser and go to `http://127.0.0.1:5000`.

## Features
- `http://127.0.0.1:5000/` showing a simple message.

    ![](/readme_resource/main.png)

- `http://127.0.0.1:5000/test` page showing a simple message from template

    ![](/readme_resource/test.png)

- `http://127.0.0.1:5000/test/<name>` page showing a simple message with name from template

    ![](/readme_resource/test_name.png)

- `http://127.0.0.1:5000/login` page showing a simple login form
    - showing error when submit the wrong username and password
    - redirect to `test/<name>` page when submit the correct username and password
    
    ![](/readme_resource/error.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.