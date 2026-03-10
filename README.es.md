> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI Outfit Generator GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

Una moderna interfaz gráfica de usuario para la biblioteca [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator). ¡Genera fácilmente atuendos personalizados para Haydee sin lidiar con terminales ni variables de entorno!

### 📥 [Descarga la última versión de HaydeeOutfitGenerator.exe aquí](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ Ejemplos Generados

¡Mira lo que puedes crear! Los siguientes atuendos fueron generados usando esta herramienta y se incluyen en el mod [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) en la Steam Workshop.

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ Características

- **Moderna Interfaz Oscura**: Construida con `CustomTkinter` para una apariencia elegante con temática de videojuegos.
- **Tres Flujos de Trabajo Únicos**: Cambia sin problemas entre generar atuendos totalmente nuevos por IA, obtener inspiración creativa para tus estilos y agrupar tus mods existentes en un único multi-mod.
- **Control de Generación Granular**: Alterna individualmente la generación de mapas Difusos (Color), Especulares (Material/Brillo) y Normales (Relieve 3D) para ahorrar solicitudes a la API o regenerar partes específicas.
- **Modelos de IA Personalizables**: Elige exactamente qué modelo de IA Gemini procesa tu solicitud (por ejemplo, `gemini-3.1-flash-image-preview` u otros modelos compatibles).
- **Resiliencia de Red**: Parches integrados de tiempo de espera del SDK de 10 minutos y bucles automáticos de 3 reintentos en la API garantizan que tus generaciones no fallen debido a congestiones temporales en los servidores de la API de Google o errores `503/504 Deadline Exceeded`.
- **No Requiere Terminal**: Configura todas las rutas y maneja el registro de eventos automáticamente.
- **Procesamiento Asíncrono**: La interfaz de usuario se mantiene receptiva mientras el atuendo se genera por IA o mientras se agrupan los mods.
- **Ejecutable Independiente**: Empaqueta fácilmente la aplicación en un solo archivo `.exe` que cualquier usuario de Windows puede ejecutar sin configuración previa.

## 🚀 Inicio Rápido (Para Usuarios)

1. [Descarga la última versión de `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases).
2. Inicia la aplicación.
3. Completa el panel de **Ajustes** (**Settings**):
   - Tu **Clave API de Gemini** (**Gemini API Key**).
   - Ruta al directorio de instalación de tu juego **Haydee**.
   - Tu **Nombre de Autor** (**Author Name**) (Opcional, aplicado a todos los mods generados o agrupados).
   - Tu **Modelo de IA** (**AI Model**) (Por defecto `gemini-3.1-flash-image-preview`).
4. Haz clic en **Guardar Ajustes** (**Save Settings**).
5. Elige tu pestaña de flujo de trabajo:
   - **✨ Generar Atuendo** (**Generate Outfit**): Introduce un nombre único para el mod, una descripción del estilo (prompt) y selecciona qué texturas deseas generar (Difusa, Especular o Normal) antes de empezar.
   - **💡 Ideas de Prompts** (**Prompt Ideas**): ¿Te falta inspiración? Introduce una temática sencilla (como "Cyberpunk") y obtén conceptos de atuendos generados por IA. Aplica las ideas directamente al generador con un solo clic.
   - **📦 Agrupar Mods** (**Group Mods**): Combina varios mods existentes en un multi-mod. Introduce el nuevo nombre del multi-mod, los mods de origen a agrupar (p. ej., `red, green, blue`) y la categoría de la ranura (p. ej., `color`).
6. Haz clic en **Iniciar Generación** (**Start Generation**), **Generar Ideas de Prompts** (**Generate Prompt Ideas**) o **Agrupar Atuendos** (**Group Outfits**) ¡y observa cómo ocurre la magia en la ventana de consola integrada!

*(Nota: La aplicación guardará automáticamente tus ajustes en `AppData/Local/HaydeeOutfitGenerator/settings.json` para que no tengas que introducir tus datos cada vez.)*

### 🔑 Obteniendo una Clave API de Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/).
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en el botón "Create API key".
4. Si se te solicita, lee y acepta los términos de servicio.
5. Haz clic en "Create API key in new project" (o usa un proyecto existente).
6. Copia la clave generada. Necesitarás pegarla en el panel de **Ajustes** (**Settings**) de la aplicación.

## 🛠️ Configuración para Desarrolladores

Si deseas contribuir o compilar la aplicación tú mismo:

### Requisitos previos

- Python 3.12+
- Git

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación desde el código fuente:
   ```bash
   python main.py
   ```

### Compilando el Ejecutable

Este proyecto incluye un script automatizado que utiliza `PyInstaller` para empaquetar la aplicación en un archivo `.exe` independiente sin la ventana negra de consola.

Para compilar:
```bash
python build.py
```

Una vez finalizada la compilación, tu aplicación estará disponible en la carpeta `dist/` como `HaydeeOutfitGenerator.exe`.

### Ejecutando las Pruebas

Este proyecto incluye pruebas automatizadas para la GUI escritas con `pytest` y `pytest-mock`.

1. Instala las dependencias de prueba:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Ejecuta las pruebas:
   ```bash
   pytest tests/
   ```

### Ejecutando el Linter

Este proyecto utiliza `flake8` para asegurar el estilo del código.

1. Asegúrate de tener instaladas las dependencias de prueba:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Ejecuta el linter:
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.