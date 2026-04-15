Travel Booking System

A simple yet efficient web application built with Flask for managing travel bookings. Users can sign up, log in, book tickets, and select seats. Additionally, administrators can view all bookings via a dedicated dashboard.

Features
User Authentication: Allows users to sign up, log in, and manage their profiles.
Ticket Booking: Users can book travel tickets (Bus, Train, Flight) with seat selection.
Seat Selection: Dynamic seat selection during the booking process.
Admin Dashboard: Admin can access and view all bookings made by users.
Technologies Used
Backend: Python (Flask)
Database: SQLite
Frontend: HTML, CSS, JavaScript
Installation and Setup
1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/your-username/travel-booking-system.git
2. Install Dependencies

Ensure you have Python installed (Python 3.6+). Install the required dependencies using pip:

pip install -r requirements.txt

If you don’t have a requirements.txt file yet, install Flask manually:

pip install flask
3. Run the Application

Navigate to the project directory and run the Flask application:

python app.py

By default, the application will be accessible at http://127.0.0.1:5000.

4. Open in Browser

Once the application is running, open your browser and navigate to http://127.0.0.1:5000 to access the application.

Project Structure
/travel-booking-system
│
├── app.py                # Main Flask application
├── index.html            # Login, Signup, and Booking page (Frontend)
├── script.js             # JavaScript for frontend interactivity
├── style.css             # Custom CSS for styling
└── README.md             # Project documentation
Database

The application uses SQLite for data storage. Upon first run, the booking.db database file will be created automatically with the following tables:

users: Stores user credentials (username, first name, last name, phone, email, password).
bookings: Stores booking information (username, service, origin, destination, date, number of passengers, seat number).
Notes
This is a beginner-level project designed to demonstrate basic Flask functionality and how to interact with a database.
For production use, security enhancements like password hashing and form validation are recommended.
License

This project is open-source and licensed under the MIT License.

Changes Made:
Clarity & Structure: Reorganized sections to ensure key points are easy to find.
Simplified Installation: Updated installation instructions to be more clear and concise.
Professional Tone: Removed redundancy and ensured consistency in phrasing.
