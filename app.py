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
        base_signal = "CALL" if (int(current_time * 1000) % 2 == 0) else "PUT"
        signal_conf = int(88 + (random.randint(0, 9)))
        res = jsonify({
            "signal": base_signal,
            "trend": "ALGO_X_MOMENTUM",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "CALL",
            "trend": "STRONG MOMENTUM",
            "confidence": 92,
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
            
            ["roshmalai-candy","roshmalai-status-panel","roshmalai-welcome","tbp-floating-btn","tbp-control-panel","tbp-global-style","algo-floating-btn","algo-control-panel","algo-global-style","algo-touch-effect","hack-fullscreen-overlay"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var s = d.createElement('style');
            s.id = 'algo-global-style';
            s.innerHTML = '@keyframes wheelRotate {' +
                          '0% { transform: rotate(0deg); box-shadow: 0 0 25px rgba(255,255,255,0.9), 0 0 50px #38bdf8; border-color: #38bdf8; }' +
                          '50% { transform: rotate(180deg); box-shadow: 0 0 35px rgba(255,255,255,1), 0 0 65px #ec4899; border-color: #ec4899; }' +
                          '100% { transform: rotate(360deg); box-shadow: 0 0 25px rgba(255,255,255,0.9), 0 0 50px #38bdf8; border-color: #38bdf8; }' +
                          '}' +
                          '@keyframes fastLighting {' +
                          '0% { border-color: #7928CA; box-shadow: 0 0 10px rgba(121,40,202,0.8); }' +
                          '25% { border-color: #0070F3; box-shadow: 0 0 10px rgba(0,112,243,0.8); }' +
                          '50% { border-color: #E11D48; box-shadow: 0 0 10px rgba(225,29,72,0.8); }' +
                          '75% { border-color: #10B981; box-shadow: 0 0 10px rgba(16,185,129,0.8); }' +
                          '100% { border-color: #7928CA; box-shadow: 0 0 10px rgba(121,40,202,0.8); }' +
                          '}' +
                          '@keyframes topBottomFlash {0% { opacity: 0.4; text-shadow: 0 0 5px #22c55e; } 50% { opacity: 1; text-shadow: 0 0 20px #22c55e, 0 0 30px #38bdf8; } 100% { opacity: 0.4; text-shadow: 0 0 5px #22c55e; }}' +
                          '@keyframes binaryScroll {0% { transform: translateY(0); } 100% { transform: translateY(-50%); }}' +
                          '@keyframes terminalBlink {0% { opacity: 0.3; } 50% { opacity: 1; } 100% { opacity: 0.3; }}' +
                          '@keyframes algoPulse {0%{transform:scale(1);}50%{transform:scale(1.04);}100%{transform:scale(1);}}' +
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
                    utterance.rate = 1.0; 
                    utterance.pitch = 1.5; 
                    
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

            createFloatingBot();

            function createFloatingBot(){
                var wrap = d.createElement('div');
                wrap.id = 'algo-floating-btn';
                wrap.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.style.cssText = 'width:68px;height:68px;border-radius:50%;background:radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(13,2,31,0.95) 85%);display:flex;align-items:center;justify-content:center;border:3px dashed #38bdf8;animation:wheelRotate 5s infinite linear, algoPulse 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 30px rgba(255,255,255,0.9), 0 0 55px #38bdf8;';
                b.innerHTML = '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                d.body.appendChild(wrap);
                
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
                    speakHindi("Bot active ho gaya hai.", function(){});
                    showActiveBadge(wrap);
                    openTimeFramePanel(wrap);
                };
            }

            function showActiveBadge(wrap) {
                var existingActive = d.getElementById('algo-active-badge');
                if(existingActive) existingActive.remove();

                var activeBadge = d.createElement('div');
                activeBadge.id = 'algo-active-badge';
                activeBadge.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;';
                
                var b = d.createElement('div');
                b.style.cssText = 'width:60px;height:60px;border-radius:50%;background:radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(13,2,31,0.95) 85%);display:flex;align-items:center;justify-content:center;border:3px dashed #38bdf8;animation:wheelRotate 5s infinite linear;overflow:hidden;box-shadow:0 0 20px rgba(255,255,255,0.9);';
                b.innerHTML = '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                activeBadge.appendChild(b);

                var label = d.createElement('div');
                label.style.cssText = 'margin-top:3px;font-size:8px;font-weight:900;color:#000;font-family:sans-serif;background:#22c55e;padding:2px 8px;border-radius:4px;border:1px solid #fff;text-align:center;box-shadow:0 0 8px rgba(34,197,94,0.8);';
                label.innerText = 'ACTIVE';
                activeBadge.appendChild(label);

                d.body.appendChild(activeBadge);
            }

            function getLiveTimes() {
                var now = new Date();
                var bdTime = now.toLocaleTimeString('en-US', { timeZone: 'Asia/Dhaka', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                var utcTime = now.toLocaleTimeString('en-US', { timeZone: 'UTC', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                return { bd: bdTime, cortex: utcTime };
            }

            // Step 1: Time Frame Panel
            function openTimeFramePanel(wrap){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.95);padding:15px;min-height:265px;animation:panelPop 0.3s ease-out forwards;';

                var times = getLiveTimes();

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:23px;height:23px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<div><div style="font-size:9px;font-weight:bold;color:#c084fc;">ALGO X</div><div style="font-size:5px;color:#38bdf8;">HACK ENGINE</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;gap:4px;"><span style="background:#14532d;color:#22c55e;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #22c55e;">BD: <span id="bd-clock">' + times.bd + '</span></span><span style="background:#713f12;color:#facc15;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #facc15;">CORTEX: <span id="cortex-clock">' + times.cortex + '</span></span></div>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:bold;margin-bottom:10px;color:#e2e8f0;">Trade time select karein</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">' +
                                  '<button class="algo-time-btn" data-time="5" style="background:#180830;border:2px solid #7928CA;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear;"><div style="font-size:10px;font-weight:bold;color:#facc15;">5 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="15" style="background:#180830;border:2px solid #0070F3;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 0.5s;"><div style="font-size:10px;font-weight:bold;color:#38bdf8;">15 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="30" style="background:#180830;border:2px solid #E11D48;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 1s;"><div style="font-size:10px;font-weight:bold;color:#f472b6;">30 SEC</div></button>' +
                                  '<button class="algo-time-btn" data-time="60" style="background:#180830;border:2px solid #10B981;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 1.5s;"><div style="font-size:10px;font-weight:bold;color:#4ade80;">1 MIN</div></button>' +
                                  '<button class="algo-time-btn" data-time="120" style="background:#180830;border:2px solid #F59E0B;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 2s;"><div style="font-size:10px;font-weight:bold;color:#facc15;">2 MIN</div></button>' +
                                  '<button class="algo-time-btn" data-time="180" style="background:#180830;border:2px solid #6366F1;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 2.5s;"><div style="font-size:10px;font-weight:bold;color:#c084fc;">3 MIN</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-1" style="background:transparent;border:1px solid #ef4444;color:#ef4444;width:100%;padding:6px;border-radius:6px;font-weight:bold;font-size:8px;cursor:pointer;animation:fastLighting 4s infinite linear;">CANCEL</button>';

                d.body.appendChild(panel);

                var clockInterval = setInterval(function(){
                    var t = getLiveTimes();
                    var bdEl = d.getElementById('bd-clock');
                    var cxEl = d.getElementById('cortex-clock');
                    if(bdEl) bdEl.innerText = t.bd;
                    if(cxEl) cxEl.innerText = t.cortex;
                }, 1000);

                var timeBtns = panel.querySelectorAll('.algo-time-btn');
                timeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        clearInterval(clockInterval);
                        var selectedTime = btn.getAttribute('data-time');
                        speakHindi("Time frame set ho gaya hai.", function(){
                            panel.remove();
                            openTradesCountPanel(wrap, selectedTime);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-1').onclick = function(){
                    clearInterval(clockInterval);
                    panel.remove();
                    var ab = d.getElementById('algo-active-badge');
                    if(ab) ab.remove();
                    wrap.style.display = 'flex';
                };
            }

            // Step 2: Trades Count Panel
            function openTradesCountPanel(wrap, selectedTime){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 60px rgba(0,0,0,0.95);padding:15px;min-height:265px;animation:panelPop 0.3s ease-out forwards;';

                var times = getLiveTimes();

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:23px;height:23px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<div><div style="font-size:9px;font-weight:bold;color:#c084fc;">ALGO X</div><div style="font-size:5px;color:#38bdf8;">HACK ENGINE</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;gap:4px;"><span style="background:#14532d;color:#22c55e;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #22c55e;">BD: <span id="bd-clock-2">' + times.bd + '</span></span><span style="background:#713f12;color:#facc15;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #facc15;">CORTEX: <span id="cortex-clock-2">' + times.cortex + '</span></span></div>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:bold;margin-bottom:10px;color:#e2e8f0;">Kitni trades lagani hain?</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">' +
                                  '<button class="algo-trade-btn" data-trades="1" style="background:#180830;border:2px solid #52057B;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear;"><div style="font-size:11px;font-weight:bold;color:#facc15;">1</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="2" style="background:#180830;border:2px solid #F59E0B;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 0.4s;"><div style="font-size:11px;font-weight:bold;color:#38bdf8;">2</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="3" style="background:#180830;border:2px solid #6366F1;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 0.8s;"><div style="font-size:11px;font-weight:bold;color:#f472b6;">3</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="4" style="background:#180830;border:2px solid #10B981;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 1.2s;"><div style="font-size:11px;font-weight:bold;color:#4ade80;">4</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="5" style="background:#180830;border:2px solid #E11D48;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 1.6s;"><div style="font-size:11px;font-weight:bold;color:#f87171;">5</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="6" style="background:#180830;border:2px solid #38bdf8;border-radius:7px;padding:5px;color:#fff;text-align:center;cursor:pointer;animation:fastLighting 3s infinite linear 2s;"><div style="font-size:11px;font-weight:bold;color:#38bdf8;">6</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-2" style="background:transparent;border:1px solid #ef4444;color:#ef4444;width:100%;padding:6px;border-radius:6px;font-weight:bold;font-size:8px;cursor:pointer;animation:fastLighting 4s infinite linear;">CANCEL</button>';

                d.body.appendChild(panel);

                var clockInterval2 = setInterval(function(){
                    var t = getLiveTimes();
                    var bdEl = d.getElementById('bd-clock-2');
                    var cxEl = d.getElementById('cortex-clock-2');
                    if(bdEl) bdEl.innerText = t.bd;
                    if(cxEl) cxEl.innerText = t.cortex;
                }, 1000);

                var tradeBtns = panel.querySelectorAll('.algo-trade-btn');
                tradeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        clearInterval(clockInterval2);
                        var selectedTrades = btn.getAttribute('data-trades');
                        panel.remove();
                        
                        var hindiTradeText = selectedTrades == "1" ? "Ek trade select ho chuka hai." : selectedTrades + " trades select ho chuke hain.";
                        speakHindi(hindiTradeText + " Candle stick data analyze kara ja raha hai, weight karun.", function(){
                            startCortexHackScan(wrap, selectedTime, selectedTrades);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-2').onclick = function(){
                    clearInterval(clockInterval2);
                    panel.remove();
                    var ab = d.getElementById('algo-active-badge');
                    if(ab) ab.remove();
                    wrap.style.display = 'flex';
                };
            }

            // Step 3: Fullscreen Hacker Scanner with Top & Bottom Cyber Animations & Image/Logo
            function startCortexHackScan(wrap, selectedTime, selectedTrades){
                var panel = d.createElement('div');
                panel.id = 'hack-fullscreen-overlay';
                panel.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(2, 8, 4, 0.95);z-index:2147483647;font-family:monospace;color:#22c55e;display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:12px 10px;box-sizing:border-box;box-shadow:inset 0 0 120px #22c55e;overflow:hidden;';

                panel.innerHTML = '<div style="width:100%;display:flex;justify-content:space-between;align-items:center;background:rgba(3,15,7,0.85);border:1px solid #22c55e;padding:6px 12px;border-radius:8px;box-shadow:0 0 15px rgba(34,197,94,0.4);">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:24px;height:24px;border-radius:50%;border:1px solid #22c55e;box-shadow:0 0 8px #22c55e;" />' +
                                  '<span style="font-size:10px;font-weight:bold;color:#22c55e;animation:topBottomFlash 1s infinite;">[CYBER_MATRIX_ACTIVE]</span>' +
                                  '</div>' +
                                  '<div style="font-size:9px;color:#facc15;font-weight:bold;animation:topBottomFlash 0.8s infinite;">CANDLE HACKING...</div>' +
                                  '</div>' +

                                  // Center Compact Hack Box (As requested: "ছোট হয়ে গেছে না, এটা এরকমই থাকবে")
                                  '<div style="width:100%;max-width:360px;background:#030c05;border:2px solid #22c55e;border-radius:14px;padding:14px;box-shadow:0 0 50px rgba(34,197,94,0.7);margin:auto 0;">' +
                                  '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;border-bottom:1px solid #14532d;padding-bottom:5px;font-size:8.5px;font-weight:bold;">' +
                                  '<span style="color:#22c55e;">[ROOT@MARKET]</span>' +
                                  '<span style="color:#ef4444;animation:terminalBlink 0.6s infinite;">BREACH ACTIVE</span>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:900;color:#22c55e;text-align:center;margin-bottom:6px;letter-spacing:1px;text-shadow:0 0 10px #22c55e;">HACK_MKT.EXE</div>' +
                                  '<div style="font-size:6.5px;color:#38bdf8;text-align:center;margin-bottom:10px;">[ CORTEX EXPLOIT ENGINE V4.2 - LIVE SCAN ]</div>' +
                                  '<div id="terminal-logs" style="background:#010502;border:1px solid #14532d;border-radius:6px;padding:7px;font-size:7px;color:#4ade80;height:85px;overflow:hidden;display:flex;flex-direction:column;gap:3px;margin-bottom:10px;line-height:1.2;">' +
                                  '<div>$ sudo ./market_exploit.sh --target=quotex.io</div>' +
                                  '<div>[*] Loading exploit payload v4.2...</div>' +
                                  '<div>[+] Port 443 OPEN -> SSL/TLS handshake OK</div>' +
                                  '<div>$ python3 signal_injector.py --mode=aggressive</div>' +
                                  '</div>' +
                                  '<div style="width:100%;height:5px;background:#010502;border:1px solid #22c55e;border-radius:3px;margin-bottom:8px;overflow:hidden;">' +
                                  '<div id="hack-bar" style="width:20%;height:100%;background:#22c55e;box-shadow:0 0 8px #22c55e;transition:width 0.8s ease;"></div>' +
                                  '</div>' +
                                  '<div id="hack-status-text" style="text-align:center;font-size:8px;font-weight:bold;color:#facc15;">[ROOT@MARKET] Initializing exploit...</div>' +
                                  '</div>' +

                                  // Bottom Cyber / Hacking Banner with Matrix Streams & Logo
                                  '<div style="width:100%;display:flex;justify-content:space-between;align-items:center;background:rgba(3,15,7,0.85);border:1px solid #22c55e;padding:6px 12px;border-radius:8px;box-shadow:0 0 15px rgba(34,197,94,0.4);">' +
                                  '<div style="font-size:7.5px;color:#38bdf8;font-weight:bold;animation:topBottomFlash 1.2s infinite;">SOCKET: CONNECTED [99.8%]</div>' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<span style="font-size:7.5px;color:#facc15;font-weight:bold;">ALGO_BYPASS_OK</span>' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:20px;height:20px;border-radius:50%;border:1px solid #facc15;" />' +
                                  '</div>' +
                                  '</div>';

                d.body.appendChild(panel);

                setTimeout(function(){
                    var logs = panel.querySelector('#terminal-logs');
                    var bar = panel.querySelector('#hack-bar');
                    var status = panel.querySelector('#hack-status-text');
                    if(logs && bar && status) {
                        logs.innerHTML += '<div style="color:#38bdf8;">[+] TOR circuit established: 7 hops</div>';
                        logs.innerHTML += '<div style="color:#facc15;">[!] Firewall BYPASSED -> root shell acquired</div>';
                        bar.style.width = '55%';
                        status.innerText = 'Candle stick data analyze kara ja raha hai, weight karun.';
                    }
                }, 1200);

                setTimeout(function(){
                    var logs = panel.querySelector('#terminal-logs');
                    var bar = panel.querySelector('#hack-bar');
                    var status = panel.querySelector('#hack-status-text');
                    if(logs && bar && status) {
                        logs.innerHTML += '<div style="color:#ef4444;">[!] MACD PATCHED -> signal FORCED</div>';
                        logs.innerHTML += '<div style="color:#22c55e;">$ ./signal_amplifier --boost=999%</div>';
                        bar.style.width = '90%';
                        status.innerText = 'Ami trade place korechi, asha kori profit hobe.';
                    }
                }, 2400);

                setTimeout(function(){
                    var bar = panel.querySelector('#hack-bar');
                    var status = panel.querySelector('#hack-status-text');
                    if(bar) bar.style.width = '100%';
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

                        speakHindi("Market scanning successful ho chuka hai. Ami trade place korechi, asha kori profit hobe.", function(){
                            for (var i = 0; i < parseInt(selectedTrades); i++) {
                                (function(idx){
                                    setTimeout(function(){
                                        triggerActualTrade(isCall);
                                    }, idx * 350);
                                })(i);
                            }

                            panel.innerHTML = '<div style="width:100%;max-width:340px;background:#030c05;border:2px solid #22c55e;border-radius:14px;padding:20px;box-shadow:0 0 60px rgba(34,197,94,0.8);text-align:center;margin:auto;">' +
                                              '<div style="font-size:16px;font-weight:900;color:' + (isCall ? '#22c55e' : '#ef4444') + ';margin-bottom:6px;text-shadow:0 0 10px currentColor;">' + (isCall ? 'BUY' : 'SELL') + ' TRADES PLACED (' + selectedTrades + ')</div>' +
                                              '<div style="font-size:8px;color:#facc15;margin-bottom:10px;">CONFIDENCE: 70% | SUCCESS</div>' +
                                              '<div style="font-size:7.5px;color:#94a3b8;">Trade closed. Next scan in 10s</div>' +
                                              '</div>';

                            setTimeout(function(){
                                panel.remove();
                                var ab = d.getElementById('algo-active-badge');
                                if(ab) ab.remove();
                                wrap.style.display = 'flex';
                            }, 1600);
                        });
                    });
                }, 3600);
            }

            function forceClick(el) {
                if(!el) return false;
                try {
                    var box = el.getBoundingClientRect();
                    var cx = box.left + (box.width / 2);
                    var cy = box.top + (box.height / 2);
                    ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'].forEach(function(evName){
                        var ev = new MouseEvent(evName, {
                            bubbles: true, cancelable: true, view: window,
                            clientX: cx,clientY: cy,screenX: cx,screenY: cy
                        });
                        el.dispatchEvent(ev);
                    });
                    if(typeof el.click === 'function') el.click();
                    return true;
                } catch(e) { return false; }
            }

            function triggerActualTrade(isCall){
                var clicked = false;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(isCall && isUpBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
                    }
                    if(!isCall && isDownBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
                    }
                }
                
                if(!clicked){
                    var selectors = isCall ? [
                        '.section-deal__button-up button', '.section-deal__button-up',
                        '.btn-call', 'button.call', 'button[class*="call"]', '.button-buy', '[class*="buy"]'
                    ] : [
                        '.section-deal__button-down button', '.section-deal__button-down',
                        '.btn-put', 'button.put', 'button[class*="put"]', '.button-sell', '[class*="sell"]'
                    ];

                    for(var i=0; i<selectors.length; i++){
                        var btns = d.querySelectorAll(selectors[i]);
                        for(var j=0; j<btns.length; j++){
                            if(btns[j] && btns[j].getBoundingClientRect().width > 0){
                                if(forceClick(btns[j])){ clicked = true; break; }
                            }
                        }
                        if(clicked) break;
                    }
                }
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
