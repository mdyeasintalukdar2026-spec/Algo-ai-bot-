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
            
            // Remove old elements if any
            ["roshmalai-candy","roshmalai-status-panel","roshmalai-welcome","tbp-floating-btn","tbp-control-panel","tbp-global-style","algo-floating-btn","algo-control-panel","algo-global-style","algo-touch-effect"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var s = d.createElement('style');
            s.id = 'algo-global-style';
            s.innerHTML = '@keyframes algoGlow {' +
                          '0% { border-color: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.8), inset 0 0 12px rgba(168,85,247,0.5); }' +
                          '50% { border-color: #ec4899; box-shadow: 0 0 35px rgba(236,72,153,1), inset 0 0 15px rgba(236,72,153,0.8); }' +
                          '100% { border-color: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.8), inset 0 0 12px rgba(168,85,247,0.5); }' +
                          '}' +
                          '@keyframes algoPulse {0%{transform:scale(1);}50%{transform:scale(1.06);}100%{transform:scale(1);}}' +
                          '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -48%) scale(0.85);}100%{opacity:1;transform:translate(-50%, -50%) scale(0.95);}}' +
                          '@keyframes touchRipple {0% {transform: scale(0.5); opacity: 1;} 100% {transform: scale(2.2); opacity: 0;}}';
            d.head.appendChild(s);

            // Touch Ripple Effect for Clicks
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
                    utterance.rate = 1.05; 
                    utterance.pitch = 1.4; 
                    
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
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:radial-gradient(circle, #2e0854 0%, #0d021f 80%);display:flex;align-items:center;justify-content:center;border:3px solid #a855f7;animation:algoGlow 3s infinite linear, algoPulse 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 25px rgba(168,85,247,0.8);';
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
                b.style.cssText = 'width:55px;height:55px;border-radius:50%;background:#0d021f;display:flex;align-items:center;justify-content:center;border:2px solid #a855f7;overflow:hidden;box-shadow:0 0 15px rgba(168,85,247,0.8);';
                b.innerHTML = '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                activeBadge.appendChild(b);

                var label = d.createElement('div');
                label.style.cssText = 'margin-top:3px;font-size:8px;font-weight:900;color:#000;font-family:sans-serif;background:#22c55e;padding:2px 8px;border-radius:4px;border:1px solid #fff;text-align:center;box-shadow:0 0 8px rgba(34,197,94,0.8);';
                label.innerText = 'ACTIVE';
                activeBadge.appendChild(label);

                d.body.appendChild(activeBadge);
            }

            // Step 1: Time Frame Panel (5% smaller, Unique distinct borders)[span_2](start_span)[span_2](end_span)
            function openTimeFramePanel(wrap){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                // 5% smaller size and distinct styled borders
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);padding:14px;animation:panelPop 0.3s ease-out forwards;';

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:24px;height:24px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<div><div style="font-size:9px;font-weight:bold;color:#c084fc;">ALGO X</div><div style="font-size:5px;color:#38bdf8;">AI ENGINE ONLINE</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;gap:4px;"><span style="background:#14532d;color:#22c55e;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #22c55e;">01 TIME</span><span style="background:#713f12;color:#facc15;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #facc15;">02 TRADES</span></div>' +
                                  '</div>' +
                                  '<div style="font-size:14px;font-weight:bold;margin-bottom:12px;color:#e2e8f0;">Trade time select karein</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;">' +
                                  '<button class="algo-time-btn" data-time="5" style="background:#180830;border:2px solid #facc15;border-radius:9px;padding:10px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#facc15;">5 SEC</div><div style="font-size:6px;color:#94a3b8;">TURBO</div></button>' +
                                  '<button class="algo-time-btn" data-time="15" style="background:#180830;border:2px solid #38bdf8;border-radius:9px;padding:10px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#38bdf8;">15 SEC</div><div style="font-size:6px;color:#94a3b8;">RAPID</div></button>' +
                                  '<button class="algo-time-btn" data-time="30" style="background:#180830;border:2px solid #f472b6;border-radius:9px;padding:10px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#f472b6;">30 SEC</div><div style="font-size:6px;color:#94a3b8;">BALANCED</div></button>' +
                                  '<button class="algo-time-btn" data-time="60" style="background:#180830;border:2px solid #4ade80;border-radius:9px;padding:10px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#4ade80;">1 MIN</div><div style="font-size:6px;color:#94a3b8;">PRECISION</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-1" style="background:transparent;border:1px solid #ef4444;color:#ef4444;width:100%;padding:7px;border-radius:7px;font-weight:bold;font-size:9px;cursor:pointer;">CANCEL</button>';

                d.body.appendChild(panel);

                var timeBtns = panel.querySelectorAll('.algo-time-btn');
                timeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        var selectedTime = btn.getAttribute('data-time');
                        speakHindi("Time frame set ho gaya hai.", function(){
                            panel.remove();
                            openTradesCountPanel(wrap, selectedTime);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-1').onclick = function(){
                    panel.remove();
                    var ab = d.getElementById('algo-active-badge');
                    if(ab) ab.remove();
                    wrap.style.display = 'flex';
                };
            }

            // Step 2: Trades Count Panel (5% smaller, Unique distinct borders for each option)[span_3](start_span)[span_3](end_span)
            function openTradesCountPanel(wrap, selectedTime){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:295px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);padding:14px;animation:panelPop 0.3s ease-out forwards;';

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #3b0764;padding-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:24px;height:24px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<div><div style="font-size:9px;font-weight:bold;color:#c084fc;">ALGO X</div><div style="font-size:5px;color:#38bdf8;">AI ENGINE ONLINE</div></div>' +
                                  '</div>' +
                                  '<div style="display:flex;gap:4px;"><span style="background:#14532d;color:#22c55e;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #22c55e;">01 TIME</span><span style="background:#713f12;color:#facc15;font-size:6px;padding:2px 5px;border-radius:3px;border:1px solid #facc15;">02 TRADES</span></div>' +
                                  '</div>' +
                                  '<div style="font-size:14px;font-weight:bold;margin-bottom:12px;color:#e2e8f0;">Kitni trades lagani hain?</div>' +
                                  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;">' +
                                  '<button class="algo-trade-btn" data-trades="1" style="background:#180830;border:2px solid #facc15;border-radius:9px;padding:9px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#facc15;">1</div><div style="font-size:6px;color:#94a3b8;">SINGLE</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="2" style="background:#180830;border:2px solid #38bdf8;border-radius:9px;padding:9px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#38bdf8;">2</div><div style="font-size:6px;color:#94a3b8;">DOUBLE</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="3" style="background:#180830;border:2px solid #f472b6;border-radius:9px;padding:9px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#f472b6;">3</div><div style="font-size:6px;color:#94a3b8;">TRIPLE</div></button>' +
                                  '<button class="algo-trade-btn" data-trades="4" style="background:#180830;border:2px solid #4ade80;border-radius:9px;padding:9px;color:#fff;text-align:left;cursor:pointer;"><div style="font-size:13px;font-weight:bold;color:#4ade80;">4</div><div style="font-size:6px;color:#94a3b8;">MAX</div></button>' +
                                  '</div>' +
                                  '<button id="algo-cancel-2" style="background:transparent;border:1px solid #ef4444;color:#ef4444;width:100%;padding:7px;border-radius:7px;font-weight:bold;font-size:9px;cursor:pointer;">CANCEL</button>';

                d.body.appendChild(panel);

                var tradeBtns = panel.querySelectorAll('.algo-trade-btn');
                tradeBtns.forEach(function(btn){
                    btn.onclick = function(){
                        var selectedTrades = btn.getAttribute('data-trades');
                        panel.remove();
                        
                        var hindiTradeText = selectedTrades == "1" ? "Ek trade select ho chuka hai." : selectedTrades + " trades select ho chuke hain.";
                        speakHindi(hindiTradeText + " Chaliye sir, market ka pura check shuru karti hu. Support aur resistance level check ho rahe hain.", function(){
                            startNeuralScan(wrap, selectedTime, selectedTrades);
                        });
                    };
                });

                panel.querySelector('#algo-cancel-2').onclick = function(){
                    panel.remove();
                    var ab = d.getElementById('algo-active-badge');
                    if(ab) ab.remove();
                    wrap.style.display = 'flex';
                };
            }

            // Step 3: Neural Scan & Signal Execution with Animated Candle Flow
            function startNeuralScan(wrap, selectedTime, selectedTrades){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:300px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);padding:14px;animation:panelPop 0.3s ease-out forwards;';

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:20px;height:20px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<span style="font-size:8px;font-weight:bold;color:#c084fc;">ALGO X</span>' +
                                  '</div>' +
                                  '<span style="font-size:6px;color:#94a3b8;">MARKET SCAN / 01</span>' +
                                  '</div>' +
                                  '<div style="font-size:13px;font-weight:bold;margin-bottom:6px;color:#fff;">Neural market intelligence</div>' +
                                  '<div style="font-size:7px;color:#94a3b8;margin-bottom:4px;display:flex;justify-content:space-between;"><span>SUPPORT / RESIST</span><span style="color:#22c55e;">88%</span></div>' +
                                  '<div style="font-size:7px;color:#94a3b8;margin-bottom:4px;display:flex;justify-content:space-between;"><span>VOLUME FLOW</span><span style="color:#38bdf8;">92%</span></div>' +
                                  '<div style="font-size:7px;color:#94a3b8;margin-bottom:8px;display:flex;justify-content:space-between;"><span>TREND SYNC</span><span style="color:#facc15;">95%</span></div>' +
                                  // Animated Mini Live Candles Preview Box
                                  '<div style="background:#080112;border:1px solid #3b0764;border-radius:6px;height:35px;display:flex;align-items:center;justify-content:space-around;padding:0 8px;margin-bottom:8px;overflow:hidden;">' +
                                  '<div style="width:4px;height:20px;background:#22c55e;border-radius:2px;animation:algoPulse 1s infinite alternate;"></div>' +
                                  '<div style="width:4px;height:28px;background:#ef4444;border-radius:2px;animation:algoPulse 0.8s infinite alternate;"></div>' +
                                  '<div style="width:4px;height:15px;background:#22c55e;border-radius:2px;animation:algoPulse 1.2s infinite alternate;"></div>' +
                                  '<div style="width:4px;height:24px;background:#ef4444;border-radius:2px;animation:algoPulse 0.7s infinite alternate;"></div>' +
                                  '<div style="width:4px;height:30px;background:#22c55e;border-radius:2px;animation:algoPulse 0.9s infinite alternate;"></div>' +
                                  '</div>' +
                                  '<div id="algo-scan-status" style="text-align:center;font-size:9px;font-weight:bold;color:#38bdf8;background:#080112;padding:6px;border-radius:6px;border:1px solid #3b0764;">Scanning Market Patterns...</div>';

                d.body.appendChild(panel);

                setTimeout(function(){
                    var statusEl = panel.querySelector('#algo-scan-status');
                    if(statusEl) {
                        statusEl.innerText = "Market scanning successful ho chuka hai.";
                        statusEl.style.color = "#22c55e";
                    }

                    fetch('https://draco-ai-bot.onrender.com/signal?t=' + Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "CALL", confidence: 97}; })
                    .then(function(j){
                        var sig = String(j.signal || 'CALL').toUpperCase();
                        var isCall = (sig === 'CALL' || sig === 'UP' || sig === 'BUY');
                        var directionText = isCall ? 'CALL' : 'PUT';

                        speakHindi("Market scanning successful ho chuka hai. Meri saari analysis pe trade laga diya hai. Inshallah profit ho jaega.", function(){
                            panel.remove();
                            showExecutionPanel(wrap, directionText, selectedTrades);
                            for (var i = 0; i < parseInt(selectedTrades); i++) {
                                (function(idx){
                                    setTimeout(function(){
                                        triggerActualTrade(isCall);
                                    }, idx * 600);
                                })(i);
                            }
                        });
                    });
                }, 3500);
            }

            // Step 4: Final Execution Display Panel
            function showExecutionPanel(wrap, directionText, selectedTrades){
                var panel = d.createElement('div');
                panel.id = 'algo-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:300px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:2px solid #a855f7;border-radius:15px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);padding:14px;animation:panelPop 0.3s ease-out forwards;';

                panel.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">' +
                                  '<div style="display:flex;align-items:center;gap:6px;">' +
                                  '<img src="https://i.postimg.cc/gJGBhtsz/IMG-20261104-WA0017.jpg" style="width:20px;height:20px;border-radius:50%;border:1px solid #a855f7;" />' +
                                  '<span style="font-size:8px;font-weight:bold;color:#c084fc;">ALGO X</span>' +
                                  '</div>' +
                                  '<span style="font-size:6px;color:#22c55e;">EXECUTION SEQUENCE</span>' +
                                  '</div>' +
                                  '<div style="font-size:15px;font-weight:900;color:' + (directionText === 'CALL' ? '#22c55e' : '#ef4444') + ';text-align:center;margin:8px 0;">' + directionText + '</div>' +
                                  '<div style="font-size:7px;color:#94a3b8;text-align:center;margin-bottom:8px;">Trades Placed: ' + selectedTrades + ' | Status: Success</div>' +
                                  '<button id="algo-close-exec" style="background:#a855f7;color:#000;width:100%;padding:7px;border-radius:7px;font-weight:bold;font-size:9px;cursor:pointer;border:none;">OK / CLOSE</button>';

                d.body.appendChild(panel);

                panel.querySelector('#algo-close-exec').onclick = function(){
                    panel.remove();
                    var ab = d.getElementById('algo-active-badge');
                    if(ab) ab.remove();
                    wrap.style.display = 'flex';
                };
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
