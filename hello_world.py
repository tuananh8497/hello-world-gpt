import os
import openai

# ENVIRONMENT VARIABLES
ORGANIZATION=os.getenv('OPENAI_ORGANISATION')
OPENAI_API_KEY= os.getenv('OPENAI_API_KEY')

# CONST VARIABLE
OPENAI_MODEL = 'gpt-3.5-turbo'

MESSAGE_FORMAT = """
USER: {msg}

ChatGPT: {content}
"""

def send_request(
    msg: str
):
    """
    SEND REQUEST to OpenAI server, input is a message 

    See: https://platform.openai.com/docs/api-reference/chat/create
    ALSO: https://platform.openai.com/docs/api-reference/completions/create
    """
    print('\nSTART PROGRAM !!!\n')
    openai.organization = ORGANIZATION
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[generate_message('user', msg)],
        temperature=0.6,
    )
    content = response['choices'][0]['message']['content']
    
    print(f'response msg: {response}\n')
    
    print_message = MESSAGE_FORMAT.format(
        msg=msg,
        content=content
    )

    print(print_message)
    print('FINISHED !!!')

def generate_message(
    role: str = 'user', 
    content: str =''
) -> tuple:
    """
    HELPER FUNCTION to help generate a tuple of message for the API call to the server.

    See: https://platform.openai.com/docs/api-reference/chat/create
    """
    return {"role": role, "content": content}

def main():
    # Change here
    message = "Give me list of some NFP organisation in Australia and some information on the fields of work"
    send_request(message)

if __name__=='__main__':
    main()