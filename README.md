# Multi Disease Prediction Webpage

Multi Disease Prediction Webpage is a Streamlit-based web application that provides quick machine-learning predictions for Diabetes, Heart Disease, and Parkinson's disease using pre-trained scikit-learn models. It’s intended for demonstration and prototyping — clinicians should NOT use it for real medical decision-making.

## Features
- Three prediction pages in one UI:
  - Diabetes Prediction (SVC model)
  - Heart Disease Prediction (SVC model)
  - Parkinson Prediction (SVC model)
- Built with Streamlit for a simple interactive web UI.
- Easy to deploy to platforms that support Streamlit (repository includes Railway config).

## Stack
- Language(s): Python 3.11
- Framework / runtime: Streamlit
- Notable libraries: scikit-learn (models), streamlit-option-menu (sidebar navigation), numpy

## Repository layout
```
app.py                      # Streamlit application (main entry)
requirements.txt            # Python dependencies
setup.sh                    # Writes .streamlit/config.toml for hosted environments
railway.json                # Railway deploy config (startCommand)
runtime.txt                 # Python runtime specification (python-3.11.8)
Model_save.sav              # Saved Parkinson model (pickle)
Model_save_Diabeties.sav    # Saved Diabetes model (pickle)
Model_save_heart.sav        # Saved Heart Disease model (pickle)
```

How it fits together:
- app.py is the single Streamlit app. On startup it loads three pickled sklearn models and renders a sidebar menu (streamlit-option-menu) that switches between three pages. Each page collects input fields from the user and calls the corresponding model’s predict method to return a diagnosis string.
- setup.sh and railway.json prepare the app for a deployment environment (setup.sh creates .streamlit/config.toml so Streamlit runs headlessly and uses $PORT).

## Quickstart — run locally
1. Clone the repository:
   git clone https://github.com/S-Harish-Dev/Multi_Disease_Prediction_Webpage.git
   cd Multi_Disease_Prediction_Webpage

2. Create a virtual environment (recommended) and install dependencies:
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt

3. Run the app:
   python -m streamlit run app.py
   # or
   streamlit run app.py

4. Open the local URL printed by Streamlit (default http://localhost:8501).

Notes:
- The app expects numeric inputs for the model features. The current inputs come from st.text_input; consider entering numbers only (or improve app.py to cast/validate inputs).
- runtime.txt indicates a Python 3.11.8 runtime for hosted environments.

## Deploying (example: Railway)
The repository includes railway.json which uses a start command:
- railway.json startCommand runs: chmod +x setup.sh && ./setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
- The setup.sh script creates .streamlit/config.toml with the port configuration required for headless hosting.

When deploying to any host:
- Ensure the host exposes the $PORT environment variable to the process.
- Install dependencies with pip install -r requirements.txt using Python 3.11.x.

## Usage
- Launch the app and use the left sidebar to choose one of:
  - Diabetes Prediction — provide: Pregnancies, Glucose, Blood_pressure, Skin_Thickness, Insulin, BMI, Diabetes_Pedigree_Function, Age
  - Heart Disease Prediction — provide: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
  - Parkinson Prediction — provide vocal features (MDVP:Fo, Fhi, Flo, jitter, shimmer, HNR, RPDE, DFA, etc.)
- Click the corresponding "Test Result" button to get the prediction text displayed by st.success().

## Model & data notes
- The app loads three pre-trained models from pickled .sav files at the repository root (Model_save*.sav). These are scikit-learn models (SVC).
- The models and their training datasets are not included in source form; only compiled pickles are present. If you want to retrain models, add training scripts and raw datasets and include versioning and evaluation metrics.
