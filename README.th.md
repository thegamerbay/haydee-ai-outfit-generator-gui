> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

อินเทอร์เฟซผู้ใช้แบบกราฟิกที่ทันสมัยสำหรับไลบรารี [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) สร้างชุดแต่งกายแบบกำหนดเองสำหรับ Haydee ได้อย่างง่ายดาย โดยไม่ต้องยุ่งยากกับเทอร์มินัลหรือตัวแปรสภาพแวดล้อม!

### 📥 [ดาวน์โหลด HaydeeOutfitGenerator.exe เวอร์ชันล่าสุดได้ที่นี่](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ ตัวอย่างที่สร้างขึ้น

ลองดูสิ่งที่คุณสามารถสร้างได้สิ! ชุดแต่งกายต่อไปนี้ถูกสร้างขึ้นโดยใช้เครื่องมือนี้และมีให้เห็นในม็อด [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) บน Steam Workshop

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

- **อินเทอร์เฟซสีเข้มที่ทันสมัย**: สร้างด้วย `CustomTkinter` เพื่อรูปลักษณ์ที่โฉบเฉี่ยวและเข้ากับธีมของเกม
- **สามเวิร์กโฟลว์ที่ไม่เหมือนใคร**: สลับไปมาระหว่างการสร้างชุดใหม่เอี่ยมผ่าน AI, การรับแรงบันดาลใจสร้างสรรค์สำหรับสไตล์ของคุณ และการจัดกลุ่มม็อดที่มีอยู่ของคุณให้เป็นมัลติม็อดเดียวได้อย่างราบรื่น
- **การควบคุมการสร้างอย่างละเอียด**: สลับเปิด/ปิดการสร้างแผนที่ Diffuse (สี), Specular (วัสดุ/ความเงา), และ Normal (พื้นผิว 3 มิติ) แยกกันอย่างอิสระ เพื่อประหยัดจำนวนการเรียก API หรือสร้างใหม่เฉพาะส่วนได้
- **ปรับแต่งโมเดล AI ได้**: เลือกโมเดล Gemini AI ที่จะประมวลผลคำขอของคุณได้อย่างเจาะจง (เช่น `gemini-3.1-flash-image-preview` หรือโมเดลอื่น ๆ ที่รองรับ)
- **ลูปการประกันคุณภาพ**: ตรวจสอบความถูกต้องของพื้นผิว (textures) ที่ AI สร้างขึ้นโดยอัตโนมัติ เพื่อหาข้อบกพร่องทางโครงสร้าง (เช่น กายวิภาคที่ไม่ถูกต้องหรือรอยต่อ) โดยใช้โมเดลขั้นสูงกว่า และส่งข้อเสนอแนะกลับไปยัง AI เพื่อวาดใหม่สูงสุด 3 ครั้งก่อนบันทึก
- **ความเสถียรของเครือข่าย**: มีการแพตช์การหมดเวลา SDK 10 นาทีในตัว และลูปการลองเรียก API ซ้ำอัตโนมัติ 3 ครั้ง เพื่อให้แน่ใจว่าการสร้างของคุณจะไม่ล้มเหลวเนื่องจากเซิร์ฟเวอร์ Google API หนาแน่นชั่วคราว หรือข้อผิดพลาด `503/504 Deadline Exceeded`
- **ไม่ต้องใช้เทอร์มินัล**: กำหนดค่าเส้นทางทั้งหมดและจัดการการบันทึก (logging) โดยอัตโนมัติ
- **การประมวลผลแบบอะซิงโครนัส**: UI ยังคงตอบสนองในขณะที่ชุดแต่งกายกำลังถูกสร้างผ่าน AI หรือในขณะที่กำลังจัดกลุ่มม็อด
- **โปรแกรมที่รันได้ในตัว (Standalone Executable)**: แพ็กเกจแอปให้เป็นไฟล์ `.exe` เดียวได้อย่างง่ายดาย ซึ่งผู้ใช้ Windows ทุกคนสามารถเปิดใช้งานได้ทันที

## 🚀 เริ่มต้นใช้งานด่วน (สำหรับผู้ใช้)

1. [ดาวน์โหลดรีลีส `HaydeeOutfitGenerator.exe` ล่าสุด](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)
2. เปิดแอปพลิเคชัน
3. กรอกข้อมูลในแผง **Settings** (การตั้งค่า):
   - **Gemini API Key** ของคุณ
   - เส้นทาง (Path) ไปยังไดเรกทอรีการติดตั้งเกม **Haydee** ของคุณ
   - **Author Name** (ชื่อผู้สร้าง) ของคุณ (ทางเลือก, จะถูกใช้กับม็อดทั้งหมดที่สร้างหรือจัดกลุ่ม)
   - **AI Model** ของคุณ (ค่าเริ่มต้นคือ `gemini-3.1-flash-image-preview`)
   - **Validation AI Model** ของคุณ (ค่าเริ่มต้นคือ `gemini-3.1-pro-preview`)
