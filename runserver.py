import sys
from survey import app, db
from survey import views

def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    return 0 

if __name__ == '__main__':
    sys.exit(main())
    