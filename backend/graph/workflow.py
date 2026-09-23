from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.fast_agent import testpilot_agent


class TestPilotState(TypedDict):
    code: str
    result: str


def testpilot_node(state: TestPilotState):
    return {
        "result": testpilot_agent(state["code"])
    }


workflow = StateGraph(TestPilotState)

workflow.add_node("testpilot", testpilot_node)

workflow.set_entry_point("testpilot")

workflow.add_edge("testpilot", END)

testpilot_graph = workflow.compile()