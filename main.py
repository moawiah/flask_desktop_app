from flask import Flask, render_template, request, redirect, url_for
from models import TaskManager
import webview
import threading

app = Flask(__name__)
task_manager = TaskManager()


@app.route('/')
def index():
    tasks = task_manager.get_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        task_manager.add_task(task_name)
        return redirect(url_for('index'))
    return render_template('add_task.html')


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))


def start_flask():
    app.run()


if __name__ == "__main__":
    # Start Flask app in a separate thread
    threading.Thread(target=start_flask).start()

    # Open the Flask app in a desktop window using PyWebView
    webview.create_window('My Flask App', 'http://127.0.0.1:5000')
    webview.start()
