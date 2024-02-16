# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos, Salir,Parcelas,Cubiertas_Mejoras

# ----- Procesos Costa Rica ---- #

def Procesos_Costa_Rica(usuario,puesto,perfil):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False: 

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        procesos_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        parcelas_2 = placeholder8_2.button("Parcelas",key="parcelas_2")

        placeholder9_2 = st.empty()
        cubiertas_mejoras_2 = placeholder9_2.button("Cubiertas y Mejoras",key="cubiertas_mejoras_2")

        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial_Costa_Rica=True
            Historial.Historial_Costa_Rica(usuario,puesto,perfil)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion_Costa_Rica=True
            Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto,perfil)

        # ----- Bonos ---- #

        elif bonos_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto,perfil)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Ingreso= False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Parcelas Costa Rica ---- #

        elif parcelas_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Parcelas_Costa_Rica=True
            Parcelas.Parcelas_Costa_Rica(usuario,puesto,perfil)

        # ----- Cubiertas y Mejoras Costa Rica---- #

        elif cubiertas_mejoras_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Cubiertas_Mejoras_Costa_Rica=True
            Cubiertas_Mejoras.Cubiertas_Mejoras_Costa_Rica(usuario,puesto,perfil)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial_Costa_Rica==True:
            Historial.Historial_Costa_Rica(usuario,puesto,perfil)

        elif st.session_state.Capacitacion_Costa_Rica==True:
            Capacitacion.Capacitacion_Costa_Rica(usuario,puesto,perfil)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto,perfil)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto,perfil)

        elif st.session_state.Parcelas_Costa_Rica==True:
            Parcelas.Parcelas_Costa_Rica(usuario,puesto,perfil)

        elif st.session_state.Cubiertas_Mejoras_Costa_Rica==True:
            Cubiertas_Mejoras.Cubiertas_Mejoras_Costa_Rica(usuario,puesto,perfil)

# ----- Procesos Argentina ---- #

def Procesos_Argentina(usuario,puesto,perfil):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False:

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2= st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        salir_2 = placeholder4_2.button("Salir",key="salir_2")

        placeholder5_2 = st.empty()
        procesos_2 = placeholder5_2.title("Procesos")

        placeholder6_2 = st.empty()
        parcelas_2 = placeholder6_2.button("Parcelas",key="parcelas_2")

        placeholder7_2 = st.empty()
        cubiertas_mejoras_2 = placeholder7_2.button("Cubiertas y Mejoras",key="cubiertas_mejoras_2")
        
        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial_Argentina=True
            Historial.Historial_Argentina(usuario,puesto,perfil)

                # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion_Argentina=True
            Capacitacion.Capacitacion_Argentina(usuario,puesto,perfil)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            st.session_state.Ingreso = False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Parcelas Argentina ---- #

        elif parcelas_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            st.session_state.Procesos=True
            st.session_state.Parcelas_Argentina=True
            Parcelas.Parcelas_Argentina(usuario,puesto,perfil)

        # ----- Cubiertas y Mejoras Argentina---- #

        elif cubiertas_mejoras_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            st.session_state.Procesos=True
            st.session_state.Cubiertas_Mejoras_Argentina=True
            Cubiertas_Mejoras.Cubiertas_Mejoras_Argetnina(usuario,puesto,perfil)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial_Argentina==True:
            Historial.Historial_Argentina(usuario,puesto,perfil)

        if st.session_state.Capacitacion_Argentina==True:
            Capacitacion.Capacitacion_Argentina(usuario,puesto,perfil)

        elif st.session_state.Parcelas_Argentina==True:
            Parcelas.Parcelas_Argentina(usuario,puesto,perfil)

        elif st.session_state.Cubiertas_Mejoras_Argentina==True:
            Cubiertas_Mejoras.Cubiertas_Mejoras_Argentina(usuario,puesto,perfil)
