# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

  # ----- Parcelas Costa Rica ---- #

def Parcelas_Costa_Rica(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_10= st.sidebar.empty()
  titulo= placeholder1_10.title("Menú")

  placeholder2_10 = st.sidebar.empty()
  procesos_10 = placeholder2_10.button("Procesos",key="procesos_10")

  placeholder3_10 = st.sidebar.empty()
  historial_10 = placeholder3_10.button("Historial",key="historial_10")

  placeholder4_10 = st.sidebar.empty()
  capacitacion_10 = placeholder4_10.button("Capacitaciones",key="capacitacion_10")

  placeholder5_10 = st.sidebar.empty()
  otros_registros_10 = placeholder5_10.button("Otros Registros",key="otros_registros_10")

  placeholder6_10 = st.sidebar.empty()
  bonos_10 = placeholder6_10.button("Bonos",key="bonos_10")

  placeholder7_10 = st.sidebar.empty()
  salir_10 = placeholder7_10.button("Salir",key="salir_10")

  placeholder8_10 = st.empty()
  parcelas_10 = placeholder8_10.title("Parcelas")

  default_date_10 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_10= st.empty()
  fecha_inicio_10= placeholder9_10.date_input("Fecha de Inicio",value=default_date_10,key="fecha_inicio_10")

  placeholder10_10= st.empty()
  fecha_finalizacion_10= placeholder10_10.date_input("Fecha de Finalización",value=default_date_10,key="fecha_finalizacion_10")

  placeholder11_10= st.empty()
  zona_10= placeholder11_10.selectbox("Zona", options=("Beltran","El Salto","Gral Alvear","Junin","La Colonia Alvear","La Consulta","La Dormida","Las Catitas","Las Vegas","Malargue","Rivadavia","Rodeo Fray","San Carlos","San Martin","San Rafael","Tulumaya","Tunuyan","Tupungato",), key="zona_10")
       
  placeholder12_10= st.empty()
  bloques_10= placeholder12_10.number_input("Cantidad de Bloques Finalizados",min_value=1,step=1,key="bloques_10")

  placeholder13_10= st.empty()
  horas_10= placeholder13_10.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_10")

  placeholder14_10 = st.empty()
  reporte_10 = placeholder14_10.button("Generar Reporte",key="reporte_10")

  # ----- Procesos ---- #
    
  if procesos_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Procesos=False
    st.session_state.Parcelas_Costa_Rica=False             
    Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)
              
  #----- Historial ---- #
    
  elif historial_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Parcelas_Costa_Rica=False
    st.session_state.Historial_Costa_Rica=True
    Historial.Historial_Costa_Rica(usuario,puesto,perfil)   

  # ----- Capacitación ---- #
    
  elif capacitacion_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Parcelas_Costa_Rica=False
    st.session_state.Capacitacion_Costa_Rica=True
    Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

  # ----- Otros Registros ---- #
    
  elif otros_registros_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Parcelas_Costa_Rica=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto,perfil)

  # ----- Bonos ---- #
    
  elif bonos_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Parcelas_Costa_Rica=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto,perfil)    

  # ----- Salir ---- #
    
  elif salir_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    st.session_state.Parcelas_Costa_Rica=False
    st.session_state.Conformacion=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_10:

    cursor01=con.cursor()

    marca_10=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_10= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_10 = nombre_10.loc[0,'nombre']

    supervisor_10= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_10 = supervisor_10.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,bloques_o_parcelas,cubiertas_y_mejoras,horas)VALUES('{marca_10}','{usuario}','{nombre_10}','{perfil}','{puesto}','{supervisor_10}','Parcelas','{fecha_inicio_10}','{fecha_finalizacion_10}','{zona_10}','{bloques_10}','0','{horas_10}')")
    con.commit()
    st.success('Reporte enviado correctamente')

  # ----- Parcelas Argentina ---- #

def Parcelas_Argentina(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_10= st.sidebar.empty()
  titulo= placeholder1_10.title("Menú")

  placeholder2_10 = st.sidebar.empty()
  procesos_10 = placeholder2_10.button("Procesos",key="procesos_10")

  placeholder3_10 = st.sidebar.empty()
  historial_10 = placeholder3_10.button("Historial",key="historial_10")

  placeholder4_10 = st.sidebar.empty()
  capacitacion_10 = placeholder4_10.button("Capacitaciones",key="capacitacion_10")

  placeholder5_10 = st.sidebar.empty()
  salir_10 = placeholder5_10.button("Salir",key="salir_10")

  placeholder6_10 = st.empty()
  parcelas_10 = placeholder6_10.title("Parcelas")

  default_date_10 = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))

  placeholder7_10= st.empty()
  fecha_inicio_10= placeholder7_10.date_input("Fecha de Inicio",value=default_date_10,key="fecha_inicio_10")

  placeholder8_10= st.empty()
  fecha_finalizacion_10= placeholder8_10.date_input("Fecha de Finalización",value=default_date_10,key="fecha_finalizacion_10")

  placeholder9_10= st.empty()
  zona_10= placeholder9_10.selectbox("Zona", options=("Beltran","El Salto","Gral Alvear","Junin","La Colonia Alvear","La Consulta","La Dormida","Las Catitas","Las Vegas","Malargue","Rivadavia","Rodeo Fray","San Carlos","San Martin","San Rafael","Tulumaya","Tunuyan","Tupungato",), key="zona_10")
       
  placeholder10_10= st.empty()
  bloques_10= placeholder10_10.number_input("Cantidad de Bloques Finalizados",min_value=1,step=1,key="predios_10")

  placeholder11_10= st.empty()
  horas_10= placeholder11_10.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_10")

  placeholder12_10 = st.empty()
  reporte_10 = placeholder12_10.button("Generar Reporte",key="reporte_10")

  # ----- Procesos ---- #
    
  if procesos_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    st.session_state.Procesos=False
    st.session_state.Parcelas_Argentina=False            
    Procesos.Procesos_Argentina(usuario,puesto,perfil)   
  
  #----- Historial ---- #
    
  elif historial_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    st.session_state.Parcelas_Argentina=False
    st.session_state.Historial_Argentina=True
    Historial.Historial_Argentina(usuario,puesto,perfil)   

  # ----- Capacitación ---- #
    
  elif capacitacion_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    st.session_state.Parcelas_Argentina=False
    st.session_state.Capacitacion_Argentina=True
    Capacitacion.Capacitacion_Argentina(usuario,puesto,perfil)

  # ----- Salir ---- #
    
  elif salir_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    st.session_state.Ingreso = False
    st.session_state.Parcelas_Argentina=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_10:

    cursor01=con.cursor()

    marca_10=datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_10= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_10 = nombre_10.loc[0,'nombre']

    supervisor_10= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_10 = supervisor_10.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,bloques_o_parcelas,cubiertas_y_mejoras,horas)VALUES('{marca_10}','{usuario}','{nombre_10}','{perfil}','{puesto}','{supervisor_10}','Parcelas','{fecha_inicio_10}','{fecha_finalizacion_10}','{zona_10}','{bloques_10}','0','{horas_10}')")
    con.commit()
    st.success('Reporte enviado correctamente')