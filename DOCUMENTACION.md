# Documentación del Proyecto - TP Gestión Colaborativa

## Integrantes del Equipo
- **Hugo (P1)** - Líder y Organizador: Creación del repositorio y estructura
- **Paco (P2)** - Desarrollador Técnico: Script de análisis de ventas
- **Luis (P3)** - Revisor y QA: Revisión, documentación y gestión del PR

## Escenario Elegido
**Escenario B – Análisis de Ventas de una Pequeña Empresa**

## Dataset Utilizado
- Archivo: `sales_sample_2024.csv`
- Columnas: id, sales_date, sales_amount
- Período: Enero a Diciembre 2024
- Cantidad de registros: 367 ventas

## Estructura del Proyecto
TP_2_OE/
├── datos/
│ └── sales_sample_2024.csv
├── scripts/
│ └── analisis.py
├── resultados/
│ ├── ventas_totales.txt
│ ├── ventas_por_mes.csv
│ ├── ventas_por_trimestre.csv
│ ├── estadisticas_por_mes.csv
│ ├── ventas_por_mes_barras.png
│ ├── ventas_tendencia.png
│ └── distribucion_ventas.png
├── README.md
├── .gitignore
└── DOCUMENTACION.md


## Cómo ejecutar el proyecto
1. Clonar el repositorio
2. Instalar dependencias: `pip install pandas matplotlib`
3. Ejecutar: `python scripts/analisis.py`
4. Los resultados se guardan en la carpeta `/resultados`

## Resultados Obtenidos
- Ventas totales del período: [ver resultados/ventas_totales.txt]
- Mejor mes de ventas: [ver resultados/ventas_por_mes.csv]

## Revisión de Calidad (QA)
- Script probado y funcionando correctamente
- Comentarios técnicos agregados
- Código reproducible en Google Colab
- Sin datos sensibles expuestos
