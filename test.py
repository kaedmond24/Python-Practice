import json
import os
import csv


response = """
{
    "tests": [
      {
        "public_id": "12345678-1234-5678-abcd-1234567890ab",
        "name": "Example Test 1",
        "type": "api",
        "tags": ["tag1", "tag2"],
        "status": "live",
        "monitor_id": "87654321-4321-5678-dcba-0987654321ab",
        "creator": "John Doe",
        "creation_date": 1678929800,
        "locations": ["aws:us-east-1", "gcp:us-central1", "azure:westus"],
        "config": {
          "request": {
            "method": "GET",
            "url": "https://api.example.com/endpoint"
          },
          "assertions": [
            {
              "operator": "statusCode",
              "target": 200
            },
            {
              "operator": "bodyContains",
              "target": "Example response"
            }
          ]
        }
      },
      {
        "public_id": "09876543-4321-5678-dcba-0987654321ab",
        "name": "Example Test 2",
        "type": "browser",
        "tags": ["tag3", "tag4"],
        "status": "paused",
        "monitor_id": "56789012-2109-8765-dcba-0987654321ab",
        "creator": "Jane Smith",
        "creation_date": 1678929500,
        "locations": ["aws:us-west-2", "gcp:europe-west1", "azure:westeurope"],
        "config": {
          "script": "console.log('Hello, World!');",
          "assertions": [
            {
              "operator": "status",
              "target": "completed"
            },
            {
              "operator": "steps",
              "target": 5
            }
          ]
        }
      },
      {
        "public_id": "abcedfgh-1234-5678-abcd-1234567890ab",
        "name": "Example Test 3",
        "type": "api",
        "tags": ["tag5", "tag6"],
        "status": "live",
        "monitor_id": "45678901-4321-5678-dcba-0987654321ab",
        "creator": "Alice Johnson",
        "creation_date": 1678930100,
        "locations": ["aws:us-west-1", "gcp:asia-northeast1", "azure:eastus"],
        "config": {
          "request": {
            "method": "POST",
            "url": "https://api.example.com/create"
          },
          "assertions": [
            {
              "operator": "statusCode",
              "target": 201
            },
            {
              "operator": "bodyContains",
              "target": "Created successfully"
            }
          ]
        }
      },
      {
        "public_id": "ijklmnop-4321-5678-dcba-0987654321ab",
        "name": "Example Test 4",
        "type": "browser",
        "tags": ["tag7", "tag8"],
        "status": "live",
        "monitor_id": "34567890-2109-8765-dcba-0987654321ab",
        "creator": "Bob Smith",
        "creation_date": 1678930400,
        "locations": ["aws:ap-southeast-1", "gcp:australia-southeast1", "azure:australiaeast"],
        "config": {
          "script": "console.log('Testing...');",
          "assertions": [
            {
              "operator": "status",
              "target": "completed"
            },
            {
              "operator": "steps",
              "target": 10
            }
          ]
        }
      },
      {
        "public_id": "qrstuvwx-1234-5678-abcd-1234567890ab",
        "name": "Example Test 5",
        "type": "api",
        "tags": ["tag9", "tag10"],
        "status": "paused",
        "monitor_id": "23456789-4321-5678-dcba-0987654321ab",
        "creator": "Eve Johnson",
        "creation_date": 1678930700,
        "locations": ["aws:eu-west-1", "gcp:southamerica-east1", "azure:centralus"],
        "config": {
          "request": {
            "method": "GET",
            "url": "https://api.example.com/data"
          },
          "assertions": [
            {
              "operator": "statusCode",
              "target": 200
            },
            {
              "operator": "bodyContains",
              "target": "Data retrieved"
            }
          ]
        }
      },
      {
        "public_id": "yz012345-4321-5678-dcba-0987654321ab",
        "name": "Example Test 6",
        "type": "browser",
        "tags": ["tag11", "tag12"],
        "status": "paused",
        "monitor_id": "12345678-2109-8765-dcba-0987654321ab",
        "creator": "Mark Johnson",
        "creation_date": 1678931000,
        "locations": ["aws:eu-central-1", "gcp:asia-southeast1", "azure:southeastasia"],
        "config": {
          "script": "console.log('Hello, World!');",
          "assertions": [
            {
              "operator": "status",
              "target": "completed"
            },
            {
              "operator": "steps",
              "target": 5
            }
          ]
        }
      },
      {
        "public_id": "mnopqrst-1234-5678-abcd-1234567890ab",
        "name": "Example Test 7",
        "type": "api",
        "tags": ["tag13", "tag14"],
        "status": "live",
        "monitor_id": "34567890-4321-5678-dcba-0987654321ab",
        "creator": "Sarah Smith",
        "creation_date": 1678931300,
        "locations": ["aws:ap-northeast-1", "gcp:asia-east1", "azure:australiacentral"],
        "config": {
          "request": {
            "method": "POST",
            "url": "https://api.example.com/update"
          },
          "assertions": [
            {
              "operator": "statusCode",
              "target": 204
            },
            {
              "operator": "bodyContains",
              "target": "Updated successfully"
            }
          ]
        }
      },
      {
        "public_id": "uvwxyz01-4321-5678-dcba-0987654321ab",
        "name": "Example Test 8",
        "type": "browser",
        "tags": ["tag15", "tag16"],
        "status": "live",
        "monitor_id": "23456789-2109-8765-dcba-0987654321ab",
        "creator": "Alex Johnson",
        "creation_date": 1678931600,
        "locations": ["aws:ap-south-1", "gcp:asia-northeast2", "azure:uksouth"],
        "config": {
          "script": "console.log('Testing...');",
          "assertions": [
            {
              "operator": "status",
              "target": "completed"
            },
            {
              "operator": "steps",
              "target": 10
            }
          ]
        }
      },
      {
        "public_id": "23456789-1234-5678-abcd-1234567890ab",
        "name": "Example Test 9",
        "type": "api",
        "tags": ["tag17", "tag18"],
        "status": "paused",
        "monitor_id": "87654321-4321-5678-dcba-0987654321ab",
        "creator": "Emily Johnson",
        "creation_date": 1678931900,
        "locations": ["aws:ca-central-1", "gcp:europe-north1", "azure:northeurope"],
        "config": {
          "request": {
            "method": "GET",
            "url": "https://api.example.com/info"
          },
          "assertions": [
            {
              "operator": "statusCode",
              "target": 200
            },
            {
              "operator": "bodyContains",
              "target": "Info received"
            }
          ]
        }
      },
      {
        "public_id": "45678901-4321-5678-dcba-0987654321ab",
        "name": "Example Test 10",
        "type": "browser",
        "tags": ["tag19", "tag20"],
        "status": "live",
        "monitor_id": "76543210-2109-8765-dcba-0987654321ab",
        "creator": "Michael Smith",
        "creation_date": 1678932200,
        "locations": ["aws:sa-east-1", "gcp:asia-south1", "azure:brazilsouth"],
        "config": {
          "script": "console.log('Hello, World!');",
          "assertions": [
            {
              "operator": "status",
              "target": "completed"
            },
            {
              "operator": "steps",
              "target": 5
            }
          ]
        }
      }
    ]
}
"""


# Converting String/DocString into Dictionary
response = json.loads(response)


# Columns 'Test Name', 'ID Number'  Type, Status, numOfLocations, Location, Creator, Tags, Details
totalTests = len(response["tests"])


# Function to make CSV
def makeCSV():
    fieldnames = ['Test Name', 'ID Number', 'Type', 'Status', 'numOfLocations', 'Locations', 'Creator', 'Tags', 'Details' ]
    rows = []

    # for test in response['test']:

    for idx in range(0, totalTests):
        rows.append({'Test Name': response['tests'][idx]['name'],
        'ID Number': response['tests'][idx]['monitor_id'],
        'ID Number': response['tests'][idx]['monitor_id'],
        'Type':response['tests'][idx]['type'],
        'Status':response['tests'][idx]['status'],
        'numOfLocations':len(response['tests'][idx]['locations']),
        'Locations':response['tests'][idx]['locations'],
        'Creator':response['tests'][idx]['creator'],
        'Tags':response['tests'][idx]['tags'],
        'Details':response['tests'][idx]['config']
        })


    # Creating a CSV file
    with open('TestFile.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("CSV Created")


makeCSV()