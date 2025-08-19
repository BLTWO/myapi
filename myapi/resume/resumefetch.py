from google.oauth2 import service_account
from googleapiclient.discovery import build


def fetch_and_update_resume():
    try:
        SERVICE_ACCOUNT_FILE = "../service_account_cred.json"
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        service = build("drive", "v3", credentials=credentials)

        # Get the file metadata (for modified time)
        file_metadata = (
            service.files()
            .get(
                fileId="10e7tnaku_r1-6PL3iId3qqQAC2ea3mFRzAvnPCRjR74",
                fields="modifiedTime",
            )
            .execute()
        )
        date_modified = file_metadata.get("modifiedTime")

        # Get the export link for PDF (Google Docs files require export)
        resumefile_dic = (
            service.files()
            .download(
                fileId="10e7tnaku_r1-6PL3iId3qqQAC2ea3mFRzAvnPCRjR74",
                mimeType="application/pdf",
            )
            .execute()
        )

        download_uri = resumefile_dic["response"]["downloadUri"]
        print(download_uri)

        # Import here to avoid app loading issues
        from .models import Resume

        resume, created = Resume.objects.get_or_create(id=1)
        resume.resume_uri = download_uri
        resume.date = date_modified
        resume.save()

    except Exception as e:
        print(f"Error fetching resume in ready(): {e}")
