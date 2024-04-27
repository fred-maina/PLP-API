import requests
url='https://opentdb.com/api.php?amount=4&category=19&difficulty=easy&type=multiple'
response = requests.get(url)
data=response.json()
answer_dict=[]
for question in data['results']:
    print(question['question'])
    answer_dict.append(question['correct_answer'])
    for answer in question['incorrect_answers']:
        answer_dict.append(answer)
print (len(answer_dict))