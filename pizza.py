#!/home/tomaszs/python/bin/python3
from flask import Flask, request, render_template
from pizzamath import pizza_math

app = Flask(__name__)

@app.route('/pizza')
def hello() -> 'html':
    return render_template('base.html',
                            the_title = 'Pizza calculator',
                            napis = 'Compute!')

@app.route('/result', methods=['GET', 'POST'])
def compute_pizza():
    print(request.form.get('half_2'))
    try:
        pizza_1 = pizza_math(float(request.form['diameter_1']),
                            float(request.form['price_1']),
                            request.form.get('half_1'))

        pizza_2 = pizza_math(float(request.form['diameter_2']),
                            float(request.form['price_2']),
                            request.form.get('half_2'))
    except:
        return render_template('result.html',
                                the_title = 'incorrect value!',)
    return render_template('result.html',
                            the_title = 'Result',
                            half_1 = pizza_1[2],
                            surface_1 = str(pizza_1[0]) + ' cm^2',
                            cm2_price_1 = str(pizza_1[1]) + ' cm^2',
                            half_2 = pizza_2[2],
                            surface_2 = str(pizza_2[0]) + ' cm^2',
                            cm2_price_2 = str(pizza_2[1]) + ' cm^2')

app.run(debug=False)
