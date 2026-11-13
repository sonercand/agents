# ADK Calculator Agent

A local AI calculator agent built with the **Google Agent Development Kit (ADK)** and powered by **Gemini** on Google Cloud Platform (GCP).

---

## Prerequisites

* Python 3.10 or higher
* A Google Cloud Platform (GCP) account with billing enabled
* [Google Cloud CLI (`gcloud`)](https://cloud.google.com/sdk/docs/install) installed locally
* brew install --cask google-cloud-sdk

---

## 1. GCP Portal & CLI Setup

1. **Create a GCP Project**
   * Go to the [Google Cloud Console](https://console.cloud.google.com/projectcreate) and create a new project (e.g., `adk-calculator-lab`).
   * Link your billing account/credits to the project and copy your **Project ID**.

2. **Enable the Vertex AI API**
   * Enable the required API via the GCP Console API Library or by running:
     ```bash
     gcloud services enable aiplatform.googleapis.com
     ```

3. **Authenticate Your Local Desktop**
   * Log in to your Google Cloud account and set your active project:
     ```bash
     gcloud auth login
     gcloud config set project YOUR_PROJECT_ID
     ```
   * Generate local Application Default Credentials (ADC) so ADK can authenticate securely without hardcoded keys:
     ```bash
     gcloud auth application-default login
     ```

---

## 2. Local Environment Installation

1. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv

   # macOS / Linux
   source .venv/bin/activate

   # Windows (Command Prompt)
   .venv\Scripts\activate
   # pip install google-adk
   # export GOOGLE_GENAI_USE_VERTEXAI=1
   # export GOOGLE_CLOUD_PROJECT=$(gcloud config get project)

   # export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/gcloud/application_default_credentials.json"