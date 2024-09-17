ADMIN_USERS = {
    'vera_1029@outlook.com',
    'oldhomeless@gmail.com',
    'oldhomeless@yahoo.com'
}
if st.experimental_user.email in ADMIN_USERS:
    display_the_extra_admin_buttons()
display_the_interface_everyone_sees()