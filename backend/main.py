import streamlit as st 
from extract import Extract 
from transform import Transform
from consulta import Consulta
from streamlit_option_menu import option_menu
from streamlit_kpi import streamlit_kpi
from st_aggrid import AgGrid,GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_elements import html, mui, elements
from streamlit_extras.metric_cards import style_metric_cards 
import streamlit.components.v1 as components
import pandas as pd 
import time 

        

extract=Extract(); 
data=extract.extract_data(); 
transform=Transform(); 
consulta=Consulta()
data=transform.transform_json_dataFrame(data); 
data=transform.eliminarPrimerFila(data)
data=transform.transformFechas(data); 
data=transform.eliminarFechas(data); 
data=transform.cambiarFormatoFechas(data) 
dataEstado=transform.ObtenerEstado(data)
TareasTerminadas=consulta.CantidadTareasCompletadas(data); 


menu=option_menu( 
        menu_title=None, 
        options=["Tareas", "Dashboard"], 
        icons=["table","file-earmark-bar-graph"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal", 
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
    )
col1,col2=st.columns(2)
if menu=="Tareas": 
   
    with col1: 
        
        st.metric("Tareas completadas", value=TareasTerminadas)
        style_metric_cards(border_left_color="yellow", box_shadow=True, border_radius_px=10)
    with elements("new_element"): 
       mui.Typography("Listas de Tareas",variant="h3", mt={4}, Type="left", fontSize="3rem", color="blue")
    
    config= { 
        'FechaInicio':st.column_config.DateColumn('FechaInicio', format="DD/MM/YYYY"),
        'FechaTerminado':st.column_config.DateColumn('FechaTerminado', format="DD/MM/YYYY"), 
        'Asignacion':st.column_config.DateColumn('Asignacion', format="DD/MM/YYYY")
    }

    listaColumnas=["Modelo", "Tareas", "Responsable", "Asignacion", "FechaInicio","FechaTerminado","Observaciones", "Estado", "Proyecto"]

    option=st.selectbox("Estado:", 
                        dataEstado, placeholder="Seleccione un Estado", index=None)
    data=consulta.FiltroPorEstado(data,option)

    gd=GridOptionsBuilder.from_dataframe(data)
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False,paginationPageSize=10)
    gd.configure_default_column(editable=False,groupable=True)
    go=gd.build()
    AgGrid(data, gridOptions=go, update_mode=GridUpdateMode.VALUE_CHANGED | GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.FILTERING_CHANGED,
           theme='material'
           )
    
    
if menu=='Dashboard': 
    
    st.markdown("""
    <iframe  src="https://lookerstudio.google.com/embed/reporting/033203f2-3241-4f80-9458-3de74dbc8364/page/TQgdD" frameborder="0" seamless="seamless"  style="position:absolute;top:0px;left:0px;bottom:0px;right:0px;width:100vw;height:100vh; border:none;margin:0;padding:0;overflow:hidden;z-index:999999;" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    




