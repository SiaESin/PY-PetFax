from flask import (Flask, url_for)

from flask_migrate import Migrate
# factory 
def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P0tter619@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    
    @app.route('/')
    def index():
        return 'Hello, PetFax!'
        
    #register pet blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # with app.test_request_context():
    #     print(url_for('pet.show_pet', id="1"))
    return app