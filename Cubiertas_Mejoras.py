# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

# ----- Cubiertas y Mejoras Costa Rica ---- #

def Cubiertas_Mejoras_Costa_Rica(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_11= st.sidebar.empty()
  titulo= placeholder1_11.title("Menú")

  placeholder2_11 = st.sidebar.empty()
  procesos_11 = placeholder2_11.button("Procesos",key="procesos_11")

  placeholder3_11 = st.sidebar.empty()
  historial_11 = placeholder3_11.button("Historial",key="historial_11")

  placeholder4_11 = st.sidebar.empty()
  capacitacion_11 = placeholder4_11.button("Capacitaciones",key="capacitacion_11")

  placeholder5_11 = st.sidebar.empty()
  otros_registros_11 = placeholder5_11.button("Otros Registros",key="otros_registros_11")

  placeholder6_11 = st.sidebar.empty()
  bonos_11 = placeholder6_11.button("Bonos",key="bonos_11")

  placeholder7_11 = st.sidebar.empty()
  salir_11 = placeholder7_11.button("Salir",key="salir_11")

  placeholder8_11 = st.empty()
  cubiertas_mejoras_11 = placeholder8_11.title("Cubiertas y Mejoras")

  default_date_11 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_11= st.empty()
  fecha_inicio_11= placeholder9_11.date_input("Fecha de Inicio",value=default_date_11,key="fecha_inicio_11")

  placeholder10_11= st.empty()
  fecha_finalizacion_11= placeholder10_11.date_input("Fecha de Finalización",value=default_date_11,key="fecha_finalizacion_11")

  placeholder11_11= st.empty()
  zona_11= placeholder11_11.selectbox("Zona o Subpolígono", options=("Beltran","Col Alvear"," Salto","Gral. Alvear 1","Gral. Alvear 2","La Colonia","La Consulta","La Dormida","La Paz","Las Catitas","Las Vegas","Lavalle (Va. Tulumaya)","Malargue 1","Malargue 2","Malargue 3","Poligono 1 - Las Heras","Poligono 2 - Las Heras","Poligono 3 - Las Heras","Poligono 4 - Las Heras/Capital","Poligono 5 - Las Heras/Capital","Poligono 6 - Las Heras/Capital","Poligono 7 – Capital","Poligono 8 – Capital","Poligono 9 - Godoy Cruz","Poligono 10 - Godoy Cruz","Poligono 11 - Godoy Cruz/Guaymallen","Poligono 12 - Godoy Cruz","Poligono 13 - Las Heras","Poligono 14 – Guaymallen","Poligono 15 – Guaymallen","Poligono 16 – Guaymallen","Poligono 17 – Guaymallen","Poligono 18 – Guaymallen","Poligono 19 – Maipu","Poligono 20 – Maipu","Poligono 21 – Maipu","Poligono 22 - Lujan de Cuyo","Poligono 23 - Lujan de Cuyo","Poligono 24 - Lujan de Cuyo","Poligono 25 – Maipu","Poligono 26 - Lujan de Cuyo","Poligono 27 – Maipu","Rivadavia","Rodeo Fray","San Carlos","San Martin 1","San Martin 2","San Martin 3","San Martin 4","San Rafael 1","San Rafael 2","San Rafael 3","San Rafael 4","San Rafael 5","San Rafael 6","Tunuyan","Tupungato"), key="zona_10")

  placeholder12_11= st.empty()
  parcelas_11= placeholder12_11.number_input("Cantidad de Parcelas Finalizadas",min_value=1,step=1,key="parcelas_11")

  placeholder13_11= st.empty()
  cubiertas_11= placeholder13_11.number_input("Cantidad de Cubiertas y Mejoras Finalizadas",min_value=1,step=1,key="cubiertas_11")

  placeholder14_11= st.empty()
  horas_11= placeholder14_11.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_11")

  placeholder15_11 = st.empty()
  reporte_11 = placeholder15_11.button("Generar Reporte",key="reporte_11")

  # ----- Procesos ---- #
    
  if procesos_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Procesos=False
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False          
    Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)

  #----- Historial ---- #
    
  elif historial_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False
    st.session_state.Historial_Costa_Rica=True
    Historial.Historial_Costa_Rica(usuario,puesto,perfil)   

  # ----- Capacitación ---- #
    
  elif capacitacion_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False
    st.session_state.Capacitacion_Costa_Rica=True
    Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

  # ----- Otros Registros ---- #
    
  elif otros_registros_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto,perfil)

  # ----- Bonos ---- #
    
  elif bonos_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto,perfil)    

  # ----- Salir ---- #
    
  elif salir_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    placeholder15_11.empty()
    st.session_state.Ingreso=False
    st.session_state.Cubiertas_Mejoras_Costa_Rica=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_11:

    cursor01=con.cursor()

    marca_11=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_11= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_11 = nombre_11.loc[0,'nombre']

    supervisor_11= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_11 = supervisor_11.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,bloques_o_parcelas,parcelas_o_cubiertas_y_mejoras,horas)VALUES('{marca_11}','{usuario}','{nombre_11}','{perfil}','{puesto}','{supervisor_11}','Cubiertas y Mejoras','{fecha_inicio_11}','{fecha_finalizacion_11}','{zona_11}','{parcelas_11}','{cubiertas_11}','{horas_11}')")
    con.commit()
    st.success('Reporte enviado correctamente')

