from flask import render_template
from app import app

@app.errorhandler(404)
def four_o_four(error):
    """ 
    function to render the 404 page 
    """

    return render_template('404.html'), 404