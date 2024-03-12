import logging
from typing import Dict

from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

logger = logging.getLogger(__name__)


def summarize_row(
    row: Dict[str, str], model_name: str = "gpt-3.5-turbo-instruct"
) -> str:
    """
    Summarizes table row data using LangChain and a template.

    Parameters:
    - row (Dict[str, str]): The table row to summarize, with column names as keys and their values as values.
    - model_name (str): Model for summarization (default: "gpt-3.5-turbo-instruct").
    - api_key (str): OpenAI API key (optional, uses environment's default if None).

    Returns:
    - str: Summary of the provided row.

    Raises:
    - ValueError: If the provided row is empty.
    - Exception: For errors from the API or summarization process.
    """

    # Setup for LangChain's OpenAI LLM with API key if provided
    llm = OpenAI(model_name=model_name)

    # Define the instruction template
    template = SummarizePromptTemplate.from_template(
        "Summarize the following details: ${details}"
    )

    # Convert the row dict to a string format that fits our template
    details = ", ".join([f"{key}: {value}" for key, value in row.items()])

    # Use SingleShotChain for executing the templated instruction
    chain = SingleShotChain(llm=llm, prompt=template)

    # Attempt to generate the summarization
    try:
        response = chain.run({"details": details})
        summarization = response.strip()
        return summarization
    except Exception as e:
        raise SummarizationError(e) from e


class SummarizePromptTemplate(PromptTemplate):
    pass


class SingleShotChain:
    def __init__(
        self,
        llm: OpenAI,
        prompt: SummarizePromptTemplate,
        preprocessors=None,
        postprocessors=None,
    ):
        if postprocessors is None:
            postprocessors = []
        if preprocessors is None:
            preprocessors = []
        self.llm = llm
        self.prompt = prompt
        self.preprocessors = preprocessors
        self.postprocessors = postprocessors

    def run(self, details: Dict[str, str]) -> str:
        """
        Summarizes details using a template and a language model.

        Parameters:
            details: A dictionary with keys as detail types and values as the actual details.

        Returns:
            The summary produced by the language model, after processing with any specified preprocessors and postprocessors.
        """
        for preprocessor in self.preprocessors:
            self.prompt = preprocessor(self.prompt)

        llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)
        response = llm_chain.invoke(details)
        for postprocessor in self.postprocessors:
            response = postprocessor(response)
        return response.get("text", "")


class SummarizationError(Exception):
    """Exception raised for errors in the summarization process."""

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def __str__(self):
        return f"summarization process: {str(self.original_exception)}"


# Example usage
