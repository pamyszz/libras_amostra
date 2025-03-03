import cv2
import mediapipe as mp
import math

# Inicializando as variáveis do MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializando a captura de vídeo
cap = cv2.VideoCapture("/dev/video1", cv2.CAP_V4L2)

# Verificando se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# Inicializando o detector de mãos do MediaPipe
hands = mp_hands.Hands()

def distance(a, b):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

# Função para verificar a letra "A"
def is_letter_a(landmarks):
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    
    # Polegar para cima e indicador dobrado
    return thumb.y < index_finger.y

# Função para verificar a letra "B"
def is_letter_b(landmarks):
    # Todos os dedos estendidos e juntos
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    
    return (index_finger.y < thumb.y and
            middle_finger.y < thumb.y and
            ring_finger.y < thumb.y and
            pinky.y < thumb.y)

# Função corrigida para verificar a letra "C"
def is_letter_c(landmarks):
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
    ring_finger = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    # Verifica se a mão forma um "C" curvado com a distância entre polegar e indicador
    return (distance(thumb, index_finger) > 0.05 and
            distance(index_finger, pinky) > 0.05 and
            thumb.x > pinky.x and thumb.y < pinky.y)

# Função corrigida para verificar a letra "D"
def is_letter_d(landmarks):
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    return (distance(thumb, index_finger) < 0.05 and
            middle_finger.y > index_finger.y and
            ring_finger.y > index_finger.y and
            pinky.y > index_finger.y)

# Função pra verificar a letra "E"
def is_letter_e(landmarks):
    # Todos os dedos curvados sobre a palma
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    
    return (index_finger.y > thumb.y and
            middle_finger.y > thumb.y and
            ring_finger.y > thumb.y and
            pinky.y > thumb.y)

# Loop para capturar os frames da câmera
while True:
    ret, image = cap.read()
    if not ret:
        print("Falha ao capturar imagem.")
        break
    
    # Convertendo a imagem de BGR para RGB
    image_rgb = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
    # Processando a imagem para detectar as mãos
    results = hands.process(image_rgb)
    
    # Convertendo de volta para BGR
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    
    # Verificando se há landmarks das mãos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image_bgr, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Verificando as letras de A a E
            if is_letter_a(hand_landmarks.landmark):
                cv2.putText(image_bgr, "Letra: A", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif is_letter_b(hand_landmarks.landmark):
                cv2.putText(image_bgr, "Letra: B", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif is_letter_c(hand_landmarks.landmark):
                cv2.putText(image_bgr, "Letra: C", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif is_letter_d(hand_landmarks.landmark):
                cv2.putText(image_bgr, "Letra: D", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif is_letter_e(hand_landmarks.landmark):
                cv2.putText(image_bgr, "Letra: E", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Exibindo a imagem
    cv2.imshow('Hand Tracker', image_bgr)

    # Fechar a aplicação ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando os recursos
cap.release()
cv2.destroyAllWindows()
