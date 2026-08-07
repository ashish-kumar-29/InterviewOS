from app.agents.evaluator import AnswerEvaluator

evaluator = AnswerEvaluator()

result = evaluator.evaluate(
    "RAG improves performance because retrieved documents provide relevant context. For example, enterprise chatbots use vector databases to retrieve company knowledge before generation."
)

print(result)