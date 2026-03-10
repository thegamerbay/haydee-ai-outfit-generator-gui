> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

ส่วนติดต่อผู้ใช้แบบกราฟิก (GUI) ที่ทันสมัยสำหรับไลบรารี [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) ช่วยให้คุณสร้างชุดแต่งกายแบบกำหนดเองสำหรับเกม Haydee ได้อย่างง่ายดาย โดยไม่ต้องยุ่งยากกับการใช้เทอร์มินัลหรือการตั้งค่าตัวแปรสภาพแวดล้อม (environment variables)!

### 📥 [ดาวน์โหลด HaydeeOutfitGenerator.exe เวอร์ชันล่าสุดได้ที่นี่](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

![GUI Generate Outfit Preview](assets/gui-generate-outfit.png)
![GUI Group Mods Preview](assets/gui-group-mods.png)

## 🖼️ ตัวอย่างที่ถูกสร้างขึ้น

ลองดูสิ่งที่คุณสามารถสร้างได้สิ! ชุดแต่งกายต่อไปนี้ถูกสร้างขึ้นโดยใช้เครื่องมือนี้และได้ถูกนำไปใช้ในม็อด [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) บน Steam Workshop

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ คุณสมบัติหลัก

- **อินเทอร์เฟซโทนดาร์กที่ทันสมัย**: สร้างด้วย `CustomTkinter` เพื่อรูปลักษณ์ที่โฉบเฉี่ยวและเข้ากับธีมของเกม
- **สามกระบวนการทำงานที่ไม่เหมือนใคร**: สลับการทำงานได้อย่างราบรื่น ไม่ว่าจะเป็นการสร้างชุดใหม่เอี่ยมด้วย AI, การหาแรงบันดาลใจในการออกแบบสไตล์ของคุณ หรือการจัดกลุ่มม็อดที่มีอยู่แล้วให้เป็นม็อดรวม (multi-mods) ในหนึ่งเดียว
- **ควบคุมการสร้างได้อย่างละเอียด**: สามารถเลือกเปิด/ปิดการสร้างแผนที่พื้นผิวแบบ Diffuse (สี), Specular (วัสดุ/ความเงา) และ Normal (รอยนูน 3 มิติ) ได้อย่างอิสระ เพื่อประหยัดการเรียกใช้งาน API หรือสร้างเฉพาะส่วนที่ต้องการใหม่ได้
- **ปรับแต่งโมเดล AI ได้**: เลือกโมเดล Gemini AI ที่ต้องการให้ประมวลผลคำขอของคุณได้อย่างแม่นยำ (เช่น `gemini-3.1-flash-image-preview` หรือโมเดลอื่นๆ ที่รองรับ)
- **ความยืดหยุ่นของเครือข่าย**: มีการแพตช์ระยะเวลาหมดอายุ (timeout) ของ SDK ไว้ที่ 10 นาที และระบบพยายามเรียก API ซ้ำอัตโนมัติ 3 ครั้ง เพื่อให้มั่นใจว่าการสร้างของคุณจะไม่ล้มเหลวเนื่องจากปัญหาเซิร์ฟเวอร์ Google API หนาแน่นชั่วคราว หรือข้อผิดพลาด `503/504 Deadline Exceeded`
- **ไม่ต้องใช้เทอร์มินัล**: จัดการตั้งค่าเส้นทาง (paths) ทั้งหมดและการบันทึกประวัติการทำงาน (logging) ให้โดยอัตโนมัติ
- **การประมวลผลแบบอะซิงโครนัส (Asynchronous)**: หน้าจอ UI จะยังคงตอบสนองต่อการใช้งานได้ตามปกติ ในขณะที่ AI กำลังสร้างชุด หรือขณะที่กำลังจัดกลุ่มม็อด
- **ไฟล์โปรแกรมแบบ Standalone**: สามารถแพ็กเกจแอปพลิเคชันให้กลายเป็นไฟล์ `.exe` เดี่ยวๆ ที่ผู้ใช้ Windows ทุกคนสามารถเปิดใช้งานได้ทันที

## 🚀 เริ่มต้นใช้งานอย่างรวดเร็ว (สำหรับผู้ใช้ทั่วไป)

