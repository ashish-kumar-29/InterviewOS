from app.controllers.interview_controller import InterviewController

controller = InterviewController()

result = controller.start("CAND-001")

print(result)