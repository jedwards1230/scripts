import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY", "")


def read_description(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return ""


def build_messages():
    description = read_description("description.txt")
    resume = read_description("resume.txt")
    input = """
        Create a cover letter for a software engineer position. 
        Emphasize my role as a full stack developer.
        Only use the information provided in the following resume:
        Resume: {0} 
        Job Description: {1}
    """
    return input.format(resume, description)


def play_sound():
    sound_file = "/System/Library/Sounds/Ping.aiff"
    if os.path.isfile(sound_file):
        os.system(f"afplay {sound_file}")
    else:
        print("Error: Sound file not found.")


def get_letter() -> None:
    messages = {"role": "system", "content": build_messages()}
    model_id = "gpt-4"

    try:
        content = (
            openai.ChatCompletion.create(messages=[messages], model=model_id)
            .choices[0]
            .message.content
        )
        print(f"\n\n{content}\n\n")
        play_sound()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_letter()
