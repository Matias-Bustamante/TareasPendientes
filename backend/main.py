import streamlit as st 
from extract import Extract 
from transform import Transform
from consulta import Consulta
from streamlit_option_menu import option_menu
from streamlit_kpi import streamlit_kpi
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
    st.empty()
   
    with col1: 
        streamlit_kpi(height="70",title="Tareas Completadas", value=str(TareasTerminadas), icon="fa-solid fa-check", 
                      textAlign="center", backgroundColor="white", iconColor="green")
    st.title("Tareas Pendientes", anchor=False)
    config= { 
        'FechaInicio':st.column_config.DateColumn('FechaInicio', format="DD/MM/YYYY"),
        'FechaTerminado':st.column_config.DateColumn('FechaTerminado', format="DD/MM/YYYY"), 
        'Asignacion':st.column_config.DateColumn('Asignacion', format="DD/MM/YYYY")
    }

    listaColumnas=["Modelo", "Tareas", "Responsable", "Asignacion", "FechaInicio","FechaTerminado","Observaciones", "Estado", "Proyecto"]

    option=st.selectbox("Estado:", 
                        dataEstado, placeholder="Seleccione un Estado", index=None)
    data=consulta.FiltroPorEstado(data,option)
    st.data_editor(data,column_config=config, hide_index=True, use_container_width=True, column_order=listaColumnas, 
                num_rows="dynamic")




