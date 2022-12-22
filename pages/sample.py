import streamlit as st

expanded = False

def render():
  global expanded
  if expanded:
    st.markdown(
      """




      <div class="footer">
        <p>&copy; 2020 Company</p>
    
          <a href="www.company.com/about">About</a>
          <a href="www.company.com/contact">Contact</a>

      </div>
      """
    , unsafe_allow_html=True)
  else:
    st.markdown(
      """
      <div class="footer">
        <p>&copy; 2020 Company</p>
      </div>
      """
    , unsafe_allow_html=True)
    if st.button('Expand Footer'):
      expanded = True

render()