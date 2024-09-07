# Django Registration Form

This project is a simple **Django-based registration form** that validates user input, including custom password validation rules. The form uses Bootstrap for styling, making it responsive and user-friendly.

## Features

- **User Registration Form**: Includes fields for username, email, and password.
- **Custom Password Validation**: Ensures the password meets specific requirements, including:
  - At least 8 characters long
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one number
  - Contains at least one special character (`@`, `$`, `!`, `%`, `*`, `?`, `&`)
- **Success & Error Messages**: Display a success message when the form is submitted successfully and error messages if the validation fails.
- **Bootstrap Integration**: The form uses Bootstrap for a modern, responsive design.
- **Floating Labels**: Clean design using floating labels from Bootstrap to display input field placeholders.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Bootstrap (integrated via CDN)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/django-registration-form.git
    cd django-registration-form
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install django
    ```

4. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to `http://127.0.0.1:8000/accounts/register/` to view the form.

### Usage

- Fill out the registration form.
- If the password meets all validation criteria, a success message will be displayed.
- If any validation rules are violated, error messages will guide the user to correct the input.
