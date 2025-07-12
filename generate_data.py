import boto3
import json
import time

def invoke_llm(body: any, retries: int = 0):
  print("invoking llm, retries:", retries)

  modelId = "anthropic.claude-3-5-sonnet-20241022-v2:0"
  client = boto3.client("bedrock-runtime", region_name="us-west-2")

  try:
    response = client.invoke_model(modelId=modelId, body=json.dumps(body))
    response_body = json.loads(response["body"].read())
    return response_body["content"][0]["text"]
  
  except Exception as e:
    if "(ThrottlingException)" in str(e) and retries < 3:
      time.sleep((retries + 1) * 8)
      return invoke_llm(
          body,
          modelId,
          retries + 1,
        )
    print(e)
    exit(1)

def generate_synthetic_students(num_students: int):
  message = f"""
    Generate {num_students} synthetic student records as a JSON array.
    Each record should have the following fields:
      "student_id": "string (format: STU followed by 6 digits)",
      "first_name": "string",
      "last_name": "string",
      "email": "string (format: firstname.lastname@university.edu)",
      "date_of_birth": "string (format: YYYY-MM-DD)",
      "enrollment_date": "string (format: YYYY-MM-DD)",
      "major": "string",
      "year": "string (Freshman, Sophomore, Junior, Senior)",
      "gpa": "number (between 2.0 and 4.0)",
      "credits_completed": "number (0-150)",
      "status": "string (Active, Inactive, Graduated)"

    Output only valid JSON.
    """
  payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": message}],
  }

  response = invoke_llm(payload)
  return response

def main() -> None:
  students = generate_synthetic_students(num_students=5)


  with open("synthetic_students.json", "w") as f:
    f.write(students)
  print("Wrote synthetic_students.json")

  students = json.loads(students)
  for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}")

if __name__ == "__main__":
  main()
