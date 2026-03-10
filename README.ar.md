> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# واجهة المستخدم الرسومية لمولد أزياء Haydee بالذكاء الاصطناعي

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

واجهة مستخدم رسومية حديثة لمكتبة [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator). قم بتوليد أزياء مخصصة للعبة Haydee بسهولة دون الحاجة للتعامل مع سطر الأوامر (terminals) أو متغيرات البيئة!

### 📥 [قم بتنزيل أحدث إصدار من HaydeeOutfitGenerator.exe من هنا](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ أمثلة مُولدة

ألقِ نظرة على ما يمكنك إنشاؤه! تم إنشاء الأزياء التالية باستخدام هذه الأداة وهي معروضة في تعديل (مود) [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) على ورشة Steam.

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

- **واجهة داكنة حديثة**: مبنية باستخدام `CustomTkinter` للحصول على مظهر أنيق ومناسب لأجواء الألعاب.
- **ثلاث آليات عمل فريدة**: بدّل بسلاسة بين إنشاء أزياء جديدة تمامًا باستخدام الذكاء الاصطناعي، والحصول على إلهام إبداعي لتصميماتك، وتجميع تعديلاتك (mods) الحالية في تعديلات متعددة (multi-mods) داخل حزمة واحدة.
- **تحكم دقيق في التوليد**: قم بتفعيل أو تعطيل توليد خرائط Diffuse (اللون)، و Specular (الخامة/اللمعان)، و Normal (النتوءات ثلاثية الأبعاد) بشكل فردي لتوفير طلبات API أو إعادة توليد أجزاء معينة.
- **نماذج ذكاء اصطناعي قابلة للتخصيص**: اختر بدقة نموذج Gemini للذكاء الاصطناعي الذي يعالج طلبك (مثل `gemini-3.1-flash-image-preview` أو غيره من النماذج المدعومة).
- **حلقة ضمان الجودة**: التحقق التلقائي من الخامات المُولدة بالذكاء الاصطناعي بحثاً عن العيوب الهيكلية (مثل التشريح غير الصحيح أو فواصل الإكساء) باستخدام نموذج أكثر تقدماً، وإرسال ملاحظات للذكاء الاصطناعي لإعادة رسمها حتى 3 مرات قبل الحفظ.
- **مرونة الشبكة**: تصحيحات مدمجة لمهلة SDK تصل إلى 10 دقائق وحلقات إعادة محاولة تلقائية لطلبات API تصل إلى 3 محاولات لضمان عدم فشل عمليات التوليد بسبب الازدحام المؤقت في خوادم Google API أو أخطاء `503/504 Deadline Exceeded`.
- **لا حاجة لسطر الأوامر (Terminal)**: يقوم بتهيئة جميع المسارات والتعامل مع السجلات (logging) بشكل تلقائي.
- **معالجة غير متزامنة**: تظل واجهة المستخدم مستجيبة أثناء توليد الزي عبر الذكاء الاصطناعي أو أثناء تجميع التعديلات.
- **ملف تنفيذي مستقل**: سهولة تحزيم التطبيق في ملف `.exe` واحد يمكن لأي مستخدم Windows تشغيله مباشرة دون أي إعدادات مسبقة.

## 🚀 البدء السريع (للمستخدمين)

