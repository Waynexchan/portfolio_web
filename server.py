from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('/<string:page_name>.html')
def html_page(page_name='index'):
    return render_template(f'{page_name}.html')

def write_to_file(data):
    with open('database.txt',mode='a') as new_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        new_file.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer=csv.writer(database,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
          data=request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou.html')
      except:
          return 'Did not save to database'
    else:
        return 'something went wrong'

if __name__ =='__main__':
    app.run(debug=True)