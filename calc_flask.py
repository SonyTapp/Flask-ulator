''' python3 -m venv venv          THIS CREATES VIRUAL ENVIROMENT
    source venv/bin/activate           ACTIVATES IT

(venv) sony@Sonys-Air...'''   

from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)
display_input = ''
sum_output = ''



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/showsum', methods=['POST'])
def show_sum():
    global display_input
    input_value = request.form['input_button']
    if input_value == 'C':
        display_input = '' 
    else:
        display_input += input_value 
    return render_template('index.html', display=display_input)



@app.route('/answer_sum', methods=['POST'])
def answer_sum():
    global sum_output, display_input

    try:
        sum_output = eval(display_input)
    except:
        sum_output = "Error"
   
    return render_template('index.html', display=display_input, display2=sum_output)




if __name__ == '__main__':
    app.run(debug=True)