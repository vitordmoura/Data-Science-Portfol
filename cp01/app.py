import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson


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
    /* Estilo para os botões */
    .button {
        background-color: #61a2da; /* Cor do botão */
        color: white; /* Cor do texto */
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
        text-decoration: none; /* Remove sublinhado */
        cursor: pointer;
    }
    .button:hover {
        background-color: #005f99; /* Cor ao passar o mouse */
        color: white; /* Texto continua branco */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.image("./logo.png", width=250)
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

    # Certificados Dinâmicos
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
    st.image("./skil.png", width=520)
    st.subheader("📌Ferramentas:")
    st.write("Streamlit, Tableau, Power BI")
    st.subheader("📌Soft Skills:")
    st.write("Comunicação, Trabalho em equipe, Resiliência, Criatividade, Proatividade.")

with tabs[3]:
    st.header("Análise de Dados")
    st.subheader("1. Apresentação dos Dados")

    try:
        # Leitura dos dados
        df = pd.read_csv("./ed_basica_2023.csv", encoding='latin1', delimiter=';')

        # Descrição do conjunto de dados
        st.write("""
        Este conjunto de dados foi retirado do Censo Escolar da Educação Básica 2023.
        Ele contém informações sobre escolas, matrículas, infraestrutura, turmas e docentes em todas as regiões do Brasil.
        Abaixo está uma amostra dos dados e a categorização das variáveis:
        """)

        # Amostra dos dados
        st.write("Amostra dos Dados:")
        st.write(df.head())

        # Tabela explicativa sobre os tipos de variáveis
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

        # Perguntas principais de análise
        st.write("**Perguntas de Análise:**")
        st.write("""
        1. Como estão distribuídas as escolas por regiões e estados?
        2. Qual a disponibilidade de infraestrutura básica (banheiros e água potável)?
        3. Qual a correlação entre o número de salas utilizadas e o número de matrículas?
        4. Como se comportam as distribuições das variáveis chave?
        """)
    except Exception as e:
        st.write(f"Erro ao carregar os dados: {e}")

        st.subheader("2. Medidas Centrais e Análise Inicial")

    if {'QT_SALAS_UTILIZADAS', 'QT_MAT_BAS'}.issubset(df.columns):
        # Medidas centrais
        media = df['QT_MAT_BAS'].mean()
        mediana = df['QT_MAT_BAS'].median()
        moda = df['QT_MAT_BAS'].mode()[0]
        desvio_padrao = df['QT_MAT_BAS'].std()
        variancia = df['QT_MAT_BAS'].var()

        st.write("**Medidas Centrais:**")
        st.write(f"- Média: {media:.2f}")
        st.write(f"- Mediana: {mediana:.2f}")
        st.write(f"- Moda: {moda:.2f}")
        st.write(f"- Desvio Padrão: {desvio_padrao:.2f}")
        st.write(f"- Variância: {variancia:.2f}")

        st.write("""
        As métricas indicam uma variação significativa no número de matrículas entre escolas. A proximidade entre média e mediana
        sugere que os dados estão moderadamente equilibrados, mas o desvio padrão elevado indica a presença de outliers.
        """)

        # Gráfico de dispersão: Salas x Matrículas
        st.write("**Correlação entre Salas e Matrículas:**")
        fig, ax = plt.subplots()
        ax.scatter(df['QT_SALAS_UTILIZADAS'], df['QT_MAT_BAS'], alpha=0.5, color='blue')
        ax.set_title("Correlação entre Salas Utilizadas e Matrículas")
        ax.set_xlabel("Número de Salas Utilizadas")
        ax.set_ylabel("Número de Matrículas")
        st.pyplot(fig)

        st.write("""
        O gráfico sugere uma correlação positiva entre o número de salas utilizadas e o número de matrículas.
        Isso reflete que escolas com mais infraestrutura tendem a atender mais alunos.
        """)
    st.subheader("Distribuição de Matrículas por Região")

if {'QT_MAT_BAS', 'NO_REGIAO'}.issubset(df.columns):
    # Agrupar os dados por região e calcular o total de matrículas por região
    matriculas_por_regiao = df.groupby('NO_REGIAO')['QT_MAT_BAS'].sum()

    # Criar o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    matriculas_por_regiao.plot(kind='bar', color='#87CEFA', alpha=0.8, edgecolor='black', ax=ax)
    ax.set_title("Distribuição de Matrículas por Região", fontsize=16, fontweight='bold', color='darkblue')
    ax.set_xlabel("Região", fontsize=12)
    ax.set_ylabel("Quantidade de Matrículas", fontsize=12)
    ax.grid(axis='y', linestyle='--', linewidth=0.5, color='lightgray')
    st.pyplot(fig)

    # Explicação
    st.write("""
    Este gráfico apresenta a distribuição total de matrículas por região do Brasil. 
    Ele permite observar quais regiões possuem maior ou menor concentração de matrículas, 
    fornecendo insights sobre a dinâmica educacional no país.
    """)
else:
    st.warning("As colunas necessárias ('QT_MAT_BAS', 'NO_REGIAO') não estão disponíveis no conjunto de dados.")

# 2. Distribuição Poisson: Matrículas por Escola
st.subheader("Distribuição Poisson: Matrículas por Escola")

if 'QT_MAT_BAS' in df.columns:
    # Calcular o número médio de matrículas
    media_matriculas = df['QT_MAT_BAS'].mean()

    # Gerar os valores para a distribuição Poisson
    x = np.arange(0, int(media_matriculas) * 2)  # Intervalo de valores (até o dobro da média)
    y = poisson.pmf(x, media_matriculas)

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x, y, color='#87CEEB', alpha=0.8, edgecolor='black')
    ax.set_title("Distribuição Poisson: Matrículas por Escola", fontsize=16, fontweight='bold')
    ax.set_xlabel("Quantidade de Matrículas", fontsize=12)
    ax.set_ylabel("Probabilidade", fontsize=12)
    ax.grid(axis='y', linestyle='--', linewidth=0.5, color='lightgray')
    st.pyplot(fig)

    # Explicação textual
    st.write(f"""
    **Média de Matrículas por Escola:** {media_matriculas:.2f}

    Este gráfico apresenta a distribuição Poisson modelando o número de matrículas por escola.
    A distribuição é baseada na média calculada e mostra a probabilidade de diferentes 
    quantidades de matrículas ocorrerem.
    """)
else:
    st.warning("A coluna 'QT_MAT_BAS' não está disponível no conjunto de dados.")
    
    st.subheader("Distribuição Normal: Matrículas por Região")

    if {'QT_MAT_BAS', 'NO_REGIAO'}.issubset(df.columns):
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

        st.write(f"**Média:** {media:.2f} | **Desvio Padrão:** {desvio_padrao:.2f}")
        st.write("""
        A curva mostra que a maior concentração de matrículas está perto da média, com variações nas regiões extremas.
        """)
        st.subheader("Distribuição Binomial: Presença de Banheiros")

    if 'IN_BANHEIRO' in df.columns:
        sucesso = df['IN_BANHEIRO'].value_counts().get(1, 0)
        total = len(df['IN_BANHEIRO'])
        probabilidade = sucesso / total

        n = 10  # Número de ensaios
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
        """)





