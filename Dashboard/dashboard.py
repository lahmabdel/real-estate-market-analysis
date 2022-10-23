import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.colors as colors
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
page = st.selectbox("Choose your page", ["Page 1", "Page 2"])

if page == "Page 1":

    df1=pd.read_csv('vol_trans.csv',sep=';')
    df=pd.read_csv('nombre_trans.csv',sep=';')

   

    nom_com = st.sidebar.multiselect(
            "Selectionner le nom de la commune:",
            options=df["nom_commune"].unique()
    )

    df_selection = df.query(
            ''' nom_commune == @nom_com '''
         )
    df_selection1 = df1.query(
            ''' nom_commune == @nom_com '''
         )
    
   # df_selection['date']=[str(df_selection.iloc[i]['year_mutation'])+' - '+str(df_selection.iloc[i]['mois_mutation']) for i in range(len(df_selection))]
    
    ##
    st.title('nombre transaction')
    fig=px.bar(df_selection,  x='mois_mutation', y='valeur_fonciere',color='nom_commune')
    st.plotly_chart(fig, use_container_width=True)
    
    ###
    st.title('volume transaction')
    
    fig=px.line(df_selection1,  x='mois_mutation', y='valeur_fonciere',color='nom_commune', symbol="nom_commune")
    st.plotly_chart(fig, use_container_width=True)
   


########
    st.title('croissance volume transaction')
    
    fig=px.line(df_selection1,  x='mois_mutation', y='croissance',color='nom_commune', symbol="nom_commune")
    st.plotly_chart(fig, use_container_width=True)
   





    # Display details of page 1
elif page == "Page 2":
    choice = st.selectbox("Choose a type", ["maison", "appart"])
    if choice=="maison":
        
        df2 = pd.read_csv('avg_maison.csv', sep=',')
        
        nom_com = st.sidebar.multiselect(
            "Selectionner le nom de la commune:",
            options=df2["nom_commune"].unique()
        )
    
        df_selection2 = df2.query(
            '''nom_commune == @nom_com '''
        )
       
        st.title('avg_maison')
        
        fig=px.line(df_selection2,  x='mois_mutation', y='valeur_m2',color='nom_commune', symbol="nom_commune")
        
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.title('croissance avg_maison')
        fig=px.line(df_selection2,  x='mois_mutation', y='croissance',color='nom_commune', symbol="nom_commune")
        st.plotly_chart(fig, use_container_width=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    elif choice=="appart":
        
        
        df3 = pd.read_csv('avg_apprt.csv', sep=',')
        
        nom_com = st.sidebar.multiselect(
            "Selectionner le nom de la commune:",
            options=df3["nom_commune"].unique()
        )
        df_selection3 = df3.query(
            ''' nom_commune == @nom_com '''
        )
        st.title(' avg_apprt')
       
        fig=px.line(df_selection3,  x='mois_mutation', y='valeur_m2',color='nom_commune', symbol="nom_commune")
        st.plotly_chart(fig, use_container_width=True)
        
      
        
        st.title('croissance avg_apprt')
        
        
        fig=px.line(df_selection3,  x='mois_mutation', y='croissance',color='nom_commune', symbol="nom_commune")
        st.plotly_chart(fig, use_container_width=True)
       
      
        
        
        
