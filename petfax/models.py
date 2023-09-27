from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ =  'facts' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(100)) 
    fact = db.Column(db.Text) 