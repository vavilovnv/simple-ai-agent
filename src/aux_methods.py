"""Module for auxiliary methods."""

import sys
from typing import Any

from langchain_core.messages import BaseMessage, convert_to_messages


def get_user_input(prompt) -> str:
    """Get user input with proper encoding handling."""
    try:
        return input(prompt)
    except UnicodeDecodeError:
        print(prompt, end="", flush=True)

        if hasattr(sys.stdin, "buffer"):
            line = sys.stdin.buffer.readline()
            return line.decode("utf-8", errors="replace").strip()

        return sys.stdin.readline().strip()


def pretty_print_message(message: BaseMessage, should_indent: bool = False) -> None:
    """Print a message in a pretty format with optional indentation."""
    formatted_message = message.pretty_repr(html=True)
    if not should_indent:
        print(formatted_message)
        return

    indented_message = "\n".join("\t" + line for line in formatted_message.split("\n"))
    print(indented_message)


def pretty_print_messages(
    graph_update: dict[str, Any] | tuple[list[str], dict[str, Any]],
    show_last_message_only: bool = False,
) -> None:
    """Print messages from a graph update in a pretty format."""
    is_from_subgraph = False

    # Handle subgraph updates
    if isinstance(graph_update, tuple):
        namespace, update_data = graph_update
        if not len(namespace):
            return

        subgraph_id = namespace[-1].split(":")[0]
        print(f"Update from subgraph {subgraph_id}:")
        print("\n")
        is_from_subgraph = True
        graph_update = update_data

    # Process each node in the update
    for node_name, node_data in graph_update.items():
        node_update_label = f"Update from node {node_name}:"
        if is_from_subgraph:
            node_update_label = "\t" + node_update_label

        print(node_update_label)
        print("\n")

        # Convert and filter messages
        converted_messages = convert_to_messages(node_data["messages"])
        if show_last_message_only:
            converted_messages = converted_messages[-1:]

        for message in converted_messages:
            pretty_print_message(message, should_indent=is_from_subgraph)
        print("\n")
