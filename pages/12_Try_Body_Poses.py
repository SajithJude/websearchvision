import streamlit as st

import streamlit.components.v1 as components


components.html(
    """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/control_utils/control_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/control_utils_3d/control_utils_3d.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils/drawing_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/pose/pose.js" crossorigin="anonymous"></script>
</head>

<body>
  <div class="container">
    <video class="input_video"></video>
    <canvas class="output_canvas" width="1280px" height="720px"></canvas>
    <div class="landmark-grid-container"></div>
  </div>


<script type="module">
const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');
const landmarkContainer = document.getElementsByClassName('landmark-grid-container')[0];
const grid = new LandmarkGrid(landmarkContainer);

function onResults(results) {
  if (!results.poseLandmarks) {
    grid.updateLandmarks([]);
    return;
  }

  canvasCtx.save();
  canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
  canvasCtx.drawImage(results.segmentationMask, 0, 0,
                      canvasElement.width, canvasElement.height);

  // Only overwrite existing pixels.
  canvasCtx.globalCompositeOperation = 'source-in';
  canvasCtx.fillStyle = '#00FF00';
  canvasCtx.fillRect(0, 0, canvasElement.width, canvasElement.height);

  // Only overwrite missing pixels.
  canvasCtx.globalCompositeOperation = 'destination-atop';
  canvasCtx.drawImage(
      results.image, 0, 0, canvasElement.width, canvasElement.height);

  canvasCtx.globalCompositeOperation = 'source-over';
  drawConnectors(canvasCtx, results.poseLandmarks, POSE_CONNECTIONS,
                 {color: '#00FF00', lineWidth: 4});
  drawLandmarks(canvasCtx, results.poseLandmarks,
                {color: '#FF0000', lineWidth: 2});
  canvasCtx.restore();

  grid.updateLandmarks(results.poseWorldLandmarks);
}

const pose = new Pose({locateFile: (file) => {
  return `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`;
}});
pose.setOptions({
  modelComplexity: 1,
  smoothLandmarks: true,
  enableSegmentation: true,
  smoothSegmentation: true,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
});
pose.onResults(onResults);

const camera = new Camera(videoElement, {
  onFrame: async () => {
    await pose.send({image: videoElement});
  },
  width: 1280,
  height: 720
});
camera.start();
</script>
</body>
</html>
    """,
    height=600,
)

# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb


# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))


# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)


# def layout(*args):

#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
#      .stApp { bottom: 105px; }
#     </style>
#     """

#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         color="black",
#         text_align="center",
#         height="auto",
#         opacity=1
#     )

#     style_hr = styles(
#         display="block",
#         margin=px(8, 8, "auto", "auto"),
#         border_style="inset",
#         border_width=px(2)
#     )

#     body = p()
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)

#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)

# def footer():
#     myargs = [
#         "Made with ❤️ from ",
        
#         link("www.instancy.com","Instancy Inc"),
#         br(),
#     ]
#     layout(*myargs)


# if __name__ == "__main__":
#     st.caption("Point your camera to a picture of a body pose or take your own video. Then click on try it, by pointing the camera at yourself to find out if you did the pose correctly.​")
#     col1,col2  = st.columns(2)
#     with col1:
#         st.write("Trainer video")
#         st.video("https://www.youtube.com/watch?v=IODxDxX7oi4")
#         # st.write(gl)

#     with col2:
#         # st.header("Detected Entities")
#         # st.write(ent)
#         img_file_buffer = st.camera_input("Try it")
#         if img_file_buffer is not None:
#             st.image(img_file_buffer)
#             # encoded_image = base64.b64encode(img_file_buffer.read())
#             # result = callAPI(encoded_image)
#     footer()