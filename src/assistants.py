"""Module for AI assistants."""

from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from settings import settings
from src.prompts import (
    REGULAR_ASSISTANT_PROMPT,
    SUPERVISOR_PROMPT,
    THINKING_ASSISTANT_PROMPT,
)
from src.strings import REGULAR_ASSISTANT, THINKING_ASSISTANT
from src.tools import web_search_tool

regular_assistant = create_react_agent(
    model=settings.LLM_NAME,
    tools=[web_search_tool],
    prompt=REGULAR_ASSISTANT_PROMPT.format(language=settings.LANGUAGE),
    name=REGULAR_ASSISTANT,
)

thinking_assistant = create_react_agent(
    model=settings.LLM_NAME,
    tools=[web_search_tool],
    prompt=THINKING_ASSISTANT_PROMPT.format(language=settings.LANGUAGE),
    name=THINKING_ASSISTANT,
)

supervisor = create_supervisor(
    model=init_chat_model(settings.LLM_NAME),
    agents=[regular_assistant, thinking_assistant],
    prompt=SUPERVISOR_PROMPT.format(language=settings.LANGUAGE),
    add_handoff_back_messages=True,
    output_mode="full_history",
).compile()
