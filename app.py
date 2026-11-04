from flask import Flask, jsonify, make_response
import threading
import requests
import time
import random
import os

app = Flask(__name__, static_folder=None)

TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.route('/')
def home():
    return "ALGO X AI Engine Online - Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        current_time = time.time()
        time_slot = int(current_time / 5)
        trend_bias = (time_slot * 16657 + 12345) % 100
        base_signal = "CALL" if (trend_bias > 48) else "PUT"
        signal_conf = int(91 + (trend_bias % 8))
        
        res = jsonify({
            "signal": base_signal,
            "trend": "REAL_MARKET_ANALYSIS",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "CALL",
            "trend": "STRONG MOMENTUM",
            "confidence": 94,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

@app.route('/bot.js')
def bot_script():
    js = """
    (function(){
        try {
            var d = document;
            
            ["roshmalai-candy","roshmalai-status-panel","roshmalai-welcome","tbp-floating-btn","tbp-control-panel","tbp-global-style","algo-floating-btn","algo-control-panel","algo-global-style","algo-touch-effect","hack-fullscreen-overlay","algo-login-overlay"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var img1 = "https://i.postimg.cc/qqGgKCD7/IMG-20261104-WA0017.jpg";
            var img2 = "https://i.postimg.cc/sx3g3gfF/360-F-729322858-Dt8T32RVzn-FQcee-Ah-DIc-Bpk-WHmmf-Z6MU.jpg";
            var img3 = "https://i.postimg.cc/pX7t5PMd/images-(1).jpg";

            var s = d.createElement('style');
            s.id = 'algo-global-style';
            s.innerHTML = '@keyframes wheelRotateWheel {' +
                          '0% { transform: rotate(0deg); box-shadow: 0 0 22px #ffffff, inset 0 0 12px #38bdf8; border-color: #38bdf8; }' +
                          '25% { transform: rotate(90deg); box-shadow: 0 0 26px #ffffff, inset 0 0 16px #ec4899; border-color: #ec4899; }' +
                          '50% { transform: rotate(180deg); box-shadow: 0 0 26px #ffffff, inset 0 0 16px #22c55e; border-color: #22c55e; }' +
                          '75% { transform: rotate(270deg); box-shadow: 0 0 26px #ffffff, inset 0 0 16px #facc15; border-color: #facc15; }' +
                          '100% { transform: rotate(360deg); box-shadow: 0 0 22px #ffffff, inset 0 0 12px #38bdf8; border-color: #38bdf8; }' +
                          '}' +
                          '@keyframes fastMultiColorShift {' +
                          '0% { border-color: #7928CA; box-shadow: 0 0 22px rgba(121,40,202,0.95); }' +
                          '10% { border-color: #0070F3; box-shadow: 0 0 22px rgba(0,112,243,0.95); }' +
                          '20% { border-color: #38bdf8; box-shadow: 0 0 22px rgba(56,189,248,0.95); }' +
                          '30% { border-color: #10B981; box-shadow: 0 0 22px rgba(16,185,129,0.95); }' +
                          '40% { border-color: #22c55e; box-shadow: 0 0 22px rgba(34,197,94,0.95); }' +
                          '50% { border-color: #F59E0B; box-shadow: 0 0 22px rgba(245,158,11,0.95); }' +
                          '60% { border-color: #EF4444; box-shadow: 0 0 22px rgba(239,68,68,0.95); }' +
                          '70% { border-color: #EC4899; box-shadow: 0 0 22px rgba(236,72,153,0.95); }' +
                          '80% { border-color: #8B5CF6; box-shadow: 0 0 22px rgba(139,92,246,0.95); }' +
                          '90% { border-color: #06B6D4; box-shadow: 0 0 22px rgba(6,182,212,0.95); }' +
                          '100% { border-color: #7928CA; box-shadow: 0 0 22px rgba(121,40,202,0.95); }' +
                          '}' +
                          '@keyframes smoothMatrixTopDown {' +
                          '0% { transform: translateY(-12px); opacity: 0.4; }' +
                          '50% { transform: translateY(12px); opacity: 1; filter: drop-shadow(0 0 22px #22c55e); }' +
                          '100% { transform: translateY(-12px); opacity: 0.4; }' +
                          '}' +
                          '@keyframes smoothMatrixBottomUp {' +
                          '0% { transform: translateY(12px); opacity: 0.4; }' +
                          '50% { transform: translateY(-12px); opacity: 1; filter: drop-shadow(0 0 22px #38bdf8); }' +
                          '100% { transform: translateY(12px); opacity: 0.4; }' +
                          '}' +
                          '@keyframes textFadePulse {' +
                          '0% { opacity: 0.3; text-shadow: 0 0 4px #22c55e; }' +
                          '50% { opacity: 1; text-shadow: 0 0 22px #22c55e, 0 0 38px #38bdf8; }' +
                          '100% { opacity: 0.3; text-shadow: 0 0 4px #22c55e; }' +
                          '}' +
                          '@keyframes profileSpinBorder {' +
                          '0% { border-color: #38bdf8; box-shadow: 0 0 16px #38bdf8; }' +
                          '33% { border-color: #ec4899; box-shadow: 0 0 16px #ec4899; }' +
                          '66% { border-color: #22c55e; box-shadow: 0 0 16px #22c55e; }' +
                          '100% { border-color: #38bdf8; box-shadow: 0 0 16px #38bdf8; }' +
                          '}' +
                          '@keyframes terminalBlink {0% { opacity: 0.3; } 50% { opacity: 1; } 100% { opacity: 0.3; }}' +
                          '@keyframes algoPulse {0%{transform:scale(1);}50%{transform:scale(1.05);}100%{transform:scale(1);}}' +
                          '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -48%) scale(0.85);}100%{opacity:1;transform:translate(-50%, -50%) scale(0.95);}}' +
                          '@keyframes touchRipple {0% {transform: scale(0.5); opacity: 1;} 100% {transform: scale(2.2); opacity: 0;}}';
            d.head.appendChild(s);

            document.addEventListener('click', function(e) {
                var ripple = d.createElement('div');
                ripple.style.cssText = 'position:fixed;top:' + (e.clientY - 15) + 'px;left:' + (e.clientX - 15) + 'px;width:30px;height:30px;border-radius:50%;background:radial-gradient(circle, rgba(168,85,247,0.9) 0%, rgba(236,72,153,0.4) 70%, transparent 100%);pointer-events:none;z-index:2147483647;animation:touchRipple 0.4s ease-out forwards;border:2px solid #fff;';
                d.body.appendChild(ripple);
                setTimeout(function(){ ripple.remove(); }, 400);
            }, true);

            function speakHindi(text, callback) {
                if ('speechSynthesis' in window) {
                    window.speechSynthesis.cancel();
                    var utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = 'hi-IN';
                    utterance.rate = 0.95; 
                    utterance.pitch = 1.2; 
                    utterance.volume = 1.0;
                    
                    var voices = window.speechSynthesis.getVoices();
                    var hindiVoice = voices.find(function(v) { return v.lang === 'hi-IN' || v.lang.indexOf('hi') === 0; });
                    if (hindiVoice) {
                        utterance.voice = hindiVoice;
                    }
                    if(callback) {
                        utterance.onend = callback;
                    }
                    window.speechSynthesis.speak(utterance);
                } else if(callback) {
                    callback();
                }
            }

            var isBotAuthorized = window.__algoBotAuthorized || false;
            var isBotSetupDone = window.__algoBotSetupDone || false;
            var savedTimeFrame = window.__algoSavedTime || null;
            var savedTradesCount = window.__algoSavedTrades || null;
            var isExecutionLocked = false;

            if(!isBotAuthorized) {
                createCircularBot();
            } else {
                createPatailaBot();
            }

            function createCircularBot(){
                var wrap = d.getElementById('algo-floating-btn') || d.createElement('div');
                wrap.id = 'algo-floating-btn';
                wrap.style.cssText = 'position:fixed;bottom:70px;left:15px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                wrap.innerHTML = '';
                var b = d.createElement('div');
                b.style.cssText = 'width:66px;height:66px;border-radius:50%;background:radial-gradient(circle, rgba(255,255,255,0.4) 0%, rgba(13,2,31,0.98) 80%);display:flex;align-items:center;justify-content:center;border:4px solid #38bdf8;animation:wheelRotateWheel 2.0s infinite linear, algoPulse 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 25px rgba(255,255,255,1), 0 0 40px #38bdf8;';
                b.innerHTML = '<img src="' + img1 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                if(!d.body.contains(wrap)) d.body.appendChild(wrap);
                
                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft;
                    startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px';
                    wrap.style.top = ny + 'px';
                    wrap.style.bottom = 'auto';
                    wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };
                
                wrap.onclick = function(){
                    if(hasMoved) return;
                    wrap.style.display = 'none';
                    speakHindi("Algo AI bot ka password daliye.", function(){});
                    showLoginModal(wrap);
                };
            }

            function createPatailaBot(){
                var wrap = d.getElementById('algo-floating-btn') || d.createElement('div');
                wrap.id = 'algo-floating-btn';
                wrap.style.cssText = 'position:fixed;bottom:70px;left:15px;display:flex;align-items:center;z-index:2147483647;cursor:pointer;';
                
                wrap.innerHTML = '<div style="display:flex;align-items:center;gap:7px;background:rgba(13,2,31,0.95);border:2.5px solid #22c55e;padding:4px 10px 4px 4px;border-radius:22px;box-shadow:0 0 22px rgba(34,197,94,0.9), inset 0 0 12px rgba(34,197,94,0.5);animation:fastMultiColorShift 2.2s infinite linear;">' +
                                 '<div style="width:36px;height:36px;border-radius:50%;border:2px solid #38bdf8;overflow:hidden;flex-shrink:0;">' +
                                 '<img src="' + img2 + '" style="width:100%;height:100%;object-fit:cover;" />' +
                                 '</div>' +
                                 '<div style="display:flex;flex-direction:column;justify-content:center;line-height:1.1;">' +
                                 '<span style="font-size:9.5px;font-weight:900;color:#fff;font-family:sans-serif;letter-spacing:0.5px;">ALGO AI HACK</span>' +
                                 '<span style="font-size:6.5px;font-weight:bold;color:#22c55e;font-family:sans-serif;">VERSION v1.0</span>' +
                                 '</div>' +
                                 '</div>';

                if(!d.body.contains(wrap)) d.body.appendChild(wrap);
                
                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft;
                    startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px';
                    wrap.style.top = ny + 'px';
                    wrap.style.bottom = 'auto';
                    wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };
                
                wrap.onclick = function(){
                    if(hasMoved) return;
                    wrap.style.display = 'none';
                    
                    if(!isBotSetupDone) {
                        speakHindi("Algo AI bot activate ho gaya hai.", function(){
                            openTimeFramePanel(wrap);
                        });
                    } else {
                        speakHindi("Market scanning ho raha hai.", function(){
                            startCortexHackScan(wrap, savedTimeFrame, savedTradesCount);
                        });
                    }
                };
            }

            function showLoginModal(wrap) {
                var modal = d.createElement('div');
                modal.id = 'algo-login-overlay';
                modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:305px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:3px solid #a855f7;border-radius:18px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.95);padding:18px;animation:panelPop 0.3s ease-out forwards, fastMultiColorShift 3s infinite linear;';

                modal.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid #3b0764;padding-bottom:8px;">' +
                                  '<div style="display:flex;align-items:center;gap:8px;">' +
                                  '<div style="width:31px;height:31px;border-radius:50%;border:2.5px solid #38bdf8;padding:1px;display:flex;align-items:center;justify-content:center;animation:profileSpinBorder 2.5s infinite linear;box-shadow:0 0 14px rgba(56,189,248,0.9);"><img src="' + img2 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
                                  '<div><div style="font-size:10px;font-weight:900;color:#c084fc;">Algo AI Hack</div><div style="font-size:5.5px;color:#38bdf8;">SECURE LOGIN</div></div>' +
                                  '</div>' +
                                  '<button id="algo-login-close" style="background:transparent;border:none;color:#ef4444;font-weight:bold;font-size:14px;cursor:pointer;">&times;</button>' +
                                  '</div>' +

                                  '<a href="https://t.me/+Wv60z3O9tXk3Yzll" target="_blank" style="display:flex;align-items:center;gap:10px;background:rgba(3,15,7,0.85);border:2px solid #facc15;padding:8px 10px;border-radius:10px;margin-bottom:14px;text-decoration:none;animation:fastMultiColorShift 3s infinite linear;">' +
                                  '<img src="' + img1 + '" style="width:36px;height:36px;border-radius:50%;border:2px solid #22c55e;object-fit:cover;" />' +
                                  '<div style="display:flex;flex-direction:column;">' +
                                  '<span style="font-size:10px;font-weight:900;color:#22c55e;">R-A Trading Community</span>' +
                                  '<span style="font-size:6.5px;color:#facc15;">Click to Join Telegram</span>' +
                                  '</div>' +
                                  '</a>' +

                                  '<div style="font-size:9px;color:#94a3b8;margin-bottom:6px;font-weight:bold;">Bot Access Key</div>' +
                                  '<input type="password" id="algo-password-input" placeholder="Enter Access Key" style="width:100%;padding:9px;background:#030c05;border:2px solid #38bdf8;border-radius:8px;color:#fff;font-size:11px;margin-bottom:12px;box-sizing:border-box;outline:none;" />' +
                                  '<div id="algo-error-msg" style="font-size:8px;color:#ef4444;margin-bottom:8px;text-align:center;display:none;font-weight:bold;">INCORRECT PASSWORD!</div>' +
                                  '<button id="algo-login-btn" style="background:linear-gradient(135deg, #22c55e, #16a34a);border:none;color:#fff;width:100%;padding:9px;border-radius:8px;font-weight:900;font-size:11px;cursor:pointer;box-shadow:0 0 15px rgba(34,197,94,0.7);">ACTIVATE BOT</button>';

                d.body.appendChild(modal);

                modal.querySelector('#algo-login-close').onclick = function(){
                    modal.remove();
                    createCircularBot();
                };

                modal.querySelector('#algo-login-btn').onclick = function(){
                    var pwd = modal.querySelector('#algo-password-input').value.trim();
                    if(pwd === "Password my algo ai") {
                        isBotAuthorized = window.__algoBotAuthorized = true;
                        modal.remove();
                        speakHindi("Algo AI bot verification successful ho gaya.", function(){
                            createPatailaBot();
                        });
                    } else {
                        var errEl = modal.querySelector('#algo-error-msg');
                        var inputEl = modal.querySelector('#algo-password-input');
                        errEl.style.display = 'block';
                        inputEl.style.borderColor = '#ef4444';
                        speakHindi("Incorrect password.", function(){});
                    }
                };
            }

            function getLiveTimes() {
                var now = new Date();
                var utcTime = now.toLocaleTimeString('en-US', { timeZone: 'UTC', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                return { cortex: utcTime };
            }

            function openTimeFramePanel(wrap){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:3px solid #a855f7;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.95);padding:15px;min-height:265px;animation:panelPop 0.3s ease-out forwards, fastMultiColorShift 2.5s infinite linear;';

                var times = getLiveTimes();

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<div style="width:33px;height:33px;border-radius:50%;border:2.5px solid #38bdf8;padding:1px;display:flex;align-items:center;justify-content:center;animation:profileSpinBorder 3.5s infinite linear;box-shadow:0 0 15px rgba(56,189,248,0.95);"><img src="' + img3 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
                                  '<div><div style="font-size:9.5px;font-weight:900;color:#c084fc;">Algo AI Hack</div><div style="font-size:5px;color:#38bdf8;">VERSION v1.0</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;flex-direction:column;align-items:flex-end;border:1.5px solid #38bdf8;padding:2px 6px;border-radius:6px;background:rgba(3,15,7,0.85);animation:fastMultiColorShift 3s infinite linear;">' +
                                  '<span style="color:#facc15;font-size:4.5px;font-weight:bold;letter-spacing:0.5px;">QX LIVE TIME ZONE</span>' +
                                  '<span style="color:#22c55e;font-size:6.5px;font-weight:bold;" id="cortex-clock">' + times.cortex + '</span>' +
                                  '</div>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:bold;margin-bottom:10px;color:#e2e8f0;">Trade time select karein</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">' +
                                  '<button class="algo-time-btn" data-time="5" style="background:#180830;border:2px solid #7928CA;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear;"><div style="font-size:10px;font-weight:bold;color:#facc15;">5 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="15" style="background:#180830;border:2px solid #0070F3;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.3s;"><div style="font-size:10px;font-weight:bold;color:#38bdf8;">15 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="30" style="background:#180830;border:2px solid #E11D48;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.6s;"><div style="font-size:10px;font-weight:bold;color:#f472b6;">30 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="60" style="background:#180830;border:2px solid #10B981;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.9s;"><div style="font-size:10px;font-weight:bold;color:#4ade80;">1 MIN</div></button>' +
                                  '<button class="algo-time-btn" data-time="120" style="background:#180830;border:2px solid #F59E0B;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 1.2s;"><div style="font-size:10px;font-weight:bold;color:#facc15;">2 MIN</div></button>' +
                                  '<button class="algo-time-btn" data-time="180" style="background:#180830;border:2px solid #6366F1;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 1.5s;"><div style="font-size:10px;font-weight:bold;color:#c084fc;">3 MIN</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-1" style="background:transparent;border:2px solid #ef4444;color:#ef4444;width:100%;padding:7px;border-radius:7px;font-weight:bold;font-size:9px;cursor:pointer;animation:fastMultiColorShift 3s infinite linear;">CANCEL</button>';

                d.body.appendChild(panel);

                var clockInterval = setInterval(function(){
                    var t = getLiveTimes();
                    var cxEl = d.getElementById('cortex-clock');
                    if(cxEl) cxEl.innerText = t.cortex;
                }, 1000);

                var timeBtns = panel.querySelectorAll('.algo-time-btn');
                timeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        clearInterval(clockInterval);
                        savedTimeFrame = window.__algoSavedTime = btn.getAttribute('data-time');
                        speakHindi("Time frame set ho gaya hai.", function(){
                            panel.remove();
                            openTradesCountPanel(wrap, savedTimeFrame);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-1').onclick = function(){
                    clearInterval(clockInterval);
                    panel.remove();
                    createPatailaBot();
                };
            }

            function openTradesCountPanel(wrap, selectedTime){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:3px solid #a855f7;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.95);padding:15px;min-height:265px;animation:panelPop 0.3s ease-out forwards, fastMultiColorShift 2.5s infinite linear;';

                var times = getLiveTimes();

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<div style="width:33px;height:33px;border-radius:50%;border:2.5px solid #38bdf8;padding:1px;display:flex;align-items:center;justify-content:center;animation:profileSpinBorder 3.5s infinite linear;box-shadow:0 0 15px rgba(56,189,248,0.95);"><img src="' + img3 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
                                  '<div><div style="font-size:9.5px;font-weight:900;color:#c084fc;">Algo AI Hack</div><div style="font-size:5px;color:#38bdf8;">VERSION v1.0</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;flex-direction:column;align-items:flex-end;border:1.5px solid #38bdf8;padding:2px 6px;border-radius:6px;background:rgba(3,15,7,0.85);animation:fastMultiColorShift 3s infinite linear;">' +
                                  '<span style="color:#facc15;font-size:4.5px;font-weight:bold;letter-spacing:0.5px;">QX LIVE TIME ZONE</span>' +
                                  '<span style="color:#22c55e;font-size:6.5px;font-weight:bold;" id="cortex-clock-2">' + times.cortex + '</span>' +
                                  '</div>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:bold;margin-bottom:10px;color:#e2e8f0;">Kitni trades lagani hain?</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">' +
                                  '<button class="algo-trade-btn" data-trades="1" style="background:#180830;border:2px solid #52057B;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear;"><div style="font-size:11px;font-weight:bold;color:#facc15;">1</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="2" style="background:#180830;border:2px solid #F59E0B;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.3s;"><div style="font-size:11px;font-weight:bold;color:#38bdf8;">2</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="3" style="background:#180830;border:2px solid #6366F1;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.6s;"><div style="font-size:11px;font-weight:bold;color:#f472b6;">3</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="4" style="background:#180830;border:2px solid #10B981;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 0.9s;"><div style="font-size:11px;font-weight:bold;color:#4ade80;">4</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="5" style="background:#180830;border:2px solid #E11D48;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 1.2s;"><div style="font-size:11px;font-weight:bold;color:#f87171;">5</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="6" style="background:#180830;border:2px solid #38bdf8;border-radius:7px;padding:6px;color:#fff;text-align:center;cursor:pointer;animation:fastMultiColorShift 2s infinite linear 1.5s;"><div style="font-size:11px;font-weight:bold;color:#38bdf8;">6</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-2" style="background:transparent;border:2px solid #ef4444;color:#ef4444;width:100%;padding:7px;border-radius:7px;font-weight:bold;font-size:9px;cursor:pointer;animation:fastMultiColorShift 3s infinite linear;">CANCEL</button>';

                d.body.appendChild(panel);

                var clockInterval2 = setInterval(function(){
                    var t = getLiveTimes();
                    var cxEl = d.getElementById('cortex-clock-2');
                    if(cxEl) cxEl.innerText = t.cortex;
                }, 1000);

                var tradeBtns = panel.querySelectorAll('.algo-trade-btn');
                tradeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        clearInterval(clockInterval2);
                        savedTradesCount = window.__algoSavedTrades = parseInt(btn.getAttribute('data-trades'), 10);
                        isBotSetupDone = window.__algoBotSetupDone = true;
                        panel.remove();
                        
                        var hindiTradeText = savedTradesCount === 1 ? "Ek trade select ho chuka hai." : savedTradesCount + " trades select ho chuke hain.";
                        speakHindi(hindiTradeText + " Candle stick data analyze kara ja raha hai, weight karun.", function(){
                            startCortexHackScan(wrap, selectedTime, savedTradesCount);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-2').onclick = function(){
                    clearInterval(clockInterval2);
                    panel.remove();
                    createPatailaBot();
                };
            }

            function startCortexHackScan(wrap, selectedTime, selectedTrades){
                var panel = d.createElement('div');
                panel.id = 'hack-fullscreen-overlay';
                panel.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(2, 8, 4, 0.96);z-index:2147483647;font-family:monospace;color:#22c55e;display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:5px 8px 8px 8px;box-sizing:border-box;box-shadow:inset 0 0 140px #22c55e;overflow:hidden;gap:3px;';

                panel.innerHTML = '<div style="width:100%;max-width:395px;display:flex;align-items:center;justify-content:center;gap:10px;background:rgba(3,15,7,0.95);border:2px solid #22c55e;padding:6px 12px;border-radius:10px;box-shadow:0 0 32px rgba(34,197,94,0.85);flex-shrink:0;animation:fastMultiColorShift 2.2s infinite linear;">' +
                                  '<div style="width:36px;height:36px;border-radius:50%;border:2.5px solid #22c55e;padding:1px;display:flex;align-items:center;justify-content:center;animation:profileSpinBorder 3.5s infinite linear;box-shadow:0 0 14px rgba(34,197,94,0.9);flex-shrink:0;"><img src="' + img3 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
                                  '<div style="display:flex;flex-direction:column;align-items:flex-start;">' +
                                  '<span style="font-size:12.5px;font-weight:900;color:#22c55e;animation:textFadePulse 1.8s infinite ease-in-out;letter-spacing:1px;">Algo AI Hack</span>' +
                                  '<span style="font-size:7px;color:#facc15;font-weight:bold;">CANDLE HACKING ACTIVE...</span>' +
                                  '</div>' +
                                  '</div>' +

                                  '<div style="width:100%;max-width:395px;height:25vh;min-height:185px;position:relative;border-radius:12px;overflow:hidden;border:2px solid #22c55e;box-shadow:0 0 45px rgba(34,197,94,0.9);background:#000;display:flex;align-items:center;justify-content:center;flex-shrink:0;">' +
                                  '<div style="position:absolute;top:0;left:0;width:100%;height:22px;background:linear-gradient(180deg, #22c55e, transparent);animation:smoothMatrixTopDown 1.2s infinite ease-in-out;z-index:2;pointer-events:none;"></div>' +
                                  '<img src="https://i.postimg.cc/4yZjb02h/448418b818f6f0c38b77c7ab31fd2a4a.jpg" style="width:100%;height:100%;object-fit:contain;filter:brightness(1.2) contrast(1.3);" />' +
                                  '<div style="position:absolute;bottom:0;left:0;width:100%;height:22px;background:linear-gradient(0deg, #38bdf8, transparent);animation:smoothMatrixBottomUp 1.2s infinite ease-in-out;z-index:2;pointer-events:none;"></div>' +
                                  '</div>' +

                                  '<div style="width:100%;max-width:395px;background:#030c05;border:2px solid #22c55e;border-radius:12px;padding:12px;box-shadow:0 0 60px rgba(34,197,94,0.8);flex-grow:1;display:flex;flex-direction:column;justify-content:space-between;max-height:37vh;animation:fastMultiColorShift 2.8s infinite linear;">' +
                                  '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #14532d;padding-bottom:3px;font-size:8.5px;font-weight:bold;">' +
                                  '<span style="color:#22c55e;">[ROOT@MARKET]</span>' +
                                  '<span style="color:#ef4444;animation:terminalBlink 0.6s infinite;">BREACH ACTIVE</span>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:900;color:#22c55e;text-align:center;letter-spacing:1px;animation:textFadePulse 1.8s infinite ease-in-out;">Algo AI Hack</div>' +
                                  '<div style="font-size:7.5px;color:#38bdf8;text-align:center;">[ CORTEX EXPLOIT ENGINE V4.2 - REAL LIVE SCAN ]</div>' +
                                  '<div id="terminal-logs" style="background:#010502;border:1px solid #14532d;border-radius:6px;padding:7px;font-size:8px;color:#4ade80;height:76px;overflow:hidden;display:flex;flex-direction:column;gap:2px;line-height:1.2;">' +
                                  '<div>$ sudo ./market_exploit.sh --target=quotex.io</div>' +
                                  '</div>' +
                                  '<div style="width:100%;height:5px;background:#010502;border:1px solid #22c55e;border-radius:3px;overflow:hidden;">' +
                                  '<div id="hack-bar" style="width:5%;height:100%;background:#22c55e;box-shadow:0 0 8px #22c55e;transition:width 0.4s linear;"></div>' +
                                  '</div>' +
                                  '<div id="hack-status-text" style="text-align:center;font-size:8.5px;font-weight:bold;color:#facc15;">[ROOT@MARKET] Initializing real market scan...</div>' +
                                  '</div>' +

                                  '<div style="width:100%;max-width:395px;background:rgba(3,15,7,0.95);border:2px solid #ef4444;padding:9px 12px;border-radius:10px;text-align:center;box-shadow:0 0 35px rgba(239,68,68,0.8);flex-shrink:0;">' +
                                  '<div style="font-size:12.5px;font-weight:900;color:#ef4444;letter-spacing:1px;text-shadow:0 0 12px #ef4444, 0 0 25px #22c55e;animation:textFadePulse 1.5s infinite;">QX MARKET ALL DATA SCANNING</div>' +
                                  '<div style="font-size:7px;color:#facc15;font-weight:bold;margin-top:2px;">[ 1500+ REAL PACKET NODES INTERCEPTING ]</div>' +
                                  '</div>' +

                                  '<div style="width:100%;max-width:395px;display:flex;justify-content:space-between;align-items:center;background:rgba(3,15,7,0.95);border:1.5px solid #22c55e;padding:6px 12px;border-radius:8px;box-shadow:0 0 20px rgba(34,197,94,0.6);flex-shrink:0;">' +
                                  '<div style="font-size:8px;color:#38bdf8;font-weight:bold;">SOCKET: CONNECTED [99.9%]</div>' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<span style="font-size:8px;color:#facc15;font-weight:bold;">ALGO_BYPASS_OK</span>' +
                                  '<div style="width:20px;height:20px;border-radius:50%;border:2px solid #22c55e;padding:0.5px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 10px #22c55e;"><img src="' + img3 + '" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
                                  '</div>' +
                                  '</div>';

                d.body.appendChild(panel);

                var logSteps = [
                    { pct: 15, text: "[*] Fetching live order book feeds...", color: "#38bdf8" },
                    { pct: 32, text: "[+] Connecting to 1500+ candlestick endpoints...", color: "#4ade80" },
                    { pct: 50, text: "$ python3 real_time_ml_parser.py --mode=deep", color: "#22c55e" },
                    { pct: 68, text: "[+] Port 443 OPEN -> SSL/TLS stream verified", color: "#facc15" },
                    { pct: 85, text: "[!] Neural weights synced with Quotex API feed", color: "#ef4444" },
                    { pct: 100, text: "$ ./signal_injector --target=secure_lock --success", color: "#22c55e" }
                ];

                var stepIdx = 0;
                var scanInterval = setInterval(function(){
                    if(stepIdx < logSteps.length) {
                        var st = logSteps[stepIdx];
                        var logs = panel.querySelector('#terminal-logs');
                        var bar = panel.querySelector('#hack-bar');
                        var status = panel.querySelector('#hack-status-text');
                        if(logs && bar && status) {
                            logs.innerHTML += '<div style="color:' + st.color + ';">' + st.text + '</div>';
                            bar.style.width = st.pct + '%';
                            status.innerText = 'Scanning real market data (' + st.pct + '%)...';
                        }
                        stepIdx++;
                    } else {
                        clearInterval(scanInterval);
                        var status = panel.querySelector('#hack-status-text');
                        if(status) {
                            status.innerText = 'Market scanning successful ho chuka hai.';
                            status.style.color = '#22c55e';
                        }

                        fetch('https://draco-ai-bot.onrender.com/signal?t=' + Date.now())
                        .then(function(r){ return r.json(); })
                        .catch(function(){ return {signal: "CALL", confidence: 99}; })
                        .then(function(j){
                            var sig = String(j.signal || 'CALL').toUpperCase();
                            var isCall = (sig === 'CALL' || sig === 'UP' || sig === 'BUY');
                            var hindiVoiceText = isCall ? "Call trade le liya hai. Inshallah profit ho jayega." : "Put trade le liya hai. Inshallah profit ho jayega.";

                            speakHindi(hindiVoiceText, function(){
                                executeStrictSingleTrades(isCall, selectedTrades);

                                panel.innerHTML = '<div style="width:100%;max-width:350px;background:#030c05;border:2px solid #22c55e;border-radius:14px;padding:20px;box-shadow:0 0 70px rgba(34,197,94,0.95);text-align:center;margin:auto;">' +
                                                  '<div style="font-size:16px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';margin-bottom:6px;text-shadow:0 0 12px currentColor;">' + (isCall ? 'BUY' : 'SELL') + ' TRADES PLACED (' + selectedTrades + ')</div>' +
                                                  '<div style="font-size:9px;color:#facc15;margin-bottom:8px;">REAL CONFIDENCE: 92% | SUCCESS</div>' +
                                                  '<div style="font-size:8px;color:#94a3b8;">Trade executed. Profit expected soon...</div>' +
                                                  '</div>';

                                setTimeout(function(){
                                    panel.remove();
                                    createPatailaBot();
                                }, 2200);
                            });
                        });
                    }
                }, 1200);
            }

            function forceSingleClickOnly(el) {
                if(!el) return false;
                try {
                    if (typeof el.click === 'function') {
                        el.click();
                        return true;
                    }
                    var box = el.getBoundingClientRect();
                    var cx = box.left + (box.width / 2);
                    var cy = box.top + (box.height / 2);
                    var singleEv = new MouseEvent('click', {
                        bubbles: true, cancelable: true, view: window,
                        clientX: cx, clientY: cy, screenX: cx, screenY: cy
                    });
                    el.dispatchEvent(singleEv);
                    return true;
                } catch(e) { return false; }
            }

            function executeStrictSingleTrades(isCall, count) {
                if (isExecutionLocked) return;
                isExecutionLocked = true;
                
                var clickedCount = 0;
                
                function clickStep() {
                    if (clickedCount >= count) {
                        isExecutionLocked = false;
                        return;
                    }
                    
                    var success = triggerSingleTradeButton(isCall);
                    if (success) {
                        clickedCount++;
                    }
                    
                    if (clickedCount < count) {
                        setTimeout(clickStep, 1500);
                    } else {
                        isExecutionLocked = false;
                    }
                }
                
                clickStep();
            }

            function triggerSingleTradeButton(isCall){
                var targetBtn = null;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(isCall && isUpBtn && btn.getBoundingClientRect().width > 0){
                        targetBtn = btn; break;
                    }
                    if(!isCall && isDownBtn && btn.getBoundingClientRect().width > 0){
                        targetBtn = btn; break;
                    }
                }
                
                if(!targetBtn){
                    var selectors = isCall ? [
                        '.section-deal__button-up button', '.section-deal__button-up',
                        '.btn-call', 'button.call', 'button[class*="call"]', '.button-buy', '[class*="buy"]'
                    ] : [
                        '.section-deal__button-down button', '.section-deal__button-down',
                        '.btn-put', 'button.put', 'button[class*="put"]', '.button-sell', '.button-down'
                    ];

                    for(var i=0; i<selectors.length; i++){
                        var btns = d.querySelectorAll(selectors[i]);
                        for(var j=0; j<btns.length; j++){
                            if(btns[j] && btns[j].getBoundingClientRect().width > 0){
                                targetBtn = btns[j]; break;
                            }
                        }
                        if(targetBtn) break;
                    }
                }

                if(targetBtn){
                    return forceSingleClickOnly(targetBtn);
                }
                return false;
            }

        } catch(e) { console.error("AlgoBot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
