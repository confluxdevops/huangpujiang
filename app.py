from flask import Flask, render_template

app = Flask(__name__)

# 记录访问次数的变量
visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    return render_template('index.html', count=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
