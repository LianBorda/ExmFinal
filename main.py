import cv2
import math
import mediapipe as mp
import time 

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture("def.mp4")

def angulo(lm1,lm2,lm3):
    print("Puntos de referencia: ", lm1,lm2,lm3)
    x1, y1 = lm1
    x2, y2 = lm2
    x3, y3 = lm3
    angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2, x1-x2))
    if angle <= 0:
        angle += 360
    print("Angulo entre los puntos: ", angle)
    return angle


def angulo_brazo_izq():
    x1 = int(results.pose_landmarks.landmark[11].x * width)
    y1 = int(results.pose_landmarks.landmark[11].y * height)
    lm1 = x1, y1 

    x2 = int(results.pose_landmarks.landmark[13].x * width)
    y2 = int(results.pose_landmarks.landmark[13].y * height)
    lm2 = x2, y2
                
    x3 = int(results.pose_landmarks.landmark[15].x * width)
    y3 = int(results.pose_landmarks.landmark[15].y * height)
    lm3 = x3, y3
    #cv2.circle(frame, (x1,y1), 2, (255,0,0), 1)
    #cv2.circle(frame, (x2,y2), 2, (255,0,0), 1)
    #cv2.circle(frame, (x3,y3), 2, (255,0,0), 1)
    angle = angulo(lm1,lm2,lm3)
    print("Este es el angulo: ", angle)
    return angle
    

def angulo_brazo_der():
    x1 = int(results.pose_landmarks.landmark[12].x * width)
    y1 = int(results.pose_landmarks.landmark[12].y * height)
    lm1 = x1, y1 

    x2 = int(results.pose_landmarks.landmark[14].x * width)
    y2 = int(results.pose_landmarks.landmark[14].y * height)
    lm2 = x2, y2
                
    x3 = int(results.pose_landmarks.landmark[16].x * width)
    y3 = int(results.pose_landmarks.landmark[16].y * height)
    lm3 = x3, y3
    #cv2.circle(frame, (x1,y1), 2, (255,0,0), 1)
    #cv2.circle(frame, (x2,y2), 2, (255,0,0), 1)
    #cv2.circle(frame, (x3,y3), 2, (255,0,0), 1)
    angle = angulo(lm1,lm2,lm3)
    return angle

def angulo_dorso_izq():
    x1 = int(results.pose_landmarks.landmark[13].x * width)
    y1 = int(results.pose_landmarks.landmark[13].y * height)
    lm1 = x1, y1 

    x2 = int(results.pose_landmarks.landmark[11].x * width)
    y2 = int(results.pose_landmarks.landmark[11].y * height)
    lm2 = x2, y2
                
    x3 = int(results.pose_landmarks.landmark[23].x * width)
    y3 = int(results.pose_landmarks.landmark[23].y * height)
    lm3 = x3, y3
    #cv2.circle(frame, (x1,y1), 2, (255,0,0), 1)
    #cv2.circle(frame, (x2,y2), 2, (255,0,0), 1)
    #cv2.circle(frame, (x3,y3), 2, (255,0,0), 1)
    angle = angulo(lm1,lm2,lm3)
    return angle

def angulo_dorso_der():
    x1 = int(results.pose_landmarks.landmark[14].x * width)
    y1 = int(results.pose_landmarks.landmark[14].y * height)
    lm1 = x1, y1 

    x2 = int(results.pose_landmarks.landmark[12].x * width)
    y2 = int(results.pose_landmarks.landmark[12].y * height)
    lm2 = x2, y2
                
    x3 = int(results.pose_landmarks.landmark[24].x * width)
    y3 = int(results.pose_landmarks.landmark[24].y * height)
    lm3 = x3, y3
    #cv2.circle(frame, (x1,y1), 2, (255,0,0), 1)
    #cv2.circle(frame, (x2,y2), 2, (255,0,0), 1)
    #cv2.circle(frame, (x3,y3), 2, (255,0,0), 1)
    angle = angulo(lm1,lm2,lm3)
    return angle


with mp_pose.Pose(static_image_mode=False) as pose:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        if results.pose_landmarks is not None:
            indicador = "Desconocido"
            color_señal = (0,0,255)
            #mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            #mp_drawing.DrawingSpec(color = (128, 0, 250), thickness=1, circle_radius = 1))
            angulo_bi = angulo_brazo_izq() #Angulo del brazo izquierdo
            angulo_bd = angulo_brazo_der()  #Angulo del brazo derecho
            angulo_di = angulo_dorso_izq()  #Angulo del dorso izquierdo
            angulo_dd = angulo_dorso_der()  #Angulo del dorso derecho
            
            if angulo_bi >= 140 and angulo_di >=60 and angulo_di<=110 :
                indicador = "Giro a la Izquierda"
                color_señal = (0,255,0)
            elif angulo_bd >= 140 and angulo_dd>=230 and angulo_dd <=285 :
                indicador = "Giro a la Derecha"
                color_señal = (0,255,0)
            elif angulo_bd >= 140 and angulo_dd>=100 and angulo_dd <=260:
                indicador = "Stop"
                color_señal = (0,255,0)
            elif angulo_bd >= 140 and angulo_dd>=260 and angulo_dd <=325:
                indicador = "Reducir Velocidad"
                color_señal = (0,255,0)
            elif angulo_bd >= 140 and angulo_dd>=325 and angulo_dd <=333:
                indicador = "Obstaculo a la Derecha"
                color_señal = (0,255,0)
            elif angulo_bi >= 140 and angulo_di>=40 and angulo_di <=45:
                indicador = "Obstaculo a la Izquierda"
                color_señal = (0,255,0) 
            elif angulo_bi >= 30 and angulo_bi<=140 and angulo_di>=180 and angulo_di <=360:
                indicador = "Adelantar"
                color_señal = (0,255,0)        
            

                
            print("Este es el angulo brazo izq:", angulo_bi)
            print("Este es el angulo brazo der: ", angulo_bd)
            print("Este es el angulo dorzo izq: ", angulo_di)
            print("Este es el angulo dorzo der: ", angulo_dd,"\n")
            cv2.rectangle(frame,(0,0),(frame.shape[1],30), (0,0,0), cv2.FILLED)
            cv2.putText(frame,indicador,(8,20), cv2.FONT_HERSHEY_COMPLEX,0.7,color_señal)
        cv2.imshow("Señales Ciclistas", frame)
        if cv2.waitKey(1) == 27:
            break




