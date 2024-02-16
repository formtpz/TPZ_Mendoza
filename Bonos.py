# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Salir
from sqlalchemy import create_engine

def Bonos(usuario,puesto,perfil):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_9= st.sidebar.empty()
  titulo= placeholder1_9.title("Menú")

  placeholder2_9 = st.sidebar.empty()
  procesos_9 = placeholder2_9.button("Procesos",key="procesos_9")

  placeholder3_9 = st.sidebar.empty()
  historial_9 = placeholder3_9.button("Historial",key="historial_9")

  placeholder4_9 = st.sidebar.empty()
  capacitacion_9= placeholder4_9.button("Capacitaciones",key="capacitacion_9")

  placeholder5_9 = st.sidebar.empty()
  otros_registros_9= placeholder5_9.button("Otros Registros",key="otros_registros_9")

  placeholder6_9 = st.sidebar.empty()
  salir_9 = placeholder6_9.button("Salir",key="salir_9")

  placeholder7_9 = st.empty()
  registro_de_bonos_9 = placeholder7_9.title("Registro de Bonos")

  nombre_9= pd.read_sql(f"select nombre from usuarios where usuario='{usuario}'",uri)
  nombre_9 = nombre_9.loc[0,'nombre']

  if nombre_9=="Basilio Antonio Salazar Nunez":

    placeholder8_9 = st.empty()
    archivos = placeholder8_9.subheader("Archivos")

    placeholder9_9 = st.empty()
    bloques_nuevos_9 = placeholder9_9.file_uploader("Cargar Archivo de Bloques",['csv','xlsx'])

    placeholder10_9 = st.empty()
    bonos_nuevos_9 = placeholder10_9.file_uploader("Cargar Archivo de Bonos",['csv','xlsx'])

    placeholder11_9 = st.empty()
    cargar_archivos_9 = placeholder11_9.button("Cargar Archivos",key="cargar_archivos_9")

    if cargar_archivos_9:

      if bloques_nuevos_9 is None or bonos_nuevos_9 is None:

        st.error('Favor cargar los archivos solicitados')

      else: 

        bloques_nuevos_9=pd.DataFrame(pd.read_excel(bloques_nuevos_9))
        bonos_nuevos_9=pd.DataFrame(pd.read_excel(bonos_nuevos_9))

        cursor01=con.cursor()

        cursor01.execute('DELETE FROM bloques;',)
        cursor01.execute('DELETE FROM bonos;',)

        con.commit()      

        engine = create_engine(uri)
    
        bloques_nuevos_9.to_sql(name='bloques', con = engine, if_exists = 'append',index_label='id')
    
        bonos_nuevos_9.to_sql(name='bonos', con = engine, if_exists = 'append',index_label='id')

        st.success('Archivos Cargados Correctamente')

  elif nombre_9=="Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

    placeholder12_9 = st.empty()
    titulo_bonos_9 = placeholder12_9.subheader("Bonos")

    data_personal_9 = pd.read_sql(f"select nombre from usuarios where estado='Activo'", con)
    placeholder13_9 = st.empty()
    personal_9= placeholder13_9.selectbox("Personal",data_personal_9,key="personal_9")

    placeholder14_9 = st.empty()
    periodo_bonos_9 = placeholder14_9.selectbox("Periodo de Bono", options=("Febrero-2023","Marzo-2023","Abril-2023","Mayo-2023","Junio-2023","Julio-2023","Agosto-2023","Septiembre-2023","Octubre-2023","Noviembre-2023","Diciembre-2023","Enero-2024","Febrero-2024","Marzo-2024","Abril-2024","Mayo-2024","Junio-2024"), key="periodo_bonos_9")    

    if personal_9 == "Todos" :

      bonos_9= pd.read_sql(f"select a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103 from bonos where a103='{periodo_bonos_9}'", con)
      bonos_9=  pd.DataFrame(data=bonos_9)

      pivot1= len(bonos_9.iloc[:,0])

      if pivot1==0:

        placeholder15_9 = st.empty()
        error_9 = placeholder15_9.error('No existen datos para mostrar')

      else:

        bonos_variables_9=0
        bonos_fijos_9=0
        otros_bonos_9=0
        
        for a in range(0,pivot1):

            bonos_variables_9 = bonos_variables_9 + sum([float(bonos_9.iloc[a,65]),float(bonos_9.iloc[a,66]),float(bonos_9.iloc[a,67]),float(bonos_9.iloc[a,68]),float(bonos_9.iloc[a,69]),float(bonos_9.iloc[a,70]),float(bonos_9.iloc[a,71]),float(bonos_9.iloc[a,72]),float(bonos_9.iloc[a,73])])
            bonos_fijos_9 = bonos_fijos_9 + sum([float(bonos_9.iloc[a,75]),float(bonos_9.iloc[a,76]),float(bonos_9.iloc[a,77]),float(bonos_9.iloc[a,78]),float(bonos_9.iloc[a,79]),float(bonos_9.iloc[a,80]),float(bonos_9.iloc[a,81]),float(bonos_9.iloc[a,82]),float(bonos_9.iloc[a,83])])
            otros_bonos_9 = otros_bonos_9 + sum([float(bonos_9.iloc[a,95]),float(bonos_9.iloc[a,96]),float(bonos_9.iloc[a,97]),float(bonos_9.iloc[a,98]),float(bonos_9.iloc[a,99])])
            bonos_total=sum([float(bonos_variables_9),float(bonos_fijos_9),float(otros_bonos_9)])
            
        placeholder16_9 = st.empty()
        col1, col2, col3, col4 = placeholder16_9.columns(4)
        col1.metric("Bonos Variables",bonos_variables_9)
        col2.metric("Bonos Fijos",bonos_fijos_9)
        col3.metric("Otros Bonos",otros_bonos_9)
        col4.metric("Total",bonos_total)

    else:
    
      bonos_9= pd.read_sql(f"select a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103 from bonos where a1='{personal_9}' and a103='{periodo_bonos_9}'", con)
      bonos_9=  pd.DataFrame(data=bonos_9)

      pivot2= len(bonos_9.iloc[:,0])

      if pivot2==0:

        placeholder17_9 = st.empty()
        error_9 = placeholder17_9.error('No existen datos para mostrar')

      else:

        # Resumen #

        bonos_variables_9 = sum([float(bonos_9.iloc[0,65]),float(bonos_9.iloc[0,66]),float(bonos_9.iloc[0,67]),float(bonos_9.iloc[0,68]),float(bonos_9.iloc[0,69]),float(bonos_9.iloc[0,70]),float(bonos_9.iloc[0,71]),float(bonos_9.iloc[0,72]),float(bonos_9.iloc[0,73])])
        bonos_fijos_9 = sum([float(bonos_9.iloc[0,75]),float(bonos_9.iloc[0,76]),float(bonos_9.iloc[0,77]),float(bonos_9.iloc[0,78]),float(bonos_9.iloc[0,79]),float(bonos_9.iloc[0,80]),float(bonos_9.iloc[0,81]),float(bonos_9.iloc[0,82]),float(bonos_9.iloc[0,83])])
        otros_bonos_9 = sum([float(bonos_9.iloc[0,95]),float(bonos_9.iloc[0,96]),float(bonos_9.iloc[0,97]),float(bonos_9.iloc[0,98]),float(bonos_9.iloc[0,99])])

        placeholder18_9 = st.empty()
        col1, col2, col3, col4 = placeholder18_9.columns(4)
        col1.metric("Bonos Variables",bonos_variables_9)
        col2.metric("Bonos Fijos",bonos_fijos_9)
        col3.metric("Otros Bonos",otros_bonos_9)
        col4.metric("Total",bonos_9.iloc[0,102])

        # Procesos #
          
        variables_9=["Ratio Promedio por Bloque (Predio/Día)","Duración (Día)","Producción (Según Reportes)","Producción Limpia","Producción (Según Ratio)","Producción (Estándar)","Bono Variable","Bono Fijo","Cantidad de Personal"]								

        conciliacion_9=[0]*9
        ubicacion_9=[0]*9
        conformacion_9=[0]*9
        cc_conformacion_9=[0]*9 	
        validacion_9=[0]*9	
        if_i_9=[0]*9
        cc_if_i_9=[0]*9
        if_ii_9=[0]*9
        if_iii_9=[0]*9

        bonos_procesos_9= pd.DataFrame(data={"Variables":variables_9,"Conciliación":conciliacion_9,"Ubicación":ubicacion_9,"Conformación":conformacion_9,"CC Conformación":cc_conformacion_9,"Validación":validacion_9,"Información Final I":if_i_9,"CC Información Final I":cc_if_i_9,"Información Final II":if_ii_9,"Información Final III":if_iii_9})

        # Conciliación #
          
        bonos_procesos_9.iloc[0,1] = bonos_9.iloc[0,5]
        bonos_procesos_9.iloc[1,1] = bonos_9.iloc[0,15]
        bonos_procesos_9.iloc[2,1] = bonos_9.iloc[0,25]
        bonos_procesos_9.iloc[3,1] = bonos_9.iloc[0,35]
        bonos_procesos_9.iloc[4,1] = bonos_9.iloc[0,45]
        bonos_procesos_9.iloc[5,1] = bonos_9.iloc[0,55]
        bonos_procesos_9.iloc[6,1] = bonos_9.iloc[0,65]
        bonos_procesos_9.iloc[7,1] = bonos_9.iloc[0,75]
        bonos_procesos_9.iloc[8,1] = bonos_9.iloc[0,85]

        # Ubicación #
          
        bonos_procesos_9.iloc[0,2] = bonos_9.iloc[0,6]
        bonos_procesos_9.iloc[1,2] = bonos_9.iloc[0,16]
        bonos_procesos_9.iloc[2,2] = bonos_9.iloc[0,26]
        bonos_procesos_9.iloc[3,2] = bonos_9.iloc[0,36]
        bonos_procesos_9.iloc[4,2] = bonos_9.iloc[0,46]
        bonos_procesos_9.iloc[5,2] = bonos_9.iloc[0,56]
        bonos_procesos_9.iloc[6,2] = bonos_9.iloc[0,66]
        bonos_procesos_9.iloc[7,2] = bonos_9.iloc[0,76]
        bonos_procesos_9.iloc[8,2] = bonos_9.iloc[0,86]

        # Conformación #
          
        bonos_procesos_9.iloc[0,3] = bonos_9.iloc[0,7]
        bonos_procesos_9.iloc[1,3] = bonos_9.iloc[0,17]
        bonos_procesos_9.iloc[2,3] = bonos_9.iloc[0,27]
        bonos_procesos_9.iloc[3,3] = bonos_9.iloc[0,37]
        bonos_procesos_9.iloc[4,3] = bonos_9.iloc[0,47]
        bonos_procesos_9.iloc[5,3] = bonos_9.iloc[0,57]
        bonos_procesos_9.iloc[6,3] = bonos_9.iloc[0,67]
        bonos_procesos_9.iloc[7,3] = bonos_9.iloc[0,77]
        bonos_procesos_9.iloc[8,3] = bonos_9.iloc[0,87]

        #  Control de Calidad Conformación #
          
        bonos_procesos_9.iloc[0,4] = bonos_9.iloc[0,8]
        bonos_procesos_9.iloc[1,4] = bonos_9.iloc[0,18]
        bonos_procesos_9.iloc[2,4] = bonos_9.iloc[0,28]
        bonos_procesos_9.iloc[3,4] = bonos_9.iloc[0,38]
        bonos_procesos_9.iloc[4,4] = bonos_9.iloc[0,48]
        bonos_procesos_9.iloc[5,4] = bonos_9.iloc[0,58]
        bonos_procesos_9.iloc[6,4] = bonos_9.iloc[0,68]
        bonos_procesos_9.iloc[7,4] = bonos_9.iloc[0,78]
        bonos_procesos_9.iloc[8,4] = bonos_9.iloc[0,88]

        # Validación #
          
        bonos_procesos_9.iloc[0,5] = bonos_9.iloc[0,9]
        bonos_procesos_9.iloc[1,5] = bonos_9.iloc[0,19]
        bonos_procesos_9.iloc[2,5] = bonos_9.iloc[0,29]
        bonos_procesos_9.iloc[3,5] = bonos_9.iloc[0,39]
        bonos_procesos_9.iloc[4,5] = bonos_9.iloc[0,49]
        bonos_procesos_9.iloc[5,5] = bonos_9.iloc[0,59]
        bonos_procesos_9.iloc[6,5] = bonos_9.iloc[0,69]
        bonos_procesos_9.iloc[7,5] = bonos_9.iloc[0,79]
        bonos_procesos_9.iloc[8,5] = bonos_9.iloc[0,89]

        # Información Final I #

        bonos_procesos_9.iloc[0,6] = bonos_9.iloc[0,10]
        bonos_procesos_9.iloc[1,6] = bonos_9.iloc[0,20]
        bonos_procesos_9.iloc[2,6] = bonos_9.iloc[0,30]
        bonos_procesos_9.iloc[3,6] = bonos_9.iloc[0,40]
        bonos_procesos_9.iloc[4,6] = bonos_9.iloc[0,50]
        bonos_procesos_9.iloc[5,6] = bonos_9.iloc[0,60]
        bonos_procesos_9.iloc[6,6] = bonos_9.iloc[0,70]
        bonos_procesos_9.iloc[7,6] = bonos_9.iloc[0,80]
        bonos_procesos_9.iloc[8,6] = bonos_9.iloc[0,90]

        # Control de Calidad Información Final I #

        bonos_procesos_9.iloc[0,7] = bonos_9.iloc[0,11]
        bonos_procesos_9.iloc[1,7] = bonos_9.iloc[0,21]
        bonos_procesos_9.iloc[2,7] = bonos_9.iloc[0,31]
        bonos_procesos_9.iloc[3,7] = bonos_9.iloc[0,41]
        bonos_procesos_9.iloc[4,7] = bonos_9.iloc[0,51]
        bonos_procesos_9.iloc[5,7] = bonos_9.iloc[0,61]
        bonos_procesos_9.iloc[6,7] = bonos_9.iloc[0,71]
        bonos_procesos_9.iloc[7,7] = bonos_9.iloc[0,81]
        bonos_procesos_9.iloc[8,7] = bonos_9.iloc[0,91]

        # Información Final II #

        bonos_procesos_9.iloc[0,8] = bonos_9.iloc[0,12]
        bonos_procesos_9.iloc[1,8] = bonos_9.iloc[0,22]
        bonos_procesos_9.iloc[2,8] = bonos_9.iloc[0,32]
        bonos_procesos_9.iloc[3,8] = bonos_9.iloc[0,42]
        bonos_procesos_9.iloc[4,8] = bonos_9.iloc[0,52]
        bonos_procesos_9.iloc[5,8] = bonos_9.iloc[0,62]
        bonos_procesos_9.iloc[6,8] = bonos_9.iloc[0,72]
        bonos_procesos_9.iloc[7,8] = bonos_9.iloc[0,82]
        bonos_procesos_9.iloc[8,8] = bonos_9.iloc[0,92]

        # Información Final III #

        bonos_procesos_9.iloc[0,9] = bonos_9.iloc[0,13]
        bonos_procesos_9.iloc[1,9] = bonos_9.iloc[0,23]
        bonos_procesos_9.iloc[2,9] = bonos_9.iloc[0,33]
        bonos_procesos_9.iloc[3,9] = bonos_9.iloc[0,43]
        bonos_procesos_9.iloc[4,9] = bonos_9.iloc[0,53]
        bonos_procesos_9.iloc[5,9] = bonos_9.iloc[0,63]
        bonos_procesos_9.iloc[6,9] = bonos_9.iloc[0,73]
        bonos_procesos_9.iloc[7,9] = bonos_9.iloc[0,83]
        bonos_procesos_9.iloc[8,9] = bonos_9.iloc[0,93]

        placeholder19_9 = st.empty()
        dataframe_bonos_procesos_9=placeholder19_9.dataframe(data=bonos_procesos_9)

        placeholder20_9 = st.empty()
        descarga_procesos_9 = placeholder20_9.download_button("Decargar CSV",data=bonos_procesos_9.to_csv(),mime="text/csv",key="descarga_procesos_9")

        # Otros Bonos #

        variables_9=["Bonos Variables","Bonos Fijos","Bonificación por Entregas","Bonificación Cumplimiento RN","Bonificación Supervisión","Bonificación Exposiciones Públicas","Bonificación Otras Funciones","Observaciones","Bonificación Total"]								
        valor_9=[0]*9

        otros_bonos_9= pd.DataFrame(data={"Variables":variables_9,"Valor":valor_9})
          
        otros_bonos_9.iloc[0,1] = bonos_variables_9
        otros_bonos_9.iloc[1,1] = bonos_fijos_9
        otros_bonos_9.iloc[2,1] = bonos_9.iloc[0,95]
        otros_bonos_9.iloc[3,1] = bonos_9.iloc[0,96]
        otros_bonos_9.iloc[4,1] = bonos_9.iloc[0,97]
        otros_bonos_9.iloc[5,1] = bonos_9.iloc[0,98]
        otros_bonos_9.iloc[6,1] = bonos_9.iloc[0,99]
        otros_bonos_9.iloc[7,1] = bonos_9.iloc[0,101]
        otros_bonos_9.iloc[8,1] = bonos_9.iloc[0,102]

        placeholder21_9 = st.empty()
        dataframe_otros_bonos_9=placeholder21_9.dataframe(data=otros_bonos_9)

        placeholder22_9 = st.empty()
        descarga_otros_bonos_9 = placeholder22_9.download_button("Decargar CSV",data=otros_bonos_9.to_csv(),mime="text/csv",key="descarga_otros_bonos_9")

  else:
    
    placeholder23_9 = st.empty()
    titulo_bonos_9 = placeholder23_9.subheader("Bonos")

    placeholder24_9 = st.empty()
    periodo_bonos_9 = placeholder24_9.selectbox("Periodo de Bono",options=("Febrero-2023","Marzo-2023","Abril-2023","Mayo-2023","Junio-2023","Julio-2023","Agosto-2023","Septiembre-2023","Octubre-2023","Noviembre-2023","Diciembre-2023","Enero-2024","Febrero-2024","Marzo-2024","Abril-2024","Mayo-2024","Junio-2024"), key="periodo_bonos_9")    

    bonos_9= pd.read_sql(f"select a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103 from bonos where a0='{usuario}' and a103='{periodo_bonos_9}'", con)
    bonos_9=  pd.DataFrame(data=bonos_9)

    pivot3= len(bonos_9.iloc[:,0])

    if pivot3==0:

      placeholder25_9 = st.empty()
      error_9 = placeholder25_9.error('No existen datos para mostrar')

    else:

      # Resumen #

      bonos_variables_9 = sum([float(bonos_9.iloc[0,65]),float(bonos_9.iloc[0,66]),float(bonos_9.iloc[0,67]),float(bonos_9.iloc[0,68]),float(bonos_9.iloc[0,69]),float(bonos_9.iloc[0,70]),float(bonos_9.iloc[0,71]),float(bonos_9.iloc[0,72]),float(bonos_9.iloc[0,73])])
      bonos_fijos_9 = sum([float(bonos_9.iloc[0,75]),float(bonos_9.iloc[0,76]),float(bonos_9.iloc[0,77]),float(bonos_9.iloc[0,78]),float(bonos_9.iloc[0,79]),float(bonos_9.iloc[0,80]),float(bonos_9.iloc[0,81]),float(bonos_9.iloc[0,82]),float(bonos_9.iloc[0,83])])
      otros_bonos_9 = sum([float(bonos_9.iloc[0,95]),float(bonos_9.iloc[0,96]),float(bonos_9.iloc[0,97]),float(bonos_9.iloc[0,98]),float(bonos_9.iloc[0,99])])

      placeholder26_9 = st.empty()
      col1, col2, col3, col4 = placeholder26_9.columns(4)
      col1.metric("Bonos Variables",bonos_variables_9)
      col2.metric("Bonos Fijos",bonos_fijos_9)
      col3.metric("Otros Bonos",otros_bonos_9)
      col4.metric("Total",bonos_9.iloc[0,102])

      # Procesos #
      
      variables_1_9=["Ratio Promedio por Bloque (Predio/Día)","Duración (Día)","Producción (Según Reportes)","Producción Limpia","Producción (Según Ratio)","Producción (Estándar)","Bono Variable","Bono Fijo","Cantidad de Personal"]								

      conciliacion_9=[0]*9
      ubicacion_9=[0]*9
      conformacion_9=[0]*9
      cc_conformacion_9=[0]*9 	
      validacion_9=[0]*9	
      if_i_9=[0]*9
      cc_if_i_9=[0]*9
      if_ii_9=[0]*9
      if_iii_9=[0]*9

      bonos_procesos_9= pd.DataFrame(data={"Variables":variables_1_9,"Conciliación":conciliacion_9,"Ubicación":ubicacion_9,"Conformación":conformacion_9,"CC Conformación":cc_conformacion_9,"Validación":validacion_9,"Información Final I":if_i_9,"CC Información Final I":cc_if_i_9,"Información Final II":if_ii_9,"Información Final III":if_iii_9})

      # Conciliación #
      
      bonos_procesos_9.iloc[0,1] = bonos_9.iloc[0,5]
      bonos_procesos_9.iloc[1,1] = bonos_9.iloc[0,15]
      bonos_procesos_9.iloc[2,1] = bonos_9.iloc[0,25]
      bonos_procesos_9.iloc[3,1] = bonos_9.iloc[0,35]
      bonos_procesos_9.iloc[4,1] = bonos_9.iloc[0,45]
      bonos_procesos_9.iloc[5,1] = bonos_9.iloc[0,55]
      bonos_procesos_9.iloc[6,1] = bonos_9.iloc[0,65]
      bonos_procesos_9.iloc[7,1] = bonos_9.iloc[0,75]
      bonos_procesos_9.iloc[8,1] = bonos_9.iloc[0,85]

      # Ubicación #
      
      bonos_procesos_9.iloc[0,2] = bonos_9.iloc[0,6]
      bonos_procesos_9.iloc[1,2] = bonos_9.iloc[0,16]
      bonos_procesos_9.iloc[2,2] = bonos_9.iloc[0,26]
      bonos_procesos_9.iloc[3,2] = bonos_9.iloc[0,36]
      bonos_procesos_9.iloc[4,2] = bonos_9.iloc[0,46]
      bonos_procesos_9.iloc[5,2] = bonos_9.iloc[0,56]
      bonos_procesos_9.iloc[6,2] = bonos_9.iloc[0,66]
      bonos_procesos_9.iloc[7,2] = bonos_9.iloc[0,76]
      bonos_procesos_9.iloc[8,2] = bonos_9.iloc[0,86]

      # Conformación #
      
      bonos_procesos_9.iloc[0,3] = bonos_9.iloc[0,7]
      bonos_procesos_9.iloc[1,3] = bonos_9.iloc[0,17]
      bonos_procesos_9.iloc[2,3] = bonos_9.iloc[0,27]
      bonos_procesos_9.iloc[3,3] = bonos_9.iloc[0,37]
      bonos_procesos_9.iloc[4,3] = bonos_9.iloc[0,47]
      bonos_procesos_9.iloc[5,3] = bonos_9.iloc[0,57]
      bonos_procesos_9.iloc[6,3] = bonos_9.iloc[0,67]
      bonos_procesos_9.iloc[7,3] = bonos_9.iloc[0,77]
      bonos_procesos_9.iloc[8,3] = bonos_9.iloc[0,87]

      #  Control de Calidad Conformación #
      
      bonos_procesos_9.iloc[0,4] = bonos_9.iloc[0,8]
      bonos_procesos_9.iloc[1,4] = bonos_9.iloc[0,18]
      bonos_procesos_9.iloc[2,4] = bonos_9.iloc[0,28]
      bonos_procesos_9.iloc[3,4] = bonos_9.iloc[0,38]
      bonos_procesos_9.iloc[4,4] = bonos_9.iloc[0,48]
      bonos_procesos_9.iloc[5,4] = bonos_9.iloc[0,58]
      bonos_procesos_9.iloc[6,4] = bonos_9.iloc[0,68]
      bonos_procesos_9.iloc[7,4] = bonos_9.iloc[0,78]
      bonos_procesos_9.iloc[8,4] = bonos_9.iloc[0,88]

      # Validación #
      
      bonos_procesos_9.iloc[0,5] = bonos_9.iloc[0,9]
      bonos_procesos_9.iloc[1,5] = bonos_9.iloc[0,19]
      bonos_procesos_9.iloc[2,5] = bonos_9.iloc[0,29]
      bonos_procesos_9.iloc[3,5] = bonos_9.iloc[0,39]
      bonos_procesos_9.iloc[4,5] = bonos_9.iloc[0,49]
      bonos_procesos_9.iloc[5,5] = bonos_9.iloc[0,59]
      bonos_procesos_9.iloc[6,5] = bonos_9.iloc[0,69]
      bonos_procesos_9.iloc[7,5] = bonos_9.iloc[0,79]
      bonos_procesos_9.iloc[8,5] = bonos_9.iloc[0,89]

      # Información Final I #

      bonos_procesos_9.iloc[0,6] = bonos_9.iloc[0,10]
      bonos_procesos_9.iloc[1,6] = bonos_9.iloc[0,20]
      bonos_procesos_9.iloc[2,6] = bonos_9.iloc[0,30]
      bonos_procesos_9.iloc[3,6] = bonos_9.iloc[0,40]
      bonos_procesos_9.iloc[4,6] = bonos_9.iloc[0,50]
      bonos_procesos_9.iloc[5,6] = bonos_9.iloc[0,60]
      bonos_procesos_9.iloc[6,6] = bonos_9.iloc[0,70]
      bonos_procesos_9.iloc[7,6] = bonos_9.iloc[0,80]
      bonos_procesos_9.iloc[8,6] = bonos_9.iloc[0,90]

      # Control de Calidad Información Final I #

      bonos_procesos_9.iloc[0,7] = bonos_9.iloc[0,11]
      bonos_procesos_9.iloc[1,7] = bonos_9.iloc[0,21]
      bonos_procesos_9.iloc[2,7] = bonos_9.iloc[0,31]
      bonos_procesos_9.iloc[3,7] = bonos_9.iloc[0,41]
      bonos_procesos_9.iloc[4,7] = bonos_9.iloc[0,51]
      bonos_procesos_9.iloc[5,7] = bonos_9.iloc[0,61]
      bonos_procesos_9.iloc[6,7] = bonos_9.iloc[0,71]
      bonos_procesos_9.iloc[7,7] = bonos_9.iloc[0,81]
      bonos_procesos_9.iloc[8,7] = bonos_9.iloc[0,91]

      # Información Final II #

      bonos_procesos_9.iloc[0,8] = bonos_9.iloc[0,12]
      bonos_procesos_9.iloc[1,8] = bonos_9.iloc[0,22]
      bonos_procesos_9.iloc[2,8] = bonos_9.iloc[0,32]
      bonos_procesos_9.iloc[3,8] = bonos_9.iloc[0,42]
      bonos_procesos_9.iloc[4,8] = bonos_9.iloc[0,52]
      bonos_procesos_9.iloc[5,8] = bonos_9.iloc[0,62]
      bonos_procesos_9.iloc[6,8] = bonos_9.iloc[0,72]
      bonos_procesos_9.iloc[7,8] = bonos_9.iloc[0,82]
      bonos_procesos_9.iloc[8,8] = bonos_9.iloc[0,92]

      # Información Final III #

      bonos_procesos_9.iloc[0,9] = bonos_9.iloc[0,13]
      bonos_procesos_9.iloc[1,9] = bonos_9.iloc[0,23]
      bonos_procesos_9.iloc[2,9] = bonos_9.iloc[0,33]
      bonos_procesos_9.iloc[3,9] = bonos_9.iloc[0,43]
      bonos_procesos_9.iloc[4,9] = bonos_9.iloc[0,53]
      bonos_procesos_9.iloc[5,9] = bonos_9.iloc[0,63]
      bonos_procesos_9.iloc[6,9] = bonos_9.iloc[0,73]
      bonos_procesos_9.iloc[7,9] = bonos_9.iloc[0,83]
      bonos_procesos_9.iloc[8,9] = bonos_9.iloc[0,93]

      placeholder27_9 = st.empty()
      dataframe_bonos_procesos_9=placeholder27_9.dataframe(data=bonos_procesos_9)

      placeholder28_9 = st.empty()
      descarga_procesos_9 = placeholder28_9.download_button("Decargar CSV",data=bonos_procesos_9.to_csv(),mime="text/csv",key="descarga_procesos_9")

      # Otros Bonos #

      variables_2_9=["Bonos Variables","Bonos Fijos","Bonificación por Entregas","Bonificación Cumplimiento RN","Bonificación Supervisión","Bonificación Exposiciones Públicas","Bonificación Otras Funciones","Observaciones","Bonificación Total"]								
      valor_9=[0]*9

      otros_bonos_9= pd.DataFrame(data={"Variables":variables_2_9,"Valor":valor_9})
      
      otros_bonos_9.iloc[0,1] = bonos_variables_9
      otros_bonos_9.iloc[1,1] = bonos_fijos_9
      otros_bonos_9.iloc[2,1] = bonos_9.iloc[0,95]
      otros_bonos_9.iloc[3,1] = bonos_9.iloc[0,96]
      otros_bonos_9.iloc[4,1] = bonos_9.iloc[0,97]
      otros_bonos_9.iloc[5,1] = bonos_9.iloc[0,98]
      otros_bonos_9.iloc[6,1] = bonos_9.iloc[0,99]
      otros_bonos_9.iloc[7,1] = bonos_9.iloc[0,101]
      otros_bonos_9.iloc[8,1] = bonos_9.iloc[0,102]


      placeholder29_9 = st.empty()
      dataframe_otros_bonos_9=placeholder29_9.dataframe(data=otros_bonos_9)

      placeholder30_9 = st.empty()
      descarga_otros_bonos_9 = placeholder30_9.download_button("Decargar CSV",data=otros_bonos_9.to_csv(),mime="text/csv",key="descarga_otros_bonos_9")
    
    placeholder31_9= st.empty()
    separador_9 = placeholder31_9.markdown("_____")
    
    # Bloques #

    placeholder32_9 = st.empty()
    titulo_bloques_9 = placeholder32_9.subheader("Bloques")

    placeholder33_9 = st.empty()
    periodo_bloques_9 = placeholder33_9.selectbox("Fecha de Producción", options=("Todos","Marzo-2023","Abril-2023","Mayo-2023","Junio-2023","Julio-2023","Agosto-2023","Septiembre-2023","Octubre-2023","Noviembre-2023","Diciembre-2023","Enero-2024","Febrero-2024","Marzo-2024","Abril-2024","Mayo-2024","Junio-2024"), key="periodo_bloques_9")    

    if periodo_bloques_9=="Todos":

      bloques_9= pd.read_sql(f"select usuario,nombre,supervisor,proceso,tipo_revision,bloque_distrito,produccion_segun_reporte,horas,produccion_estandar,produccion_rechazada_primera_revision,produccion_aprobada_primera_revision,porcentage_error,produccion_penalizada,produccion_limpia,ratio_limpio_predio_por_dia,primera_reinspeccion,segunda_reinspeccion,porcentage_penalizacion_ratio,ratio_penalizado_predio_por_dia,fecha_produccion,fecha_corte,fecha_bono from bloques where usuario='{usuario}'", con)
      bloques_9=  pd.DataFrame(data=bloques_9)
    
    else:

      bloques_9= pd.read_sql(f"select usuario,nombre,supervisor,proceso,tipo_revision,bloque_distrito,produccion_segun_reporte,horas,produccion_estandar,produccion_rechazada_primera_revision,produccion_aprobada_primera_revision,porcentage_error,produccion_penalizada,produccion_limpia,ratio_limpio_predio_por_dia,primera_reinspeccion,segunda_reinspeccion,porcentage_penalizacion_ratio,ratio_penalizado_predio_por_dia,fecha_produccion,fecha_corte,fecha_bono from bloques where usuario='{usuario}' and fecha_produccion='{periodo_bloques_9}'", con)
      bloques_9=  pd.DataFrame(data=bloques_9)

    pivot4= len(bloques_9.iloc[:,1])

    if pivot4 ==0:

      placeholder34_9 = st.empty()
      error_9 = placeholder34_9.error('No existen datos para mostrar')

    else:

      placeholder35_9 = st.empty()
      dataframe_bloques_9=placeholder35_9.dataframe(data=bloques_9)

      placeholder36_9 = st.empty()
      descarga_bloques_9 = placeholder36_9.download_button("Decargar CSV",data=bloques_9.to_csv(),mime="text/csv",key="descarga_bloques_9")

  # ----- Procesos ---- #
    
  if procesos_9:

    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()

    if nombre_9=="Basilio Antonio Salazar Nunez":

      placeholder8_9.empty()
      placeholder9_9.empty()
      placeholder10_9.empty()
      placeholder11_9.empty()
    
    elif nombre_9== "Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

      placeholder12_9.empty()
      placeholder13_9.empty()
      placeholder14_9.empty()

      if personal_9=="Todos":

        if pivot1==0:
        
          placeholder15_9.empty()
      
        else:

          placeholder16_9.empty()

      else:

        if pivot2==0:

          placeholder17_9.empty()

        else:

          placeholder18_9.empty()
          placeholder19_9.empty()
          placeholder20_9.empty()
          placeholder21_9.empty()
          placeholder22_9.empty()

    else:
      
      placeholder23_9.empty()
      placeholder24_9.empty()
      placeholder31_9.empty()
      placeholder32_9.empty()
      placeholder33_9.empty()

      if pivot3==0:

        placeholder25_9.empty()

      else:

        placeholder26_9.empty()
        placeholder27_9.empty()
        placeholder28_9.empty()
        placeholder29_9.empty()
        placeholder30_9.empty()

      if pivot4==0:

        placeholder34_9.empty()

      else:

        placeholder35_9.empty()
        placeholder36_9.empty()
     
    st.session_state.Procesos=False
    st.session_state.Bonos=False            
    Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)
  
  # ----- Historial ---- #
    
  elif historial_9:

    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()

    if nombre_9=="Basilio Antonio Salazar Nunez":

      placeholder8_9.empty()
      placeholder9_9.empty()
      placeholder10_9.empty()
      placeholder11_9.empty()
    
    elif nombre_9== "Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

      placeholder12_9.empty()
      placeholder13_9.empty()
      placeholder14_9.empty()

      if personal_9=="Todos":

        if pivot1==0:
        
          placeholder15_9.empty()
      
        else:

          placeholder16_9.empty()

      else:

        if pivot2==0:

          placeholder17_9.empty()

        else:

          placeholder18_9.empty()
          placeholder19_9.empty()
          placeholder20_9.empty()
          placeholder21_9.empty()
          placeholder22_9.empty()

    else:
      
      placeholder23_9.empty()
      placeholder24_9.empty()
      placeholder31_9.empty()
      placeholder32_9.empty()
      placeholder33_9.empty()

      if pivot3==0:

        placeholder25_9.empty()

      else:

        placeholder26_9.empty()
        placeholder27_9.empty()
        placeholder28_9.empty()
        placeholder29_9.empty()
        placeholder30_9.empty()

      if pivot4==0:

        placeholder34_9.empty()

      else:

        placeholder35_9.empty()
        placeholder36_9.empty()
     
    st.session_state.Bonos=False
    st.session_state.Historial_Costa_Rica=True
    Historial.Historial_Costa_Rica(usuario,puesto,perfil)

  # ----- Capacitación ---- #
    
  elif capacitacion_9:

    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()

    if nombre_9=="Basilio Antonio Salazar Nunez":

      placeholder8_9.empty()
      placeholder9_9.empty()
      placeholder10_9.empty()
      placeholder11_9.empty()
    
    elif nombre_9== "Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

      placeholder12_9.empty()
      placeholder13_9.empty()
      placeholder14_9.empty()

      if personal_9=="Todos":

        if pivot1==0:
        
          placeholder15_9.empty()
      
        else:

          placeholder16_9.empty()

      else:

        if pivot2==0:

          placeholder17_9.empty()

        else:

          placeholder18_9.empty()
          placeholder19_9.empty()
          placeholder20_9.empty()
          placeholder21_9.empty()
          placeholder22_9.empty()

    else:
      
      placeholder23_9.empty()
      placeholder24_9.empty()
      placeholder31_9.empty()
      placeholder32_9.empty()
      placeholder33_9.empty()

      if pivot3==0:

        placeholder25_9.empty()

      else:

        placeholder26_9.empty()
        placeholder27_9.empty()
        placeholder28_9.empty()
        placeholder29_9.empty()
        placeholder30_9.empty()

      if pivot4==0:

        placeholder34_9.empty()

      else:

        placeholder35_9.empty()
        placeholder36_9.empty()
     
    st.session_state.Bonos=False
    st.session_state.Capacitacion_Costa_Rica=True
    Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

  # ----- Otros Registros ---- #
    
  elif otros_registros_9:
    
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()

    if nombre_9=="Basilio Antonio Salazar Nunez":

      placeholder8_9.empty()
      placeholder9_9.empty()
      placeholder10_9.empty()
      placeholder11_9.empty()
    
    elif nombre_9== "Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

      placeholder12_9.empty()
      placeholder13_9.empty()
      placeholder14_9.empty()

      if personal_9=="Todos":

        if pivot1==0:
        
          placeholder15_9.empty()
      
        else:

          placeholder16_9.empty()

      else:

        if pivot2==0:

          placeholder17_9.empty()

        else:

          placeholder18_9.empty()
          placeholder19_9.empty()
          placeholder20_9.empty()
          placeholder21_9.empty()
          placeholder22_9.empty()

    else:
      
      placeholder23_9.empty()
      placeholder24_9.empty()
      placeholder31_9.empty()
      placeholder32_9.empty()
      placeholder33_9.empty()

      if pivot3==0:

        placeholder25_9.empty()

      else:

        placeholder26_9.empty()
        placeholder27_9.empty()
        placeholder28_9.empty()
        placeholder29_9.empty()
        placeholder30_9.empty()

      if pivot4==0:

        placeholder34_9.empty()

      else:

        placeholder35_9.empty()
        placeholder36_9.empty()
     
    st.session_state.Bonos=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto,perfil)

  # ----- Salir ---- #
    
  elif salir_9:

    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()

    if nombre_9=="Basilio Antonio Salazar Nunez":

      placeholder8_9.empty()
      placeholder9_9.empty()
      placeholder10_9.empty()
      placeholder11_9.empty()
    
    elif nombre_9== "Gabriel Martin Prieto" or nombre_9=="Madeline Hernandez Gamboa":

      placeholder12_9.empty()
      placeholder13_9.empty()
      placeholder14_9.empty()

      if personal_9=="Todos":

        if pivot1==0:
        
          placeholder15_9.empty()
      
        else:

          placeholder16_9.empty()

      else:

        if pivot2==0:

          placeholder17_9.empty()

        else:

          placeholder18_9.empty()
          placeholder19_9.empty()
          placeholder20_9.empty()
          placeholder21_9.empty()
          placeholder22_9.empty()

    else:
      
      placeholder23_9.empty()
      placeholder24_9.empty()
      placeholder31_9.empty()
      placeholder32_9.empty()
      placeholder33_9.empty()

      if pivot3==0:

        placeholder25_9.empty()

      else:

        placeholder26_9.empty()
        placeholder27_9.empty()
        placeholder28_9.empty()
        placeholder29_9.empty()
        placeholder30_9.empty()

      if pivot4==0:

        placeholder34_9.empty()

      else:

        placeholder35_9.empty()
        placeholder36_9.empty()
     
    st.session_state.Ingreso = False
    st.session_state.Bonos=False
    st.session_state.Salir=True
    Salir.Salir()
