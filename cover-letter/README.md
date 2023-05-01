# Cover Letter Script

This script generates a cover letter for a software engineer position based on a given resume and job description. It emphasizes the role of the applicant as a full stack developer. After generating the cover letter, the script plays a notification sound.


## Requirements

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Set up your OpenAI API key in your environment variables. Add your API key in a `.env` file in the following format:

   ```
   OPENAI_KEY=your_api_key_here
   ```

2. Add your resume text file (`resume.txt`) and job description text file (`description.txt`).

3. To execute the script, run the following command:

   ```
   python cover.py
   ```