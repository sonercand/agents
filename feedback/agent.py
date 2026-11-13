import os
from datetime import date
from typing import Literal, Optional

from google.adk.agents import Agent
from pydantic import BaseModel, Field

script_dir = os.path.dirname(os.path.abspath(__file__))
instruction_file_path = os.path.join(script_dir, "instructions.txt")
with open(instruction_file_path, "r") as f:
    instruction = f.read()


class FeedbackSummary(BaseModel):
    customer_name: Optional[str] = Field(
        default=None,
        description="The full name of the customer providing feedback, if mentioned in the text.",
    )
    feedback_date: Optional[date] = Field(
        default=None,
        description="The date the feedback or service occurred in YYYY-MM-DD format, if mentioned.",
    )
    feedback_type: Literal["complaint", "suggestion", "praise"] = Field(
        description="The category of the feedback: 'complaint' for dissatisfaction/issues, 'suggestion' for feature requests/improvements, or 'praise' for positive compliments."
    )
    summary: str = Field(
        description="A concise, objective summary of the customer's feedback."
    )


# Note: Switch to "gemini-3.8-flash" if your GCP project returns a 404 on 2.5-flash
model = "gemini-3.8-flash"

root_agent = Agent(
    name="information_summarizer",
    description="A tool for summarizing customer service feedback.",
    instruction=instruction,
    model=model,
    output_schema=FeedbackSummary,
)