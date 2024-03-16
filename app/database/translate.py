import json
import logging
from typing import Dict, Any

from langchain.chains import LLMChain
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    PromptTemplate,
)
from langchain_openai import ChatOpenAI


def translate_row(
    row: Dict[str, str],
    model_name: str = "gpt-3.5-turbo-0613",
    language: str = "chinese",
) -> dict[str, Any]:
    """Translate a row of data using the specified model and language.

    Arguments:
        row: A dictionary representing a single row of data. The keys are the column names, and the values are the
            corresponding cell values.
        model_name: The name of the model to use for translation. Defaults to "gpt-3.5-turbo-0613".
        language: The language to translate the row data to. Defaults to "english".

    Returns:
        The translated row data as a string.
    """
    system_prompt = """
    You are an assistant that translates the input text to {language}. The results will be presented as key/value pairs
    in {language} as JSON format. Here’s an example of how it works:
    
    example:
    Input:{{"name: jack", "age: twelve"}}
    Output:{{"姓名": "杰克", "年龄": "12"}}
    """
    system_prompt_template = SystemMessagePromptTemplate.from_template(
        system_prompt
    )

    human_prompt = PromptTemplate(
        input_variables=["pairs"], template="{pairs}"
    )
    human_prompt_template = HumanMessagePromptTemplate(prompt=human_prompt)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_prompt_template, human_prompt_template]
    )

    chat = ChatOpenAI(temperature=0, model=model_name)
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    pairs = [f"{key}: {value}" for key, value in row.items()]
    result = chain.invoke(input={"pairs": pairs, "language": language})
    return {"text": json.loads(result.get("text", ""))}
