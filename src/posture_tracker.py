import cv2
import mediapipe as mp
import time
import math
import os

# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def get_photo_info():
    pass

# METHODS
# warns user when poor posture is detected over a certain time period.
def sendWarning(title, message):
	pass
  
# finds the distance between 2 coordinates, a and b
def findDistance(a_x, a_y, b_x, b_y):
    return math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)

def findMidpoint(a_x, a_y, b_x, b_y):
    return (int((a_x + b_x) / 2.0), int((a_y + b_y) / 2.0))

def check_shoulder2shoulder(s1_x, s1_y, s2_x, s2_y, benchmark_dist, max_pct):
    curr_dist = findDistance(s1_x, s1_y, s2_x, s2_y)
    if (math.abs(curr_dist - benchmark_dist)) / benchmark_dist > max_pct:
        return True # True means bad posture
    else:
        return False

def check_head2neckbase(a_x,a_y, b_x, b_y, benchmark_dist, max_pct):
  curr_dist = findDistance(a_x,a_y, b_x, b_y)
  return math.abs(curr_dist - benchmark_dist) / benchmark_dist > max_pct

def check_headtilt(shoulder1_x, shoulder1_y, shoulder2_x, shoulder2_y, head_x, head_y, max_degree):
    m_x, m_y = findMidpoint(shoulder1_x, shoulder1_y, shoulder2_x, shoulder2_y)
  
    v1_x = shoulder1_x - shoulder2_x
    v1_y = shoulder1_y - shoulder2_y
  
    v2_x = head_x - m_x
    v2_y = head_y - m_y
  
    # find degree angle between v1 and v2.
    # dotproduct(v1,v2) / magnitude(v1) * magnitude(v2)
    dot_product = ( (v1_x)*(v2_x) + (v1_y)*(v2_y) )
    theta = math.acos( dot_product / (math.sqrt((v1_y - v1_x)**2 + (v2_y - v2_x)**2) * v2_x ) )
    degree = int(180/math.pi)*theta
    return math.abs(degree - 90) > max_degree

  
def benchmark_photo(image):

    # Get height and width.
    h, w = image.shape[:2]

    # Convert the BGR image to RGB.
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # image = cv2.resize(image, None, interpolation=cv2.INTER_AREA)
    
    # image_output = cv2.ImageWriter("analysed_img.png", (h,w))  ### ?

    ###
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # cv2.imshow('Posture Tracker', image)

    # Convert the image back to BGR.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image.
    keypoints = pose.process(image)

    # Use lm and lmPose as representative of the following methods.
    lm = keypoints.pose_landmarks
    lmPose = mp_pose.PoseLandmark

    try:
        # Acquire the landmark coordinate of the necessary body parts
        # (Head, Neck, Shoulder, Ears, etc.)
        # Once aligned properly, left or right should not be a concern.
        # Left shoulder.
        l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
        l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
        # Right shoulder
        r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
        r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
        # Left ear.
        l_ear_x = int(lm.landmark[lmPose.LEFT_EAR].x * w)
        l_ear_y = int(lm.landmark[lmPose.LEFT_EAR].y * h)
        # Right ear.
        l_ear_x = int(lm.landmark[lmPose.RIGHT_EAR].x * w)
        l_ear_y = int(lm.landmark[lmPose.RIGHT_EAR].y * h)

        nose_x = int(lm.landmark[lmPose.NOSE].x * w)
        nose_y = int(lm.landmark[lmPose.NOSE].y * h)

        print("L SHOULDER", l_shldr_x, l_shldr_y)
        print("R SHOULDER", r_shldr_x, r_shldr_y)
        print("L EAR", l_ear_x, l_ear_y)
        print("L EAR", l_ear_x, l_ear_y)

        print("X NOSE", nose_x)
        print("Y NOSE", nose_y)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        shoulder_midpoint = findMidpoint(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)
        shoulder_distance = findDistance(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)

        # analysis - point landmarks
        image = cv2.circle(image, (l_shldr_x, l_shldr_y), 7, (255, 255, 0), -1)
        image = cv2.circle(image, (r_shldr_x, r_shldr_y), 7, (255, 255, 0), -1)
        image = cv2.circle(image, (nose_x, nose_y), 7, (255, 255, 0), -1)
        image = cv2.circle(image, (shoulder_midpoint), 7, (255, 255, 0), -1)
        
        # analysis - join landmarks
        image = cv2.line(image, (l_shldr_x, l_shldr_y), (r_shldr_x, r_shldr_y), (0, 255, 0), 4)
        image = cv2.line(image, (shoulder_midpoint), (nose_x, nose_y), (0, 255, 0), 4)
        image = cv2.line(image, (l_shldr_x, l_shldr_y), (nose_x, nose_y), (0, 255, 0), 4)
        image = cv2.line(image, (r_shldr_x, r_shldr_y), (nose_x, nose_y), (0, 255, 0), 4)

        # to add later: angles, figures
        
        
        # return analysed_picture (picture with shoulder, head points)

        # cv2.imshow("Analysed image", image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # This function will send to UI:
        return image

    except AttributeError as ae:
        pass
  

  
  	# UI will do:
    # cv2.imshow("Analysed Benchmark Posture", image)
    
    # also consider sending figures such as lengths, angles
    


