from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
def main():
    llm = OpenAI(model="gpt-3.5-turbo-")
    response = llm("What is the capital of France?")
    print(response)
if __name__ == "__main__":    main()