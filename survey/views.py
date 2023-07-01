from flask import render_template
from survey import app
from survey.models import Question
import requests
from . import db

@app.route('/', methods=['GET'])
def home():
    questions = Question.query.all()
    context = {'questions': questions,
               'number_of_questions': len(questions)}
    return render_template('index.html', **context)

@app.route('/questions/new', methods=['GET'])
def new_questions():
    return render_template('new.html')

@app.route('/questions', methods=['POST'])
def create_questions():
    if requests.form["question_text"].strip() != "":
        new_questions = Question(question_text=requests.form["question_text"])
        db.session.add(Question)
        db.session.commit()
        message = "Successfully added a new poll!"
    else:
        message = "Poll question should not be an empty string."
    
    context = {'questions': Question.query.all(),
               'message': message}
    return render_template('index.html', **context)

@app.route('/questions/<int:question_id>', methods=['GET'])
def show_questions(question_id):
    context = {'question': db.session.get(Question, question_id)}
    return render_template('show.html', **context)

@app.route('/questions/<int:question_id>', methods=['PUT'])
def update_questions(question_id):
    question = db.session.get(Question, question_id)
    if requests.form["question_text"].strip() != "":
        question.question_text = requests.form["question_text"]
        db.session.add(question)
        db.session.commit()
        message = "Successfully updated a poll!"
    else:
        message = "Question cannot be empty."
        
    context = {'question': question,
               'message': message}
    return render_template('show.html', **context)

@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_questions(question_id):
    question = db.session.get(Question, question_id)
    db.session.delete(question)
    db.session.commit()
    context = {'questions': Question.query.all(),
               'message': 'Successfully deleted'}
    return render_template('index.html', **context)


@app.route('/questions/<int:question_id>/vote', methods=['GET'])
def new_vote_questions(question_id):
    question = db.session.get(Question, question_id)
    context = {'question': question}
    return render_template('vote.html', **context)

@app.route('/questions/<int:question_id>/vote', methods=['POST'])
def create_vote_questions(question_id):
    question = db.session.get(Question, question_id)
    if requests.form["vote"] in ["yes", "no", "maybe"]:
        question.vote(requests.form["vote"])
    db.session.add(question)
    db.session.commit()
    return render_template(f"questions/{question_id}")