4. คลิก **Save Settings** (บันทึกการตั้งค่า)
5. เลือกแท็บเวิร์กโฟลว์ของคุณ:
   - **✨ Generate Outfit** (สร้างชุดแต่งกาย): ป้อนชื่อม็อดที่ไม่ซ้ำใคร, คำอธิบายสไตล์ (prompt), และสลับเลือกพื้นผิวที่คุณต้องการสร้าง (Diffuse, Specular, หรือ Normal) ก่อนเริ่มต้น
   - ** Prompt Ideas** (ไอเดียสำหรับพร้อมต์): นึกอะไรไม่ออกใช่ไหม? ป้อนธีมง่าย ๆ (เช่น "Cyberpunk") และรับแนวคิดชุดแต่งกายที่สร้างโดย AI นำไอเดียไปใช้โดยตรงกับเครื่องมือสร้างได้ในคลิกเดียว
   - **📦 Group Mods** (จัดกลุ่มม็อด): รวมม็อดที่มีอยู่หลายตัวเข้าเป็นมัลติม็อดเดียว ป้อนชื่อมัลติม็อดใหม่, ม็อดต้นทางที่ต้องการจัดกลุ่ม (เช่น `red, green, blue`), และหมวดหมู่สล็อต (เช่น `color`)
6. คลิก **Start Generation** (เริ่มการสร้าง), **Generate Prompt Ideas** (สร้างไอเดียพร้อมต์), หรือ **Group Outfits** (จัดกลุ่มชุดแต่งกาย) และดูความมหัศจรรย์เกิดขึ้นในหน้าต่างคอนโซลที่ติดตั้งมาในตัว!

*(หมายเหตุ: แอปจะบันทึกการตั้งค่าของคุณโดยอัตโนมัติใน `AppData/Local/HaydeeOutfitGenerator/settings.json` เพื่อให้คุณไม่ต้องป้อนรายละเอียดของคุณใหม่ทุกครั้ง)*

### 🔑 การรับ Gemini API Key

1. ไปที่ [Google AI Studio](https://aistudio.google.com/)
2. ลงชื่อเข้าใช้ด้วยบัญชี Google ของคุณ
3. คลิกปุ่ม "Create API key" (สร้างคีย์ API)
4. หากได้รับข้อความแจ้ง ให้อ่านและยอมรับเงื่อนไขการให้บริการ
5. คลิกที่ "Create API key in new project" (หรือใช้โปรเจกต์ที่มีอยู่)
6. คัดลอกคีย์ที่สร้างขึ้น คุณจะต้องนำไปวางในแผง **Settings** (การตั้งค่า) ของแอปพลิเคชัน

## 🛠️ การตั้งค่าสำหรับนักพัฒนา

หากคุณต้องการมีส่วนร่วมหรือสร้างแอปพลิเคชันด้วยตัวเอง:

### สิ่งที่ต้องมีเบื้องต้น

- Python 3.12+
- Git

### การติดตั้ง

1. โคลนที่เก็บ (repository) นี้:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. ติดตั้งการพึ่งพา (dependencies):
   ```bash
   pip install -r requirements.txt
   ```

3. รันแอปพลิเคชันจากซอร์สโค้ด:
   ```bash
   python main.py
   ```

### การสร้างไฟล์ Executable (การบิลด์)

โปรเจกต์นี้มีสคริปต์อัตโนมัติที่ใช้ `PyInstaller` เพื่อแพ็กเกจแอปให้เป็นไฟล์ `.exe` แบบสแตนด์อโลนโดยไม่มีหน้าต่างคอนโซลสีดำ

วิธีบิลด์:
```bash
python build.py
```

หลังจากที่บิลด์เสร็จสมบูรณ์ แอปพลิเคชันของคุณจะอยู่ในโฟลเดอร์ `dist/` ในชื่อ `HaydeeOutfitGenerator.exe`

### การรันการทดสอบ

โปรเจกต์นี้รวมการทดสอบ GUI อัตโนมัติที่เขียนด้วย `pytest` และ `pytest-mock`

1. ติดตั้งการพึ่งพา (dependencies) สำหรับการทดสอบ:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รันการทดสอบ:
   ```bash
   pytest tests/
   ```

### การรัน Linting

โปรเจกต์นี้ใช้ `flake8` เพื่อบังคับใช้สไตล์โค้ด

1. ตรวจสอบให้แน่ใจว่าได้ติดตั้งการพึ่งพา (dependencies) สำหรับการทดสอบแล้ว:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. รัน Linter:
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 ใบอนุญาต (License)

โปรเจกต์นี้ได้รับอนุญาตภายใต้ MIT License - ดูรายละเอียดที่ไฟล์ [LICENSE](LICENSE)