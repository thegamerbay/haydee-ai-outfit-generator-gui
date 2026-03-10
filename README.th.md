> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

หน้าจอผู้ใช้งานแบบกราฟิก (GUI) ที่ทันสมัยสำหรับไลบรารี [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) สร้างชุดแต่งกายแบบปรับแต่งเองสำหรับเกม Haydee ได้อย่างง่ายดายโดยไม่ต้องยุ่งยากกับเทอร์มินัลหรือตัวแปรสภาพแวดล้อม (Environment Variables)!

### 📥 [ดาวน์โหลด HaydeeOutfitGenerator.exe เวอร์ชันล่าสุดได้ที่นี่](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ ตัวอย่างที่ถูกสร้างขึ้น

มาดูสิ่งที่คุณสามารถสร้างได้กันเถอะ! ชุดแต่งกายต่อไปนี้ถูกสร้างขึ้นโดยใช้เครื่องมือนี้ และถูกนำไปจัดแสดงในม็อด [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) บน Steam Workshop

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ คุณสมบัติ

- **อินเทอร์เฟซโทนสีเข้มที่ทันสมัย**: สร้างขึ้นด้วย `CustomTkinter` เพื่อรูปลักษณ์ที่โฉบเฉี่ยวและเข้ากับธีมของเกม
- **สองขั้นตอนการทำงานที่ไม่เหมือนใคร**: สลับไปมาระหว่างการสร้างชุดแต่งกายใหม่เอี่ยมด้วย AI และการจัดกลุ่มม็อดที่คุณมีอยู่ให้เป็นม็อดรวม (multi-mods) ได้อย่างราบรื่น
- **การควบคุมการสร้างอย่างละเอียด**: สามารถเลือกเปิด/ปิดการสร้างแผนที่พื้นผิวแบบ Diffuse (สี), Specular (วัสดุ/ความเงา) และ Normal (รอยนูน 3 มิติ) แยกกันได้ เพื่อประหยัดจำนวนการเรียกใช้ API หรือใช้สำหรับสร้างใหม่เฉพาะบางส่วน
- **ปรับแต่งโมเดล AI ได้**: เลือกโมเดล AI ของ Gemini ที่ต้องการใช้ประมวลผลคำขอของคุณได้อย่างแม่นยำ (เช่น `gemini-3.1-flash-image-preview` หรือโมเดลอื่นๆ ที่รองรับ)
- **ความยืดหยุ่นของเครือข่าย**: มีการแพตช์การหมดเวลา SDK (timeout) 10 นาทีในตัว และระบบลูปอัตโนมัติที่พยายามเรียกใช้ API ซ้ำถึง 3 ครั้ง เพื่อให้แน่ใจว่าการสร้างของคุณจะไม่ล้มเหลวเนื่องจากเซิร์ฟเวอร์ Google API หนาแน่นชั่วคราว หรือข้อผิดพลาด `503/504 Deadline Exceeded`
- **ไม่ต้องใช้เทอร์มินัล**: จัดการการตั้งค่าพาธและบันทึกล็อก (logging) ทั้งหมดโดยอัตโนมัติ
- **การประมวลผลแบบอะซิงโครนัส**: UI จะยังคงตอบสนองในขณะที่ AI กำลังสร้างชุดแต่งกาย หรือในขณะที่กำลังจัดกลุ่มม็อด
- **ไฟล์เรียกทำงานแบบ Standalone**: สามารถแพ็กเกจแอปให้เป็นไฟล์ `.exe` เดี่ยวที่ผู้ใช้ Windows ทุกคนสามารถเรียกใช้งานได้ทันที

## 🚀 เริ่มต้นใช้งานด่วน (สำหรับผู้ใช้งาน)

