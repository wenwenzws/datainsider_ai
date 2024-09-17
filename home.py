import streamlit as st

def app():
    st.header('Profit maker tools for your business')
    
    header1, header2 = st.columns([0.75, 3])
    with header1:
        container1 = st.container(border=True)   
        container1.image('images/moneylogo.jpeg', width=100)
  
    st.header(' :green[Getting Started!!]')
    col1, col2 = st.columns([2, 3])
    #col1.video('simu.mp4')  
    col2.markdown(' **The best platform for monitoring your business** ')
    col2.markdown('''The secret for top performer owners!''')
    col2.markdown('''Our platform is designed to help you monitor your business performance, track your sales, and manage your inventory, make more profit!''') 
    col2.write('[Learn More](https://wa.link/p7ke9l)')
    with col2:
        col5, col6 = st.columns(2)
        col5.button(' :green[**Sign Up**]', use_container_width=True)
        


    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    mid1, mid2, mid3 = st.columns([4, 2, 4])
    mid2.subheader('Explore')
    mid6, mid7, mid8 = st.columns([0.5, 15, 0.5])
    mid7.write('**Get to know how to get started, save money and make profit.**')

    mid4, mid5 = st.columns([3,4])
    #st.video('MWANACHUO.mp4')
    #st.caption("DISCLAIMER: Photo was taken from twitter acc UDSM ICON")
    st.write(' ### ')
    container = st.container(border=True)
    with container:
        col1, col2 = st.columns([4,2])
        col1.subheader(':green[**Subscribe to our newsletter**] ')
        col1.write('**Get our real time updates**')
        col2.text_input(label='', placeholder='Your Email')
        col2.button("Subscribe")
    st.write(' ### ')
    st.markdown(''' This easy tool will help you with your sales and employee management''')
    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('datainsiderai.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')
