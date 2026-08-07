from app.memory.session_manager import SessionManager

manager = SessionManager()

session = manager.create_session("CAND-001")

print(session)

manager.add_question(session, "Explain RAG.")

manager.add_answer(session, "RAG combines retrieval with generation.")

manager.cover_day(session, 12)

print(manager.get_session(session))