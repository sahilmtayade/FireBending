---
layout: default
---
# FireBending

FireBending VFX using pure Numpy Classical Computer Vision Algorithms.
[@EthanHarp](https://github.com/EthanHarp) was my teammate in charge of the steam notebook.

## Short Unoptimized Combined Demo

You can see in this demo how the code that takes the dot product of velocity and median direction vectors prevents me from blasting my own face at the end, as my speed was high enough to produce flames!
<video width="640" height="360" controls>
  <source src="https://github.com/sahilmtayade/FireBending/raw/main/CVSteam_and_fire.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


Currently the steam and fire parts are separate notebooks, so you will have to take the steam output and read that in before calling the draw function in the fire notebook. But make sure to run all the other calculation cells in the fire notebook with the original video! Sorry about that; finals and job searches keep me busy.

## Methods Used

### Mean Shift Tracking for Hand Detection

We utilized Mean Shift tracking to accurately detect and track the position of hands in each frame of the video. This algorithm provides a robust approach for object tracking, making it suitable for real-time applications.

### Linear Algebra Dot Product for Motion Analysis

The dot product of velocity and median direction vectors was employed to determine if hands are moving outwards or inwards. This technique helped in triggering the fire effects based on the motion characteristics of the hands.

### Motion History Image (MHI) for Steam Effect Timing

Motion History Image (MHI) was employed to determine when to trigger steam effects based on the total amount of motion in an N-frame chunk. This method enhances the visual realism of the steam effects.

### Edge Detection for Steam Placement

Edge detection algorithms were used to find suitable positions for placing the steam effects. This approach enhances the accuracy of steam placement and contributes to the overall visual quality of the effects.

> "The combination of these methods creates a dynamic and visually engaging FireBending effect using classical computer vision algorithms."

