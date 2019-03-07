Instructions:

1) Firstly, you have to create a gesture database. 
For that, run 'create_gest.py'. Enter the gesture name and you will get 2 frames displayed. Look at the contour frame and adjust your hand to make sure that you capture the features of your hand. Press 'c' for capturing the images. It will take 1200 images of one gesture. 

2) Repeat this for all the features you want.


3) Run 'create_csv.py' for converting the images to a CSV file


4) If you want to train the model, run 'train_emojinator.py'


5) Finally, run 'emojinator.py' for testing your model via webcam.