# Examen Final
*Santiago Salguero

*Lian Camilo Borda

# Proyecto: 

Resumen

En este proyecto, se realiza una detección de pose 3D usando la biblioteca mediapipe en Python. Después de eso, calcularemos los ángulos entre las articulaciones del cuerpo y los combinaremos con algunas heurísticas para crear un sistema de clasificación de señalizaciones mas usadas por los ciclistas cuandovan en la via. 

Todo esto funcionará mediante el uso de videos y esta planteado para que luego se pueda usar en tiempo real mediante el uso de una  camara en la parte frotal del ciclista. 

![image](https://user-images.githubusercontent.com/81332414/137357760-ed5d8cf4-7f53-45b2-8604-88dff20dc5c0.png)


* Introducción a la detección de poses:

La detección de pose o estimación de pose es un problema muy popular en la visión por computadora, de hecho, pertenece a una clase más amplia de dominio de la visión por computadora llamado estimación de puntos clave. Paa nuestro proyecto usamos la Detección de pose, donde intentaremos localizar 33 puntos de referencia corporales clave en una persona, por ejemplo, codos, rodillas, tobillos, etc.

![image](https://user-images.githubusercontent.com/81332414/137357594-f6723a4e-009d-4693-aa3c-26baff1ffdc7.png)

* Codigo: Importacion de las librerias

![image](https://user-images.githubusercontent.com/81332414/137357975-ed2a25ad-9f2a-420a-8871-56b5dc3fdba3.png)

Inicializar el modelo de detección de pose
Lo primero que debemos hacer es inicializar la clase pose usando la  mp.solutions.pose sintaxis y luego llamaremos a la función de configuración  mp.solutions.pose.Pose() con los argumentos:

static_image_mode - Es un valor booleano que, si se establece en  False, el detector solo se invoca cuando es necesario, es decir, en el primer cuadro o cuando el rastreador pierde la pista. Si se establece en  True, el detector de personas se invoca en cada imagen de entrada. Por lo tanto, probablemente debería establecer este valor en Verdadero cuando trabaje con un montón de imágenes no relacionadas, no videos. Su valor predeterminado es  False.

![image](https://user-images.githubusercontent.com/81332414/137358377-b389bf0b-bb15-4f2a-8afe-2d3dd00ac9cc.png)

* Realizar detección de pose

Ahora pasaremos el video  a la canalización de aprendizaje automático de detección de pose mediante el uso de la función  mp.solutions.pose.Pose().process(). Pero la canalización espera las imágenes de entrada en  RGB formato de color, por lo que primero tendremos que convertir la imagen de muestra de  BGR a  RGB formato usando la función,  cv2.cvtColor() ya que OpenCV lee las imágenes en  BGR formato (en lugar de  RGB).

Después de realizar la detección de pose, obtendremos una lista de treinta y tres puntos de referencia que representan las ubicaciones de las articulaciones del cuerpo de la persona prominente en la imagen. Cada hito tiene:

x - Es la coordenada x del punto de referencia normalizada a [0.0, 1.0] por el ancho de la imagen.
y: Es la coordenada y del punto de referencia normalizada a [0.0, 1.0] por la altura de la imagen.

* Parte 3: Clasificación de pose con heurística de ángulos

calculamos los angulos de varias articulaciones. Primero detectaremos los puntos de referencia de la pose y luego los usaremos para calcular los ángulos entre las articulaciones y, dependiendo de esos ángulos, reconoceremos la señal que el ciclista realiza en el video.

![image](https://user-images.githubusercontent.com/81332414/137359292-3a3569f7-2958-45e0-9688-ecbdf118d4d3.png)

* Crear una función para calcular el ángulo entre las marcas

Ahora crearemos una función que será capaz de calcular ángulos entre tres puntos de referencia. es decir  calcular el ángulo entre dos líneas.

![image](https://user-images.githubusercontent.com/81332414/137359455-a2765c28-d87b-4cc6-909a-904eb1732622.png)

* Codigo:

![image](https://user-images.githubusercontent.com/81332414/137359529-5f4e6539-d0ac-4587-b0b6-e2737566de39.png)


# Clasificacion de Señales:

Crear una función para realizar la clasificación de señales de los ciclistas
Ahora crearemos una función que será capaz de clasificar diferentes señales de los ciclistas utilizando los ángulos calculados de varias articulaciones. La función será capaz de identificar 6 señales de ciclistas:
se crear condicionales que se deben cumplir para que una pose se clasifique segun su significado ejemplo:

* Señal giro a la izquierda

1. El angulo del brazo izquiero debe ser mayor a 140 grados
2. El angulo del dorzo izquierdo debe ser mayor a 60 grados
3. El angulo del dorzo izquierdo debe ser menor de 110 grados

![image](https://user-images.githubusercontent.com/81332414/137359918-32b8d2f0-67ac-44a9-a1f6-0227e4c350e7.png)

# Clasificacion de las 7 señales de ciclistas

![image](https://user-images.githubusercontent.com/81332414/137360863-400172a5-ddc4-4f0f-9f38-cf1f756ebce6.png)


 



