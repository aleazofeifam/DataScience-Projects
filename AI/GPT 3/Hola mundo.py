import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  engine="ada",
  prompt="What are some key points I should know when studying Ancient Rome?\n\n1.",
  temperature=1,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
