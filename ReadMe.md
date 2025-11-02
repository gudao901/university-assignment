# README.md
## Project Overview
CLIUniApp and GUIUniApp are developed for the University of Technology Sydney to facilitate student self-enrolment and admin student management. The system supports two user roles (students and admins) with dedicated functionalities, storing all student data in a `students.data` file for persistent access.

### Core Features
- **Student Functions**: Registration, login, enrolling in up to 4 subjects, removing subjects, viewing enrolment details, and changing passwords.
- **Admin Functions**: Viewing all students, grouping students by grades, categorizing students into PASS/FAIL, removing individual students, and clearing the entire student database.
- **Dual Interface**: CLI (CLIUniApp) for full functionality (students and admins) and GUI (GUIUniApp) for students to perform basic enrolment operations.

## System Requirements
- Python 3.8 or higher
- No external dependencies (uses only Python's built-in libraries: `tkinter`, `os`, `json`, `re`, `random`, `functools`)

## Source Code Structure
```
project-root/
├── src/
│   ├── controllers/
│   │   ├── admin.py                    # Admin menu and management 
│   │   ├── enrolment.py                # Student enrolment-related operations
│   │   ├── student.py                  # Student CLI registration/login 
│   │   ├── student_gui_controller.py   # GUI student login/registration/change password 
│   │   ├── subject_gui_controller.py   # GUI subject/enrolment 
│   │   └── university.py               # Main CLI menu (switch between admin/student/GUI)
│   ├── models/
│   │   ├── database.py                 # Data persistence (read/write to students.data)
│   │   ├── student.py                  # Student class definition
│   │   └── subject.py                  # Subject class definition
│   ├── utils/
│   │   ├── grading.py                  # Grade calculation and PASS/FAIL logic
│   │   ├── ids.py                      # Generate unique student/subject IDs
│   │   └── validators.py               # Email and password format validation
│   └── view/
│       └── student_gui_view.py         # GUI interface (login/register/enrolment)
├── CLIUniApp.py                        # CLI application entry point
├── GUIUniApp.py                        # GUI application entry point
├── students.data                       # Data permanent(read,write,update)
└── README.md                           # Project documentation (this file)
```

## Installation and Setup Instructions
1. **Clone or Download the Project**  
   Obtain the source code package and extract it to your desired directory.
2. **Verify Python Installation**  
   Ensure Python 3.8+ is installed on your system. Run the following command to check:
   ```bash
   python --version  # or python3 --version (depending on your OS)
   ```
3. **No Additional Setup Required**  
   The project uses only Python's built-in libraries. No external packages need to be installed.

## Configurations
- **Data File**: Student data is automatically saved to `students.data` in the project root directory. This file is created on the first run if it does not exist.
- **Validation Rules** (predefined, no manual configuration):
  - Email: Must end with `@university.com` (e.g., `firstname.lastname@university.com`).
  - Password: Starts with an uppercase letter, followed by at least 5 letters and 3+ digits (e.g., `Banana123`).
  - Student ID: Auto-generated 6-digit unique number (e.g., `001234`).
  - Subject ID: Auto-generated 3-digit unique number (e.g., `011`).

## How to Run the Software
### Run CLIUniApp (Full Functionality)
1. Navigate to the project root directory using the terminal.
2. Execute the following command:
   ```bash
   python CLIUniApp.py  # or python3 CLIUniApp.py
   ```
3. The main menu will appear. Select an option by entering the corresponding letter:
   - `A`: Access Admin Subsystem
   - `S`: Access Student Subsystem
   - `G`: Launch Student GUI
   - `X`: Exit the application

### Run GUIUniApp (Student-Only GUI)
1. Navigate to the project root directory using the terminal.
2. Execute the following command:
   ```bash
   python GUIUniApp.py  # or python3 GUIUniApp.py
   ```
3. The GUI login window will open directly (for student use only).


## How to Use the Software
### Student Operations (CLI)
   - Select `S` (Student Subsystem) from the main menu.
1. **Register**:
   - Enter `r` (Register), then provide your name, valid email, and valid password.
   - A unique student ID will be generated; save it for future login.
2. **Login**:
   - Enter `l` (Login) in the Student Subsystem, then provide your email and password. If login success, go to Enrolment Menu
3. **Enrolment Menu**:
   - `e`: Enrol in a new subject (max 4 subjects).
   - `r`: Remove a subject (enter the subject ID).
   - `s`: View enrolled subjects, average mark, and status.
   - `c`: Change your password (must follow the password rule).
   - `x`: Exit to the Student Subsystem.

### Student Operations (GUI)
   - Select `G` (GUI for Student Subsystem) from the main menu, or Run GUIUniApp directly.
1. **Login/Register**:
   - Use the login window to enter your email/student ID and password.
   - Click `Register` to open a new window (Register Window) for register.
   - `Quit`: Close the application or go back to main menu (if from CLI).
2. **Register Window**:
   - Fill in name, email, and password twice, then Click `Register` to create a new account.
   - Check the email: end of @university.com (Case insensitive, Unique)
   - Check the password: Starts with an uppercase letter, followed by at least 5 letters and then 3+ digits
   - `Back`: Return to the login window.
   - `Quit`: Close the application or go back to main menu (if from CLI).
3. **Enrolment Window**:
   - `Manage Subject`: View enrolled subjects, average mark, and PASS/FAIL status. Click `Enrol Subject` to add a new subject or `Remove Subject` to delete one.
   - `Change Password`: Enter your current password and new password (twice) to update.
   - `Back`: Return to the login window.
   - `Quit`: Close the application or go back to main menu (if from CLI).

### Admin Operations (CLI)
1. Select `A` (Admin Subsystem) from the main menu.
2. Use the following options:
   - `s`: Show all students (ID, name, email, subject count, and average mark).
   - `g`: Group students by grade (HD/D/C/P/F/N/A).
   - `p`: Partition students into PASS/FAIL (PASS requires 4 subjects and average ≥50).
   - `r`: Remove a student (enter the student ID).
   - `c`: Clear all student data (requires confirmation).
   - `x`: Exit to the main menu.

## Testing the Software
### Functional Testing
- **Registration**: Test with invalid email (e.g., `test@university`) or password (e.g., `pass123`, `Apple123`) to verify error messages.
- **Enrolment**: Attempt to enrol in 5 subjects to confirm the maximum limit is enforced.
- **Admin Operations**: Test removing a non-existent student ID or clearing the database to ensure proper feedback.
- **GUI Exceptions**: Leave login fields empty or enter mismatched passwords to verify error dialogs.

### Data Persistence Test
- Register a student, enrol in subjects, and close the application.
- Re-run the app and log in to confirm the student data and enrolment details are retained.