from google.adk.agents.llm_agent import Agent

def square_number(n:int) -> int:
    """
    This tool performs the square for the n given by the user.
    n should be greater than 0.
    """
    return n*n

def factorial(n:int) -> int:
    """
    This tool performs factorial of n given by the user.
    n should be greater than 0.
    """
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def cube_number(n:int) -> int:
    """
    This tool performs cube of n given by the user.
    Perform the request only if the user asks in request format with words like please etectra.
    """
    return n*n*n


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions .',
    instruction='Answer user questions to the best of your knowledge',
    tools= [square_number, factorial, cube_number]
)
