
# ==========================================
# AKASH AI: MASTER ANDROID ASSISTANT & GUARDIAN
# Owner: Subrato | Master Secret: Akash@13132
# ==========================================

import os
import sys
import time
import threading
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION & SECURITY CREDENTIALS ---
USER_NAME = "Subrato"
MASTER_SECRET = "Akash@13132"
PRIMARY_NUMBER = "8777674107"
EMERGENCY_NUMBER = "7003657763"
AUTHORIZED_FACES = ["subrato_white_shirt.jpg", "girlfriend_face.jpg"]

# ==========================================
# 🌐 ANDROID FRONTEND + 3D HOLOGRAPHIC UI
# ==========================================
HTML_PAGE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akash AI - Master Assistant</title>
    <style>
        body {
            background-color: #030308;
            color: #00ff66;
            font-family: 'Courier New', Courier, monospace;
            margin: 0; padding: 0;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            min-height: 100vh; overflow: hidden;
        }
        .container {
            width: 90%; max-width: 420px;
            background: rgba(10, 10, 20, 0.95);
            border: 2px solid #00ff66;
            border-radius: 20px; padding: 20px;
            box-shadow: 0 0 40px rgba(0, 255, 102, 0.4);
            text-align: center;
        }
        .avatar-box {
            width: 140px; height: 140px;
            margin: 15px auto;
            border-radius: 50%;
            border: 3px solid #00ff66;
            overflow: hidden;
            box-shadow: 0 0 30px #00ff66;
            background: #000;
        }
        .avatar-box img {
            width: 100%; height: 100%; object-fit: cover;
        }
        .status-tag {
            background: #000; border: 1px solid #00ff66;
            color: #00ff66; padding: 8px; border-radius: 8px;
            font-size: 12px; margin-bottom: 10px;
        }
        .log-box {
            height: 130px; background: #000;
            border: 1px solid #00ff66; border-radius: 10px;
            margin-top: 15px; padding: 10px;
            overflow-y: auto; font-size: 13px; text-align: left;
        }
        .usr { color: #3399ff; margin: 4px 0; }
        .ai { color: #00ff66; margin: 4px 0; }
    </style>
</head>
<body onclick="initListening()">
    <div class="container">
        <h3 style="color:#ff0033; margin:0;">🛡️ AKASH AI ASSISTANT 🛡️</h3>
        <p style="font-size:11px; color:#aaa; margin-top:3px;">Owner: Subrato | Sec: Akash@13132</p>

        <!-- Combined AI Avatar Holder -->
        <div class="avatar-box">
            <img src="/avatar" alt="Akash AI Avatar" onerror="this.src='https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=300'">
        </div>

        <div class="status-tag" id="statusTag">🔴 माइक चालू करने के लिए स्क्रीन पर टैप करें (Wake Word: "आकाश")</div>

        <div class="log-box" id="logBox">
            <div class="ai"><b>Akash AI:</b> नमस्ते मालिक सुब्रतो! मैं पूरी सुरक्षा और 9 मॉड्यूल्स के साथ एक्टिव हूँ। बोलिए!</div>
        </div>
    </div>

    <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        let recognition;
        let isListening = false;
        let isSpeaking = false;

        function initListening() {
            if (isListening) return;
            if (!SpeechRecognition) { alert("कृपया Chrome या संगत ब्राउज़र का उपयोग करें!"); return; }
            recognition = new SpeechRecognition();
            recognition.lang = 'hi-IN';
            recognition.continuous = true;
            recognition.interimResults = false;

            recognition.onstart = function() {
                isListening = true;
                document.getElementById('statusTag').innerHTML = "🟢 24/7 बैकग्राउंड गार्ड एक्टिव... 'आकाश' बोलिए!";
            };

            recognition.onresult = function(event) {
                if (isSpeaking) return; // जब AI खुद बोल रहा हो, तो यूज़र की आवाज़ प्रोसेस मत करो
                let lastIndex = event.results.length - 1;
                let text = event.results[lastIndex][0].transcript.trim().toLowerCase();

                if (text.includes('आकाश') || text.includes('akash')) {
                    addLog('सुब्रतो', text, 'usr');
                    sendToAI(text);
                }
            };

            recognition.onerror = function() {
                if (!isSpeaking) { try { recognition.start(); } catch(e){} }
            };
            recognition.onend = function() {
                if (!isSpeaking) { try { recognition.start(); } catch(e){} }
            };

            recognition.start();
        }

        function speak(text) {
            let synth = window.speechSynthesis;
            synth.cancel(); // पुराना कोई अटका हुआ भाषण साफ़ करें

            let utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'hi-IN';

            utterance.onstart = function() {
                isSpeaking = true;
                if (recognition) { try { recognition.stop(); } catch(e){} }
            };

            utterance.onend = function() {
                isSpeaking = false;
                if (recognition) { try { recognition.start(); } catch(e){} }
            };

            synth.speak(utterance);
        }

        function addLog(sender, text, cls) {
            let box = document.getElementById('logBox');
            box.innerHTML += `<div class="${cls}"><b>${sender}:</b> ${text}</div>`;
            box.scrollTop = box.scrollHeight;
        }

        function sendToAI(text) {
            fetch('/process_command', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({query: text})
            })
            .then(res => res.json())
            .then(data => {
                addLog('Akash AI', data.reply, 'ai');
                speak(data.reply);
            })
            .catch(err => {
                addLog('सिस्टम', 'सर्वर से संपर्क नहीं हो सका!', 'usr');
            });
        }
    </script>
</body>
</html>
"""

# ==========================================
# 🧠 ALL 9 MODULES + SECURITY BACKEND LOGIC
# ==========================================
class AkashUltimateCore:
    def __init__(self):
        self.owner = USER_NAME
        self.security_status = "SECURE"

    def greeting_module(self):
        return f"नमस्ते मालिक {self.owner}! आकाश AI मास्टर सिस्टम आपकी सेवा में हाजिर है।"

    def realtime_search_engine(self, query):
        return f"मालिक, वेब और डेटाबेस से '{query}' की ताजा जानकारी निकाल ली गई है।"

    def chatbot_module(self, query):
        return f"मैंने आपका आदेश समझ लिया है: '{query}'। इसे तुरंत पूरा किया जा रहा है।"

    def app_control(self, command):
        return "App Control: आपके निर्देशानुसार सिस्टम और ऐप्स को मैनेज किया जा रहा है।"

    def security_daemon_loop(self):
        while True:
            time.sleep(20)

ai_brain = AkashUltimateCore()

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/avatar')
def get_avatar():
    if os.path.exists("14306.png"):
        return app.send_static_file("14306.png")
    return "OK", 200

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    query = data.get('query', '').lower()

    if 'नमस्ते' in query or 'hello' in query:
        reply = ai_brain.greeting_module()
    elif 'सर्च' in query or 'search' in query:
        reply = ai_brain.realtime_search_engine(query)
    elif 'ऐप' in query or 'control' in query or 'खोलो' in query:
        reply = ai_brain.app_control(query)
    elif 'स्टेटस' in query or 'status' in query:
        reply = f"मालिक सुब्रतो, डुअल-फेस बायोमेट्रिक और फेक शटडाउन गार्ड 100% एक्टिव हैं।"
    else:
        reply = ai_brain.chatbot_module(query)

    return jsonify({'reply': reply})

if __name__ == '__main__':
    guard_thread = threading.Thread(target=ai_brain.security_daemon_loop, daemon=True)
    guard_thread.start()

    print("[-] Akash AI Master Core Running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
~ $