1. [قم بتنزيل أحدث إصدار من `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases).
2. قم بتشغيل التطبيق.
3. املأ حقول لوحة **الإعدادات (Settings)**:
   - **مفتاح واجهة برمجة تطبيقات Gemini (Gemini API Key)** الخاص بك.
   - مسار مجلد تثبيت لعبة **Haydee**.
   - **اسم المؤلف (Author Name)** (اختياري، يتم تطبيقه على جميع التعديلات المُولدة أو المُجمّعة).
   - **نموذج الذكاء الاصطناعي (AI Model)** الخاص بك (الافتراضي هو `gemini-3.1-flash-image-preview`).
   - **نموذج الذكاء الاصطناعي للتحقق (Validation AI Model)** (الافتراضي هو `gemini-3.1-pro-preview`).
4. انقر على **حفظ الإعدادات (Save Settings)**.
5. اختر علامة تبويب آلية العمل التي تفضلها:
   - **✨ توليد زي (Generate Outfit)**: أدخل اسماً فريداً للتعديل، وموجّه (prompt) وصفي للأسلوب، وقم باختيار الخامات التي ترغب في توليدها (Diffuse، أو Specular، أو Normal) قبل البدء.
   - ** أفكار للموجّهات (Prompt Ideas)**: هل تشعر بالتعثر؟ أدخل سِمة بسيطة (مثل "Cyberpunk") واحصل على مفاهيم أزياء مُولدة بالذكاء الاصطناعي. طبّق الأفكار مباشرة في أداة التوليد بنقرة واحدة.
   - **📦 تجميع التعديلات (Group Mods)**: ادمج عدة تعديلات (mods) حالية في تعديل متعدد (multi-mod) واحد. أدخل الاسم الجديد للتعديل المتعدد، والتعديلات المصدرية المراد تجميعها (مثل `red, green, blue`)، وفئة الفتحة (مثل `color`).
6. انقر على **بدء التوليد (Start Generation)**، أو **توليد أفكار للموجّهات (Generate Prompt Ideas)**، أو **تجميع الأزياء (Group Outfits)** وشاهد السحر يحدث في نافذة وحدة التحكم المدمجة!

*(ملاحظة: سيقوم التطبيق تلقائيًا بحفظ إعداداتك في `AppData/Local/HaydeeOutfitGenerator/settings.json` لتجنب إدخال تفاصيلك في كل مرة.)*

### 🔑 الحصول على مفتاح واجهة برمجة تطبيقات Gemini (Gemini API Key)

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. انقر على زر "Create API key" (إنشاء مفتاح API).
4. إذا طُلب منك، اقرأ شروط الخدمة ووافق عليها.
5. انقر على "Create API key in new project" (إنشاء مفتاح API في مشروع جديد) (أو استخدم مشروعاً حالياً).
6. انسخ المفتاح المُنشأ. ستحتاج إلى لصقه في لوحة **الإعدادات (Settings)** الخاصة بالتطبيق.

## 🛠️ إعداد المطورين

إذا كنت ترغب في المساهمة أو بناء التطبيق بنفسك:

### المتطلبات الأساسية

- Python 3.12 أو أحدث
- Git

### التثبيت

1. استنسخ هذا المستودع:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. ثبّت الاعتمادات:
   ```bash
   pip install -r requirements.txt
   ```

3. شغّل التطبيق من المصدر:
   ```bash
   python main.py
   ```

### بناء الملف التنفيذي (Executable)

يتضمن هذا المشروع برنامجاً نصياً (script) آلياً يستخدم `PyInstaller` لتحزيم التطبيق في ملف `.exe` مستقل بدون نافذة الأوامر السوداء.

للبناء:
```bash
python build.py
```

بعد اكتمال عملية البناء، سيكون تطبيقك متاحاً في مجلد `dist/` باسم `HaydeeOutfitGenerator.exe`.

### تشغيل الاختبارات

يحتوي هذا المشروع على اختبارات تلقائية لواجهة المستخدم الرسومية مكتوبة باستخدام `pytest` و `pytest-mock`.

1. ثبّت اعتمادات الاختبار:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. شغّل الاختبارات:
   ```bash
   pytest tests/
   ```

### تشغيل التحقق من الكود (Linting)

يستخدم هذا المشروع `flake8` لفرض نمط كتابة الكود.

1. تأكد من تثبيت اعتمادات الاختبار:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. شغّل أداة التحقق من الكود (linter):
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [الترخيص (LICENSE)](LICENSE) للحصول على التفاصيل.