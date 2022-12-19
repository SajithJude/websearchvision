import streamlit as st
import streamlit.components.v1 as components

st.title("Face tracking using face landmark detectioon using googles opensource mediapipe framework..")
# """
# This demo would just capture the incput from camera and and detect allavailable landmarks on te humanface,
# and would connect all points that would make it seem like a mesh, I havent found any usecases for this at the moment, 
# But I feel it could make some impact on drowsiness detection during online lectures and attention tracking
# """

components.html(
    """

<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="https://cdn.jsdelivr.net/gh/hiukim/mind-ar-js@1.1.5/dist/mindar-image.prod.js"></script>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/donmccurdy/aframe-extras@v6.1.1/dist/aframe-extras.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/hiukim/mind-ar-js@1.1.5/dist/mindar-image-aframe.prod.js"></script>
  </head>
  <body>
    <a-scene mindar-image="imageTargetSrc: targets1.mind;" color-space="sRGB" renderer="colorManagement: true, physicallyCorrectLights" vr-mode-ui="enabled: false" device-orientation-permission-ui="enabled: false">
      <a-assets>
        <a-asset-item id="robot" src="models/robot.glb"></a-asset-item>
        <a-asset-item id="raccoonModel" src="https://cdn.jsdelivr.net/gh/hiukim/mind-ar-js@1.1.5/examples/image-tracking/assets/band-example/raccoon/scene.gltf"></a-asset-item>
         <video
          id="video"
          preload="auto"
          src="video/robot-info.mp4" 
          autoplay
          loop="true"
          crossorigin="anonymous"
          width="1"
          height="0.552"
          webkit-playsinline
        ></video>
      </a-assets>

      <a-camera position="0 0 0" look-controls="enabled: false"></a-camera>

      <a-entity
        mindar-image-target="targetIndex: 1"
        material="shader: flat; src: #video"
        geometry="primitive: plane; width: 1.5; height: 1"
        position="0 0 0"
        rotation="0 0 0"
        play-on-click
        visible="false"
      >
      </a-entity>
      <a-entity mindar-image-target="targetIndex: 0">
        <a-gltf-model rotation="0 0 0 " position="0 -0.5 0" scale="0.5 0.5 0.5" src="#robot" animation-mixer>
      </a-entity>
    </a-scene>
    <script>
    
      var vimeoPlayer = document.querySelector('#video');
      var i=0;
      window.addEventListener('click', function () { 
          if(i%2==0)
          {
              vimeoPlayer.play();
          }else
          {
              vimeoPlayer.pause();
          }
          i++
      });

    </script>
  </body>
</html>


      """,
      height=420, width=1200
    
)