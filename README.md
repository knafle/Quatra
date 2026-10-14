# Quatra — Software & Herramientas a Medida para Logística PyME

> **"El software se adapta a tu operación, no tu equipo al software."**

Quatra es un servicio de consultoría e ingeniería operativa para PyMEs de transporte y depósitos de logística. Auditamos in-situ los procesos de planta y desarrollamos herramientas satélite a medida para automatizar tareas repetitivas y devolver cientos de horas-hombre al mes.

---

## 🚀 Versiones Visuales Disponibles

El sitio incluye un selector interactivo flotante (`VersionSwitcher`) que permite alternar entre 3 enfoques de diseño y comunicación:

| Versión | Ruta | Enfoque |
| :--- | :--- | :--- |
| **v1: Minimal Noir** | `/1` | Estética *Linear / Apple*, alto contraste blanco sobre negro, tarjeta insignia squircle y acabados limpios. |
| **v2: Industrial Tech** | `/2` | Fondo pizarra oscura, acentos en **ámbar de seguridad y muelle**, cuadrícula de plano (*blueprint*) y estética de telemetría de operaciones. |
| **v3: Boutique Studio** | `/3` | Enfoque editorial centrado en los 4 hermanos fundadores, acentos verde esmeralda y tono de cercanía artesanal. |

---

## ⚡ Características Principales

- **Calculadora Interactiva de ROI y Horas-Hombre:** Permite a los prospectos ingresar su dotación de personal y horas manuales para proyectar el ahorro de tiempo y dinero, con enlace dinámico pre-cargado a WhatsApp.
- **Los 4 Pilares de Quatra:** Diagnóstico In-Situ, Herramientas Satélite, Integración Invisible y Medición de Impacto.
- **Configuración Centralizada:** Parámetros de marca, número de WhatsApp y enlaces editables desde un único archivo (`src/data/siteConfig.ts`).
- **Arquitectura de Carga Rápida:** Construido con Astro y Tailwind CSS v4 para rendimiento instantáneo y SEO optimizado.

---

## 🛠️ Tecnologías

- **Framework:** [Astro](https://astro.build/)
- **Estilos:** [Tailwind CSS v4](https://tailwindcss.com/)
- **Iconos:** [@lucide/astro](https://lucide.dev/)
- **Tipografía:** Plus Jakarta Sans

---

## 📦 Estructura del Proyecto

```text
/
├── public/
│   ├── quatra-badge-hd.png          # Isotipo squircle en alta resolución
│   ├── quatra-knot-white.png        # Símbolo vectorial transparente blanco
│   ├── quatra-knot-black.png        # Símbolo vectorial transparente negro
│   └── favicon.png                  # Favicon oficial
├── src/
│   ├── components/
│   │   ├── VersionSwitcher.astro    # Barra flotante para alternar entre /1, /2 y /3
│   │   ├── Navbar.astro             # Navegación responsive
│   │   ├── Hero.astro               # Sección principal
│   │   ├── Comparison.astro         # Comparativa frente a ERPs y planillas Excel
│   │   ├── RoiCalculator.astro      # Calculadora interactiva de horas-hombre
│   │   ├── Methodology.astro        # Los 4 pilares operativos
│   │   ├── SolutionsShowcase.astro  # Casos reales de herramientas creadas
│   │   ├── AboutUs.astro            # Los hermanos fundadores
│   │   ├── Faq.astro                # Preguntas frecuentes
│   │   ├── CtaBanner.astro          # Llamado final a la acción
│   │   └── Footer.astro             # Pie de página
│   ├── data/
│   │   └── siteConfig.ts            # Configuración de marca y contacto
│   ├── layouts/
│   │   └── Layout.astro             # Layout principal y metadatos SEO / OpenGraph
│   ├── pages/
│   │   ├── index.astro              # Redirección a /1
│   │   ├── 1.astro                  # Versión 1: Minimalist Noir
│   │   ├── 2.astro                  # Versión 2: Industrial Tech
│   │   └── 3.astro                  # Versión 3: Boutique Studio
│   └── styles/
│       └── global.css               # Estilos globales y capas Tailwind
└── package.json
```

---

## 💻 Desarrollo Local

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev

# Compilar para producción
npm run build

# Vista previa de producción
npm run preview
```
