import os
import requests

def download_file_from_url(url, dest_path):
    print(f"⬇️ Téléchargement de {os.path.basename(dest_path)} depuis {url}")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Téléchargement terminé : {dest_path}")
    else:
        print(f"❌ Échec du téléchargement : {response.status_code} - {response.reason}")

# === PARAMÈTRES ===

url_food_model = "https://licornemlflow.s3.eu-west-3.amazonaws.com/models/yolov8x-seg_tuned_foodseg103_aug/best.pt"
dest_path_food_model = "D:/jedha/full_stack/projet/projet_final/models/yolov8x-seg_tuned_foodseg103_aug/weights/best.pt"

url_api_mod = "https://licornemlflow.s3.eu-west-3.amazonaws.com/models/api_glucipred/best.pt"
dest_path_api_mod = "D:/jedha/full_stack/projet/projet_final/API-glucipred/best.pt"

url_plate_model = "https://licornemlflow.s3.eu-west-3.amazonaws.com/models/yolo_plate_only_v8x_freeze8_contours_30px/best.pt"
dest_path_plate_model = "D:/jedha/full_stack/projet/projet_final/models/yolo_plate_only_v8x_freeze8_contours_30px/weights/best.pt"

# === TÉLÉCHARGEMENTS ===

download_file_from_url(url_food_model, dest_path_food_model)
download_file_from_url(url_plate_model, dest_path_plate_model)
download_file_from_url(url_api_mod, dest_path_api_mod)


