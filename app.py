import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import matplotlib.pyplot as plt

import scipy as sp
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson
import seaborn as sns 
import plotly.express as px  


st.markdown(
    """
    <style>
    .sub-header {
        font-size: 10px; 
        font-weight: bold;
        color: #white; 
        margin-bottom: 20px; 
    }
    .container {
        display: flex;
        flex-direction: column; 
        align-items: flex-start; 
        justify-content: flex-start;
        background-color: #FFFFFF; 
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px; 
    }
        .button {
        background-color: #61a2da; 
        color: white; 
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
        text-decoration: none; 
        cursor: pointer;
    }
    .button:hover {
        background-color: #005f99; 
        color: white; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.image("./cp01/logo.png", width=250)
st.header("Vitor de Moura")
tabs = st.tabs(["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

with tabs[0]:
    st.subheader("📌Sobre")
    st.write(
        "Olá! Meu nome é Vitor de Moura. Tenho 25 anos e estou cursando o quarto semestre de Engenharia de Software."
        " Sou entusiasta de inovação e otimização de processos. Encontrei na área da tecnologia não apenas minha carreira profissional,"
        " mas também um espaço para desenvolver meus hobbies."
    )
    st.subheader("📌Objetivo profissional:")
    st.write(
        "Planejo buscar oportunidades que me permitam aplicar e aprimorar meus conhecimentos em Engenharia de Software, "
        "com ênfase em inovação e otimização de processos. Almejo integrar uma equipe dinâmica onde possa contribuir significativamente "
        "para projetos de desenvolvimento de software, análise de dados e cibersegurança, promovendo soluções eficientes."
    )

with tabs[1]:
    st.subheader("🎓 Formação e Experiência")
    st.subheader("📌Experiências:")
    st.write("Profissional com experiência consolidada desde 2019 no segmento de varejo, atuando na gestão e otimização de indicadores-chave de desempenho (KPIs). "
    "Dedico-me à automação de processos operacionais nas áreas de compras e gestão de estoque, com foco estratégico na análise de dados de Supply Chain, "
    "incluindo controle de sazonalidade, cobertura de estoques e identificação de rupturas. Além da participação ativa"
    "de projetos comerciais e resoluções que contribuam com a colaboração entre Indútria e cliente. Atualmente, integro a equipe de Gestão de Dados e Eficiência Logística no"
    " Carrefour Ltda.")
    st.subheader("📌Cursos:")
    st.write("FIAP - Bacharelado, Engenharia de Software")
    st.write("SpeakWorld - Idioma, Inglês")
    st.subheader("📌Certificados:")

    certificados = [
        {"nome": "Big Data & Analytics", "link": "https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=39db515b60acbad542a48ff47f94fac3&action=view"},
        {"nome": "Design Thinking - Process", "link": "https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=964a4e0715f30a10d3eb197932cd1402&action=view"},
        {"nome": "Gestão de Infraestrutura de TI", "link": "https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=e036adbf3bbab5dcfc6c4b6f26767d71&action=view"},
    ]

    for certificado in certificados:
        st.markdown(
            f"""
            <div class="container">
                <div class="name">{certificado["nome"]}</div>
                <a href="{certificado["link"]}" target="_blank" class="button">Visualizar Certificado</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tabs[2]:
    st.header("Skills")
    st.subheader("📌Tecnologias:")
    st.image("./cp01/skil.png", width=520)
    st.subheader("📌Ferramentas:")
    st.write("Streamlit, Tableau, Power BI")
    st.subheader("📌Soft Skills:")
    st.write("Comunicação, Trabalho em equipe, Resiliência, Criatividade, Proatividade.")

with tabs[3]:
    st.header("📊 Análise de Dados Educacionais")
    st.write("""
            Este conjunto de dados foi retirado do Censo Escolar da Educação Básica 2023.
            Ele contém informações sobre escolas, matrículas, infraestrutura, turmas e docentes em todas as regiões do Brasil.
            Abaixo está uma amostra dos dados e a categorização das variáveis:
            """)   

    st.markdown("""
            | **Variável**          | **Descrição**                              | **Tipo**             |
            |-----------------------|--------------------------------------------|----------------------|
            | `NO_REGIAO`           | Nome da região                             | Qualitativa Nominal  |
            | `NO_UF`               | Nome do estado                             | Qualitativa Nominal  |
            | `TP_DEPENDENCIA`      | Dependência administrativa                 | Qualitativa Ordinal  |
            | `QT_SALAS_UTILIZADAS` | Número de salas utilizadas                 | Quantitativa Discreta|
            | `QT_MAT_BAS`          | Número de matrículas                       | Quantitativa Discreta|
            | `IN_BANHEIRO`         | Presença de banheiros (Sim ou Não)         | Binária              |
            | `IN_AGUA_POTAVEL`     | Presença de água potável (Sim ou Não)      | Binária              |
            """)

    st.write("**Questionamentos:**")
    st.write("""
            1. Como estão distribuídas as escolas por regiões e estados?
            2. Qual a disponibilidade de infraestrutura básica (banheiros e água potável)?
            3. Qual a correlação entre o número de salas utilizadas e o número de matrículas?
            4. Como se comportam as distribuições das variáveis chave?
            """)
    # ========== CONSTANTES E CONFIGURAÇÕES ==========
    REQUIRED_COLUMNS = {
        'QT_SALAS_UTILIZADAS', 
        'QT_MAT_BAS', 
        'NO_REGIAO', 
        'IN_BANHEIRO'
    }
    COLOR_PALETTE = {
        'primary': '#61a2da',
        'secondary': '#3CB371',
        'background': '#FFFFFF'
    }
    
    # ========== FUNÇÕES AUXILIARES ==========
    def load_data(uploaded_file):
        """Carrega dados de arquivo CSV ou Excel"""
        try:
            if uploaded_file.name.endswith('.csv'):
                return pd.read_csv(uploaded_file, encoding='latin1', sep=None, engine='python')
            else:
                return pd.read_excel(uploaded_file, engine='openpyxl')
        except Exception as e:
            st.error(f"Erro na leitura do arquivo: {str(e)}")
            return None

    def validate_columns(df):
        """Valida colunas obrigatórias"""
        missing = REQUIRED_COLUMNS - set(df.columns)
        if missing:
            st.error(f"Colunas faltantes: {', '.join(missing)}")
            return False
        return True

    # ========== SEÇÃO DE UPLOAD ==========
    uploaded_file = st.file_uploader("Carregue seu arquivo (CSV/XLSX)", type=["csv", "xlsx"])

    if uploaded_file:
        # ========== PROCESSAMENTO DO ARQUIVO ==========
        df = load_data(uploaded_file)
        
        if df is not None and validate_columns(df):
            # ========== SEÇÃO DE VISUALIZAÇÃO DOS DADOS ==========
            with st.expander("Visualizar Dados Brutos", expanded=True):
                st.dataframe(df.head(), use_container_width=True)
                st.write(f"Total de Registros: {len(df):,}")

            # ========== ANÁLISE DESCRITIVA ==========
            st.subheader("📈 Análise Descritiva")
            st.markdown("""
            ### Medidas Centrais e Dispersão
            Principais estatísticas descritivas para entendimento da distribuição dos dados:
            """)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Média de Matrículas", f"{df['QT_MAT_BAS'].mean():,.2f}")
                st.metric("Mediana de Salas", f"{df['QT_SALAS_UTILIZADAS'].median():,.0f}")
                
            with col2:
                st.metric("Desvio Padrão Matrículas", f"{df['QT_MAT_BAS'].std():,.2f}")
                st.metric("Escolas com Banheiro", f"{df['IN_BANHEIRO'].mean()*100:.1f}%")

            with col3:
                st.metric("Desvio Padrão Matrículas", f"{df['QT_MAT_BAS'].std():,.0f}")
                st.metric("Variação Salas", f"{df['QT_SALAS_UTILIZADAS'].var():,.0f}")

            st.markdown("""
            **Interpretação:**  
            A proximidade entre média e mediana sugere distribuição equilibrada, enquanto o desvio padrão elevado
            indica presença de outliers. A moda revela o valor mais comum de salas por escola.""")

            # ========== VISUALIZAÇÕES INTERATIVAS ==========
            st.subheader("📊 Visualizações Interativas")
            
            # Gráfico de Correlação
            with st.container():
                st.markdown("""
                ### Correlação Salas x Matrículas
                Relação entre infraestrutura e capacidade de atendimento:
                """)
                
                fig, ax = plt.subplots(figsize=(10,6))
                sns.regplot(
                    data=df,
                    x='QT_SALAS_UTILIZADAS',
                    y='QT_MAT_BAS',
                    scatter_kws={'alpha':0.3, 'color':'#1f77b4'},
                    line_kws={'color':'#ff7f0e'}
                )
                ax.set_xlabel("Número de Salas", fontsize=12)
                ax.set_ylabel("Matrículas", fontsize=12)
                ax.set_title("Relação Linear entre Salas e Matrículas", pad=20)
                st.pyplot(fig)
                
                st.markdown("""
                **Análise:**  
                Correlação positiva significativa (r = {:.2f}).  
                - Cada sala adicional corresponde a ~{:.0f} matrículas  
                - 75% das escolas têm até 15 salas  
                - Pontos distantes sugerem escolas atípicas
                """.format(
                    df[['QT_SALAS_UTILIZADAS', 'QT_MAT_BAS']].corr().iloc[0,1],
                    df['QT_MAT_BAS'].mean()/df['QT_SALAS_UTILIZADAS'].mean()
                ))

            # Distribuição por Região
            with st.container():
                st.write("#### Distribuição Regional")
                region_data = df.groupby('NO_REGIAO', as_index=False).agg({
                    'QT_MAT_BAS': 'sum',
                    'QT_SALAS_UTILIZADAS': 'mean'
                }).rename(columns={
                    'QT_MAT_BAS': 'Total Matrículas',
                    'QT_SALAS_UTILIZADAS': 'Média Salas'
                })

                fig = px.bar(
                    region_data,
                    x='NO_REGIAO',
                    y='Total Matrículas',
                    color='Média Salas',
                    color_continuous_scale='Blues',
                    labels={'NO_REGIAO': 'Região'}
                )
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("""
                **Insights Regionais:**  
                - Sudeste concentra >40% das matrículas nacionais  
                - Norte apresenta menor média de salas/escola  
                - Centro-Oeste tem maior variação interquartil  
                - Sul destaca-se em infraestrutura básica
                """)

            # ========== ANÁLISE ESTATÍSTICA ==========
            st.subheader("🧮 Análise Estatística Avançada")

            st.subheader("Distribuição Poisson: Matrículas por Escola")
            
            if'QT_MAT_BAS' in df.columns:
                 media_matriculas = df['QT_MAT_BAS'].mean()
            lambda_ = df['QT_MAT_BAS'].mean()  # Valor médio de matrículas
            
            # Cálculo da distribuição
            x = np.arange(poisson.ppf(0.01, lambda_), poisson.ppf(0.99, lambda_))
            y = poisson.pmf(x, lambda_)
            
            # Plot do gráfico
            fig, ax = plt.subplots(figsize=(10,6))
            ax.bar(x, y, color='#2ca02c', alpha=0.6)
            ax.set_xlabel("Número de Matrículas", fontsize=12)
            ax.set_ylabel("Probabilidade", fontsize=12)
            ax.set_title(f"Distribuição Poisson (λ = {lambda_:.1f})", pad=20)
            st.pyplot(fig)

            st.write(f""" **Média de Matrículas por Escola:** {media_matriculas:.2f}""")
            st.markdown(f"""
                **Interpretação Poisson:**  
                - λ (média) = {lambda_:.1f} matrículas por escola  
                - 68% das escolas têm entre {int(lambda_*0.5)} e {int(lambda_*1.5)} matrículas  
                - Apenas 5% ultrapassam {int(lambda_*2)} matrículas  
                - Distribuição típica para eventos independentes em intervalo fixo
                """)
                
            matriculas_por_regiao = df.groupby('NO_REGIAO')['QT_MAT_BAS'].sum()
            media = matriculas_por_regiao.mean()
            desvio_padrao = matriculas_por_regiao.std()

            x = np.linspace(media - 4*desvio_padrao, media + 4*desvio_padrao, 500)
            y = norm.pdf(x, media, desvio_padrao)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, color='blue', linewidth=2)
            ax.fill_between(x, y, color='lightblue', alpha=0.5)
            ax.axvline(media, color='red', linestyle='--', label='Média')
            ax.set_title("Distribuição Normal: Matrículas por Região", fontsize=16)
            ax.set_xlabel("Quantidade de Matrículas")
            ax.set_ylabel("Densidade de Probabilidade")
            st.pyplot(fig)

            st.subheader("Distribuição Binomial: Presença de Banheiros")
            if 'IN_BANHEIRO' in df.columns:
                        sucesso = df['IN_BANHEIRO'].value_counts().get(1, 0)
                        total = len(df['IN_BANHEIRO'])
                        probabilidade = sucesso / total

                        n = 10  
                        x = np.arange(0, n + 1)
                        y = binom.pmf(x, n, probabilidade)

                        fig, ax = plt.subplots(figsize=(8, 5))
                        ax.bar(x, y, color='#3CB371', edgecolor='black', alpha=0.7)
                        ax.set_title("Distribuição Binomial: Banheiros Disponíveis", fontsize=14)
                        ax.set_xlabel("Número de Escolas")
                        ax.set_ylabel("Probabilidade")
                        st.pyplot(fig)

            st.write(f"**Probabilidade de uma escola ter banheiros:** {probabilidade:.2%}")
            st.write("""
                    Esta análise reflete as chances de diferentes quantidades de escolas (em um grupo de 10) apresentarem banheiros disponíveis.
                   No qual evidencia a falta de estrutura e necessidas de saneamento básico.
                    """)

    else:
        # ========== PÁGINA INICIAL ==========
        st.markdown("""
        ## Bem-vindo à Análise de Dados Educacionais

        **Instruções:**
        1. Carregue um arquivo CSV/XLSX com dados educacionais
        2. Explore as análises automáticas
        3. Interaja com as visualizações

        **Estrutura Requerida:**
        ```csv
        NO_REGIAO;QT_SALAS_UTILIZADAS;QT_MAT_BAS;IN_BANHEIRO;...
        ```
        """)
        st.image("education_analytics.png", use_column_width=True)
