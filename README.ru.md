> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

Современный графический пользовательский интерфейс для библиотеки [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator). Легко создавайте собственные наряды для Haydee, не связываясь с терминалами или переменными окружения!

### 📥 [Скачать последнюю версию HaydeeOutfitGenerator.exe можно здесь](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ Примеры генерации

Посмотрите, что вы можете создать! Следующие наряды были сгенерированы с помощью этого инструмента и представлены в моде [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) в Мастерской Steam.

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ Особенности

- **Современный темный интерфейс**: Создан с использованием `CustomTkinter` для элегантного внешнего вида в игровом стиле.
- **Два уникальных рабочих процесса**: Плавное переключение между генерацией совершенно новых нарядов с помощью ИИ и объединением существующих модов в единые мультимоды.
- **Детальный контроль генерации**: Индивидуальное переключение генерации карт Diffuse (Цвет), Specular (Материал/Блеск) и Normal (3D рельеф) для экономии запросов к API или регенерации конкретных частей.
- **Настраиваемые модели ИИ**: Выбирайте, какая именно модель ИИ Gemini будет обрабатывать ваш запрос (например, `gemini-3.1-flash-image-preview` или другие поддерживаемые модели).
- **Сетевая отказоустойчивость**: Встроенные патчи 10-минутного тайм-аута SDK и циклы автоматических повторов (до 3 попыток) гарантируют, что генерация не прервется из-за временной перегрузки серверов Google API или ошибок `503/504 Deadline Exceeded`.
- **Терминал не требуется**: Автоматически настраивает все пути и обрабатывает логирование.
- **Асинхронная обработка**: Пользовательский интерфейс остается отзывчивым во время генерации наряда с помощью ИИ или при группировке модов.
- **Автономный исполняемый файл**: Приложение легко упаковывается в один `.exe` файл, который любой пользователь Windows может запустить сразу же после скачивания.

## 🚀 Быстрый старт (Для пользователей)

1. [Скачайте последний релиз `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases).
2. Запустите приложение.
3. Заполните панель **Settings** (Настройки):
   - Ваш **Gemini API Key** (API-ключ Gemini).
   - Путь к директории с установленной игрой **Haydee**.
   - Ваше **Author Name** (Имя автора) (Необязательно, применяется ко всем сгенерированным или сгруппированным модам).
   - Ваша **AI Model** (Модель ИИ) (По умолчанию `gemini-3.1-flash-image-preview`).
4. Нажмите **Save Settings** (Сохранить настройки).
5. Выберите вкладку рабочего процесса:
   - **✨ Generate Outfit** (Сгенерировать наряд): Введите уникальное имя мода, описательный промпт стиля и выберите, какие текстуры вы хотите сгенерировать (Diffuse, Specular или Normal) перед стартом.
   - **📦 Group Mods** (Группировка модов): Объедините несколько существующих модов в один мультимод. Введите новое имя мультимода, исходные моды для группировки (например, `red, green, blue`) и категорию слота (например, `color`).
6. Нажмите **Start Generation** (Начать генерацию) или **Group Outfits** (Сгруппировать наряды) и наблюдайте за происходящей магией во встроенном окне консоли!

*(Примечание: приложение автоматически сохранит ваши настройки в `AppData/Local/HaydeeOutfitGenerator/settings.json`, поэтому вам не придется каждый раз вводить свои данные.)*

### 🔑 Получение API-ключа Gemini

1. Перейдите в [Google AI Studio](https://aistudio.google.com/).
2. Войдите с помощью своего аккаунта Google.
3. Нажмите кнопку «Create API key» (Создать API-ключ).
4. Если появится запрос, прочитайте и примите условия обслуживания.
5. Нажмите «Create API key in new project» (Создать API-ключ в новом проекте) или используйте существующий проект.
6. Скопируйте сгенерированный ключ. Вам нужно будет вставить его в панель **Settings** (Настройки) в приложении.

## 🛠️ Установка для разработчиков

Если вы хотите внести свой вклад или самостоятельно собрать приложение:

### Предварительные требования

- Python 3.12+
- Git

### Установка

1. Клонируйте этот репозиторий:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение из исходного кода:
   ```bash
   python main.py
   ```

### Сборка исполняемого файла

Этот проект включает в себя автоматизированный скрипт, использующий `PyInstaller` для упаковки приложения в автономный файл `.exe` без черного окна консоли.

Для сборки:
```bash
python build.py
```

После завершения сборки ваше приложение будет доступно в папке `dist/` под названием `HaydeeOutfitGenerator.exe`.

### Запуск тестов

Этот проект включает автоматизированные тесты графического интерфейса, написанные с использованием `pytest` и `pytest-mock`.

1. Установите зависимости для тестирования:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Запустите тесты:
   ```bash
   pytest tests/
   ```

### Запуск линтинга

Этот проект использует `flake8` для обеспечения соблюдения стиля кода.

1. Убедитесь, что установлены зависимости для тестирования:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Запустите линтер:
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 Лицензия

Этот проект лицензируется в соответствии с условиями лицензии MIT — подробности см. в файле [LICENSE](LICENSE).