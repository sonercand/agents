# ADK Travel Planner Agent

An intelligent, stateful conversational travel planning assistant built using the **Google Agent Development Kit (ADK)** and powered by Gemini. 

This agent helps users organize multi-leg journeys, remember persistent user preferences (such as home locations), manage active itineraries, and fetch live weather forecasts without requiring external API keys.

---

## Features

- **User-Scoped State Persistence**: Remembers user preferences (like home location) across sessions.
- **Session-Scoped Itinerary Management**: Dynamically adds and clears cities/airports during an active trip.
- **Multi-Leg Route Calculation**: Automatically structures stops into sequential travel legs (`from` -> `to`), prepending home preferences when necessary.
- **Live Weather Integration**: Connects directly to the free Open-Meteo API to fetch real-time temperature and weather conditions for any destination.

---

## Project Structure

```text
agents/
├── agent.py            # Main agent configuration and tool registration
├── agent-prompt.txt    # Behavioral instructions and tool-triggering guidelines
├── tools.py            # Custom tool implementations (state management & weather)
├── service-account.json# GCP service account credentials for local execution
└── README.md           # Project documentation



GCP setup
# 1. Define your Google Cloud project ID and persist it in gcloud configuration
PROJECT_ID="your-google-cloud-project-id"
gcloud config set project $PROJECT_ID

# 2. Enable the Vertex AI API
gcloud services enable aiplatform.googleapis.com

# 3. Create a service account for local authentication
SA_NAME="adk-travel-agent"
SA_EMAIL="$SA_NAME@$PROJECT_ID.iam.gserviceaccount.com"

gcloud iam service-accounts create $SA_NAME \
    --description="Service account for ADK Travel Agent" \
    --display-name="ADK Travel Agent"

# 4. Grant the Vertex AI User role to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SA_EMAIL" \
    --role="roles/aiplatform.user"

# 5. Generate and download the JSON key file directly into your project folder
gcloud iam service-accounts keys create service-account.json \
    --iam-account="$SA_EMAIL"

# 6. Point your current terminal session to the key file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/service-account.json"

run
adk web