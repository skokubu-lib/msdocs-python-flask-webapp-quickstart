import os  
from slack_bolt import App  
from slack_bolt.adapter.flask import SlackRequestHandler  
from flask import Flask, request  

app = App(token=os.environ["SLACK_BOT_TOKEN"], signing_secret=os.environ["SLACK_SIGNING_SECRET"])  

@app.event("app_mention")  
async def command_handler(body, say):  
    text = body['event'].get('text')  
    print(f"Received message: {text}")  
    await say('おはよう！')  # この行を追加して、すぐに返答するようにします。  
    if 'おはよう' in text:  
        await say('おはよう！')  

flask_app = Flask(__name__)  
handler = SlackRequestHandler(app)  

@flask_app.route("/slack/events", methods=["POST"])  
def slack_events():  
    print("Received request at /slack/events")  # この行を追加  
    return handler.handle(request) 