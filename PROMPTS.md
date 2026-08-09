# PROMPTS.md — InterviewOS AI Usage Log

## About this log

This file documents how AI assistance was used during the development of **InterviewOS**, our AI Technical Interview Operating System for the ABTalks AI Engineering Hackathon.

This is a development log, not a verbatim export of the entire chat history. The entries preserve the actual development tasks, debugging problems, implementation decisions, and iterations that occurred while building the project.

---

# 1. Understanding the Hackathon Requirement

### User task
> "this is problem statement"

I provided the complete ABTalks AI Interview Agent problem statement, including the requirements for:

- A conversational technical interview
- At least 8 questions
- Coverage of at least 4 curriculum days
- Follow-up questions based on previous responses
- Conversation context
- Structured final feedback
- `POST /api/interview`

### AI-assisted work
I used AI to break the problem statement into implementation requirements and identify the major components needed for the project.

### Result
The project was planned around an interview controller, curriculum loader, candidate context, session manager, evaluator, knowledge tracker, and memory service.

---

# 2. Designing the Interview Architecture

### User task
> "make it like this and also make one starting page having all necessary and recommended items. then after clicking on the button start interview, this interview will open"

### AI-assisted work
The interview experience was organized into:

1. Start/interview introduction page
2. Candidate profile
3. Interview information
4. Start Interview button
5. Interview screen
6. Question and answer flow
7. Final result screen

The implementation was kept simple enough to work with the existing frontend while still presenting the project as a complete interview product.

---

# 3. Building the Interview Controller

The main backend flow was developed around an `InterviewController`.

### Important components

```python
self.curriculum_loader = CurriculumLoader()
self.sessions = SessionManager()
self.agent = InterviewAgent()
self.evaluator = InterviewEvaluator()
self.breeth = BreethService()
self.knowledge = KnowledgeTracker()
```

### AI-assisted reasoning

The controller was designed to:

- Start an interview when a candidate profile is supplied.
- Generate an interview plan.
- Create a session.
- Ask the first question.
- Receive subsequent answers using `sessionId`.
- Evaluate each answer.
- Update topic knowledge.
- Save the conversation to Breeth.
- Select the next question.
- Return structured final feedback.

This was one of the main pieces of the backend interview orchestration.

---

# 4. Implementing a Temporary Answer Evaluator

### User task
The evaluator was initially implemented without depending on an external LLM.

The evaluator considered:

- Answer length
- Answer depth
- Technical vocabulary
- Topic relevance

### Example implementation logic

```python
if word_count >= 80:
    score += 4
elif word_count >= 40:
    score += 3
elif word_count >= 15:
    score += 2
else:
    score += 1
```

Technical terms such as:

```text
python
api
model
data
database
machine learning
embedding
vector
llm
rag
fastapi
sql
cloud
docker
```

were also used as basic answer-quality signals.

### Why this was used

The goal was to have a deterministic evaluator that worked without requiring an external LLM during development.

This also made debugging the interview flow easier before considering more advanced evaluation.

---

# 5. Improving Topic Relevance

### User task
> "where"

The question was about where to place the objective-specific evaluation logic.

The evaluator was updated to compare words from:

```python
objective["title"]
```

against the candidate's answer.

### Logic

```python
objective_title = objective.get("title", "").lower()

title_words = [
    word for word in re.findall(r"\b[a-zA-Z]+\b", objective_title)
    if len(word) > 3
]

matched_objective_words = [
    word for word in title_words
    if word in answer_lower
]
```

If relevant words were found, the evaluator added:

```text
Addressed the interview topic directly.
```

Otherwise, it added a gap indicating that the answer did not clearly address the requested topic.

### Result

The evaluator became more topic-aware instead of relying only on answer length.

---

# 6. Adaptive Interview Behavior

### User task
The interview should behave differently depending on the previous answer.

### AI-assisted implementation

The controller used the evaluation score to decide the next question.

#### Score below 5

The interviewer revisits the current topic:

```text
Let's revisit <topic>.
Can you explain <topic> again, but this time focus
on the key concepts and practical examples?
```

#### Score 8 or above

The interviewer moves to the next topic and asks for deeper understanding.

#### Middle score

