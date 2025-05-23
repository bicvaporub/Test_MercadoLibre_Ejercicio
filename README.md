# 🧪 Test Automatizado de Búsqueda en MercadoLibre

Este proyecto realiza pruebas automatizadas en el sitio [MercadoLibre México](https://www.mercadolibre.com.mx) usando **Selenium WebDriver** y **pytest**. La prueba automatiza una búsqueda del producto "PlayStation 5", aplica filtros y extrae los primeros 5 resultados ordenados por mayor precio.

---

## 📦 Requisitos

- Python 3.8+
- Google Chrome instalado
- ChromeDriver (instalado automáticamente por `webdriver-manager`)

---

## 📁 Estructura del Proyecto

```
.
├── conftest.py
├── requirements.txt
├── test/
│   └── test_mercadolibre.py
└── README.md
```

---

## 🔧 Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu-usuario/mercadolibre-playstation-test.git
cd mercadolibre-playstation-test
```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecutar la prueba

Desde la raíz del proyecto, ejecuta:

```bash
pytest -s
```

El flag `-s` permite mostrar los `print()` del test directamente en la consola.

---

## 🧪 Detalles del test

El test realiza los siguientes pasos:

1. Accede a [mercadolibre.com](https://www.mercadolibre.com)
2. Selecciona México como país.
3. Busca el término “playstation 5”.
4. Filtra por condición **Nuevo**.
5. Filtra por ubicación: **Ciudad de México (Distrito Federal)**.
6. Ordena los resultados por **Mayor precio**.
7. Extrae los primeros **5 productos visibles**, mostrando nombre y precio en consola.

---

## ✅ Dependencias

Estas son las versiones actuales usadas en el proyecto (`requirements.txt`):

```txt
selenium==4.32.0
pytest==8.3.5
webdriver-manager==4.0.2
```

---

## 💡 Notas

- Se utiliza `webdriver-manager` para manejar automáticamente la versión compatible de ChromeDriver.
- El archivo `conftest.py` define el fixture `driver` para manejar la sesión de Chrome.
- Si el sitio web cambia estructura (HTML/CSS), es posible que debas actualizar los selectores CSS o XPath.

---

## 📄 Licencia

MIT License. Libre de usar y modificar.