def main():
    # take webcam input
    cap = cv2.VideoCapture(0)

    # Meta.
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (width, height)

    while cap.isOpened():
        # Capture frames.
        success, image = cap.read()
        if not success:
            print("Null.Frames")
            break
        # Get fps.
        fps = cap.get(cv2.CAP_PROP_FPS)
        # Get height and width.
        h, w = image.shape[:2]

        # Convert the BGR image to RGB.
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        ###
        # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Posture Tracker', image)

        c = cv2.waitKey(1)
        if c == 27:
            break
        ###

        # Process the image.
        keypoints = pose.process(image)

        # Convert the image back to BGR.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Use lm and lmPose as representative of the following methods.
        lm = keypoints.pose_landmarks
        lmPose = mp_pose.PoseLandmark

        try:
            # Acquire the landmark coordinate of the necessary body parts
            # (Head, Neck, Shoulder, Ears, etc.)
            # Once aligned properly, left or right should not be a concern.
            # Left shoulder.
            l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
            l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
            # Right shoulder
            r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
            r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
            # Left ear.
            l_ear_x = int(lm.landmark[lmPose.LEFT_EAR].x * w)
            l_ear_y = int(lm.landmark[lmPose.LEFT_EAR].y * h)
            # Right ear.
            l_ear_x = int(lm.landmark[lmPose.RIGHT_EAR].x * w)
            l_ear_y = int(lm.landmark[lmPose.RIGHT_EAR].y * h)

            nose_x = int(lm.landmark[lmPose.NOSE].x * w)
            nose_y = int(lm.landmark[lmPose.NOSE].y * w)

            print("L SHOULDER", l_shldr_x, l_shldr_y)
            print("R SHOULDER", r_shldr_x, r_shldr_y)
            print("L EAR", l_ear_x, l_ear_y)
            print("L EAR", l_ear_x, l_ear_y)

            print("X NOSE", nose_x)
            print("Y NOSE", nose_y)

            shoulder_midpoint = findMidpoint(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)

            # Calculate distance between left shoulder and right shoulder points.
            shoulder_distance = findDistance(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)
            # Assist to align the camera to point at the side view of the person.
            # shoulder_distance threshold 30 is based on results obtained from analysis over 100 samples.
            # if shoulder_distance < 100:
            #     # we dont need to put texts, we just need to record this information for future decisions.
            #     pass
            # else:
            #     pass

            # Determine whether good posture or bad posture.
            # The threshold angles have been set based on intuition.
            # bad_frames = 0
            # good_frames = 0
            # if x:
            #     bad_frames = 0
            #     good_frames += 1
            #
            # else:
            #     good_frames = 0
            #     bad_frames += 1

            # Calculate the time of remaining in a particular posture.
            # good_time = (1 / fps) * good_frames
            # bad_time =  (1 / fps) * bad_frames
            #
            # # Pose time.
            # if good_time > 0:
            #     time_string_good = 'Good Posture Time : ' + str(round(good_time, 1)) + 's'
            # else:
            #     time_string_bad = 'Bad Posture Time : ' + str(round(bad_time, 1)) + 's'

            # If you stay in bad posture for more than 15s send an alert.
            # if bad_time > 15:
            #     sendWarning()
        except AttributeError as ae:
            pass

if __name__ == "__main__":
    main()