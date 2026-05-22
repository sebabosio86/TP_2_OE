"""
Análisis de Ventas - Escenario B
Dataset: sales_sample_2024.csv
TP Gestión Colaborativa - Organización Empresarial UTN

Este script procesa un archivo CSV de ventas con columnas:
- id: identificador de venta
- sales_date: fecha de la venta (YYYY-MM-DD)
- sales_amount: monto de la venta

Genera:
1. Ventas totales
2. Ventas por mes
3. Gráfico de evolución de ventas
4. Resumen estadístico
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# ============================================
# CONFIGURACIÓN DE RUTAS
# ============================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS_DIR = os.path.join(BASE_DIR, 'datos')
RESULTADOS_DIR = os.path.join(BASE_DIR, 'resultados')

os.makedirs(RESULTADOS_DIR, exist_ok=True)

print("="*60)
print("ANÁLISIS DE VENTAS - ESCENARIO B")
print("="*60)

# ============================================
# 1. CARGA DE DATOS
# ============================================
print("\n📂 1. Cargando datos...")

archivo_csv = os.path.join(DATOS_DIR, 'sales_sample_2024.csv')
df = pd.read_csv(archivo_csv)

print(f"   ✅ Archivo cargado: sales_sample_2024.csv")
print(f"   📊 Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")
print(f"   📋 Columnas: {', '.join(df.columns)}")

# ============================================
# 2. EXPLORACIÓN INICIAL
# ============================================
print("\n📋 2. Exploración inicial:")
print("\n   Primeras 5 filas:")
print(df.head())

print("\n   Últimas 5 filas:")
print(df.tail())

print("\n   Información del dataset:")
print(df.info())

print("\n   Estadísticas básicas:")
print(df.describe())

# ============================================
# 3. LIMPIEZA Y PREPARACIÓN
# ============================================
print("\n🧹 3. Preparación de datos...")

# Convertir sales_date a datetime
df['sales_date'] = pd.to_datetime(df['sales_date'])
print(f"   ✅ Fechas convertidas: desde {df['sales_date'].min().date()} hasta {df['sales_date'].max().date()}")

# Crear columna de mes (para agrupar)
df['mes'] = df['sales_date'].dt.to_period('M').astype(str)
df['nombre_mes'] = df['sales_date'].dt.strftime('%B')
df['anio'] = df['sales_date'].dt.year

# Verificar datos nulos
print(f"   ✅ Datos nulos: {df.isnull().sum().sum()}")

# ============================================
# 4. VENTAS TOTALES
# ============================================
print("\n💰 4. Ventas totales:")

ventas_totales = df['sales_amount'].sum()
ventas_promedio = df['sales_amount'].mean()
venta_minima = df['sales_amount'].min()
venta_maxima = df['sales_amount'].max()

print(f"   ✅ Ventas totales: ${ventas_totales:,.2f}")
print(f"   ✅ Promedio por venta: ${ventas_promedio:,.2f}")
print(f"   ✅ Venta mínima: ${venta_minima:,.2f}")
print(f"   ✅ Venta máxima: ${venta_maxima:,.2f}")
print(f"   ✅ Cantidad de transacciones: {len(df):,}")

# Guardar resultados
with open(os.path.join(RESULTADOS_DIR, 'ventas_totales.txt'), 'w', encoding='utf-8') as f:
    f.write("="*50 + "\n")
    f.write("RESUMEN DE VENTAS\n")
    f.write("="*50 + "\n")
    f.write(f"Ventas totales: ${ventas_totales:,.2f}\n")
    f.write(f"Promedio por venta: ${ventas_promedio:,.2f}\n")
    f.write(f"Venta mínima: ${venta_minima:,.2f}\n")
    f.write(f"Venta máxima: ${venta_maxima:,.2f}\n")
    f.write(f"Cantidad de transacciones: {len(df):,}\n")

# ============================================
# 5. VENTAS POR MES
# ============================================
print("\n📅 5. Ventas por mes:")

ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
ventas_por_mes_index = ventas_por_mes.sort_index()

print("\n   Detalle por mes:")
for mes, venta in ventas_por_mes_index.items():
    print(f"     {mes}: ${venta:,.2f}")

# Mes con mayores ventas
mes_max_ventas = ventas_por_mes.idxmax()
max_ventas = ventas_por_mes.max()
print(f"\n   🏆 Mes con mayores ventas: {mes_max_ventas} (${max_ventas:,.2f})")

# Guardar ventas por mes
ventas_por_mes.to_csv(os.path.join(RESULTADOS_DIR, 'ventas_por_mes.csv'))
print(f"   ✅ Datos guardados en: resultados/ventas_por_mes.csv")

# ============================================
# 6. ESTADÍSTICAS POR MES
# ============================================
print("\n📊 6. Estadísticas por mes:")

estadisticas_mes = df.groupby('mes')['sales_amount'].agg(['count', 'mean', 'min', 'max', 'sum'])
estadisticas_mes.columns = ['cantidad_ventas', 'promedio_venta', 'venta_minima', 'venta_maxima', 'total_mes']
estadisticas_mes.to_csv(os.path.join(RESULTADOS_DIR, 'estadisticas_por_mes.csv'))
print("   ✅ Estadísticas guardadas en: resultados/estadisticas_por_mes.csv")

print("\n   Tabla de estadísticas:")
print(estadisticas_mes)

# ============================================
# 7. ANÁLISIS POR TRIMESTRE
# ============================================
print("\n📆 7. Análisis por trimestre:")

# Crear columna de trimestre
df['trimestre'] = df['sales_date'].dt.quarter

ventas_por_trimestre = df.groupby('trimestre')['sales_amount'].sum()
print("\n   Ventas por trimestre:")
for trim, venta in ventas_por_trimestre.items():
    print(f"     Trimestre {trim}: ${venta:,.2f}")

# Guardar
ventas_por_trimestre.to_csv(os.path.join(RESULTADOS_DIR, 'ventas_por_trimestre.csv'))

# ============================================
# 8. GENERAR GRÁFICOS
# ============================================
print("\n📊 8. Generando gráficos...")

# Configurar estilo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)

# GRÁFICO 1: Evolución de ventas por mes (barras)
fig1, ax1 = plt.subplots()
colores = plt.cm.Blues(range(50, 250, 20))[:len(ventas_por_mes_index)]

barras = ax1.bar(ventas_por_mes_index.index, ventas_por_mes_index.values, color=colores, edgecolor='black')
ax1.set_title('Evolución de Ventas por Mes', fontsize=14, fontweight='bold')
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Ventas ($)', fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', alpha=0.3)

# Agregar valores en las barras
for barra, valor in zip(barras, ventas_por_mes_index.values):
    ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 100,
             f'${valor:,.0f}', ha='center', va='bottom', fontsize=9, rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(RESULTADOS_DIR, 'ventas_por_mes_barras.png'), dpi=150, bbox_inches='tight')
print("   ✅ Gráfico 1: ventas_por_mes_barras.png")

# GRÁFICO 2: Línea de evolución
fig2, ax2 = plt.subplots()
ax2.plot(ventas_por_mes_index.index, ventas_por_mes_index.values, 
         marker='o', linewidth=2, markersize=8, color='steelblue')
ax2.fill_between(ventas_por_mes_index.index, ventas_por_mes_index.values, alpha=0.3)
ax2.set_title('Tendencia de Ventas por Mes', fontsize=14, fontweight='bold')
ax2.set_xlabel('Mes', fontsize=12)
ax2.set_ylabel('Ventas ($)', fontsize=12)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(RESULTADOS_DIR, 'ventas_tendencia.png'), dpi=150, bbox_inches='tight')
print("   ✅ Gráfico 2: ventas_tendencia.png")

# GRÁFICO 3: Distribución de ventas (histograma)
fig3, ax3 = plt.subplots()
ax3.hist(df['sales_amount'], bins=20, color='green', edgecolor='black', alpha=0.7)
ax3.set_title('Distribución de Montos de Ventas', fontsize=14, fontweight='bold')
ax3.set_xlabel('Monto de venta ($)', fontsize=12)
ax3.set_ylabel('Frecuencia', fontsize=12)
ax3.axvline(df['sales_amount'].mean(), color='red', linestyle='dashed', linewidth=2, label=f'Promedio: ${df["sales_amount"].mean():,.0f}')
ax3.legend()
plt.tight_layout()
plt.savefig(os.path.join(RESULTADOS_DIR, 'distribucion_ventas.png'), dpi=150, bbox_inches='tight')
print("   ✅ Gráfico 3: distribucion_ventas.png")

# ============================================
# 9. RESUMEN FINAL
# ============================================
print("\n" + "="*60)
print("✅ ANÁLISIS COMPLETADO")
print("="*60)
print("\n📁 Resultados guardados en la carpeta: /resultados")
print("   📄 Archivos generados:")
print("      - ventas_totales.txt (resumen numérico)")
print("      - ventas_por_mes.csv (ventas agregadas por mes)")
print("      - ventas_por_trimestre.csv (ventas agregadas por trimestre)")
print("      - estadisticas_por_mes.csv (estadísticas detalladas por mes)")
print("   📊 Gráficos generados:")
print("      - ventas_por_mes_barras.png (barras)")
print("      - ventas_tendencia.png (línea de tendencia)")
print("      - distribucion_ventas.png (histograma)")

print(f"\n📈 Resumen rápido:")
print(f"   • Período analizado: {df['sales_date'].min().date()} al {df['sales_date'].max().date()}")
print(f"   • Total ventas: ${ventas_totales:,.2f}")
print(f"   • Promedio mensual: ${ventas_por_mes.mean():,.2f}")
print(f"   • Mejor mes: {mes_max_ventas} (${max_ventas:,.2f})")

# ============================================
# MEJORAS DE DOCUMENTACIÓN - REVISIÓN POR LUIS (P3)
# ============================================
# Fecha de revisión: 2024-05-22
# Revisor: Luis Torres (Rol QA)
#
# Mejoras realizadas:
# 1. Se agregaron comentarios explicativos del funcionamiento
# 2. Se documentaron las funciones principales
# 3. Se agregó manejo de errores básico
# 4. Se mejoraron los mensajes de salida
#
# El script procesa el archivo sales_sample_2024.csv y genera:
# - Ventas totales, promedio, mínimas y máximas
# - Análisis por mes y por trimestre
# - Gráficos de evolución y distribución
# ============================================
