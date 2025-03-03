# 🤲 Hand Gesture Recognition 🅰️🅱️
img = 
Este projeto utiliza a biblioteca **MediaPipe** para detectar e reconhecer gestos de mãos e identificar letras do alfabeto de A a E. A aplicação usa a câmera para capturar os gestos das mãos em tempo real e exibe as letras correspondentes na tela.

## ✨ Funcionalidades
- **Reconhecimento de Gestos** 🤖: Através da câmera, o sistema identifica gestos das mãos que representam as letras de A a E.
- **Desenho dos Landmarks** ✍️: O MediaPipe desenha os pontos de referência das mãos, permitindo uma visualização clara do que está sendo processado.
- **Exibição das Letras** 🔠: Quando um gesto é reconhecido, a letra correspondente é exibida na tela.
- **Tela em Tempo Real** 📹: A captura de vídeo é feita em tempo real e as letras são atualizadas conforme a detecção dos gestos.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x** 🐍
- **OpenCV** 📸: Para captura de vídeo e processamento de imagens.
- **MediaPipe** ✋: Para a detecção e análise dos landmarks das mãos.
- **Matplotlib** 📊 (se necessário para exibição de gráficos, embora não esteja presente neste código específico).

## ⚙️ Requisitos
Certifique-se de ter os seguintes pacotes Python instalados:
- `opencv-python`
- `mediapipe`
- `math` (integrado no Python)

Você pode instalar as dependências com o comando:
```bash
pip install opencv-python mediapipe
```

## 🚀 Como Usar
1. **Conecte a sua câmera** 📷: Certifique-se de que sua câmera esteja conectada ao seu dispositivo. O código usa a câmera em `/dev/video1`. Se necessário, ajuste para o dispositivo correto.
2. **Execute o Script** ▶️: Basta rodar o arquivo Python. O script irá abrir uma janela mostrando a captura da sua câmera com os gestos sendo analisados em tempo real.
   ```bash
   python hand_gesture_recognition.py
   ```
   
3. **Gestos Reconhecidos** 🤲:
   - **A**: Polegar para cima e indicador dobrado.
   - **B**: Todos os dedos estendidos e juntos.
   - **C**: Forma de "C" com a mão.
   - **D**: Polegar dobrado e os outros dedos estendidos.
   - **E**: Todos os dedos curvados sobre a palma.

4. **Fechar a Aplicação** ❌: Para fechar a aplicação, basta pressionar a tecla `q` enquanto a janela estiver aberta.


## 🧑‍💻 Estrutura do Código

- **`distance(a, b)`**: Função para calcular a distância euclidiana entre dois pontos.
- **Funções de Identificação de Letras** 🔠: As funções `is_letter_a()`, `is_letter_b()`, `is_letter_c()`, `is_letter_d()` e `is_letter_e()` são responsáveis por verificar se os gestos das mãos correspondem a uma das letras de A a E.
- **Captura de Vídeo e Processamento de Imagem** 📸: O código captura imagens da câmera, converte para RGB e processa usando o MediaPipe para detectar os landmarks das mãos.
- **Exibição de Letras** 🔠: Se um gesto correspondente for identificado, o nome da letra é exibido na tela.
