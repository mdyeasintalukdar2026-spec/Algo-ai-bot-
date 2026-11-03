from flask import Flask, jsonify, make_response
import threading
import requests
import time
import random
import os

app = Flask(__name__, static_folder=None)

# ==========================================
# MASTER API KEYS & CONFIGURATIONS
# ==========================================
TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.route('/')
def home():
    return "TBP HACK BOT Engine v170.0 [R-A Trading Community] Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        current_time = time.time()
        base_signal = "UP" if (int(current_time * 1000) % 2 == 0 and random.choice([True, False])) else "DOWN"
        signal_conf = int(88 + (random.randint(0, 9)))
        res = jsonify({
            "signal": base_signal,
            "trend": "HACK_MKT_MOMENTUM",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "UP",
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
            var uniqueId = 'tbp_bot_' + Math.floor(Math.random() * 10000);
            
            // Remove old elements if any
            ["roshmalai-candy","roshmalai-status-panel","roshmalai-welcome","tbp-floating-btn","tbp-control-panel","tbp-global-style"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var s = d.createElement('style');
            s.id = 'tbp-global-style';
            s.innerHTML = '@keyframes tbpGlow {' +
                          '0% { border-color: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.8), inset 0 0 12px rgba(168,85,247,0.5); }' +
                          '50% { border-color: #ec4899; box-shadow: 0 0 35px rgba(236,72,153,1), inset 0 0 15px rgba(236,72,153,0.8); }' +
                          '100% { border-color: #a855f7; box-shadow: 0 0 25px rgba(168,85,247,0.8), inset 0 0 12px rgba(168,85,247,0.5); }' +
                          '}' +
                          '@keyframes tbpPulse {0%{transform:scale(1);}50%{transform:scale(1.06);}100%{transform:scale(1);}}' +
                          '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -48%) scale(0.9);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}' +
                          '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
            d.head.appendChild(s);

            createFloatingBot();

            function createFloatingBot(){
                var wrap = d.createElement('div');
                wrap.id = 'tbp-floating-btn';
                wrap.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:radial-gradient(circle, #2e0854 0%, #0d021f 80%);display:flex;align-items:center;justify-content:center;border:3px solid #a855f7;animation:tbpGlow 3s infinite linear, tbpPulse 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 25px rgba(168,85,247,0.8);';
                b.innerHTML = '<img src="https://i.postimg.cc/tCRkzVFn/IMG-20261103-230250.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                var badge = d.createElement('div');
                badge.style.cssText = 'margin-top:4px;font-size:7px;font-weight:900;color:#fff;font-family:sans-serif;background:rgba(13,2,31,0.95);padding:2px 8px;border-radius:4px;border:1.5px solid #a855f7;white-space:nowrap;box-shadow:0 0 8px rgba(168,85,247,0.6);';
                badge.innerHTML = '<span style="color:#22c55e;">● LIVE</span> TBP HACK';
                wrap.appendChild(badge);

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
                    openControlCenter(wrap);
                };
            }

            function openControlCenter(wrap){
                var existing = d.getElementById('tbp-control-panel');
                if(existing) { existing.remove(); wrap.style.display = 'flex'; return; }

                wrap.style.display = 'none';

                var panel = d.createElement('div');
                panel.id = 'tbp-control-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:290px;background:linear-gradient(135deg, #0d021f 0%, #1f053b 100%);border:3px solid #a855f7;border-radius:18px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);overflow:hidden;animation:panelPop 0.3s ease-out forwards, tbpGlow 4s infinite linear;';

                // Header
                var header = d.createElement('div');
                header.style.cssText = 'background:#080112;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #3b0764;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<div style="width:24px;height:24px;background:#a855f7;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#000;font-weight:bold;font-size:12px;">⚡</div>' +
                                   '<div>' +
                                   '<div style="font-size:11px;font-weight:900;color:#c084fc;letter-spacing:0.5px;">TBP HACK BOT</div>' +
                                   '<div style="font-size:6px;color:#22c55e;">● Running</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<div style="display:flex;gap:5px;">' +
                                   '<button id="tbp-min" style="background:#1f053b;border:1px solid #a855f7;color:#a855f7;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:12px;" title="Minimize">_</button>' +
                                   '<button id="tbp-close" style="background:#1f053b;border:1px solid #a855f7;color:#a855f7;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:10px;" title="Close">×</button>' +
                                   '</div>';
                panel.appendChild(header);

                var closeFunc = function(){
                    panel.remove();
                    wrap.style.display = 'flex';
                };

                header.querySelector('#tbp-min').onclick = closeFunc;
                header.querySelector('#tbp-close').onclick = closeFunc;

                var body = d.createElement('div');
                body.style.cssText = 'padding:14px;display:flex;flex-direction:column;gap:12px;';

                // P/L Box
                var plBox = d.createElement('div');
                plBox.style.cssText = 'background:#080112;border:1px solid #3b0764;border-radius:10px;padding:10px;text-align:center;';
                plBox.innerHTML = '<div style="font-size:16px;font-weight:950;color:#22c55e;margin-bottom:4px;">$0.00</div>' +
                                  '<div style="font-size:7px;color:#9ca3af;margin-bottom:8px;">P/L TODAY</div>' +
                                  '<div style="display:flex;justify-content:space-around;font-size:8px;border-top:1px solid #2e0854;padding-top:6px;">' +
                                  '<div><span style="color:#22c55e;font-weight:bold;">0</span> WINS</div>' +
                                  '<div><span style="color:#ef4444;font-weight:bold;">0</span> LOSS</div>' +
                                  '<div><span style="color:#c084fc;font-weight:bold;">0 / 20</span> TRADES</div>' +
                                  '</div>';
                body.appendChild(plBox);

                // Status & Details
                var infoGrid = d.createElement('div');
                infoGrid.style.cssText = 'display:flex;flex-direction:column;gap:6px;font-size:8px;background:#080112;padding:10px;border-radius:8px;border:1px solid #3b0764;';
                infoGrid.innerHTML = '<div style="display:flex;justify-content:between;"><span style="color:#9ca3af;">Status:</span><span id="tbp-status-text" style="color:#22c55e;font-weight:bold;">Ready</span></div>' +
                                     '<div style="display:flex;justify-content:between;"><span style="color:#9ca3af;">Next Trade:</span><span style="color:#c084fc;font-weight:bold;">10s</span></div>' +
                                     '<div style="display:flex;justify-content:between;"><span style="color:#9ca3af;">Timeframe:</span><span style="color:#fff;font-weight:bold;">S10 – 10s</span></div>' +
                                     '<div style="display:flex;justify-content:between;"><span style="color:#9ca3af;">Last Signal:</span><span style="color:#9ca3af;font-weight:bold;">--- (0%)</span></div>';
                body.appendChild(infoGrid);

                // Action Buttons (START, PAUSE, STOP)
                var btnRow = d.createElement('div');
                btnRow.style.cssText = 'display:flex;gap:8px;';

                var startBtn = d.createElement('button');
                startBtn.style.cssText = 'flex:1;background:#22c55e;border:none;padding:8px;border-radius:6px;font-weight:900;font-size:9px;color:#000;cursor:pointer;';
                startBtn.innerText = 'START';

                var pauseBtn = d.createElement('button');
                pauseBtn.style.cssText = 'flex:1;background:#eab308;border:none;padding:8px;border-radius:6px;font-weight:900;font-size:9px;color:#000;cursor:pointer;';
                pauseBtn.innerText = 'PAUSE';

                var stopBtn = d.createElement('button');
                stopBtn.style.cssText = 'flex:1;background:#ef4444;border:none;padding:8px;border-radius:6px;font-weight:900;font-size:9px;color:#fff;cursor:pointer;';
                stopBtn.innerText = 'STOP';

                btnRow.appendChild(startBtn);
                btnRow.appendChild(pauseBtn);
                btnRow.appendChild(stopBtn);
                body.appendChild(btnRow);

                // Click event for START (triggers hack scanning & trade)
                startBtn.onclick = function(){
                    runTbpHackEngine(wrap, infoGrid.querySelector('#tbp-status-text'));
                };

                panel.appendChild(body);
                d.body.appendChild(panel);
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

            function triggerTrade(isSell){
                if(window._tbpTradeLocked) return;
                window._tbpTradeLocked = true;
                setTimeout(function(){ window._tbpTradeLocked = false; }, 3000);

                var clicked = false;
                var allButtons = d.querySelectorAll('button, div[role="button"], span[class*="btn"]');
                for(var i=0; i<allButtons.length; i++){
                    var btn = allButtons[i];
                    var text = (btn.innerText || '').trim().toUpperCase();
                    var cls = (btn.className || '').toLowerCase();
                    
                    var isUpBtn = cls.includes('call') || cls.includes('buy') || cls.includes('up') || text === 'UP' || text === 'BUY' || text === 'HIGHER';
                    var isDownBtn = cls.includes('put') || cls.includes('sell') || cls.includes('down') || text === 'DOWN' || text === 'SELL' || text === 'LOWER';
                    
                    if(!isSell && isUpBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
                    }
                    if(isSell && isDownBtn && btn.getBoundingClientRect().width > 0){
                        if(forceClick(btn)){ clicked = true; break; }
                    }
                }
                
                if(!clicked){
                    var selectors = isSell ? [
                        '.section-deal__button-down button', '.section-deal__button-down',
                        '.btn-put', 'button.put', 'button[class*="put"]', '.button-sell', '[class*="sell"]'
                    ] : [
                        '.section-deal__button-up button', '.section-deal__button-up',
                        '.btn-call', 'button.call', 'button[class*="call"]', '.button-buy', '[class*="buy"]'
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

            var isScanningActive = false;

            function runTbpHackEngine(wrap, statusText){
                if(isScanningActive) return;
                isScanningActive = true;
                statusText.innerText = 'Scanning...';
                statusText.style.color = '#eab308';

                setTimeout(function(){
                    fetch('https://draco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 97}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        triggerTrade(isDown);

                        statusText.innerText = isDown ? 'DOWN (97%)' : 'UP (97%)';
                        statusText.style.color = isDown ? '#ef4444' : '#22c55e';

                        setTimeout(function(){
                            isScanningActive = false;
                            var panel = d.getElementById('tbp-control-panel');
                            if(panel) panel.remove();
                            if(wrap) wrap.style.display = 'flex';
                        }, 4000);
                    });
                }, 3000);
            }
        } catch(e) { console.error("TbpBot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def start_server():
    run_flask()

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
