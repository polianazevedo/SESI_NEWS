import streamlit as st
from PIL import Image

# Definindo o CSS remover funções de adm
customizando_site = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

# Aplicando o CSS
st.markdown(customizando_site, unsafe_allow_html=True)

# Título
st.header("Bem vindo(a) ao :orange[Sesi]/:blue[Senai] News!", divider="orange")

# Guias de navegação e definição de tabelas

tab1, tab2, tab3, tab4 = st.tabs(["Olímpiadas", "RecuperArt", "Eventos", "Interclasse"])

# Tabela 1

with tab1:
    st.caption("Provas ou atividades que medem o seu entendimento em cada área. Ao final do processo, você pode ganhar medalhas ou certificados, dependendo da quantidade de pontos conquistados.")

# Colunas da tabela

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("ONHB")
        st.image("IMAGES.SITE/ONHB.png")
        st.caption("É uma olimpíada realizada em trio, que explora diversas áreas da ciência humana e linguagens, fazendo com que o conhecimento dos competidores seja explorado e enriquecido.")



    with col2:
        st.subheader("OBMEP")
        st.image("IMAGES.SITE/OBMEP.png")
        st.caption("Olimpíada de matemática composta por duas fases. A primeira, objetiva e a segunda, discursiva. Ao final da olimpíada, você pode conquistar medalhas ou certificados.")


    with col3:
        st.subheader("OP")
        st.image("IMAGES.SITE/OP.png")
        st.caption("Essa olímpiada explora nossos conhecimentos a respeito da norma culta da língua portuguesa, observando sua interpretação de texto e seus conhecimentos básicos.")

    with col4:
        st.subheader("CANGURU")
        st.image("IMAGES.SITE/CANGURU.png")
        st.caption("Olimpíada de matemática composta por duas fases. A primeira, objetiva e a segunda, discursiva. Ao final da olimpíada, você pode conquistar medalhas ou certificados.")

# Tabela 2

with tab2:

    st.caption('Na semana de recuperação, a escola propõe atividades diversificadas, para que os alunos possam explorar a si mesmo, e se descobrir na arte, além de se divertirem.')

# Colunas da tabela

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)

    with col1:
        st.subheader("KRAV MAGA")
        st.image("IMAGES.SITE/MUAY THAI.png")

    with col2:
      st.subheader("MUAY THAI")
      st.image("IMAGES.SITE/KRAV MAGA.png")

    with col3:
      st.subheader("DESENHO")
      st.image("IMAGES.SITE/DESENHO.jpg")

    with col4:
       st.subheader("FUTEBOL")
       st.image("IMAGES.SITE/FUT.png")

    with col5:
        st.subheader("VÔLEI")
        st.image("IMAGES.SITE/VOLEI.png")

    with col6:
        st.subheader("HANDEBOL")
        st.image("IMAGES.SITE/HAND.png")

    with col7:
        st.subheader("XADREZ")
        st.image("IMAGES.SITE/XADREZ.png")

    with col8:
        st.subheader("TEATRO")
        st.image("IMAGES.SITE/TEATRO.png")

    with col9:
        st.subheader("MÚSICA")
        st.image("IMAGES.SITE/MUSICA.png")

# Tabela 3

with tab3:
    col1, col2, col3 = st.columns(3)

# Colunas da tabela
    with col1:
        st.subheader("Workshop SENAI")
        st.image("IMAGES.SITE/WORKSHOP.png")
        st.caption("O Workshop é uma feira onde mostramos nosso trabalho desenvolvido no SENAI. Com muito estudo e esforço, os alunos apresentam em formato de pitch seus conhecimentos adquiridos na sala.")

    with col2:
        st.subheader("Matematicando")
        st.image("IMAGES.SITE/MATEMATICANDO.png")
        st.caption('Feira onde foi exposto trabalhos dos intinerários de matemática, não só jogos de raciocínio lógico, mas também palestras sobre diversos assuntos.')

    with col3:
        st.subheader("Feira SENAI")
        st.image("IMAGES.SITE/FEIRA SENAI.png")
        st.caption("A feira das  profissões foi um evento onde os alunos falaram sobre a área que estudam, carreira de trabalho e salário. E explicaram sobre a profissão que estão se formando e divulgando para os que não conhecem ainda.")

# Tabela 4

with tab4:

    st.caption('O momento mais esperado do ano, muita diversão, descontração e conquistas de pódios em jogos realizados e disputados com turmas da manhã e da tarde.')
    st.markdown("<h1 style='text-align: center; color: Grey;'>EM BREVE...</h1>", unsafe_allow_html=True)
    st.image("IMAGES.SITE/INTERCLASSE.jpg")