# Cal Poly AI Summer Camp: Synthetic Student Data Generator

Welcome to our AI Summer Camp! This project will teach you how to use Large Language Models (LLMs) to generate synthetic data for testing and development purposes. You'll learn how to create realistic student records using Python and Amazon Web Services (AWS) Bedrock.

## Contact Information

**Instructor**: Ryan Gertz - rgertz@calpoly.edu

Feel free to reach out if you have questions about:
- Setting up AWS credentials
- Understanding the code concepts
- Troubleshooting errors
- Ideas for extending this project
- General questions about AI and synthetic data generation

## What You'll Learn

- **Synthetic Data Generation**: Creating realistic fake data for testing and development
- **Large Language Models (LLMs)**: AI systems that can understand and generate structured data
- **AWS Bedrock**: Amazon's service that provides access to powerful AI models
- **Python Programming**: Writing code to generate and save data files
- **JSON Data Format**: Working with structured data in JSON format

## What This Code Does

This project demonstrates how to use AI to generate synthetic student records with realistic data. The code:

1. **Connects to AWS Bedrock**: Uses Claude 3.5 Sonnet model for data generation
2. **Generates Student Records**: Creates realistic student data with proper formatting
3. **Handles API Retries**: Automatically retries requests if AWS is temporarily busy
4. **Saves Data**: Outputs the generated data to a JSON file for use in other projects

## Prerequisites

Before you start, you'll need:

### 1. Python Installation
- Python 3.7 or higher installed on your computer
- You can download it from [python.org](https://www.python.org/downloads/)

### 2. AWS Account Setup
- An AWS account
- AWS credentials configured on your computer
- Access to AWS Bedrock service and Claude 3.5 Sonnet model

### 3. Required Python Packages
Install the necessary packages by running this command in your terminal:
```bash
pip install boto3
```

## Understanding the Code

### Key Components

**boto3**: Amazon's Python library that lets us connect to AWS services. Think of it as a bridge between your Python code and Amazon's AI models.

**JSON**: A structured data format that's easy for both humans and computers to read. Perfect for storing student records with multiple fields.

**AWS Bedrock**: Amazon's service that hosts various AI models. We use it to access Claude 3.5 Sonnet, which is excellent at generating structured data.

### The Functions Explained

#### Function 1: `invoke_llm(body, retries=0)`
This function handles communication with the AI model:
- Sends your request to Claude 3.5 Sonnet
- Handles errors and automatically retries if AWS is busy
- Returns the AI's response as text
- Includes built-in retry logic with exponential backoff

#### Function 2: `generate_synthetic_students(num_students)`
This function creates the prompt for generating student data:
- Specifies exactly what fields each student record should have
- Defines the format for each field (IDs, emails, dates, etc.)
- Tells the AI to output only valid JSON
- Returns the generated student records

#### Function 3: `main()`
This is the main function that:
- Calls the data generation function
- Saves the results to a JSON file
- Prints a confirmation message

## How to Run the Code

1. **Save the code**: Copy the code into a file called `synthetic_students.py`

2. **Open your terminal/command prompt**

3. **Navigate to your project folder**:
   ```bash
   cd path/to/your/project
   ```

4. **Run the code**:
   ```bash
   python synthetic_students.py
   ```

5. **Check the output**: Look for the `synthetic_students.json` file in your project folder

## Customizing The Code

### Generate Different Numbers of Students
Change the number of students generated:
```python
# In the main() function, change:
students = generate_synthetic_students(num_students=10)  # Instead of 5
```

### Add New Fields
Modify the prompt in `generate_synthetic_students()` to include additional fields:
```python
# Add fields like:
"phone_number": "string (format: XXX-XXX-XXXX)",
"address": "string",
"emergency_contact": "string",
```

## Understanding the Generated Data

The code generates realistic student records with these fields:

- **student_id**: Unique identifier (STU123456)
- **first_name/last_name**: Realistic names
- **email**: Properly formatted university email
- **date_of_birth**: Birth dates in YYYY-MM-DD format
- **enrollment_date**: When they started school
- **major**: Academic program
- **year**: Class standing (Freshman through Senior)
- **gpa**: Grade point average (2.0-4.0)
- **credits_completed**: Academic credits earned
- **status**: Current enrollment status

## Common Issues and Solutions

### "No credentials found"
This means your AWS credentials aren't set up. You need:
- AWS Access Keys
- AWS CLI configuration
- IAM permissions for Bedrock

### "Access denied to model"
Your AWS account might not have permission to use Claude 3.5 Sonnet:
- Check your AWS Bedrock model access
- Ensure you have the correct model ID
- Verify your IAM permissions

### "Module not found: boto3"
Install the required package:
```bash
pip install boto3
```

### "ThrottlingException"
This happens when you make too many requests too quickly:
- The code automatically handles this with retries
- Wait a few seconds and try again if it persists

### "Invalid JSON output"
Sometimes the AI might generate malformed JSON:
- Check the `synthetic_students.json` file
- The code asks for "valid JSON only" but AI responses can vary
- You might need to clean up the output manually

## Important Notes

- **Cost Awareness**: Each API call to AWS Bedrock costs money (usually just a few cents per request)
- **Rate Limits**: AWS has limits on how many requests you can make per minute
- **Data Privacy**: This generates synthetic data only - no real student information is used
- **Realistic but Fake**: The data looks realistic but is entirely AI-generated

## Use Cases for Synthetic Data

This type of synthetic data generation is useful for:
- **Testing Applications**: Test your software with realistic data
- **Database Development**: Populate test databases
- **Machine Learning**: Train models without using real personal data
- **Privacy Protection**: Develop systems without exposing real information

## Getting Help

If you run into issues:
1. Check the error message carefully
2. Ask our camp staff for assistance
3. Look up the specific error message online
4. Try running the code with fewer students first (num_students=1)

## Extending This Project

Ideas for making this project more advanced:
- Add data validation to ensure all fields are properly formatted
- Create different types of synthetic data (faculty, courses, grades)
- Build a web interface for generating data
- Add export options for different file formats
- Include data relationships (students enrolled in specific courses)

## Resources for Further Learning

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Synthetic Data Reading](https://aws.amazon.com/what-is/synthetic-data/)

---


Happy coding! 🚀
