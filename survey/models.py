from survey import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200))
    number_of_yes_votes = db.Column(db.Integer, default=0)
    number_of_no_votes = db.Column(db.Integer, default=0)
    number_of_maybe_votes = db.Column(db.Interger, default=0)
    
    def __init__(self, question_text, number_of_yes_votes=0, number_of_no_votes=0, number_of_maybe_votes=0):
        
        self.question_text = question_text
        self.number_of_yes_votes = number_of_yes_votes
        self.number_of_no_votes = number_of_no_votes
        self.number_of_maybe_votes = number_of_maybe_votes
        
    def vote(self, vote_type):
        if vote_type == 'yes':
            self.number_of_yes_votes += 1
        elif vote_type == 'no':
            self.number_of_no_votes += 1
        elif vote_type == 'maybe':
            self.number_of_maybe_votes += 1
        else:
            raise Exception("Invalid vote type!")
        
    