import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def game1():
    df=pd.read_csv('money.csv')
    
    with st.form('my form'):
        money=st.number_input('Enter money',step=None,value=df['money'][0])
        angle1=st.number_input('Enter angle between 29 and 71(angle 1(red))',min_value=30,max_value=70)
        angle2=st.number_input('Enter angle between 29 and 71(angle 2(green))',min_value=30,max_value=70)
        submitted=st.form_submit_button('submit')
        if submitted:
            dot_x=np.random.uniform(0,3)
            dot_y=np.random.uniform(0,3)
            fig, ax = plt.subplots()
            ax.plot([3,0],[0,0],color='b')
            ax.plot([0,3*np.cos(angle1*np.pi/180)],[0,3*np.sin(angle1*np.pi/180)],label=str(angle1)+'°',color='r')
            ax.plot([0,3*np.cos(angle2*np.pi/180)],[0,3*np.sin(angle2*np.pi/180)],label=str(angle2)+'°',color='g')
            plt.xticks([])
            plt.yticks([])
            plt.scatter(dot_x,dot_y,color='black')
            plt.legend(loc='best')
            st.pyplot(fig)


            sr=(3*np.sin(angle1*np.pi/180))/(3*np.cos(angle1*np.pi/180))#slope of red line
            sg=(3*np.sin(angle2*np.pi/180))/(3*np.cos(angle2*np.pi/180))#slope of green line
            sd=dot_y/dot_x#slope of dot
            st.write(f'red slope {sr}')
            st.write(f'green slope {sg}')
            st.write(f'dot slope {sd}')

            angle=lambda m1,m2:np.abs(m1-m2)/(1+(m1*m2))
           


            if math.degrees(math.atan(angle(sr,sd)))<math.degrees(math.atan(angle(sg,sd))):
                st.write('dot is more closer to red')
                df['money'][0]=money-10
                df.to_csv('money.csv',index=False)
                file=pd.read_csv('money.csv')
                st.write('Current money',file['money'][0],'(-10)')
                

            elif math.degrees(math.atan(angle(sr,sd)))>math.degrees(math.atan(angle(sg,sd))):
                st.write('dot is more closer to green')
                df['money'][0]=money+10
                df.to_csv('money.csv',index=False)
                file=pd.read_csv('money.csv')
                st.write('Current money',file['money'][0],'(+10)')
            elif math.degrees(math.atan(angle(sr,sd)))==math.degrees(math.atan(angle(sg,sd))):
                st.write('dot is equidistant from red and green lines')
            
    st.button('Reload Game')
    
game1()


