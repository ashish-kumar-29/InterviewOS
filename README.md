# InterviewOS

## AI Technical Interview Operating System

InterviewOS is an AI-powered technical interview platform designed to simulate a structured, adaptive technical interview.

Built for the **ABTalks AI Engineering Hackathon**, InterviewOS evaluates candidates based on their answers, adapts the next question according to performance, tracks knowledge gaps, stores interview memory using Breeth, and generates a final performance report.

---

## 📸 Screenshots
## 🎯 HomePage
<img width="1867" height="1168" alt="Screenshot 2026-08-09 173958" src="https://github.com/user-attachments/assets/ce6905d5-6779-455e-aca2-f4486b8bea0e" />

## 🎯 Interview
<img width="1867" height="1097" alt="Screenshot 2026-08-09 174008" src="https://github.com/user-attachments/assets/38e5dfe7-1659-45fd-b632-cbfbd1d8b970" />

---

## 🚀 Key Features

### 🎯 Adaptive Technical Interviews

InterviewOS does not follow a completely fixed question sequence.

The next question is influenced by the candidate's previous performance:

- **Low score** → revisit the current topic
- **Medium score** → move to the next topic
- **High score** → move forward with deeper questions

This creates a more realistic interview experience.

---

### 🧠 Candidate-Aware Interview Planning

The interview is generated based on candidate information such as:

- Name
- Job role
- Years of experience
- Education
- Interview objectives
- Curriculum topics

The system creates an interview plan containing multiple technical objectives.

---

### 📝 Technical Question Generation

InterviewOS generates questions according to the selected technical topic.

Supported areas include concepts such as:

- Python
- Programming Fundamentals
- Data Structures & Algorithms
- Object-Oriented Programming
- SQL
- Database Systems
- Machine Learning
- Deep Learning
- Generative AI
- Large Language Models
- APIs & Backend Development
- FastAPI
- Cloud Computing

---

### 📊 Automated Answer Evaluation

Candidate answers are evaluated using multiple signals:

- Answer depth
- Answer length
- Technical terminology
- Topic relevance
- Technical concepts used

Each answer receives a score from **0–10**.

The evaluator also identifies:

- Strengths
- Knowledge gaps
- Feedback

---

### 📚 Knowledge Tracking

InterviewOS tracks candidate performance across interview topics.

Weak topics are identified and converted into personalized next steps.

Example:

```text
Weak Topic
    ↓
Data Structures & Algorithms
    ↓
Knowledge Tracker
    ↓
Recommended Action
    ↓
Review Data Structures & Algorithms
