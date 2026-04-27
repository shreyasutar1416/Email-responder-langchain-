import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts import intent_prompt
from utils.llm_config import get_llm

llm = get_llm(temperature=0.0)

intent_chain = intent_prompt.intent_prompt | llm
