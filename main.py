from flask import Flask, render_template, request
import os

app = Flask(__name__)

questions = [
    {
        "question": "Which choice best maintains the tone of the passage?",
        "options": ["A) Completely boring.", "B) Utterly ridiculous.", "C) Mildly humorous.", "D) Sharply analytical."],
        "answer": "D"
    },
    {
        "question": "If 3x + 5 = 20, what is the value of x?",
        "options": ["A) 3", "B) 5", "C) 7", "D) 15"],
        "answer": "B"
    },
    {
        "question": "The author's primary purpose in the passage is to:",
        "options": ["A) Criticize an existing theory.", "B) Present a personal story.", "C) Describe a historical event.", "D) Propose a solution to a problem."],
        "answer": "C"
    }
]

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    for i, q in enumerate(questions):
        selected = request.form.get(f'q{i}')
        correct = q['answer']
        is_correct = selected == correct
        if is_correct:
            score += 1
        results.append({
            'question': q['question'],
            'selected': selected,
            'correct': correct,
            'is_correct': is_correct
        })
    return render_template('result.html', score=score, total=len(questions), results=results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
