# Face Recognition Attendance System

This project is an automated attendance system using face recognition technology. The system captures images of faces and recognizes them to mark attendance. It leverages machine learning algorithms for face detection and recognition, and integrates with Firebase for database management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Capture and store face images for attendance marking.
- Recognize faces from stored images.
- Automatically update attendance records.
- User-friendly interface for managing attendance.
- Integration with Firebase for database management.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- OpenCV
- dlib
- face_recognition library
- Firebase account

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/ishan004/Face_recognition-Attendance.git
    cd Face_recognition-Attendance
    ```

2. **Create a virtual environment (optional but recommended)**

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install additional packages if not included in `requirements.txt`**

    ```bash
    pip install opencv-python
    pip install dlib
    pip install face_recognition
    ```

5. **Set up Firebase**

    - Create a Firebase project and configure it for your application.
    - Download the `google-services.json` file from your Firebase project and place it in the project directory.

## Usage

### Initial Setup

1. **Run the initial database setup script**

    ```bash
    python initial_database.py
    ```

    This script sets up the initial Firebase database structure required for the application.

2. **Run the initial encoder setup script**

    ```bash
    python initial_encoder.py
    ```

    This script encodes the faces from the images and stores the encodings.

### Running the Application

1. **Start the web application**

    ```bash
    python webapp.py
    ```

2. **Capture and recognize faces**

    - The system will start the webcam and begin capturing faces.
    - Recognized faces will be marked as present in the attendance record.

3. **Check attendance records**

    - Attendance records will be saved in Firebase and can be accessed through the web application.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes tests for new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Firebase](https://firebase.google.com/)

---

Feel free to contribute to the project by reporting issues, suggesting features, or submitting pull requests. Your feedback and contributions are highly appreciated!

