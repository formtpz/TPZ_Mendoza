# ----- Librerías ---- #
import numpy as np
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
import plotly.graph_objects as go
import plotly.express as px
from urllib.parse import urlparse
uri=st.secrets.db_credentials.URI
import Procesos,Capacitacion,Otros_Registros,Bonos,Salir

def Historial_Costa_Rica(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_7= st.sidebar.empty()
  titulo= placeholder1_7.title("Menú")

  placeholder2_7 = st.sidebar.empty()
  procesos_7 = placeholder2_7.button("Procesos",key="procesos_7")

  placeholder3_7 = st.sidebar.empty()
  capacitacion_7 = placeholder3_7.button("Capacitaciones",key="capacitacion_7")

  placeholder4_7 = st.sidebar.empty()
  otros_registros_7 = placeholder4_7.button("Otros Registros",key="otros_registros_7")

  placeholder5_7 = st.sidebar.empty()
  bonos_7 = placeholder5_7.button("Bonos",key="bonos_7")

  placeholder6_7 = st.sidebar.empty()
  salir_7 = placeholder6_7.button("Salir",key="salir_7")

  placeholder7_7 = st.empty()
  historial_7 = placeholder7_7.title("Historial")

  default_date_7 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder8_7 = st.empty()
  fecha_referencia_1_7 = placeholder8_7.date_input("Fecha de Referencia 1",value=default_date_7,key="fecha_de_referencia_1_7")

  placeholder9_7 = st.empty()
  fecha_referencia_2_7 = placeholder9_7.date_input("Fecha de Referencia 2",value=default_date_7,key="fecha_de_referencia_2_7")
  
  nombre_7= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
  nombre_7 = nombre_7.loc[0,'nombre']

  # ----- Supervisor y Coordinador ---- #

  if puesto=="Supervisor" or puesto=="Coordinador":    

    placeholder10_7 = st.empty()
    personal_7 = placeholder10_7.selectbox("Personal", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder11_7 = st.empty()
    proceso_7_s = placeholder11_7.selectbox("Proceso", options=("Todos","Parcelas","Cubiertas y Mejoras"), key="proceso_7_s")
    
    placeholder12_7 = st.empty()
    perfil_7_s = placeholder12_7.selectbox("Perfil", options=("Todos","Costa Rica","Argentina"), key="perfil_7_s")

    if personal_7=="Todos" and proceso_7_s=="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' ", con)

    elif personal_7=="Todos" and proceso_7_s=="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and perfil='{perfil_7_s}' ", con)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and proceso='{proceso_7_s}' ", con)
  
    elif personal_7=="Todos" and proceso_7_s !="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}' ", con)
  
    elif personal_7=="Operarios" and proceso_7_s =="Todos" and perfil_7_s=="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral'", con)
 
    elif personal_7=="Operarios" and proceso_7_s =="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and perfil='{perfil_7_s}' ", con)
 
    elif personal_7=="Operarios" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and proceso='{proceso_7_s}' ", con)
 
    elif personal_7=="Operarios" and proceso_7_s !="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}' ", con)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}'", con)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and perfil='{perfil_7_s}'", con)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and proceso='{proceso_7_s}'", con)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and proceso='{proceso_7_s}' perfil='{perfil_7_s}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and perfil='{perfil_7_s}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
      
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and proceso='{proceso_7_s}'", con)
      
    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}'", con)
           
    # ----- Reportes ---- #

    placeholder13_7 = st.empty()
    reportes_7=placeholder13_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder14_7 = st.empty()
      error_reportes= placeholder14_7.error('No existen reportes para mostrar')

    else:

      placeholder15_7 = st.empty()
      historial_7_reportes=placeholder15_7.dataframe(data=data_1_r)

      placeholder16_7 = st.empty()
      descarga_7_reportes = placeholder16_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Producción ---- #

    placeholder17_7 = st.empty()
    producción_7=placeholder17_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha_finalizacion","proceso"], as_index=False)[["bloques_o_parcelas","cubiertas_y_mejoras","horas"]].agg(np.sum)

    pivot_r=len(data_2_r.iloc[:,0])

    if pivot_r==0:  

      placeholder18_7 = st.empty()
      error_producción= placeholder18_7.error('No existe producción para mostrar')

    else:
         
      placeholder19_7 = st.empty()
      historial_7_producción= placeholder19_7.dataframe(data=data_2_r)

      placeholder20_7 = st.empty()
      descarga_7_producción = placeholder20_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
          
    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha_finalizacion","proceso"], as_index=False)["bloques_o_parcelas"].agg(np.sum)

    placeholder21_7 = st.empty()
    total_7=placeholder21_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder22_7 = st.empty()
      error_total_producción= placeholder22_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha_finalizacion", y="bloques o parcelas", text="bloques o parcelas", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder23_7 = st.empty()
      grafico_producción_total= placeholder23_7.plotly_chart(fig_producción_total)

  # ----- Operario Catastral ---- #

  elif puesto=="Operario Catastral":

    placeholder24_7 = st.empty()
    proceso_7_o = placeholder24_7.selectbox("Proceso", options=("Todos","Parcelas ","Cubiertas y Mejoras"), key="proceso_7_s")
    
    if proceso_7_o =="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}'", con)

    elif proceso_7_o !="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and usuario='{proceso_7_o}'", con)

    # ----- Reportes ---- #

    placeholder25_7 = st.empty()
    reportes_7=placeholder25_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder26_7 = st.empty()
      error_reportes= placeholder26_7.error('No existen reportes para mostrar')

    else:

      placeholder27_7 = st.empty()
      historial_7_reportes=placeholder27_7.dataframe(data=data_1_r)

      placeholder28_7 = st.empty()
      descarga_7_reportes = placeholder28_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Producción ---- #

    placeholder29_7 = st.empty()
    producción_7=placeholder29_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha_finalizacion","proceso"], as_index=False)[["bloques_o_parcelas","cubiertas_y_mejoras","horas"]].agg(np.sum)

    pivot_r=len(data_2_r.iloc[:,0])

    if pivot_r==0:  

      placeholder30_7 = st.empty()
      error_producción= placeholder30_7.error('No existe producción para mostrar')

    else:
         
      placeholder31_7 = st.empty()
      historial_7_producción= placeholder31_7.dataframe(data=data_2_r)

      placeholder32_7 = st.empty()
      descarga_7_producción = placeholder32_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
  
    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha_finalizacion","proceso"], as_index=False)["bloques_o_parcelas"].agg(np.sum)

    placeholder33_7 = st.empty()
    total_7=placeholder33_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder34_7 = st.empty()
      error_total_producción= placeholder34_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha_finalizacion", y="bloques_o_parcelas", text="bloques_o_parcelas", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder35_7 = st.empty()
      grafico_producción_total= placeholder35_7.plotly_chart(fig_producción_total)

  # ----- Proceso ---- #
  
  if procesos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Procesos=False
    st.session_state.Historial_Costa_Rica=False             
    Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)
                
  # ----- Capacitación ---- #
    
  elif capacitacion_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Historial_Costa_Rica=False
    st.session_state.Capacitacion_Costa_Rica=True
    Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

  # ----- Otros Registros ---- #
    
  elif otros_registros_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Historial_Costa_Rica=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto,perfil)

  # ----- Bonos ---- #
    
  elif bonos_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Historial_Costa_Rica=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto,perfil)
   
  # ----- Salir ---- #
    
  elif salir_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Ingreso = False
    st.session_state.Historial_Costa_Rica=False
    st.session_state.Salir=True
    Salir.Salir()

