from flask import (Flask, url_for)

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello, PetFax!'
    
    
    #register pet blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    # with app.test_request_context():
    #     print(url_for('pet.show_pet', id="1"))
    return app