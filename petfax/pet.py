from flask import (Blueprint, render_template)
import json

pets=json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show_pet(id):
    pet = [pet for pet in pets if pet['pet_id'] == id]
    return render_template('pets/show_pet.html', pet=pet)
    