def Historial_Argentina(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_7= st.sidebar.empty()
  titulo= placeholder1_7.title("Menú")

  placeholder2_7 = st.sidebar.empty()
  procesos_7 = placeholder2_7.button("Procesos",key="procesos_7")

  placeholder3_7 = st.sidebar.empty()
  capacitacion_7 = placeholder3_7.button("Capacitaciones",key="capacitacion_7")

  placeholder6_7 = st.sidebar.empty()
  salir_7 = placeholder6_7.button("Salir",key="salir_7")

  placeholder7_7 = st.empty()
  historial_7 = placeholder7_7.title("Historial")

  default_date_7 = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))

  placeholder8_7 = st.empty()
  fecha_referencia_1_7 = placeholder8_7.date_input("Fecha de Referencia 1",value=default_date_7,key="fecha_de_referencia_1_7")

  placeholder9_7 = st.empty()
  fecha_referencia_2_7 = placeholder9_7.date_input("Fecha de Referencia 2",value=default_date_7,key="fecha_de_referencia_2_7")
  
  nombre_7= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
  nombre_7 = nombre_7.loc[0,'nombre']

  # ----- Supervisor y Coordinador ---- #

  if puesto=="Supervisor" or puesto=="Coordinador":    

    placeholder10_7 = st.empty()
    personal_7 = placeholder10_7.selectbox("Personal", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder11_7 = st.empty()
    proceso_7_s = placeholder11_7.selectbox("Proceso", options=("Todos","Parcelas","Cubiertas y Mejoras"), key="proceso_7_s")
    
    placeholder12_7 = st.empty()
    perfil_7_s = placeholder12_7.selectbox("Perfil", options=("Todos","Costa Rica","Argentina"), key="perfil_7_s")

    if personal_7=="Todos" and proceso_7_s=="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' ", con)

    elif personal_7=="Todos" and proceso_7_s=="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and perfil='{perfil_7_s}' ", con)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and proceso='{proceso_7_s}' ", con)
  
    elif personal_7=="Todos" and proceso_7_s !="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}' ", con)
  
    elif personal_7=="Operarios" and proceso_7_s =="Todos" and perfil_7_s=="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral'", con)
 
    elif personal_7=="Operarios" and proceso_7_s =="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and perfil='{perfil_7_s}' ", con)
 
    elif personal_7=="Operarios" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and proceso='{proceso_7_s}' ", con)
 
    elif personal_7=="Operarios" and proceso_7_s !="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and puesto='Operario Catastral' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}' ", con)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}'", con)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and perfil='{perfil_7_s}'", con)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and proceso='{proceso_7_s}'", con)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and perfil_7_s!="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and proceso='{proceso_7_s}' perfil='{perfil_7_s}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and perfil_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and perfil='{perfil_7_s}'", con)

    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and perfil_7_s=="Todos":
      
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and proceso='{proceso_7_s}'", con)
      
    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and perfil_7_s!="Todos":

      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques_o_parcelas as integer),cast(cubiertas_y_mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and supervisor='{nombre_7}' and proceso='{proceso_7_s}' and perfil='{perfil_7_s}'", con)
           
    # ----- Reportes ---- #

    placeholder13_7 = st.empty()
    reportes_7=placeholder13_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder14_7 = st.empty()
      error_reportes= placeholder14_7.error('No existen reportes para mostrar')

    else:

      placeholder15_7 = st.empty()
      historial_7_reportes=placeholder15_7.dataframe(data=data_1_r)

      placeholder16_7 = st.empty()
      descarga_7_reportes = placeholder16_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Producción ---- #

    placeholder17_7 = st.empty()
    producción_7=placeholder17_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha_finalizacion","proceso"], as_index=False)[["bloques_o_parcelas","cubiertas_y_mejoras","horas"]].agg(np.sum)

    pivot_r=len(data_2_r.iloc[:,0])

    if pivot_r==0:  

      placeholder18_7 = st.empty()
      error_producción= placeholder18_7.error('No existe producción para mostrar')

    else:
         
      placeholder19_7 = st.empty()
      historial_7_producción= placeholder19_7.dataframe(data=data_2_r)

      placeholder20_7 = st.empty()
      descarga_7_producción = placeholder20_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
          
    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha_finalizacion","proceso"], as_index=False)["bloques_o_parcelas"].agg(np.sum)

    placeholder21_7 = st.empty()
    total_7=placeholder21_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder22_7 = st.empty()
      error_total_producción= placeholder22_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha_finalizacion", y="bloques_o_parcelas", text="bloques_o_parcelas", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder23_7 = st.empty()
      grafico_producción_total= placeholder23_7.plotly_chart(fig_producción_total)

  # ----- Operario Catastral ---- #

  elif puesto=="Operario Catastral":

    placeholder24_7 = st.empty()
    proceso_7_o = placeholder24_7.selectbox("Proceso", options=("Todos","Parcelas ","Cubiertas y Mejoras"), key="proceso_7_s")
    
    if proceso_7_o =="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques o parcelas as integer),cast(cubiertas y mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}'", con)

    elif proceso_7_o !="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,perfil,puesto,supervisor,proceso,fecha_inicio,fecha_finalizacion,zona,cast(bloques o parcelas as integer),cast(cubiertas y mejoras as integer),cast(horas as float) from registro where fecha_inicio>='{fecha_referencia_1_7}' or fecha_inicio<='{fecha_referencia_2_7}' or  fecha_finalizacion>='{fecha_referencia_1_7}' or fecha_finalizacion<='{fecha_referencia_2_7}' and usuario='{usuario}' and usuario='{proceso_7_o}'", con)

    # ----- Reportes ---- #

    placeholder25_7 = st.empty()
    reportes_7=placeholder25_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder26_7 = st.empty()
      error_reportes= placeholder26_7.error('No existen reportes para mostrar')

    else:

      placeholder27_7 = st.empty()
      historial_7_reportes=placeholder27_7.dataframe(data=data_1_r)

      placeholder28_7 = st.empty()
      descarga_7_reportes = placeholder28_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Producción ---- #

    placeholder29_7 = st.empty()
    producción_7=placeholder29_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha_finalizacion","proceso"], as_index=False)[["bloques_o_parcelas","cubiertas_y_mejoras","horas"]].agg(np.sum)

    pivot_r=len(data_2_r.iloc[:,0])

    if pivot_r==0:  

      placeholder30_7 = st.empty()
      error_producción= placeholder30_7.error('No existe producción para mostrar')

    else:
         
      placeholder31_7 = st.empty()
      historial_7_producción= placeholder31_7.dataframe(data=data_2_r)

      placeholder32_7 = st.empty()
      descarga_7_producción = placeholder32_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
  
    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha_finalizacion","proceso"], as_index=False)["bloques_o_parcelas"].agg(np.sum)

    placeholder33_7 = st.empty()
    total_7=placeholder33_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder34_7 = st.empty()
      error_total_producción= placeholder34_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha_finalizacion", y="bloques_o_parcelas", text="bloques_o_parcelas", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder35_7 = st.empty()
      grafico_producción_total= placeholder35_7.plotly_chart(fig_producción_total)

  # ----- Proceso ---- #
  
  if procesos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Procesos=False
    st.session_state.Historial_Argentina=False
    Procesos.Procesos_Argentina(usuario,puesto,perfil)   

  # ----- Capacitación ---- #
    
  elif capacitacion_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Historial_Argentina=False
    st.session_state.Capacitacion_Argentina=True
    Capacitacion.Capacitacion_Argentina(usuario,puesto,perfil)

  # ----- Salir ---- #
    
  elif salir_7:

    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty() 
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 :
        placeholder18_7.empty()
        placeholder22_7.empty()

      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder23_7.empty()

    elif puesto=="Operario Catastral":
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder29_7.empty()

      if pivot_reportes==0:
        placeholder26_7.empty()
      
      else:
        placeholder27_7.empty()
        placeholder28_7.empty()
         
      if pivot_r==0:
        placeholder30_7.empty()
        placeholder34_7.empty()
        
      else:
        placeholder31_7.empty()
        placeholder32_7.empty()
        placeholder35_7.empty()

    st.session_state.Ingreso = False
    st.session_state.Historial_Argentina=False
    st.session_state.Salir=True
    Salir.Salir()
