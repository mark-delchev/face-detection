# Face detection app
## Main features
- Drawing green rectangles if any faces are detected in a video or an image
- Detecting multiple faces in an image
- Detecting if there are no faces in an image
- Detecting faces in a video or live with your webcam
- To close the webcam press 'q'
## Technologies used
- This app is made with the OpenCV Computer Vision Library and Python
## Detection results
- Detecting a single face and multiple faces
<style>
    .column {
  float: left;
  width: 33.33%;
  padding: 5px;
    }
    .row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
<div class="row">
    <div class="column">
        <img src="https://i.imgur.com/bh2TeUs.png" width = 100%>
    </div>
    <div class="column">
        <img src="https://i.imgur.com/Yprq2lO.png" width = 100%>
    </div>
</div>


## How to build
- Linux
1. Install <strong>pyinstaller</strong> with the command:
```
pip install pyinstaller
```
2. You can build the app for your specific distro using the command:
```
pyinstaller --onefile name.py
```
- Widnows
1. Install <strong>auto-py-to-exe</strong> with the command:
```
pip install auto-py-to-exe
```
2. Build the app from the GUI
<hr></hr>
<h1 align="center">Thank you for reading.</h1>
