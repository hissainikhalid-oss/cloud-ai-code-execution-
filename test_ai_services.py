from apps.llm.explain import explain_topic
from apps.llm.chat import general_chat

print("----- Explanation -----")
print(explain_topic("Explain recursion"))

print("\n----- Chat -----")
print(general_chat("Recommend some anime"))