The interviewer moves to the next objective with a normal explanation question.

### Result

The interview is not just a fixed sequence. Candidate performance influences the next question.

---

# 7. Session and Context Handling

### User task
The interview needed to maintain context across multiple HTTP requests.

### AI-assisted design

The `sessionId` is used to retrieve the interview state:

```python
session = self.sessions.get_session(
    request.sessionId
)
```

The session stores information such as:

- Current objective index
- Interview plan
- Questions
- Answers
- Evaluations
- Knowledge updates
- Candidate ID

### Result

The backend can continue an interview over multiple requests rather than treating every request as a new interview.

---

# 8. Final Feedback

### User task
The completed interview should provide useful feedback.

### AI-assisted implementation

The controller calculates the average score:

```python
average_score = round(
    sum(scores) / len(scores),
    2
)
```

It also collects:

- Strengths
- Gaps
- Weak topics
- Recommended next steps

The final API response follows the required structure:

```json
{
  "reply": "Interview completed.",
  "done": true,
  "feedback": {
    "summary": "...",
    "strengths": [],
    "gaps": [],
    "next": []
  }
}
```

---

# 9. Frontend Interview UI

### User task
The interview page was progressively redesigned to look more modern.

The UI was developed around:

- InterviewOS branding
- Candidate name
- AI Interview badge
- Technical question card
- Progress bar
- Answer textarea
- Submit Answer button
- Exit Interview button
- Evaluation/loading state
- Final score
- Strengths
- Areas to Improve
- Next Steps

The interview page contains the start page and interview page sections and switches between them during the session.

---

# 10. Candidate Name Issue

### User task
> "**Sarah Johnson** is written why"

The candidate name was hardcoded in the mock candidate object:

```javascript
name: "Sarah Johnson"
```

The frontend then displayed that value in the candidate profile.

### AI-assisted debugging

The issue was traced to the mock candidate data rather than the UI itself.

The candidate object also contained example information such as:

```text
Senior Data Engineer
9 years experience
B.Tech
```

### Result

The behavior was understood and could be changed by replacing the mock candidate profile with the supplied candidate data.

---

# 11. Exit and Home Navigation

### User task
> "also ensure that while interview start it contains exit button that redirect to homepage and after submission along with restart button it contain home button that redirect to home page"

### AI-assisted implementation

The interview screen received:

```html
<button
    id="exitBtn"
    class="exit-btn"
    onclick="goHome()"
>
    ← Exit Interview
</button>
```

The result screen received:

```html
<button id="homeBtn" onclick="goHome()">
    ← Home
</button>

<button id="restartBtn" onclick="restartInterview()">
    ↻ Restart Interview
</button>
```

The navigation was later debugged after deployment.

---

# 12. Button Alignment

### User task
> "allign buttons"

The result buttons were adjusted to use a shared flex layout and consistent dimensions.

The CSS was changed to align the Home and Restart Interview buttons horizontally with matching height and width.

### Result

The final result actions became visually consistent instead of having differently sized buttons.

---

# 13. Answer Status Message

### User task
> "where"

The frontend needed a status element for feedback after submitting an answer.

The following element was added:

```html
<div id="answerStatus"></div>
```

The JavaScript then updates it with a message such as:

```javascript
document.getElementById("answerStatus").textContent =
    "Answer evaluated. Preparing your next question...";
```

### Result

The candidate receives immediate UI feedback while the next question is being prepared.

---

# 14. Handling the Final API Response

The frontend was updated to recognize the backend's `done` flag.

```javascript
const data = await response.json();

if (!response.ok) {
    throw new Error(JSON.stringify(data));
}

if (data.done) {
    showFinalResult(data);
    return;
}

showQuestion(data.reply);
```

### Result

The frontend now distinguishes between:

- A normal interview response
- The final interview response

and displays the final report when `done` is true.

---

# 15. Deployment Planning

### User task
> "i need to deploy this on vercel or netlify"

The project was analyzed as two deployable parts:

```text
Frontend → Netlify
Backend  → Render
```

The FastAPI backend was deployed separately because the frontend is a browser application and the backend provides the interview API.

### Production API

The frontend was configured to call:

```javascript
const API_URL =
    "https://interviewos-phu5.onrender.com/api/interview";
```

