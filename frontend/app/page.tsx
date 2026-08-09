"use client";

export default function Home() {
  return (
    <main className="home-page">

      <nav className="home-navbar">
        <div className="brand">
          <span className="brand-name">InterviewOS</span>
          <span className="brand-badge">AI Interview</span>
        </div>

        <div className="nav-status">
          AI Technical Interview
        </div>
      </nav>

      <section className="hero">

        <div className="hero-badge">
          ✦ AI-Powered Technical Interview
        </div>

        <h1>
          Prepare Smarter.
          <br />
          <span>Interview Better.</span>
        </h1>

        <p className="hero-description">
          InterviewOS conducts personalized technical interviews,
          adapts to your responses, evaluates your knowledge,
          and provides actionable feedback.
        </p>

        <div className="feature-grid">

          <div className="feature-card">
            <div className="feature-icon">🧠</div>
            <h3>Adaptive Interview</h3>
            <p>
              Questions dynamically adapt according to your
              performance and understanding.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📚</div>
            <h3>Curriculum Based</h3>
            <p>
              Interview questions are generated from your
              learning objectives and technical topics.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>AI Evaluation</h3>
            <p>
              Get scores, strengths, knowledge gaps and
              personalized improvement suggestions.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">💡</div>
            <h3>Actionable Feedback</h3>
            <p>
              Identify weak areas and receive recommended
              topics to review.
            </p>
          </div>

        </div>

        <div className="start-section">

          <div className="interview-info">
            <span>8+ Questions</span>
            <span>4+ Topics</span>
            <span>Adaptive Flow</span>
            <span>AI Evaluation</span>
          </div>

          <button
            className="start-button"
            onClick={() => {
              window.location.href = "/interview.html";
            }}
          >
            Start Interview
            <span>→</span>
          </button>

          <p className="start-note">
            No account required • Technical interview simulation
          </p>

        </div>

      </section>

      <footer>
        InterviewOS · AI Technical Interview Operating System
      </footer>

    </main>
  );
}