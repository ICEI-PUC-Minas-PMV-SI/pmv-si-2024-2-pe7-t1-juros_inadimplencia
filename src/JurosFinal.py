import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carregar os dados
dados = pd.read_csv('C:/Users/Lucas Lima/Desktop/Juros/JurosInadimplencia.csv')


df = pd.read_csv('C:/Users/Lucas Lima/Desktop/Juros/JurosInadimplencia.csv')

# Conversão para numéricos
df['Endividamento_Total'] = df['Endividamento_Total'].str.replace(',', '.').astype(float)
df['Confiança_Valor'] = df['Confiança_Valor'].str.replace(',', '.').astype(float)
df['Selic_Valor'] = df['Selic_Valor'].str.replace(',', '.').astype(float)
df['Inflação_Mensal'] = df['Inflação_Mensal'].str.replace(',', '.').astype(float)

# Conversão da coluna 'Periodo' para datetime
df['Periodo'] = pd.to_datetime(df['Periodo'], format='%d/%m/%Y')

# Histogramas
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.hist(df['Endividamento_Total'], bins=20, color='skyblue')
plt.title('Histograma do Endividamento Total')
plt.xlabel('Endividamento (%)')
plt.ylabel('Frequência')

plt.subplot(2, 2, 2)
plt.hist(df['Confiança_Valor'], bins=20, color='salmon')
plt.title('Histograma da Confiança do Consumidor')
plt.xlabel('Confiança (Índice)')
plt.ylabel('Frequência')

plt.subplot(2, 2, 3)
plt.hist(df['Selic_Valor'], bins=20, color='lightgreen')
plt.title('Histograma da Taxa Selic')
plt.xlabel('Selic (%)')
plt.ylabel('Frequência')

plt.subplot(2, 2, 4)
plt.hist(df['Inflação_Mensal'], bins=20, color='gold')
plt.title('Histograma da Inflação Mensal')
plt.xlabel('Inflação (%)')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()


# Mapa de calor de correlações
plt.figure(figsize=(10, 6))
correlation_matrix = df[['Endividamento_Total', 'Confiança_Valor', 'Selic_Valor', 'Inflação_Mensal']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor - Correlação entre Variáveis')
plt.show()

# Dispersão entre SELIC e Endividamento Total
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Selic_Valor', y='Endividamento_Total', color='darkblue')
plt.title('Dispersão: SELIC vs Endividamento Total')
plt.xlabel('Taxa Selic (%)')
plt.ylabel('Endividamento Total (%)')
plt.show()

# Evolução temporal de cada variável
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(df['Periodo'], df['Endividamento_Total'], color='skyblue', label='Endividamento Total')
plt.title('Evolução do Endividamento Total (%)')
plt.xlabel('Período')
plt.ylabel('Endividamento (%)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
plt.plot(df['Periodo'], df['Confiança_Valor'], color='salmon', label='Confiança do Consumidor')
plt.title('Evolução da Confiança do Consumidor (Índice)')
plt.xlabel('Período')
plt.ylabel('Confiança (Índice)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
plt.plot(df['Periodo'], df['Selic_Valor'], color='lightgreen', label='Taxa Selic')
plt.title('Evolução da Taxa SELIC (%)')
plt.xlabel('Período')
plt.ylabel('Selic (%)')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
plt.plot(df['Periodo'], df['Inflação_Mensal'], color='gold', label='Inflação Mensal')
plt.title('Evolução da Inflação Mensal (%)')
plt.xlabel('Período')
plt.ylabel('Inflação (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Gráficos adicionais usando Período
plt.figure(figsize=(14, 12))

# Comparação entre Endividamento Total, SELIC e Inflação
plt.subplot(2, 2, 1)
plt.plot(df['Periodo'], df['Endividamento_Total'], label='Endividamento Total (%)', color='skyblue')
plt.plot(df['Periodo'], df['Selic_Valor'], label='Taxa SELIC (%)', color='lightgreen')
plt.plot(df['Periodo'], df['Inflação_Mensal'], label='Inflação Mensal (%)', color='gold')
plt.title('Evolução do Endividamento, SELIC e Inflação ao Longo do Tempo')
plt.xlabel('Período')
plt.ylabel('Valores (%)')
plt.legend(loc='best')
plt.xticks(rotation=45)

# Comparação entre Confiança do Consumidor e SELIC
plt.subplot(2, 2, 2)
plt.plot(df['Periodo'], df['Confiança_Valor'], label='Confiança do Consumidor', color='salmon')
plt.plot(df['Periodo'], df['Selic_Valor'], label='Taxa SELIC (%)', color='lightgreen')
plt.title('Evolução da Confiança do Consumidor e SELIC ao Longo do Tempo')
plt.xlabel('Período')
plt.ylabel('Valores')
plt.legend(loc='best')
plt.xticks(rotation=45)

# Diferença entre Endividamento e Inflação
plt.subplot(2, 2, 3)
plt.plot(df['Periodo'], df['Endividamento_Total'] - df['Inflação_Mensal'], label='Diferença')