from django.shortcuts import render , redirect
from django.http import JsonResponse 
from django.urls import reverse
import requests



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
        url = f'{base_url}?amount={number_of_questions}&category={category_id}&difficulty=easy&type=multiple'

        # Fetch JSON data from the URL
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Save the JSON data in the session
            request.session['json_data'] = data
            context = {'json_data': data}  # Pass the JSON data to the template
            return render(request, 'questions1.html', context)
        else:
            return render(request, 'error.html')  # Render an error page if unable to fetch data
    else:
        return render(request, 'quiz_form.html')  # Render the form page if not a POST request
def finalscore(request):
    if request.method == 'POST':
        # Get the JSON data from the session (assuming it's stored there)
        json_data = request.session.get('json_data')

        # Initialize variables for correct and total questions
        total_questions = len(json_data['results'])
        correct_questions = 0

        # Iterate over each question and extract the selected answer
        i=0
        for i, question in enumerate(json_data['results']):
            
            # Construct the name of the radio button input for this question
            radio_button_name = f'question{i+1}_choice'
            # Get the selected answer for this question from request.POST
            selected_answer = request.POST.get(radio_button_name)
            print(selected_answer)

            # Check if the selected answer matches the correct answer
            if selected_answer == question['correct_answer']:
                correct_questions += 1

        # Calculate the percentage of correct questions
        percentage = (correct_questions / total_questions) * 100

        # Pass the score data to the template
        context = {
            'total_questions': total_questions,
            'correct_questions': correct_questions,
            'percentage': percentage
        }
        return render(request, 'finalscore.html', context)
