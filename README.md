# Scripts Repo

This repository contains various useful scripts. Currently, it includes the following:

- `cover-letter`: A script to generate cover letters for job applications using OpenAI's GPT-4 model.

## Cover Letter Script

Located in the `cover-letter` folder, this script generates a cover letter for a software engineer position based on a given resume and job description. It emphasizes the role of the applicant as a full stack developer. After generating the cover letter, the script plays a notification sound.

### Usage

1. Set up your OpenAI API key in your environment variables. Add your API key in a `.env` file in the following format:

   ```
   OPENAI_KEY=your_api_key_here
   ```

2. Add your resume text file (`resume.txt`) and job description text file (`description.txt`) to the `cover-letter` folder.

3. To execute the script, navigate to the `cover-letter` directory and run the following command:

   ```
   python cover.py
   ```

---

Feel free to contribute to this repository by adding more useful scripts.
