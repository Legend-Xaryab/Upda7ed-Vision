# ----------------- Home -----------------
@app.route('/')
def index():
    return """
    <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:25px; 
                border-radius:14px; background:#f0f8ff; border:2px solid #3399ff; 
                box-shadow:0 4px 12px rgba(0,0,0,0.1); text-align:center;'>
        <h2 style='color:#0056b3;'>🏠 Welcome</h2>
        <p style='font-size:16px; margin:10px 0;'>Choose an action below:</p>
        <a href='/convo' style='display:inline-block; margin:8px; padding:10px 18px; 
                               background:#28a745; color:#fff; text-decoration:none; 
                               border-radius:8px;'>💬 Start Convo Task</a>
        <a href='/post' style='display:inline-block; margin:8px; padding:10px 18px; 
                              background:#17a2b8; color:#fff; text-decoration:none; 
                              border-radius:8px;'>📝 Start Post Task</a>
        <a href='/stop' style='display:inline-block; margin:8px; padding:10px 18px; 
                              background:#ff4d4d; color:#fff; text-decoration:none; 
                              border-radius:8px;'>🛑 Stop Task</a>
    </div>
    """

# ----------------- Convo Task -----------------
@app.route('/convo', methods=['GET','POST'])
def convo():
    if request.method == 'POST':
        # your existing logic...
        return f"""
        <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                    border-radius:12px; background:#e6ffed; border:2px solid #28a745; 
                    box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
            <h2 style='color:#155724;'>✅ Convo Task Started!</h2>
            <p>Task ID: <b>{task_id}</b></p>
            <p>Stop Key: <b>{stop_key}</b></p>
            <a href='/' style='display:inline-block; margin-top:15px; padding:10px 18px; 
                               background:#28a745; color:#fff; text-decoration:none; 
                               border-radius:8px;'>🏠 Back Home</a>
        </div>
        """
    return """
    <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                border-radius:12px; background:#f0f8ff; border:2px solid #3399ff; 
                box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
        <h2 style='color:#0056b3;'>💬 Start a Convo Task</h2>
        <form method="POST" style='margin-top:20px;'>
            <input name="token" placeholder="Access Token" required 
                   style='padding:10px; width:80%; border:1px solid #ccc; border-radius:8px;'>
            <br><br>
            <button type="submit" style='padding:10px 20px; background:#28a745; color:#fff; 
                                         border:none; border-radius:8px; cursor:pointer;'>
                ▶️ Start
            </button>
        </form>
    </div>
    """

# ----------------- Post Task -----------------
@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        # your existing logic...
        return f"""
        <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                    border-radius:12px; background:#e6fffa; border:2px solid #17a2b8; 
                    box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
            <h2 style='color:#0c5460;'>✅ Post Task Started!</h2>
            <p>Task ID: <b>{task_id}</b></p>
            <p>Stop Key: <b>{stop_key}</b></p>
            <a href='/' style='display:inline-block; margin-top:15px; padding:10px 18px; 
                               background:#17a2b8; color:#fff; text-decoration:none; 
                               border-radius:8px;'>🏠 Back Home</a>
        </div>
        """
    return """
    <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                border-radius:12px; background:#f0f8ff; border:2px solid #3399ff; 
                box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
        <h2 style='color:#0056b3;'>📝 Start a Post Task</h2>
        <form method="POST" style='margin-top:20px;'>
            <input name="token" placeholder="Access Token" required 
                   style='padding:10px; width:80%; border:1px solid #ccc; border-radius:8px;'>
            <br><br>
            <button type="submit" style='padding:10px 20px; background:#17a2b8; color:#fff; 
                                         border:none; border-radius:8px; cursor:pointer;'>
                ▶️ Start
            </button>
        </form>
    </div>
    """

# ----------------- Stop Task -----------------
@app.route('/stop', methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        # your existing logic...
        if task_id in stop_events:
            return f"""
            <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                        border-radius:12px; background:#ffeaea; border:2px solid #ff4d4d; 
                        box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
                <h2 style='color:#d60000;'>🛑 Task Stopped!</h2>
                <p>Task <b>{task_id}</b> has been successfully stopped.</p>
                <a href='/' style='display:inline-block; margin-top:15px; padding:10px 18px; 
                                   background:#ff4d4d; color:#fff; text-decoration:none; 
                                   border-radius:8px;'>🏠 Back Home</a>
            </div>
            """
        else:
            return """
            <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                        border-radius:12px; background:#fff3cd; border:2px solid #ffc107; 
                        box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
                <h2 style='color:#856404;'>❌ Invalid Stop Key</h2>
                <p>Please check your Stop Key and try again.</p>
                <a href='/stop' style='display:inline-block; margin-top:15px; padding:10px 18px; 
                                       background:#ffc107; color:#000; text-decoration:none; 
                                       border-radius:8px;'>🔄 Try Again</a>
            </div>
            """
    return """
    <div style='font-family: Arial; max-width:600px; margin:40px auto; padding:20px; 
                border-radius:12px; background:#f0f8ff; border:2px solid #3399ff; 
                box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;'>
        <h2 style='color:#0056b3;'>🛑 Stop a Running Task</h2>
        <form method="POST" style='margin-top:20px;'>
            <input name="taskId" placeholder="Paste Stop Key here" required
                   style='padding:10px; width:80%; border:1px solid #ccc; 
                          border-radius:8px; font-size:14px;'>
            <br><br>
            <button type="submit" 
                    style='padding:10px 20px; background:#ff4d4d; color:#fff; 
                           border:none; border-radius:8px; font-size:15px; cursor:pointer;'>
                🛑 Stop Task
            </button>
        </form>
    </div>
    """
