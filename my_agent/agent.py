from google.adk.agents.llm_agent import Agent

def hiteshi_format (n:int): #tool
    """Hiteshi_format returns the hiteshi format of a number.
    n should always be greater than 0. 
    If less than 0, tell the user you cannot generate the representation.""" #doc string (tool description)
    return n+100

def einstein_number (n:int) -> int: #tool -> int(returns int)
    """einstein_number returns the einstein format of a number.
""" #doc string (tool desc)
    return n-100


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[hiteshi_format,einstein_number]
)

"""
What was sent to the LLM
{
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[
        {
            tool_name : "einstein_number",
            tool_description : "...",
            input_schema : [
                {
                    n:int 
                }
            ],
            output_schema : [
                {   
                    int
                }
            ]
        }
    ],
    conversation_history: [
        {
            "user": "who are you",
            "machine": "my job is ..."
        }
    ],
    query: "what is einstein representation of 58"

}
"""
