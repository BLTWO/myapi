from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json


def fetch_and_update_resume():
    try:
        SERVICE_ACCOUNT_JSON = os.environ.get("SERVICE_ACCOUNT_KEY")
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        if not SERVICE_ACCOUNT_JSON:
            raise ValueError("SERVICE_ACCOUNT_KEY not found in environment variables")

        service_account_info = json.loads(SERVICE_ACCOUNT_JSON)
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info, scopes=SCOPES
        )

        service = build("drive", "v3", credentials=credentials)

        file = (
            service.files()
            .get(
                fileId="10e7tnaku_r1-6PL3iId3qqQAC2ea3mFRzAvnPCRjR74",
                fields="id, name, mimeType, webViewLink, thumbnailLink, modifiedTime",
            )
            .execute()
        )
        date_modified = file.get("modifiedTime")

        docLink = file.get('webViewLink')

        from .models import Resume

        last_resume = Resume.objects.order_by("-date").first()
        if not last_resume or last_resume.date != date_modified:
            Resume.objects.create(resume_uri=docLink, date=date_modified)

    except Exception as e:
        print(f"Error fetching resume in ready(): {e}")
