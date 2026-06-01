# 🔢 Conversor Multimedia de Unidades

> Aplicación de escritorio desarrollada en Python con PySide6, arquitectura MVC y interfaz MDI para convertir valores entre múltiples unidades de medida.

---

## 📋 Descripción

**Conversor Multimedia de Unidades** es una aplicación de escritorio que permite realizar conversiones entre unidades de medida de 6 categorías distintas. Cada categoría se abre como una sub-ventana independiente dentro de una interfaz MDI *(Multiple Document Interface)*, permitiendo trabajar con varias conversiones al mismo tiempo.

El proyecto fue desarrollado como trabajo universitario para la materia **Programación III** de Ingeniería de Sistemas en **UDENAR Sede Tumaco**, aplicando el patrón de arquitectura **MVC (Modelo-Vista-Controlador)** con diseño de interfaz en **Qt Designer**.

---

## ✨ Características

- 🔄 **6 categorías de conversión:**
  - Longitud — mm, cm, dm, m, dam, hm, km, in, ft, yd, mi, nmi, µm, nm
  - Masa — µg, mg, g, kg, t, oz, lb, st, ozt
  - Volumen — ml, l, m³, gal, bbl, pt, cup, fl oz, tbsp, tsp
  - Tiempo — ms, s, min, h, d, sem
  - Velocidad — m/s, km/h, mph, ft/s
  - Temperatura — °C, °F, K, °Ra *(con fórmulas no lineales)*

- 🪟 **Interfaz MDI** — múltiples sub-ventanas dentro de una ventana principal con soporte para cascada y mosaico
- 🎨 **Temas visuales** — tema claro y oscuro con QSS, persistente entre sesiones mediante QSettings
- 📜 **Historial de conversiones** — guardado en JSON agrupado por fecha
- 📚 **Teoría y tablas de referencia** — contenido educativo por categoría en formato HTML
- 📏 **ReglaVisual** — widget personalizado interactivo dibujado con QPainter
- 🔍 **Autocompletado** — QCompleter en los combobox de unidades
- 🔢 **Preferencia de decimales** — control de precisión del resultado con QSpinBox
- 📤 **Exportación a CSV** — exporta el historial de conversiones
- 📦 **Empaquetado con PyInstaller** — distribuible como ejecutable sin necesidad de instalar Python

---

## 🏗️ Arquitectura

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)**:

```
Usuario
  │
  ▼
Vista (PySide6 + Qt Designer)
  │  emite señales
  ▼
Controlador
  │  llama métodos
  ▼
Modelo (lógica de negocio)
  │  lee/escribe
  ▼
Repositorios → JSON
```

### Capas

| Capa | Responsabilidad |
|------|----------------|
| **Modelo** | Lógica de conversión, categorías, historial |
| **Vista** | Interfaz gráfica, widgets, señales |
| **Controlador** | Conecta vista y modelo, maneja eventos |
| **Repositorios** | Lectura/escritura de archivos JSON |

---

## 📁 Estructura del Proyecto

```
conversor_multimedia/
│
├── main.py                        # Punto de entrada
├── utils.py                       # Utilidades (rutas PyInstaller)
├── gestor_temas.py                # Manejo de temas QSS + QSettings
├── requirements.txt               # Requerimientos para usar el proyecto
├── README.md                      # Proporciona informacion sobre el proyecto
│
├── model/
│   ├── model.py                   # Clase principal del modelo
│   ├── categoria.py               # Clase abstracta Categoria
│   ├── categoria_lineal.py        # Conversión por factores
│   ├── categoria_temperatura.py   # Conversión por fórmulas
│   ├── unidad.py                  # Dataclass Unidad
│   └── historial.py               # Dataclass Historial
│
├── repositorios/
│   ├── base_repository.py         # Clase abstracta BaseRepository
│   ├── unidades_repository.py     # Carga unidades desde JSON
│   ├── historial_repository.py    # Carga y guarda historial
│   └── teoria_repository.py      # Carga contenido teórico
│
├── controllers/
│   ├── controller_principal.py    # Controlador principal
│   ├── controller_conversion.py   # Controlador de conversión
│   └── controller_teoria.py      # Controlador de teoría
│
├── views/
│   ├── view_principal.py          # Ventana principal QMainWindow
│   ├── view_conversion.py         # Sub-ventana de conversión
│   ├── view_teoria.py             # Sub-ventana de teoría
│   ├── dialog_historial.py        # Diálogo de historial
│   ├── regla_visual.py            # Widget QPainter personalizado
│   └── ui/                        # Archivos generados por Qt Designer
│       ├── archivos_ui/
│       │     ├── dialog_datos_historial.ui       # Archivo ui del dialog_historial.py
│       │     ├── ventana_conversion.ui           # Archivo ui de la view_conversion.py
│       │     └── ventana_principal.ui            # Archivo ui de la view_principal.py
│       │
│       └── archivos_py/
│             ├── dialog_datos_historial.py       # Archivo py del dialog_historial.py
│             ├── ui_ventana_conversion.py        # Archivo py de la view_conversion.py
│             └── ui_ventana_principal.py         # Archivo py de la view_principal.py
│
└── recursos/
    ├── datos/
    │   ├── unidades.json          # Unidades y factores de conversión
    │   ├── historial.json         # Historial persistente
    │   ├── tablas.json            # Tablas de conversion(Teoria)
    │   └── teoria.json            # Contenido teórico
    └── estilos/
        ├── claro.qss              # Tema claro
        ├── oscuro.qss             # Tema oscuro
        └── icons/
            ├── cascade.svg
            ├── close.svg
            ├── convert.svg
            ├── history.svg
            ├── ruler.svg
            ├── save.svg
            └──tile.svg
```

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|-----------|-----|
| **Python 3.12** | Lenguaje principal |
| **PySide6** | Framework de interfaz gráfica |
| **Qt Designer** | Diseño visual de interfaces `.ui` |
| **QMdiArea** | Interfaz de múltiples documentos |
| **QPainter** | Widget personalizado ReglaVisual |
| **QSettings** | Persistencia de preferencias |
| **JSON** | Almacenamiento de datos |
| **PyInstaller** | Empaquetado como ejecutable |

---

## ⚙️ Instalación y Uso

### Requisitos

- Python 3.10 o superior
- pip

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/conversor-multimedia.git
cd conversor-multimedia

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Instalar dependencias
pip install PySide6
```

### Ejecutar

```bash
python main.py
```


---

## 🎮 Uso de la Aplicación

1. **Abrir conversión** — Menú *Aplicación → Realizar conversión*, selecciona la categoría en el diálogo
2. **Convertir** — Ingresa el valor, selecciona unidades de entrada y destino, presiona *Convertir*
3. **Ver teoría** — Menú *Teorías y Tablas*, selecciona la categoría
4. **Cambiar tema** — Menú *Tema → Claro / Oscuro*
5. **Ver historial** — Menú *Aplicación → Historial*
6. **Organizar ventanas** — Menú *Ventana → Cascada / Mosaico*

---

## 📐 Diagrama UML

El proyecto fue diseñado con un diagrama UML de clases que incluye:

- Jerarquía de categorías con polimorfismo (`Categoria` abstracta → `CategoriaLineal`, `CategoriaTemperatura`)
- Patrón repositorio con clase base abstracta (`BaseRepository`)
- Separación clara de capas MVC
- Widget personalizado (`ReglaVisual` → `QWidget`)
- Clases generadas por Qt Designer como `«mixin»`

---

## 👨‍💻 Autores

**Camilo Vergara**,
**Cristian Arciniegas**,
**Jhon Mosquera**  

---

## 📄 Licencia

MIT
