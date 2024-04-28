from django.shortcuts import render , redirect
from django.http import JsonResponse 
from django.urls import reverse
import requests
import random



def index(request):
    if request.method == 'POST':
        return render(request, 'questions.html')  # Redirect to the same page for now
    # Render the initial page if it's a GET request
    return render(request, 'index.html')
# views.py
def quiz(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        number_of_questions = request.POST.get('number_of_questions')

        # Map category to category ID
        category_map = {
            'computers': '18',
            'art': '25',
            'history': '23',
            'mathematics': '19',
            'vehicles': '28',
            'anime': '31',
        }

        # Construct the URL
        base_url = 'https://opentdb.com/api.php'
        category_id = category_map.get(category, '') if category != 'random' else ''
        url = f'{base_url}?amount={number_of_questions}&category={category_id}&type=multiple'

        # Fetch JSON data from the URL
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            questions = [question['question'] for question in data['results']]
            correct_answers = {question['question']: question['correct_answer'] for question in data['results']}
            choices_list = []
            for question in data['results']:
                choices = question['incorrect_answers']
                choices.append(question['correct_answer'])
                random.shuffle(choices)
                choices_list.append(choices)

            context = {'questions': zip(questions, choices_list), 'correct_answers': correct_answers}
            
            # Store correct_answers and number_of_questions in the session
            request.session['correct_answers'] = correct_answers
            request.session['number_of_questions'] = number_of_questions
            
            print("Correct answers stored in session:", correct_answers)  # Debugging
            print("Number of questions stored in session:", number_of_questions)  # Debugging
            
            return render(request, 'questions1.html', context)
        else:
            return render(request, 'error.html')  # Render an error page if unable to fetch data
    else:
        return render(request, 'index.html')  # Render the form page if not a POST request

def finalscore(request):
    if request.method == 'POST':
        # Get the correct answers and number of questions from the session
        correct_answers = request.session.get('correct_answers')
        number_of_questions = int(request.session.get('number_of_questions', 0))

        # Initialize variables for correct and total questions
        correct_questions = 0

        # Iterate over each question and compare the selected answer with the correct answer
        for question, correct_answer in correct_answers.items():
            selected_answer = request.POST.get(question)
            if selected_answer == correct_answer:
                correct_questions += 1

        # Calculate the percentage of correct questions
        percentage = (correct_questions / number_of_questions) * 100 if number_of_questions != 0 else 0

        # Pass the score data to the template
        context = {
            'total_questions': number_of_questions,
            'correct_questions': correct_questions,
            'percentage': percentage
        }
        return render(request, 'finalscore.html', context)
