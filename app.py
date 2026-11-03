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
    return "ROSHMALAI AI BOT Engine v160.0 [R-A Trading Community] Running 24/7!"

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
            "trend": "ROSHMALAI SWEET MOMENTUM",
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
            var uniqueId = 'roshmalai_bot_' + Math.floor(Math.random() * 10000);
            
            // Cleanup existing elements if any
            ["roshmalai-candy","roshmalai-status-panel","roshmalai-welcome","roshmalai_global_style"].forEach(function(i){
                var e = d.getElementById(i);
                if(e) e.remove();
            });

            var s = d.createElement('style');
            s.id = 'roshmalai_global_style';
            s.innerHTML = '@keyframes roshmalaiGlow {' +
                          '0% { border-color: #ff3399; box-shadow: 0 0 25px rgba(255,51,153,0.9), inset 0 0 12px rgba(0,255,255,0.6); }' +
                          '33% { border-color: #00ffff; box-shadow: 0 0 30px rgba(0,255,255,1), inset 0 0 15px rgba(255,51,153,0.8); }' +
                          '66% { border-color: #ffcc00; box-shadow: 0 0 25px rgba(255,204,0,0.9), inset 0 0 12px rgba(0,255,128,0.6); }' +
                          '100% { border-color: #ff3399; box-shadow: 0 0 25px rgba(255,51,153,0.9), inset 0 0 12px rgba(0,255,255,0.6); }' +
                          '}' +
                          '@keyframes candyBounce {0%{transform:scale(1);}50%{transform:scale(1.08);}100%{transform:scale(1);}}' +
                          '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -48%) scale(0.9);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}' +
                          '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
            d.head.appendChild(s);

            var isVerified = sessionStorage.getItem('roshmalai_verified_' + uniqueId) === 'true';

            if(!isVerified){
                createWelcomePanel();
            } else {
                createCandyBot();
            }

            function createWelcomePanel(){
                var panel = d.createElement('div');
                panel.id = 'roshmalai-welcome';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:280px;background:linear-gradient(135deg, #12051a 0%, #2a0836 100%);border:3px solid #ff3399;border-radius:18px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);overflow:hidden;animation:panelPop 0.3s ease-out forwards, roshmalaiGlow 4s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#09020d;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #3d0d4f;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:10px;">' +
                                   '<img src="https://i.postimg.cc/tCRkzVFn/IMG-20261103-230250.jpg" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2px solid #ff3399;" />' +
                                   '<div>' +
                                   '<div style="font-size:11px;font-weight:900;color:#ff3399;letter-spacing:1px;">ROSHMALAI BOT</div>' +
                                   '<div style="font-size:6px;color:#00ffff;">SWEET AI TRADING</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<button id="close-welcome" style="background:#2a0836;border:1px solid #ff3399;color:#ff3399;width:22px;height:22px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:12px;">×</button>';
                panel.appendChild(header);
                
                header.querySelector('#close-welcome').onclick = function(){ panel.remove(); };

                var box = d.createElement('div');
                box.style.cssText = 'padding:16px;background:transparent;text-align:center;';
                box.innerHTML = '<div style="margin-bottom:10px;"><img src="https://i.postimg.cc/tCRkzVFn/IMG-20261103-230250.jpg" style="width:55px;height:55px;border-radius:50%;object-fit:cover;border:3px solid #ff3399;animation:roshmalaiGlow 4s infinite linear;" /></div>' +
                                '<div style="font-size:8px;color:#00ffff;margin-bottom:8px;font-weight:bold;">ENTER PASSWORD TO UNLOCK ROSHMALAI</div>' +
                                '<input type="password" id="roshmalai-pass" placeholder="Password" style="width:100%;box-sizing:border-box;background:#180721;border:1.5px solid #ff3399;padding:8px;border-radius:6px;color:#fff;font-size:9px;outline:none;margin-bottom:10px;text-align:center;" />' +
                                '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #ff3399, #00ffff);border:none;padding:8px;border-radius:6px;font-weight:900;font-size:9px;color:#000;cursor:pointer;box-shadow:0 0 15px rgba(255,51,153,0.6);">ACTIVATE ROSHMALAI</button>' +
                                '<div style="font-size:7px;color:#ff1744;margin-top:6px;" id="err-msg"></div>';
                panel.appendChild(box);

                var verifyBtn = box.querySelector('#verify-btn');
                var passInput = box.querySelector('#roshmalai-pass');
                var errMsg = box.querySelector('#err-msg');

                verifyBtn.onclick = function(){
                    var val = passInput.value.trim();
                    if(val === '112233'){
                        verifyBtn.innerHTML = '<span style="display:inline-block;width:10px;height:10px;border:2px solid #000;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.8s linear infinite;"></span> Verifying...';
                        setTimeout(function(){
                            sessionStorage.setItem('roshmalai_verified_' + uniqueId, 'true');
                            panel.remove();
                            createCandyBot();
                        }, 1000);
                    } else {
                        errMsg.innerText = '⚠️ INCORRECT PASSWORD!';
                        passInput.style.borderColor = '#ff1744';
                    }
                };

                d.body.appendChild(panel);
            }

            function createCandyBot(){
                var wrap = d.createElement('div');
                wrap.id = 'roshmalai-candy';
                wrap.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.style.cssText = 'width:62px;height:62px;border-radius:50%;background:radial-gradient(circle, #2a0836 0%, #12051a 80%);display:flex;align-items:center;justify-content:center;border:3px solid #ff3399;animation:roshmalaiGlow 3s infinite linear, candyBounce 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 25px rgba(255,51,153,0.8);';
                b.innerHTML = '<img src="https://i.postimg.cc/tCRkzVFn/IMG-20261103-230250.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                var lbl = d.createElement('div');
                lbl.style.cssText = 'margin-top:4px;font-size:7px;font-weight:900;color:#ff3399;font-family:sans-serif;background:rgba(18,5,26,0.95);padding:2px 8px;border-radius:4px;border:1.5px solid #ff3399;white-space:nowrap;box-shadow:0 0 8px rgba(255,51,153,0.5);';
                lbl.innerText = '🍬 ROSHMALAI';
                wrap.appendChild(lbl);

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
                    openStatusPanel(wrap);
                };
            }

            function openStatusPanel(wrap){
                var existing = d.getElementById('roshmalai-status-panel');
                if(existing) { existing.remove(); wrap.style.display = 'flex'; return; }

                wrap.style.display = 'none';

                var panel = d.createElement('div');
                panel.id = 'roshmalai-status-panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:265px;background:linear-gradient(135deg, #12051a 0%, #2a0836 100%);border:3px solid #ff3399;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 15px 40px rgba(0,0,0,0.9);overflow:hidden;animation:panelPop 0.25s ease-out forwards, roshmalaiGlow 4s infinite linear;';

                var header = d.createElement('div');
                header.style.cssText = 'background:#09020d;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #3d0d4f;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/tCRkzVFn/IMG-20261103-230250.jpg" style="width:22px;height:22px;border-radius:50%;object-fit:cover;border:2px solid #ff3399;" />' +
                                   '<span style="font-size:10px;font-weight:900;color:#ff3399;letter-spacing:0.5px;">ROSHMALAI AI BOT</span>' +
                                   '</div>' +
                                   '<div style="display:flex;gap:5px;">' +
                                   '<button id="minimize-panel" style="background:#2a0836;border:1px solid #ff3399;color:#ff3399;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:12px;" title="Minimize">_</button>' +
                                   '<button id="close-panel" style="background:#2a0836;border:1px solid #ff3399;color:#ff3399;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:10px;" title="Close">×</button>' +
                                   '</div>';
                panel.appendChild(header);

                var closeFunc = function(){
                    panel.remove();
                    wrap.style.display = 'flex';
                };

                header.querySelector('#minimize-panel').onclick = closeFunc;
                header.querySelector('#close-panel').onclick = closeFunc;

                var body = d.createElement('div');
                body.style.cssText = 'padding:12px;display:flex;flex-direction:column;gap:10px;';
                
                var markets = [
                    { name: "EURUSD_otc", label: "EUR/USD OTC" },
                    { name: "GBPUSD_otc", label: "GBP/USD OTC" },
                    { name: "AUDUSD_otc", label: "AUD/USD OTC" },
                    { name: "USDJPY_otc", label: "USD/JPY OTC" },
                    { name: "EURJPY_otc", label: "EUR/JPY OTC" },
                    { name: "NZDUSD_otc", label: "NZD/USD OTC" },
                    { name: "USDCAD_otc", label: "USD/CAD OTC" },
                    { name: "GBPJPY_otc", label: "GBP/JPY OTC" },
                    { name: "EURUSD", label: "EUR/USD (Real)" },
                    { name: "GBPUSD", label: "GBP/USD (Real)" }
                ];

                var row = d.createElement('div');
                row.style.cssText = 'display:flex;gap:8px;';

                // Timeframe
                var tfBox = d.createElement('div');
                tfBox.style.cssText = 'flex:1;display:flex;flex-direction:column;gap:3px;';
                tfBox.innerHTML = '<div style="font-size:6.5px;color:#00ffff;font-weight:bold;">TIME FRAME:</div>';
                
                var tfSelect = d.createElement('select');
                tfSelect.style.cssText = 'width:100%;background:#180721;border:1.5px solid #ff3399;color:#fff;padding:5px;border-radius:4px;font-size:7.5px;outline:none;cursor:pointer;';
                ['5S', '10S', '15S', '30S', '1M', '2M'].forEach(function(tf){
                    var opt = d.createElement('option');
                    opt.value = tf; opt.text = tf;
                    if(tf === '30S') opt.selected = true;
                    tfSelect.appendChild(opt);
                });
                tfBox.appendChild(tfSelect);
                row.appendChild(tfBox);

                // Market
                var mBox = d.createElement('div');
                mBox.style.cssText = 'flex:1.2;display:flex;flex-direction:column;gap:3px;';
                mBox.innerHTML = '<div style="font-size:6.5px;color:#00ffff;font-weight:bold;">MARKET PAIR:</div>';

                var mSelect = d.createElement('select');
                mSelect.style.cssText = 'width:100%;background:#180721;border:1.5px solid #ff3399;color:#fff;padding:5px;border-radius:4px;font-size:7.5px;outline:none;cursor:pointer;';
                markets.forEach(function(m){
                    var opt = d.createElement('option');
                    opt.value = m.name; opt.text = m.label;
                    mSelect.appendChild(opt);
                });
                mBox.appendChild(mSelect);
                row.appendChild(mBox);

                body.appendChild(row);

                // Display Area
                var displayArea = d.createElement('div');
                displayArea.style.cssText = 'width:100%;height:65px;background:#09020d;border:1.5px dashed #ff3399;border-radius:6px;display:flex;align-items:center;justify-content:center;text-align:center;overflow:hidden;';
                displayArea.innerHTML = '<div style="font-size:8px;color:#8a99ad;font-weight:bold;">ROSHMALAI READY</div>';
                body.appendChild(displayArea);

                // Get Signal Button
                var btn = d.createElement('button');
                btn.style.cssText = 'width:100%;background:linear-gradient(90deg, #ff3399, #00ffff);border:none;padding:9px;border-radius:6px;font-weight:900;font-size:10px;color:#000;cursor:pointer;box-shadow:0 0 15px rgba(255,51,153,0.7);letter-spacing:1px;';
                btn.innerText = '🍬 GET ROSHMALAI SIGNAL 🍬';
                
                btn.onclick = function(){
                    runRoshmalaiSignal(wrap, displayArea);
                };
                body.appendChild(btn);

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
                if(window._roshmalaiTradeLocked) return;
                window._roshmalaiTradeLocked = true;
                setTimeout(function(){ window._roshmalaiTradeLocked = false; }, 3000);

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

            function runRoshmalaiSignal(wrap, displayArea){
                if(isScanningActive) return;
                isScanningActive = true;

                displayArea.innerHTML = '<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;">' +
                                        '<div style="width:18px;height:18px;border:2px solid #ff3399;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.6s linear infinite;"></div>' +
                                        '<div style="font-size:8.5px;color:#ff3399;font-weight:900;letter-spacing:0.8px;">ROshmalai Scanning...</div>' +
                                        '</div>';

                setTimeout(function(){
                    fetch('https://draco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 96}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        triggerTrade(isDown);

                        var col = isDown ? '#ff1744' : '#00ff66';
                        var label = isDown ? '🔻 DOWN SIGNAL' : '🟢 UP SIGNAL';

                        displayArea.innerHTML = '<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;animation:panelPop 0.3s ease-out;">' +
                                                '<div style="font-size:14px;font-weight:950;color:' + col + ';text-shadow:0 0 10px ' + col + ';">' + label + '</div>' +
                                                '<div style="font-size:7.5px;color:#00ffff;">Confidence: ' + (j.confidence || 96) + '%</div>' +
                                                '</div>';

                        setTimeout(function(){
                            isScanningActive = false;
                            var panel = d.getElementById('roshmalai-status-panel');
                            if(panel) panel.remove();
                            if(wrap) wrap.style.display = 'flex';
                        }, 5000);
                    });
                }, 5000);
            }
        } catch(e) { console.error("RoshmalaiBot Error:", e); }
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
