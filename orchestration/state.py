from typing import TypedDict


class SAGEState(TypedDict, total=False):
    # -------------------------------------------------
    # USER INPUT
    # -------------------------------------------------

    user_query: str

    # -------------------------------------------------
    # DOCUMENT / RAG CONTEXT
    # -------------------------------------------------

    documents: list
    chunks: list
    sources: list

    # -------------------------------------------------
    # ORCHESTRATOR STATE
    # -------------------------------------------------

    current_objective: str

    selected_tool: str

    tool_input: dict

    # -------------------------------------------------
    # TOOL RESULTS
    # -------------------------------------------------

    tool_result: dict

    # History of previous tool calls/results
    tool_history: list

    # -------------------------------------------------
    # EXECUTION CONTROL
    # -------------------------------------------------

    iteration: int

    max_iterations: int

    task_complete: bool

    # -------------------------------------------------
    # FINAL OUTPUT
    # -------------------------------------------------

    final_answer: str

    # -------------------------------------------------
    # VERIFICATION
    # -------------------------------------------------

    verification: dict