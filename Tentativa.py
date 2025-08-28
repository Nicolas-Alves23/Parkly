import cv2
import easyocr
import requests
import datetime

# URL do seu Apps Script WebApp (deve terminar com /exec)
url = "https://script.google.com/macros/s/AKfycbxx-yxAeKjJmAzgHC-3AcMNV5NL4ZqstB3uE-PYcNNG1EVYWd1xJHWNWGVe104l45qKAA/exec"

# Inicializa OCR (Português + Inglês)
reader = easyocr.Reader(['pt', 'en'])

# Abre stream da câmera (use o IP correto do seu celular/ESP32-CAM)
cap = cv2.VideoCapture('http://10.165.21.171:8080/video')

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Falha ao capturar frame")
        break

    results = reader.readtext(frame)
    textos_filtrados = []

    for (bbox, text, conf) in results:
        # Filtra textos curtos e de baixa confiança
        if conf > 0.70 and len(text.strip()) > 2:
            textos_filtrados.append(text.strip())

            # Desenha no vídeo
            top_left = tuple([int(val) for val in bbox[0]])
            bottom_right = tuple([int(val) for val in bbox[2]])
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(frame, f'{text} ({conf:.2f})', (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Se tiver texto válido, envia para o Google Sheets
    if textos_filtrados:
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Envia como array, sem sheet_name nem comando
        payload = {
            "values": [f"{agora} - {t}" for t in textos_filtrados]  # cada valor será uma linha na coluna A
        }

        try:
            r = requests.post(url, json=payload, timeout=10)
            print("✅ Enviado:", textos_filtrados, "| Resposta:", r.text)
        except Exception as e:
            print("⚠️ Erro ao enviar:", e)

    # Mostra o vídeo com OCR
    cv2.imshow("OCR", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
