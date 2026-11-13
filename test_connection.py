import os
import subprocess
import sys
from google import genai

# Automatically fetch your active gcloud project ID
try:
    project_id = subprocess.check_output(
        ["gcloud", "config", "get", "project"], text=True
    ).strip()
    if not project_id or project_id == "(unset)":
        raise ValueError("No active gcloud project found.")
except Exception as e:
    print("Error: Could not automatically detect your gcloud project ID.")
    print("Please run: gcloud config set project YOUR_PROJECT_ID")
    sys.exit(1)

print(f"Using GCP Project ID: {project_id}")

# Initialize the GenAI client using Vertex AI with the global endpoint
client = genai.Client(vertexai=True, project=project_id, location="global")

try:
    print("Sending request to Gemini via Vertex AI global endpoint...")
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Hello Gemini! Confirming my setup works.",
    )

    print("\nSUCCESS! Gemini API responded:")
    print("-" * 40)
    print(response.text)
    print("-" * 40)

except Exception as e:
    print("\nERROR: Failed to connect to Gemini API.")
    print(e)