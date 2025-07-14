# 🥗 Glucy-pred

[![Streamlit App](https://img.shields.io/badge/Demo-Streamlit-green?logo=streamlit)](https://huggingface.co/spaces/Fanchon/stream_app)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)

> **Glucy-pred** est une application intelligente conçue pour estimer la quantité de glucides présente dans une assiette à partir d’une simple photo.
>
> Elle s’adresse principalement aux personnes diabétiques désireuses de mieux maîtriser leur apport en glucides au quotidien, et permet d’ajuster plus facilement la dose d’insuline à injecter.

>L’application repose sur un pipeline de traitement d’image intégrant des techniques de détection et de segmentation des aliments.
>À partir d’une photo contenant une assiette, les aliments sont identifiés visuellement, leur forme est délimitée précisément.
>Ces informations sont ensuite croisées avec une base de données nutritionnelle pour estimer leur poids et calculer les glucides correspondants.


## Démo en ligne

➡️ Essayez l'application ici :  
🔗 [https://huggingface.co/spaces/Fanchon/stream_app](https://huggingface.co/spaces/Fanchon/stream_app)


# Contenu du projet
1. Interface utilisateur en ligne
Une interface conviviale est disponible via Streamlit sur Hugging Face :
👉 Tester l'application Glucy-pred

#Fonctionnalités :

1-Import d’une image contenant une assiette de nourriture accompagnée d’une fourchette (référence de taille).

2-Détection des aliments présents sur l’image et estimation de leur poids à partir des surfaces segmentées.

3-Calcul des glucides estimés, aliment par aliment, ainsi que du total glucidique de l’assiette.

2. Amélioration de la détection avec le modèle CLIP
Pour améliorer l'identification des aliments, nous avons intégré le modèle CLIP (Contrastive Language-Image Pretraining) de Google.
Cela permet une reconnaissance plus fine des aliments lorsque la confiance du modèle YOLO est faible.

3. EDA et préprocessing du dataset FoodSeg103
Analyse exploratoire des données du dataset FoodSeg103 (103 classes d’aliments segmentés).

   Prétraitement des masques et annotations pour entraîner un modèle YOLOv8.

   Data augmentation : rotation, duplication et équilibrage pour améliorer la robustesse du modèle.

# Technologies utilisées
Python, TensorFlow, YOLOv8, CLIP, OpenCV, Pytorch

Streamlit pour l’interface web

Hugging Face Spaces pour le déploiement# 🥗 Glucy-pred
## 📦 Installation locale

1. **Clonez ce dépôt :**
   ```bash
   git clone <URL_DU_DEPOT>
   cd glucy-pred
   ```

2. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Importez les modèles YOLO nécessaires :**
   ```bash
   python import_models.py
   ```

4. *(Optionnel)* **Lancez l'application localement** :
   ```bash
   streamlit run app.py
   ```

---

## Dépendances utilisées (`requirements.txt`)

Voici les versions exactes des bibliothèques utilisées :

```text
fastapi==0.115.14
numpy==2.3.1
opencv_python==4.11.0.86
pandas==2.3.0
Pillow==11.3.0
pydantic==2.11.7
PyYAML==6.0.2
Requests==2.32.4
scikit_learn==1.7.0
sentence_transformers==4.1.0
torch==2.7.1+cpu
ultralytics==8.3.162
uvicorn==0.35.0
```

---

## Description du projet

Glucy-pred combine plusieurs briques technologiques pour estimer les glucides par image :

-  Détection de l’assiette : `YOLOv8`
-  Segmentation des aliments : `YOLOv8x-seg`
-  Calcul de la surface des aliments
-  Estimation du poids à partir de la densité
-  Association avec la base **Ciqual** (ANSES) enrichie

> 🧪 Une **amélioration expérimentale** via le modèle **CLIP** est en cours de test dans le notebook `model_clip.ipynb` (non encore intégrée à l'API en ligne).
            cette amelioration n'est pas encore implementé dans l'application glucipred
---

##  Arborescence des fichiers clés

```
glucy-pred/
├── app.py                       # Application Streamlit
├── import_models.py            # Téléchargement automatique des modèles YOLO
├── requirements.txt
├── preprocessing_food_seg_103/
│   └── preprocessing_food_seg_103.ipynb   # EDA + data augmentation sur FoodSeg103
├── model_clip.ipynb            # Prototype de relabeling avec CLIP (hors API)
├── bloc6 -.pptx                # Présentation PowerPoint du projet
└── README.md
```

---

##  Notebooks 

- [`preprocessing_food_seg_103/preprocessing_food_seg_103.ipynb`](preprocessing_food_seg_103/preprocessing_food_seg_103.ipynb)  
  → Préparation du dataset **FoodSeg103**, EDA, augmentation d’images.

- [`model_clip.ipynb`](model_clip.ipynb)  
  → Intégration expérimentale du modèle **CLIP** pour améliorer l’identification des aliments (non encore déployé dans l'app Streamlit).

---

## Méthodologie de calcul

1. Détection de l’assiette et segmentation des aliments via YOLOv8.
2. Calcul de la surface relative des aliments.
3. Estimation du **poids** à partir de la densité alimentaire moyenne.
4. Calcul des **glucides** via la base Ciqual enrichie.

---

## Perspectives d'amélioration

-  Intégrer le modèle CLIP à l'API pour un relabeling plus précis.
-  Améliorer l'estimation du poids (réseau de neurones ou vision 3D).
-  Étendre les datasets avec des images variées annotées.
-  Enrichir la base nutritionnelle par web scraping multi-sources.

---


##  Auteurs jerome moulinier 

Projet réalisé en collaboration avec :

- **Fanchon Kabré**
- **Clément Maulard**
- **Wafa Zeghouane**

Dans le cadre de la certification **RNCP 35288 – Bloc 6 - Concepteur Développeur en Science des Données**.
