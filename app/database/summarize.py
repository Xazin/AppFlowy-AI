import logging
from typing import Any
from typing import Dict

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI


def summarize_row(
    row: Dict[str, str], model_name: str = "gpt-3.5-turbo-instruct"
) -> dict[str, Any]:
    """
    Summarizes a table row using LangChain with a specified template.

    Args:
        row (Dict[str, str]): A mapping of column names to their values
        for summarization. model_name (str, optional): The summarization
        model to use. Defaults to "gpt-3.5-turbo-instruct".

    Returns:
        dict: Contains the summarized text under {'data': {'text': 'Summarized
        text here.'}}.

    Raises:
        ValueError: Raised if `row` is empty.
        Exception: Raised for any errors during the API call or summarization
        process.
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
        text = chain.run({"details": details}).strip()
        response = {"text": text}
        logging.debug(f"response: {response}")
        return response
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
            details: A dictionary with keys as detail types and values as the
            actual details.

        Returns:
            The summary produced by the language model, after processing with
            any specified preprocessors and postprocessors.
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