### Result

The application could be accessed without running the backend locally.

---

# 16. Netlify 404 Debugging

### User task
> "again page not found"

The deployed application initially returned a Netlify 404.

The issue was investigated by checking the project structure and the fact that Netlify detected the project as Next.js.

The project contained an `interview.html` application while the generated Next.js `app/page.tsx` was still the default starter page.

### Decision

Instead of forcing the existing HTML application into a full Next.js migration, the deployment was simplified around the working HTML frontend.

A root:

```text
index.html
```

was used as the public homepage.

### Result

The homepage became accessible through the Netlify production URL.

---

# 17. Homepage and Interview Flow

The existing HTML application already contained both the start experience and interview experience.

The start screen included:

- AI-powered interview introduction
- Candidate profile
- Interview information
- 8 questions
- 4+ curriculum areas
- AI evaluation
- Approximate interview duration
- Before-you-begin guidance
- Start Interview button

The interview section contained the technical question, answer area, progress indicator, and interview controls.

This structure was retained rather than unnecessarily rebuilding the entire UI.

---

# 18. Fixing Exit Navigation After Deployment

### User task
> "after clicking exit intervie button error"

The deployed homepage was `index.html`, so navigation to `/interview.html` was incorrect for returning to the homepage.

The `goHome()` function was changed to:

```javascript
function goHome() {
    window.location.href = "/";
}
```

The same navigation behavior was checked in the deployed copy of the application.

### Result

Exit Interview and Home return to the production homepage.

---

# 19. GitHub and Netlify Deployment Iterations

### User task
> "first push in github then do these steps"

The project was repeatedly committed and pushed while fixing:

- Frontend code
- Navigation
- Deployment configuration
- API URL
- Homepage routing

Typical deployment workflow:

```bash
git add .
git commit -m "..."
git push
```

Netlify then automatically deployed the updated GitHub commit.

### Result

The production application became accessible through the Netlify URL.

---

# 20. Production API Request

The frontend start request uses the required API endpoint:

```javascript
const response = await fetch(API_URL, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        sessionId,
        candidate
    })
});
```

Subsequent interview turns send the same session ID with the candidate's latest answer/message.

This matches the technical specification's session-based multi-turn interview model.

---

# 21. Final Testing

The deployed application was tested through the main flow:

```text
Homepage
   ↓
Start Interview
   ↓
Question
   ↓
Submit Answer
   ↓
Evaluation
   ↓
Next Question
   ↓
Adaptive Interview
   ↓
Final Feedback
   ↓
Home / Restart
```

The production setup uses:

```text
Netlify
   ↓
Frontend
   ↓
Render
   ↓
FastAPI /api/interview
```

---

# 22. Final Hackathon Checklist

Before submission, the project was checked against the Interview Agent requirements:

- [x] Conversational technical interview
- [x] At least 8 questions
- [x] Curriculum-based interview
- [x] At least 4 curriculum areas
- [x] Follow-up/adaptive behavior
- [x] Session-based context
- [x] Structured final feedback
- [x] Required HTTP endpoint
- [x] Public GitHub repository
- [x] Live deployment
- [x] AI Usage Log

The hackathon submission instructions explicitly require a publicly accessible repository, a working live demo, and an accessible AI Usage Log. The instructions also state that a `PROMPTS.md` in the repository or exported chat transcripts can be used for the AI Usage Log.

---

# 23. Development Summary

AI assistance was used during the project for:

- Understanding the problem statement
- Planning the architecture
- Designing the interview flow
- Writing and refining backend logic
- Building the evaluator
- Implementing adaptive questioning
- Designing the frontend
- Debugging API integration
- Fixing navigation
- Improving UI alignment
- Troubleshooting Netlify deployment
- Connecting the production frontend and backend
- Reviewing hackathon requirements

The implementation was iteratively tested and modified during development. AI suggestions were reviewed and adapted to the project's existing codebase and deployment setup.

---

## Main Technologies

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Netlify
- Render
- GitHub
- Breeth memory service
- Curriculum JSON
- Session-based interview state

## Project

**InterviewOS — AI Technical Interview Operating System**

Built for the **ABTalks Vibe Code Hackathon**.