1. [ดาวน์โหลดรีลีส `HaydeeOutfitGenerator.exe` เวอร์ชันล่าสุด](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)
2. เปิดใช้งานแอปพลิเคชัน
3. กรอกข้อมูลในส่วนของ **Settings** (การตั้งค่า):
   - **Gemini API Key** ของคุณ
   - เส้นทาง (Path) ไปยังโฟลเดอร์ติดตั้งเกม **Haydee** ของคุณ
   - **Author Name** (ชื่อผู้สร้าง - ระบุหรือไม่ก็ได้ ซึ่งจะถูกนำไปใช้กับม็อดที่สร้างหรือจัดกลุ่มทั้งหมด)
   - **AI Model** ของคุณ (ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`)
4. คลิก **Save Settings** (บันทึกการตั้งค่า)
5. เลือกแท็บกระบวนการทำงานของคุณ:
   - **✨ Generate Outfit** (สร้างชุด): ระบุชื่อม็อดที่ไม่ซ้ำกัน, พิมพ์คำอธิบาย (prompt) สไตล์ที่ต้องการ และเลือกเปิด/ปิดพื้นผิว (textures) ที่ต้องการสร้าง (Diffuse, Specular หรือ Normal) ก่อนที่จะเริ่มทำงาน
   - ** Prompt Ideas** (ไอเดียการเขียน Prompt): คิดไม่ออกใช่ไหม? เพียงแค่ป้อนธีมง่ายๆ (เช่น "Cyberpunk") แล้วรับแนวคิดเกี่ยวกับชุดที่ AI สร้างขึ้นให้ สามารถนำไอเดียเหล่านั้นไปใส่ในเครื่องมือสร้างชุดได้โดยตรงในคลิกเดียว
   - **📦 Group Mods** (จัดกลุ่มม็อด): รวมม็อดที่มีอยู่แล้วหลายๆ ตัวให้เป็นม็อดรวม (multi-mod) เพียงตัวเดียว โดยระบุชื่อม็อดรวมใหม่, รายชื่อม็อดต้นทางที่ต้องการจัดกลุ่ม (เช่น `red, green, blue`) และหมวดหมู่ช่องเก็บของ (เช่น `color`)
6. คลิก **Start Generation** (เริ่มการสร้าง), **Generate Prompt Ideas** (สร้างไอเดียคำอธิบาย) หรือ **Group Outfits** (จัดกลุ่มชุด) แล้วดูเวทมนตร์เกิดขึ้นในหน้าต่างคอนโซลในตัวแอปได้เลย!

*(หมายเหตุ: แอปจะบันทึกการตั้งค่าของคุณไว้ใน `AppData/Local/HaydeeOutfitGenerator/settings.json` โดยอัตโนมัติ เพื่อที่คุณจะได้ไม่ต้องกรอกข้อมูลใหม่ทุกครั้งที่ใช้งาน)*

### 🔑 วิธีรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/)
2. เข้าสู่ระบบด้วยบัญชี Google ของคุณ
3. คลิกที่ปุ่ม "Create API key"
4. หากมีข้อความแจ้งเตือน ให้อ่านและยอมรับข้อกำหนดในการให้บริการ
5. คลิกที่ "Create API key in new project" (สร้างคีย์ API ในโปรเจกต์ใหม่) หรือใช้โปรเจกต์ที่มีอยู่แล้ว
6. คัดลอกคีย์ที่สร้างขึ้น คุณจะต้องนำคีย์นี้ไปวางในส่วน **Settings** (การตั้งค่า) ของแอปพลิเคชัน

## 🛠️ การตั้งค่าสำหรับนักพัฒนา

หากคุณต้องการร่วมสมทบ (contribute) หรือทดลองสร้าง (build) แอปพลิเคชันด้วยตนเอง:

### สิ่งที่ต้องมีเบื้องต้น

- Python 3.12+
- Git

### การติดตั้ง

1. โคลนพื้นที่เก็บข้อมูล (repository) นี้:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. ติดตั้งส่วนประกอบที่จำเป็น (dependencies):
   ```bash
   pip install -r requirements.txt
   ```

3. รันแอปพลิเคชันจากซอร์สโค้ด:
   ```bash
   python main.py
   ```

### การสร้างไฟล์ Executable (.exe)

โปรเจกต์นี้มีสคริปต์อัตโนมัติที่ใช้ `PyInstaller` ในการแพ็กเกจแอปให้เป็นไฟล์ `.exe` แบบ Standalone โดยไม่มีหน้าต่างคอนโซลสีดำ

วิธีสร้าง (Build):
```bash
python build.py
```

หลังจากสร้างเสร็จสมบูรณ์ แอปพลิเคชันของคุณจะอยู่ในโฟลเดอร์ `dist/` ภายใต้ชื่อ `HaydeeOutfitGenerator.exe`

### การรันการทดสอบ (Running Tests)

โปรเจกต์นี้มีการทดสอบ GUI อัตโนมัติที่เขียนด้วย `pytest` และ `pytest-mock`

1. ติดตั้งส่วนประกอบสำหรับการทดสอบ:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รันการทดสอบ:
   ```bash
   pytest tests/
   ```

### การตรวจสอบโค้ดด้วย Linting

โปรเจกต์นี้ใช้ `flake8` ในการบังคับใช้รูปแบบโค้ด (code style)

1. ตรวจสอบให้แน่ใจว่าได้ติดตั้งส่วนประกอบสำหรับการทดสอบแล้ว:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รันการตรวจสอบ (Linter):
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 ลิขสิทธิ์และสัญญาอนุญาต (License)

โปรเจกต์นี้อยู่ภายใต้สัญญาอนุญาต MIT License - ดูรายละเอียดเพิ่มเติมได้ที่ไฟล์ [LICENSE](LICENSE)