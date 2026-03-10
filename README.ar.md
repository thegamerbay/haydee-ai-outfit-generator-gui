> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# واجهة المستخدم الرسومية لمولد أزياء Haydee بالذكاء الاصطناعي

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

واجهة مستخدم رسومية حديثة لمكتبة [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator). قم بإنشاء أزياء مخصصة لـ Haydee بسهولة دون الحاجة للتعامل مع سطر الأوامر أو متغيرات البيئة!

### 📥 [قم بتنزيل أحدث إصدار من HaydeeOutfitGenerator.exe من هنا](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ أمثلة تم إنشاؤها

اكتشف ما يمكنك إنشاؤه! تم إنشاء الأزياء التالية باستخدام هذه الأداة وهي معروضة في تعديل [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) على Steam Workshop.

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ الميزات

- **واجهة داكنة حديثة**: مبنية باستخدام `CustomTkinter` للحصول على مظهر أنيق مستوحى من اللعبة.
- **مجرَيَا عمل فريدان**: التبديل بسلاسة بين إنشاء أزياء جديدة تمامًا عبر الذكاء الاصطناعي وتجميع تعديلاتك (mods) الحالية في تعديل واحد متعدد.
- **تحكم دقيق في الإنشاء**: إمكانية تبديل إنشاء خرائط الانتشار (Diffuse/اللون) والانعكاس (Specular/المادة واللمعان) والخرائط الطبيعية (Normal/البروز ثلاثي الأبعاد) بشكل فردي لتوفير طلبات واجهة برمجة التطبيقات (API) أو إعادة إنشاء أجزاء معينة.
- **نماذج ذكاء اصطناعي قابلة للتخصيص**: اختر بالضبط نموذج الذكاء الاصطناعي Gemini الذي سيعالج طلبك (مثل `gemini-3.1-flash-image-preview` أو النماذج الأخرى المدعومة).
- **مرونة الشبكة**: تصحيحات مدمجة لمهلة حزمة تطوير البرمجيات (SDK) لمدة 10 دقائق وحلقات إعادة محاولة تلقائية لواجهة برمجة التطبيقات (API) لـ 3 مرات لضمان عدم فشل عمليات الإنشاء بسبب ازدحام خوادم Google API المؤقت أو أخطاء `503/504 Deadline Exceeded`.
- **لا حاجة لسطر الأوامر (Terminal)**: يقوم بتهيئة جميع المسارات ويتعامل مع التسجيلات تلقائيًا.
- **معالجة غير متزامنة**: تظل واجهة المستخدم مستجيبة أثناء إنشاء الزي عبر الذكاء الاصطناعي أو أثناء تجميع التعديلات.
- **ملف تنفيذي مستقل**: يمكنك بسهولة حزم التطبيق في ملف `.exe` واحد يمكن لأي مستخدم Windows تشغيله مباشرةً.

## 🚀 البدء السريع (للمستخدمين)

1. [قم بتنزيل أحدث إصدار من `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases).
2. قم بتشغيل التطبيق.
3. املأ لوحة **الإعدادات (Settings)**:
   - **مفتاح واجهة برمجة تطبيقات Gemini (Gemini API Key)** الخاص بك.
   - مسار مجلد تثبيت لعبة **Haydee** الخاص بك.
   - **اسم المؤلف (Author Name)** الخاص بك (اختياري، يتم تطبيقه على جميع التعديلات المنشأة أو المجمعة).
   - **نموذج الذكاء الاصطناعي (AI Model)** الخاص بك (الافتراضي هو `gemini-3.1-flash-image-preview`).
4. انقر على **حفظ الإعدادات (Save Settings)**.
5. اختر علامة تبويب سير العمل الخاصة بك:
   - **✨ إنشاء زي (Generate Outfit)**: أدخل اسمًا فريدًا للتعديل (mod)، ووصفًا نصيًا لأسلوب الزي، وقم بتبديل الإكساءات التي ترغب في إنشائها (Diffuse, Specular, أو Normal) قبل البدء.
   - **📦 تجميع التعديلات (Group Mods)**: دمج عدة تعديلات موجودة في تعديل متعدد واحد. أدخل الاسم الجديد للتعديل المتعدد، والتعديلات المصدرية المراد تجميعها (مثل `red, green, blue`)، وفئة الفتحة (مثل `color`).
6. انقر على **بدء الإنشاء (Start Generation)** أو **تجميع الأزياء (Group Outfits)** وشاهد السحر يحدث في نافذة سطر الأوامر المدمجة!

*(ملاحظة: سيقوم التطبيق تلقائيًا بحفظ إعداداتك في `AppData/Local/HaydeeOutfitGenerator/settings.json` حتى لا تضطر إلى إدخال بياناتك في كل مرة.)*

### 🔑 الحصول على مفتاح Gemini API

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. انقر على زر "Create API key".
4. إذا طُلب منك، اقرأ واقبل شروط الخدمة.
5. انقر على "Create API key in new project" (أو استخدم مشروعًا موجودًا مسبقًا).
6. انسخ المفتاح الذي تم إنشاؤه. ستحتاج إلى لصقه في لوحة **الإعدادات (Settings)** في التطبيق.

## 🛠️ إعدادات المطور

إذا كنت ترغب في المساهمة أو بناء التطبيق بنفسك:

### المتطلبات الأساسية

- Python 3.12+
- Git

### التثبيت

1. استنساخ هذا المستودع:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. تثبيت الاعتمادات (dependencies):
   ```bash
   pip install -r requirements.txt
   ```

3. تشغيل التطبيق من المصدر:
   ```bash
   python main.py
   ```

### بناء الملف التنفيذي

يتضمن هذا المشروع برنامجًا نصيًا آليًا يستخدم `PyInstaller` لحزم التطبيق في ملف `.exe` مستقل بدون نافذة سطر أوامر سوداء.

للبناء:
```bash
python build.py
```

بعد اكتمال عملية البناء، سيكون تطبيقك متاحًا في مجلد `dist/` باسم `HaydeeOutfitGenerator.exe`.

### تشغيل الاختبارات

يتضمن هذا المشروع اختبارات آلية لواجهة المستخدم الرسومية مكتوبة باستخدام `pytest` و `pytest-mock`.

1. تثبيت اعتمادات الاختبار:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. تشغيل الاختبارات:
   ```bash
   pytest tests/
   ```

### تشغيل التدقيق البرمجي (Linting)

يستخدم هذا المشروع `flake8` لفرض نمط كتابة الكود.

1. تأكد من تثبيت اعتمادات الاختبار:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. تشغيل المدقق (linter):
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [الترخيص (LICENSE)](LICENSE) للحصول على التفاصيل.