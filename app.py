from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4

app = Flask(__name__)

# In-memory database substitute
db = {}

@app.route('/')
def index():
    return render_template('index.html', items=db)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    description = request.form.get('description')
    if name:
        item_id = str(uuid4())
        db[item_id] = {'name': name, 'description': description}
    return redirect(url_for('index'))

@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit(item_id):
    if request.method == 'POST':
        db[item_id]['name'] = request.form.get('name')
        db[item_id]['description'] = request.form.get('description')
        return redirect(url_for('index'))
    return render_template('edit.html', item_id=item_id, item=db[item_id])

@app.route('/delete/<item_id>')
def delete(item_id):
    db.pop(item_id, None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
