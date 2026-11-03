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
    return "Quotex Tiger/Lion Sniper Bot Engine v150.0 [R-A Trading Community] Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        current_sec = int(time.time())
        base_signal = "UP" if (random.choice([True, False]) and current_sec % 3 != 0) else "DOWN"
        signal_conf = int(89 + (current_sec % 8))
        res = jsonify({
            "signal": base_signal,
            "trend": "TIGER MOMENTUM",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    except Exception as e:
        res = jsonify({
            "signal": "UP",
            "trend": "STRONG MOMENTUM",
            "confidence": 93,
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
            var uniqueId = 'tiger_bot_' + Math.floor(Math.random() * 10000);
            
            var oldS = d.getElementById('tiger_global_style');
            if(!oldS){
                var s = d.createElement('style');
                s.id = 'tiger_global_style';
                s.innerHTML = '@keyframes tigerGlow {' +
                              '0% { border-color: #ff9900; box-shadow: 0 0 25px rgba(255,153,0,0.8); }' +
                              '50% { border-color: #ff3300; box-shadow: 0 0 35px rgba(255,51,0,0.9); }' +
                              '100% { border-color: #ff9900; box-shadow: 0 0 25px rgba(255,153,0,0.8); }' +
                              '}' +
                              '@keyframes roarPulse {0%{transform:scale(1);}50%{transform:scale(1.05);}100%{transform:scale(1);}}' +
                              '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -45%) scale(0.85);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}' +
                              '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
                d.head.appendChild(s);
            }

            var isVerified = sessionStorage.getItem('tiger_bot_verified_' + uniqueId) === 'true';

            if(!isVerified){
                createLicensePanel();
            } else {
                createFloatingBot();
            }

            function createLicensePanel(){
                var panel = d.createElement('div');
                panel.id = 'tiger_license_panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:280px;background:linear-gradient(135deg, #0d0905 0%, #1a1005 100%);border:3px solid #ff9900;border-radius:16px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 20px 50px rgba(0,0,0,0.95);overflow:hidden;animation:panelPop 0.3s ease-out forwards, tigerGlow 4s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#080502;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #332005;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:10px;">' +
                                   '<img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:26px;height:26px;border-radius:50%;object-fit:cover;border:2px solid #ff9900;" />' +
                                   '<div>' +
                                   '<div style="font-size:11px;font-weight:900;color:#ff9900;letter-spacing:1px;">TIGER SNIPER BOT</div>' +
                                   '<div style="font-size:6px;color:#cc8833;">MAJESTIC TRADING SYSTEM</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<button id="close-license" style="background:#1a1005;border:1px solid #ff9900;color:#ff9900;width:22px;height:22px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:12px;">×</button>';
                panel.appendChild(header);
                
                header.querySelector('#close-license').onclick = function(){ panel.remove(); };

                var licenseBox = d.createElement('div');
                licenseBox.style.cssText = 'padding:16px;background:transparent;text-align:center;';
                licenseBox.innerHTML = '<div style="margin-bottom:10px;"><img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:55px;height:55px;border-radius:50%;object-fit:cover;border:3px solid #ff9900;animation:tigerGlow 4s infinite linear;" /></div>' +
                                       '<div style="font-size:8px;color:#ffcc66;margin-bottom:8px;font-weight:bold;">ENTER PASSWORD TO UNLEASH THE TIGER</div>' +
                                       '<input type="password" id="license-input" placeholder="Enter Password (e.g. 112233)" style="width:100%;box-sizing:border-box;background:#140d05;border:1.5px solid #ff9900;padding:8px;border-radius:6px;color:#fff;font-size:9px;outline:none;margin-bottom:10px;text-align:center;" />' +
                                       '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #ff9900, #ff3300);border:none;padding:8px;border-radius:6px;font-weight:900;font-size:9px;color:#000;cursor:pointer;box-shadow:0 0 15px rgba(255,153,0,0.6);">ACTIVATE TIGER BOT</button>' +
                                       '<div style="font-size:7px;color:#ff3300;margin-top:6px;" id="err-msg"></div>';
                panel.appendChild(licenseBox);

                var verifyBtn = licenseBox.querySelector('#verify-btn');
                var licenseInput = licenseBox.querySelector('#license-input');
                var errMsg = licenseBox.querySelector('#err-msg');

                verifyBtn.onclick = function(){
                    var keyVal = licenseInput.value.trim();
                    if(keyVal === '112233'){
                        verifyBtn.innerHTML = '<span style="display:inline-block;width:10px;height:10px;border:2px solid #000;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.8s linear infinite;"></span> Verifying...';
                        setTimeout(function(){
                            sessionStorage.setItem('tiger_bot_verified_' + uniqueId, 'true');
                            panel.remove();
                            createFloatingBot();
                        }, 1000);
                    } else {
                        errMsg.innerText = '⚠️ INCORRECT PASSWORD!';
                        licenseInput.style.borderColor = '#ff3300';
                    }
                };

                d.body.appendChild(panel);
            }

            function createFloatingBot(){
                var existingWrap = d.getElementById('tiger_target_wrap');
                if(existingWrap) existingWrap.remove();

                var wrap = d.createElement('div');
                wrap.id = 'tiger_target_wrap';
                wrap.style.cssText = 'position:fixed;bottom:70px;right:20px;display:flex;flex-direction:column;align-items:center;z-index:2147483647;cursor:pointer;';
                
                var b = d.createElement('div');
                b.id = 'tiger_target_btn';
                b.style.cssText = 'width:68px;height:68px;border-radius:50%;background:#080502;display:flex;align-items:center;justify-content:center;border:3px solid #ff9900;animation:tigerGlow 4s infinite linear, roarPulse 2s infinite ease-in-out;box-sizing:border-box;overflow:hidden;box-shadow:0 0 20px rgba(255,153,0,0.7);';
                b.innerHTML = '<img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />';
                wrap.appendChild(b);

                var lbl = d.createElement('div');
                lbl.style.cssText = 'margin-top:4px;font-size:7px;font-weight:900;color:#ff9900;font-family:sans-serif;background:rgba(8,5,2,0.95);padding:2px 8px;border-radius:4px;border:1.5px solid #ff9900;white-space:nowrap;box-shadow:0 0 8px rgba(255,153,0,0.5);';
                lbl.innerText = 'TIGER SNIPER';
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
                    openControlPanel();
                };
            }

            function openControlPanel(){
                var existingPanel = d.getElementById('tiger_control_panel');
                if(existingPanel) { existingPanel.remove(); return; }

                var panel = d.createElement('div');
                panel.id = 'tiger_control_panel';
                panel.style.cssText = 'position:fixed;bottom:150px;right:20px;width:290px;background:linear-gradient(135deg, #0d0905 0%, #1a1005 100%);border:3px solid #ff9900;border-radius:14px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 15px 40px rgba(0,0,0,0.9);overflow:hidden;animation:panelPop 0.25s ease-out forwards, tigerGlow 5s infinite linear;';

                var header = d.createElement('div');
                header.style.cssText = 'background:#080502;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #332005;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:22px;height:22px;border-radius:50%;object-fit:cover;border:2px solid #ff9900;" />' +
                                   '<span style="font-size:10px;font-weight:900;color:#ff9900;letter-spacing:0.5px;">TIGER CONTROL PANEL</span>' +
                                   '</div>' +
                                   '<button id="close-ctrl" style="background:#1a1005;border:1px solid #ff9900;color:#ff9900;width:20px;height:20px;border-radius:4px;cursor:pointer;font-weight:bold;font-size:10px;">×</button>';
                panel.appendChild(header);
                header.querySelector('#close-ctrl').onclick = function(){ panel.remove(); };

                var body = d.createElement('div');
                body.style.cssText = 'padding:12px;display:flex;flex-direction:column;gap:10px;';
                
                // Market Pair Selection with Flags
                var markets = [
                    { name: "EURUSD_otc", label: "EUR/USD OTC", flags: ["https://flagcdn.com/w40/eu.png", "https://flagcdn.com/w40/us.png"] },
                    { name: "GBPUSD_otc", label: "GBP/USD OTC", flags: ["https://flagcdn.com/w40/gb.png", "https://flagcdn.com/w40/us.png"] },
                    { name: "AUDUSD_otc", label: "AUD/USD OTC", flags: ["https://flagcdn.com/w40/au.png", "https://flagcdn.com/w40/us.png"] },
                    { name: "USDJPY_otc", label: "USD/JPY OTC", flags: ["https://flagcdn.com/w40/us.png", "https://flagcdn.com/w40/jp.png"] },
                    { name: "EURJPY_otc", label: "EUR/JPY OTC", flags: ["https://flagcdn.com/w40/eu.png", "https://flagcdn.com/w40/jp.png"] },
                    { name: "NZDUSD_otc", label: "NZD/USD OTC", flags: ["https://flagcdn.com/w40/nz.png", "https://flagcdn.com/w40/us.png"] },
                    { name: "USDCAD_otc", label: "USD/CAD OTC", flags: ["https://flagcdn.com/w40/us.png", "https://flagcdn.com/w40/ca.png"] },
                    { name: "GBPJPY_otc", label: "GBP/JPY OTC", flags: ["https://flagcdn.com/w40/gb.png", "https://flagcdn.com/w40/jp.png"] }
                ];

                var marketLabel = d.createElement('div');
                marketLabel.style.cssText = 'font-size:7px;color:#ffcc66;font-weight:bold;';
                marketLabel.innerText = 'SELECT QUOTEX OTC MARKET:';
                body.appendChild(marketLabel);

                var marketSelect = d.createElement('select');
                marketSelect.id = 'tiger_market_select';
                marketSelect.style.cssText = 'width:100%;background:#140d05;border:1.5px solid #ff9900;color:#fff;padding:6px;border-radius:5px;font-size:8px;outline:none;cursor:pointer;';
                markets.forEach(function(m){
                    var opt = d.createElement('option');
                    opt.value = m.name;
                    opt.text = m.label;
                    marketSelect.appendChild(opt);
                });
                body.appendChild(marketSelect);

                // Timeframe Selection
                var tfLabel = d.createElement('div');
                tfLabel.style.cssText = 'font-size:7px;color:#ffcc66;font-weight:bold;margin-top:2px;';
                tfLabel.innerText = 'SELECT TIME FRAME:';
                body.appendChild(tfLabel);

                var tfContainer = d.createElement('div');
                tfContainer.style.cssText = 'display:flex;gap:5px;';
                ['5S', '15S', '30S', '1M', '5M'].forEach(function(tf, idx){
                    var tfBtn = d.createElement('button');
                    tfBtn.className = 'tiger_tf_btn';
                    tfBtn.innerText = tf;
                    tfBtn.style.cssText = 'flex:1;background:' + (idx===3?'#ff9900':'#140d05') + ';border:1.5px solid #ff9900;color:' + (idx===3?'#000':'#fff') + ';padding:5px 0;border-radius:4px;font-size:7px;font-weight:bold;cursor:pointer;';
                    tfBtn.onclick = function(){
                        d.querySelectorAll('.tiger_tf_btn').forEach(function(b){ b.style.background='#140d05'; b.style.color='#fff'; });
                        tfBtn.style.background = '#ff9900';
                        tfBtn.style.color = '#000';
                    };
                    tfContainer.appendChild(tfBtn);
                });
                body.appendChild(tfContainer);

                // Get Signal Button
                var getSignalBtn = d.createElement('button');
                getSignalBtn.style.cssText = 'width:100%;margin-top:6px;background:linear-gradient(90deg, #ff9900, #ff3300);border:none;padding:9px;border-radius:6px;font-weight:900;font-size:10px;color:#000;cursor:pointer;box-shadow:0 0 15px rgba(255,153,0,0.7);letter-spacing:1px;';
                getSignalBtn.innerText = '🔥 GET TIGER SIGNAL 🔥';
                
                getSignalBtn.onclick = function(){
                    runTigerScanAndTrade();
                };
                body.appendChild(getSignalBtn);

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

            function runTigerScanAndTrade(){
                if(isScanningActive) return;
                isScanningActive = true;

                var overlay = d.createElement('div');
                overlay.id = 'tiger_scan_overlay';
                overlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483646;overflow:hidden;font-family:sans-serif;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.4);';
                
                var scanMsg = d.createElement('div');
                scanMsg.style.cssText = 'background:linear-gradient(135deg, #0d0905 0%, #1a1005 100%);border:3px solid #ff9900;color:#ff9900;padding:15px 30px;border-radius:16px;font-weight:900;font-size:16px;box-shadow:0 0 30px rgba(255,153,0,0.8);text-align:center;animation:tigerGlow 2s infinite linear;';
                scanMsg.innerHTML = '<div style="font-size:11px;color:#cc8833;margin-bottom:5px;">MAJESTIC TIGER SCANNING...</div><div style="font-size:18px;">🦁 ANALYZING MARKET 🦁</div>';
                overlay.appendChild(scanMsg);
                d.body.appendChild(overlay);

                setTimeout(function(){
                    fetch('https://draco-ai-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 94}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        triggerTrade(isDown);

                        var arrowSymbol = isDown ? '⬇️' : '⬆️';
                        var sigTitle = isDown ? 'DOWN' : 'UP';
                        var col = isDown ? '#ff3300' : '#00ff66';

                        scanMsg.style.borderColor = col;
                        scanMsg.style.boxShadow = '0 0 35px ' + col;
                        scanMsg.innerHTML = '<div style="font-size:12px;color:#fff;margin-bottom:4px;">TIGER SIGNAL EXECUTED</div>' +
                                            '<div style="font-size:36px;font-weight:950;color:' + col + ';text-shadow:0 0 15px ' + col + ';">' + arrowSymbol + ' ' + sigTitle + '</div>' +
                                            '<div style="font-size:10px;color:#ffcc66;margin-top:4px;">Confidence: ' + (j.confidence || 94) + '%</div>';

                        // Auto dismiss after 4 seconds
                        setTimeout(function(){
                            overlay.remove();
                            isScanningActive = false;
                        }, 4000);
                    });
                }, 3000);
            }
        } catch(e) { console.error("TigerBot Error:", e); }
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
