import streamlit as st

import streamlit.components.v1 as components


components.html(
  """
<div>
  <div style="display: flex; flex-direction: column; align-items: center;">
    <button id="container-expand" style="background-color: #3399FF; color: white; padding: 10px; border-radius: 5px; font-size: 1rem; margin: 8px;"> Expand Container </button>
    <div id="container" style="display: flex; width: 100%; max-height: 0px; overflow: hidden; transition: max-height 0.5s ease-out;">
      <!-- content of the container goes here -->
    </div>
  </div>
</div>

<script>
  const expandButton = document.getElementById('container-expand');
  const container = document.getElementById('container');

  expandButton.addEventListener('click', () => {
    if (container.style.maxHeight === '0px') {
      container.style.maxHeight = '100vh';
    } else {
      container.style.maxHeight = '0px';
    }
  });
</script>


  """
)