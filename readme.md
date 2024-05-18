
# Django Quiz App

The Django Quiz App is a web application that allows users to take quizzes consisting of multiple-choice questions. It provides a user-friendly interface for answering questions, calculates the score based on the user's responses, and displays the final score at the end of the quiz.
##  Live preview
You can preview this project <a href="https://quizzy-7808719c9cd7.herokuapp.com/" target="_blank"> Here </a>

The quiz questions for this application are sourced from the Open Trivia Database API. The Open Trivia Database provides a completely free JSON API for use in programming projects. It offers a wide variety of categories and questions, making it suitable for building quiz applications like this one.

To learn more about the Open Trivia Database API and explore its configuration options, visit https://opentdb.com/api_config.php.
## Features

- Create quizzes with multiple-choice questions.
- Shuffle questions to provide a different order for each quiz attempt.
- Allow users to select one answer for each question.
- Calculate the score based on the user's responses.
- Display the final score as a percentage of correct answers.

## Installation

1. Clone the repository:

```
git clone <repository-url>
```

2. Navigate to the project directory:

```
cd django-quiz-app
```

3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

On Windows:

```
venv\Scripts\activate
```

On macOS and Linux:

```
source venv/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Run the migrations:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

8. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Usage



1. Take quizzes:

- Access the quiz-taking interface by visiting [http://localhost:8000/quiz/](http://localhost:8000/quiz/).
- Select one answer for each question and submit the quiz.
- View the final score displayed on the results page.

## Contributing

Contributions are welcome! If you'd like to contribute to the Django Quiz App, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Push your branch to your fork.
5. Submit a pull request with a detailed description of your changes.