# ----- Cubiertas y Mejoras Argentina ---- #
  
def Cubiertas_Mejoras_Argentina(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_11= st.sidebar.empty()
  titulo= placeholder1_11.title("Menú")

  placeholder2_11 = st.sidebar.empty()
  procesos_11 = placeholder2_11.button("Procesos",key="procesos_11")

  placeholder3_11 = st.sidebar.empty()
  historial_11 = placeholder3_11.button("Historial",key="historial_11")

  placeholder4_11 = st.sidebar.empty()
  capacitacion_11 = placeholder4_11.button("Capacitaciones",key="capacitacion_11")

  placeholder5_11 = st.sidebar.empty()
  salir_11 = placeholder5_11.button("Salir",key="salir_11")

  placeholder6_11 = st.empty()
  cubiertas_mejoras_11 = placeholder6_11.title("Cubiertas y Mejoras")

  default_date_11 = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))

  placeholder7_11= st.empty()
  fecha_inicio_11= placeholder7_11.date_input("Fecha de Inicio",value=default_date_11,key="fecha_inicio_11")

  placeholder8_11= st.empty()
  fecha_finalizacion_11= placeholder8_11.date_input("Fecha de Finalización",value=default_date_11,key="fecha_finalizacion_11")

  placeholder9_11= st.empty()
  zona_11= placeholder9_11.selectbox("Zona o Subpolígono", options=("Beltran","Col Alvear"," Salto","Gral. Alvear 1","Gral. Alvear 2","La Colonia","La Consulta","La Dormida","La Paz","Las Catitas","Las Vegas","Lavalle (Va. Tulumaya)","Malargue 1","Malargue 2","Malargue 3","Poligono 1 - Las Heras","Poligono 2 - Las Heras","Poligono 3 - Las Heras","Poligono 4 - Las Heras/Capital","Poligono 5 - Las Heras/Capital","Poligono 6 - Las Heras/Capital","Poligono 7 – Capital","Poligono 8 – Capital","Poligono 9 - Godoy Cruz","Poligono 10 - Godoy Cruz","Poligono 11 - Godoy Cruz/Guaymallen","Poligono 12 - Godoy Cruz","Poligono 13 - Las Heras","Poligono 14 – Guaymallen","Poligono 15 – Guaymallen","Poligono 16 – Guaymallen","Poligono 17 – Guaymallen","Poligono 18 – Guaymallen","Poligono 19 – Maipu","Poligono 20 – Maipu","Poligono 21 – Maipu","Poligono 22 - Lujan de Cuyo","Poligono 23 - Lujan de Cuyo","Poligono 24 - Lujan de Cuyo","Poligono 25 – Maipu","Poligono 26 - Lujan de Cuyo","Poligono 27 – Maipu","Rivadavia","Rodeo Fray","San Carlos","San Martin 1","San Martin 2","San Martin 3","San Martin 4","San Rafael A","San Rafael B","San Rafael C","San Rafael D","San Rafael E","San Rafael F","Tunuyan","Tupungato"), key="zona_10")

  placeholder10_11= st.empty()
  parcelas_11= placeholder10_11.number_input("Cantidad de Parcelas Finalizadas",min_value=1,step=1,key="parcelas_11")

  placeholder11_11= st.empty()
  cubiertas_11= placeholder11_11.number_input("Cantidad de Cubiertas y Mejoras Finalizadas",min_value=1,step=1,key="cubiertas_11")

  placeholder12_11= st.empty()
  horas_11= placeholder12_11.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_11")

  placeholder13_11 = st.empty()
  reporte_11 = placeholder13_11.button("Generar Reporte",key="reporte_11")

  # ----- Procesos ---- #
    
  if procesos_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    st.session_state.Procesos=False
    st.session_state.Cubiertas_Mejoras_Argentina=False            
    Procesos.Procesos_Argentina(usuario,puesto,perfil)   
  
  #----- Historial ---- #
    
  elif historial_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    st.session_state.Cubiertas_Mejoras_Argentina=False
    st.session_state.Historial_Argentina=True
    Historial.Historial_Argentina(usuario,puesto,perfil)   

  # ----- Capacitación ---- #
    
  elif capacitacion_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    st.session_state.Cubiertas_Mejoras_Argentina=False
    st.session_state.Capacitacion_Argentina=True
    Capacitacion.Capacitacion_Argentina(usuario,puesto,perfil)

  # ----- Salir ---- #
    
  elif salir_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    st.session_state.Ingreso=False
    st.session_state.Cubiertas_Mejoras_Argentina=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_11:

    cursor01=con.cursor()

    marca_11=datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_11= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_11 = nombre_11.loc[0,'nombre']
      
    supervisor_11= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_11 = supervisor_11.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,bloques_o_parcelas,parcelas_o_cubiertas_y_mejoras,horas)VALUES('{marca_11}','{usuario}','{nombre_11}','{perfil}','{puesto}','{supervisor_11}','Cubiertas y Mejoras','{fecha_inicio_11}','{fecha_finalizacion_11}','{zona_11}','{parcelas_11}','{cubiertas_11}','{horas_11}')")
    con.commit()
    st.success('Reporte enviado correctamente')
