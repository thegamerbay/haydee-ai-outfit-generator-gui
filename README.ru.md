> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

Современный графический интерфейс для библиотеки [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator). Легко создавайте собственные костюмы для Haydee без необходимости возиться с терминалами или переменными среды!

### 📥 [Скачать последнюю версию HaydeeOutfitGenerator.exe можно здесь](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ Сгенерированные примеры

Посмотрите, что вы можете создать! Следующие наряды были сгенерированы с использованием этого инструмента и представлены в моде [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) в Мастерской Steam.

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

- **Современный темный интерфейс**: Создан с использованием `CustomTkinter` для элегантного внешнего вида в стиле игры.
- **Три уникальных рабочих процесса**: Плавное переключение между генерацией совершенно новых нарядов с помощью ИИ, получением творческого вдохновения для ваших стилей и группировкой существующих модов в единые мультимоды.
- **Детальный контроль генерации**: Индивидуальное переключение генерации карт Diffuse (Цвет), Specular (Материал/Блеск) и Normal (3D рельеф) для экономии API-запросов или перегенерации отдельных частей.
- **Настраиваемые модели ИИ**: Выбирайте, какая именно модель ИИ Gemini будет обрабатывать ваш запрос (например, `gemini-3.1-flash-image-preview` или другие поддерживаемые модели).
- **Устойчивость к сбоям сети**: Встроенные патчи с 10-минутным таймаутом SDK и автоматические циклы из 3 попыток повторения API-запросов гарантируют, что генерации не прервутся из-за временной перегрузки серверов Google API или ошибок `503/504 Deadline Exceeded`.
- **Без использования терминала**: Автоматически настраивает все пути и обрабатывает логирование.
- **Асинхронная обработка**: Интерфейс остается отзывчивым во время генерации наряда с помощью ИИ или группировки модов.
- **Автономный исполняемый файл**: Приложение легко упаковывается в один `.exe` файл, который любой пользователь Windows может запустить прямо из коробки.

## 🚀 Быстрый старт (для пользователей)

1. [Скачайте последний релиз `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases).
2. Запустите приложение.
3. Заполните панель **Settings** (Настройки):
   - Ваш **Ключ Gemini API**.
   - Путь к папке с установленной игрой **Haydee**.
   - Ваше **Имя автора** (необязательно, применяется ко всем сгенерированным или сгруппированным модам).
   - Ваша **Модель ИИ** (по умолчанию `gemini-3.1-flash-image-preview`).
4. Нажмите **Save Settings** (Сохранить настройки).
5. Выберите вкладку нужного рабочего процесса:
   - **✨ Generate Outfit** (Сгенерировать наряд): Введите уникальное имя мода, описательный промпт стиля и выберите, какие текстуры вы хотите сгенерировать (Diffuse, Specular или Normal) перед запуском.
   - **💡 Prompt Ideas** (Идеи для промптов): Зашли в тупик? Введите простую тему (например, "Cyberpunk") и получите сгенерированные ИИ концепты нарядов. Применяйте идеи напрямую в генератор одним кликом.
   - **📦 Group Mods** (Группировка модов): Объедините несколько существующих модов в один мультимод. Введите новое имя мультимода, исходные моды для группировки (например, `red, green, blue`) и категорию слота (например, `color`).
6. Нажмите **Start Generation**, **Generate Prompt Ideas** или **Group Outfits** и наблюдайте за волшебством во встроенном окне консоли!

*(Примечание: приложение автоматически сохранит ваши настройки в `AppData/Local/HaydeeOutfitGenerator/settings.json`, поэтому вам не придется вводить свои данные каждый раз.)*

### 🔑 Получение ключа Gemini API

1. Перейдите в [Google AI Studio](https://aistudio.google.com/).
2. Войдите с помощью вашей учетной записи Google.
3. Нажмите кнопку «Create API key».
4. При необходимости прочтите и примите условия обслуживания.
5. Нажмите «Create API key in new project» (или используйте существующий проект).
6. Скопируйте сгенерированный ключ. Вам нужно будет вставить его в панель **Settings** (Настройки) приложения.

## 🛠️ Настройка для разработчиков

Если вы хотите внести свой вклад или собрать приложение самостоятельно:

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

Этот проект включает автоматизированный скрипт, который использует `PyInstaller` для упаковки приложения в автономный `.exe` без черного окна консоли.

Для сборки:
```bash
python build.py
```

После завершения сборки ваше приложение будет доступно в папке `dist/` под именем `HaydeeOutfitGenerator.exe`.

### Запуск тестов

Этот проект включает автоматизированные тесты GUI, написанные с использованием `pytest` и `pytest-mock`.

1. Установите зависимости для тестирования:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Запустите тесты:
   ```bash
   pytest tests/
   ```

### Запуск линтера

Этот проект использует `flake8` для проверки стиля кода.

1. Убедитесь, что зависимости для тестирования установлены:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Запустите линтер:
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 Лицензия

Этот проект распространяется по лицензии MIT — см. файл [LICENSE](LICENSE) для получения подробной информации.