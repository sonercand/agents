#Creating the db 
#!/bin/bash
set -e

# --- Configuration Variables ---
export PROJECT_ID="your-gcp-project-id"
export REGION="us-central1"
export INSTANCE_NAME="warehouse-mysql-instance"
export DB_NAME="warehouse"
export DB_USER="toolbox"
export DB_PASS="ToolboxPass123!"
export ROOT_PASS="RootPass123!"

# 1. Set active GCP project & enable Cloud SQL Admin API
gcloud config set project $PROJECT_ID
gcloud services enable sqladmin.googleapis.com

# 2. Create the Cloud SQL MySQL 8.0 instance
echo "Creating Cloud SQL instance (this takes ~3-5 minutes)..."
gcloud sql instances create $INSTANCE_NAME \
  --database-version=MYSQL_8_0 \
  --tier=db-f1-micro \
  --region=$REGION \
  --root-password=$ROOT_PASS

# 3. Create the 'warehouse' database and dedicated user
echo "Creating database and user..."
gcloud sql databases create $DB_NAME --instance=$INSTANCE_NAME
gcloud sql users create $DB_USER \
  --instance=$INSTANCE_NAME \
  --password=$DB_PASS

# 4. Authorize your current public IP to connect locally
MY_IP=$(curl -s ifconfig.me)
echo "Authorizing local IP ($MY_IP)..."
gcloud sql instances patch $INSTANCE_NAME \
  --authorized-networks="${MY_IP}/32" \
  --quiet

# 5. Fetch the instance Public IP address
PUBLIC_IP=$(gcloud sql instances describe $INSTANCE_NAME --format="value(ipAddresses[0].ipAddress)")
echo "=========================================="
echo "Setup Complete! Your Cloud SQL Public IP is: $PUBLIC_IP"
echo "=========================================="