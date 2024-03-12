import logging
from typing import Dict

from langchain.chains import LLMChain
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    PromptTemplate,
)
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)


def translate_row(
    row: Dict[str, str],
    model_name: str = "gpt-3.5-turbo-0613",
    language: str = "chinese",
) -> str:
    """Translate a row of data using the specified model and language.

    Arguments:
        row: A dictionary representing a single row of data. The keys are the column names, and the values are the
            corresponding cell values.
        model_name: The name of the model to use for translation. Defaults to "gpt-3.5-turbo-0613".
        language: The language to translate the row data to. Defaults to "english".

    Returns:
        The translated row data as a string.
    """
    system_template = """
    You are a assistant that translates input text to {language}. The output is array of strings. 
    Parse as key/value in Json format.
    
    Example:
    Input:  [“name: jack"]
    Output: "姓名": "杰克"
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template = PromptTemplate(input_variables=["pairs"], template="{pairs}")
    human_message_prompt = HumanMessagePromptTemplate(prompt=human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chat = ChatOpenAI(temperature=0, model=model_name)
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    pairs = [f"{key}: {value}" for key, value in row.items()]
    result = chain.invoke(input={"pairs": pairs, "language": language})
    response = result.get("text", "")
    logger.debug(f"response: {response}")
    return response
