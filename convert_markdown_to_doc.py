import os
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import markdown2

# Authenticate and create the Google Docs API client
auth.authenticate_user()
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth import default

creds, _ = default()
service = build('docs', 'v1', credentials=creds)

def create_google_doc(title, content):
    doc = service.documents().create(body={'title': title}).execute()
    doc_id = doc['documentId']
    
    # Structure the content into Google Docs format
    requests = [
        {"insertText": {"location": {"index": 1}, "text": content}}
    ]
    
    service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
    print(f"Document created: https://docs.google.com/document/d/{doc_id}")

markdown_text = """
# Product Team Sync - May 15, 2023

## Attendees
- Sarah Chen (Product Lead)
- Mike Johnson (Engineering)
- Anna Smith (Design)
- David Park (QA)

## Agenda

### 1. Sprint Review
* Completed Features
  * User authentication flow
  * Dashboard redesign
  * Performance optimization
    * Reduced load time by 40%
    * Implemented caching solution
* Pending Items
  * Mobile responsive fixes
  * Beta testing feedback integration

### 2. Current Challenges
* Resource constraints in QA team
* Third-party API integration delays
* User feedback on new UI
  * Navigation confusion
  * Color contrast issues

### 3. Next Sprint Planning
* Priority Features
  * Payment gateway integration
  * User profile enhancement
  * Analytics dashboard
* Technical Debt
  * Code refactoring
  * Documentation updates

## Action Items
- [ ] @sarah: Finalize Q3 roadmap by Friday
- [ ] @mike: Schedule technical review for payment integration
- [ ] @anna: Share updated design system documentation
- [ ] @david: Prepare QA resource allocation proposal

## Next Steps
* Schedule individual team reviews
* Update sprint board
* Share meeting summary with stakeholders

## Notes
* Next sync scheduled for May 22, 2023
* Platform demo for stakeholders on May 25
* Remember to update JIRA tickets

---
Meeting recorded by: Sarah Chen
Duration: 45 minutes
"""

# Convert markdown to plain text
doc_content = markdown2.markdown(markdown_text)

# Create Google Doc
create_google_doc("Product Team Sync - May 15, 2023", doc_content)
