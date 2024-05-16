# ----- Librerías ---- #

import streamlit as st
import pandas as pd
from PIL import Image
import Autenticacion, Procesos

# ----- Reingreso ---- #

def Salir():

    if st.session_state.Salir==True:

        # ----- Conexión, Botones y Memoria ---- #

        uri=st.secrets.db_credentials.URI

        pivot=0 # Se requiere para mantener las indicaciones generales en caso de errores de ingreso

        placeholder1_6= st.sidebar.empty()
        titulo_6= placeholder1_6.title("Ingreso")

        placeholder2_6= st.sidebar.empty()
        usuario=placeholder2_6.text_input("Usuario",key="usuario_6")

        placeholder3_6= st.sidebar.empty()
        contraseña_6 = placeholder3_6.text_input("Contraseña", type = 'password', key="contraseña_6")

        placeholder4_6 = st.sidebar.empty()
        iniciar_sesion_6 = placeholder4_6.button("Iniciar sesión",key="iniciar_sesion_6")

        if "Ingreso" not in st.session_state:
            st.session_state.Ingreso = False

        if st.session_state.Ingreso:

            st.session_state.Ingreso=True
            placeholder1_6.empty()
            placeholder2_6.empty()
            placeholder3_6.empty()
            placeholder4_6.empty()

            puesto=pd.read_sql(f"select puesto from usuarios where usuario ='{usuario}'",uri)
            puesto= puesto.loc[0,'puesto']

            perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
            perfil= perfil.loc[0,'perfil']

            if perfil=="Costa Rica":        
                
                Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)
            
            elif perfil=="Argentina":        
                
                Procesos.Procesos_Argentina(usuario,puesto,perfil)   

            pivot=pivot + 1

        # ----- Validación ---- #

        if iniciar_sesion_6:

            if usuario == '' or contraseña_6 == '':
                st.error('Favor ingresar sus credenciales')

            else:
                
                contraseña= Autenticacion.contraseña(usuario)

                if contraseña.empty:
                    st.error('El usuario no existe, intente de nuevo')

                else:

                    contraseña = contraseña.loc[0,'contraseña']

                    if contraseña == contraseña_6:

                        nombre_6=pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
                        nombre_6 = nombre_6.loc[0,'nombre']
                        st.success(f'¡Bienvenido {nombre_6}!')

                        placeholder1_6.empty()
                        placeholder2_6.empty()
                        placeholder3_6.empty()
                        placeholder4_6.empty()

                        st.session_state.Procesos=False
                        st.session_state.Historial_Costa_Rica=False
                        st.session_state.Historial_Argentina=False
                        st.session_state.Capacitacion_Costa_Rica=False
                        st.session_state.Capacitacion_Argentina=False
                        st.session_state.Otros_Registros=False
                        st.session_state.Bonos=False
                        st.session_state.Salir=False
                        st.session_state.Parcelas_Costa_Rica=False
                        st.session_state.Parcelas_Argentina=False
                        st.session_state.Cubiertas_Mejoras_Costa_Rica=False
                        st.session_state.Cubiertas_Mejoras_Argentina=False

                        perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
                        perfil= perfil.loc[0,'perfil']

                        if perfil=="Costa Rica":        
                            
                            Procesos.Procesos_Costa_Rica(usuario,puesto,perfil)
                        
                        elif perfil=="Argentina":        
                            
                            Procesos.Procesos_Argentina(usuario,puesto,perfil)   

                        pivot=pivot + 1
             
                    else:
                        st.error('Contraseña incorrecta, intente de nuevo')

        # ----- Mensajes Generales ---- #
                 
        if pivot!=1:
    
            st.image(Image.open("logo.png"))

            st.title("Telespazio Argentina S.A.")

            st.header("Aplicación de uso exclusivo para el personal de Telespazio Argentina S.A.")

            st.subheader("Para soporte técnico favor escribir a basilio.nunez@telespazio.com")
