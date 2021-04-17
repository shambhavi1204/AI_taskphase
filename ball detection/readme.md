Object detection involves the concept of object identification and location in a image. It involves two problems image classification and identifying the location of the object which is called localization.
In image tracking the the object and its location is identified from every frame of the video.
We can use segmentation by color meathod for the same purpose. In this we reduce the patches of classification based on the color of the ball. if we can determine the color of the ball we can easily differenciate the paches which taly with the color of the ball.
In opencv the following steps are followed to detect and trace a ball:
1)detect the presence of the ball
2)track the ball as it moves around the video frame and drawing its previous position as it moves.
