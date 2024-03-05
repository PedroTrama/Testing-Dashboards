import streamlit as st
from dataset import df

st.title('Dataset de Vendas')
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Seleciona as Colunas',
        list(df.columns),
        list(df.columns)
    )

st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )
    
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
        0, 5000,
        (0, 5000)
        )
    
with st.sidebar.expander('Data da Compra'):
   data_compra = st.date_input(
       'Selecione a Data',
       (df['Data da Compra'].min(),
       df['Data da Compra'].max())
       
   )

st.dataframe(df)