1. [ดาวน์โหลด `HaydeeOutfitGenerator.exe` รีลีสล่าสุด](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)
2. เปิดใช้งานแอปพลิเคชัน
3. กรอกข้อมูลในส่วนของ **Settings** (การตั้งค่า):
   - **Gemini API Key** ของคุณ
   - พาธ (Path) ไปยังโฟลเดอร์ติดตั้งเกม **Haydee**
   - **Author Name** (ชื่อผู้สร้าง - ไม่บังคับ จะถูกนำไปใช้กับม็อดทั้งหมดที่สร้างหรือจัดกลุ่ม)
   - **AI Model** (ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`)
4. คลิก **Save Settings**
5. เลือกแท็บขั้นตอนการทำงานที่คุณต้องการ:
   - **✨ Generate Outfit**: กรอกชื่อม็อดที่ไม่ซ้ำใคร, คำอธิบายรูปแบบ (prompt) ของชุด, และสลับเลือกพื้นผิว (textures) ที่คุณต้องการสร้าง (Diffuse, Specular, หรือ Normal) ก่อนเริ่มต้น
   - **📦 Group Mods**: รวมม็อดที่มีอยู่หลายอันเข้าด้วยกันเป็นม็อดรวม (multi-mod) กรอกชื่อม็อดรวมใหม่, ม็อดต้นทางที่ต้องการจัดกลุ่ม (เช่น `red, green, blue`), และหมวดหมู่ของช่อง (slot) (เช่น `color`)
6. คลิก **Start Generation** หรือ **Group Outfits** แล้วรอดูความมหัศจรรย์เกิดขึ้นในหน้าต่างคอนโซลที่ฝังอยู่ในตัวแอปได้เลย!

*(หมายเหตุ: แอปจะบันทึกการตั้งค่าของคุณโดยอัตโนมัติไว้ที่ `AppData/Local/HaydeeOutfitGenerator/settings.json` ดังนั้นคุณจึงไม่ต้องกรอกรายละเอียดใหม่ทุกครั้ง)*

### 🔑 วิธีการขอรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/)
2. ลงชื่อเข้าใช้ด้วยบัญชี Google ของคุณ
3. คลิกปุ่ม "Create API key"
4. หากมีข้อความแจ้งเตือน ให้อ่านและยอมรับเงื่อนไขการให้บริการ
5. คลิกที่ "Create API key in new project" (หรือใช้โปรเจกต์ที่มีอยู่แล้ว)
6. คัดลอกคีย์ที่ได้ คุณจะต้องนำมาวางในส่วนของการตั้งค่า (**Settings**) ในแอปพลิเคชัน

## 🛠️ การตั้งค่าสำหรับนักพัฒนา (Developer Setup)

หากคุณต้องการมีส่วนร่วมหรือสร้างแอปพลิเคชันนี้ด้วยตัวเอง:

### สิ่งที่ต้องมีก่อน (Prerequisites)

- Python 3.12+
- Git

### การติดตั้ง

1. โคลนพื้นที่เก็บข้อมูล (repository) นี้:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. ติดตั้งส่วนที่จำเป็น (dependencies):
   ```bash
   pip install -r requirements.txt
   ```

3. รันแอปพลิเคชันจากซอร์สโค้ด:
   ```bash
   python main.py
   ```

### การสร้างไฟล์เรียกทำงาน (Building the Executable)

โปรเจกต์นี้รวมสคริปต์อัตโนมัติที่ใช้ `PyInstaller` เพื่อแพ็กเกจแอปให้เป็นไฟล์ `.exe` แบบสแตนด์อโลนโดยไม่มีหน้าต่างคอนโซลสีดำ

สำหรับการบิลด์ (build):
```bash
python build.py
```

หลังจากบิลด์เสร็จสิ้น แอปพลิเคชันของคุณจะอยู่ในโฟลเดอร์ `dist/` ในชื่อ `HaydeeOutfitGenerator.exe`

### การรันการทดสอบ (Running Tests)

โปรเจกต์นี้มีการทดสอบ GUI อัตโนมัติที่เขียนด้วย `pytest` และ `pytest-mock`

1. ติดตั้งส่วนที่จำเป็นสำหรับการทดสอบ:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รันการทดสอบ:
   ```bash
   pytest tests/
   ```

### การรันการตรวจสอบโค้ด (Running Linting)

โปรเจกต์นี้ใช้ `flake8` เพื่อบังคับใช้รูปแบบการเขียนโค้ด (code style)

1. ตรวจสอบให้แน่ใจว่าติดตั้งส่วนที่จำเป็นสำหรับการทดสอบแล้ว:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รัน linter:
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 สัญญาอนุญาต (License)

โปรเจกต์นี้ได้รับอนุญาตภายใต้ MIT License - ดูรายละเอียดได้ในไฟล์ [LICENSE](LICENSE)