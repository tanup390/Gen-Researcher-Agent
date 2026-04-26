import { useEffect, useRef, useState } from "react";
import axios from "axios";

const starterPrompts = [
  "Plan an efficient route for multi-stop delivery.",
  "Summarize shipment delays and operational risks.",
  "Suggest warehouse improvements for faster dispatch.",
];

function MessageBubble({ role, content }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "justify-end" : "justify-start"}`}>
      <div className={`message-bubble-wrap ${isUser ? "items-end" : "items-start"}`}>
        <span className="message-label">
          {isUser ? "You" : "Assistant"}
        </span>
        <div
          className={`message-bubble ${
            isUser ? "message-bubble-user" : "message-bubble-assistant"
          }`}
        >
          <p className="message-text">{content}</p>
        </div>
      </div>
    </div>
  );
}

function TypingIndicator() {
  return (
    <div className="message-row justify-start">
      <div className="message-bubble-wrap items-start">
        <span className="message-label">Assistant</span>
        <div className="message-bubble message-bubble-assistant typing-indicator">
          <span className="typing-dot" />
          <span className="typing-dot" />
          <span className="typing-dot" />
        </div>
      </div>
    </div>
  );
}

function App() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello. I am your Logistics AI copilot." },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  const sendMessage = async (value = input) => {
    const trimmedValue = value.trim();
    if (!trimmedValue || isLoading) return;

    const userMessage = { role: "user", content: trimmedValue };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:8000/ask", {
        query: trimmedValue,
      });

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: response.data.response },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Error connecting to AI backend.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="app-shell">
      <div className="app-background" />

      <main className="chat-app">
        <header className="topbar">
          <div>
            <p className="topbar-eyebrow">Operations Workspace</p>
            <h1 className="topbar-title">Logistics AI Assistant</h1>
          </div>
          <div className="status-pill">
            <span className="status-dot" />
            <span>AI Copilot • Online</span>
          </div>
        </header>

        <section className="prompt-row">
          {starterPrompts.map((prompt) => (
            <button
              key={prompt}
              type="button"
              className="prompt-chip"
              onClick={() => sendMessage(prompt)}
            >
              {prompt}
            </button>
          ))}
        </section>

        <section className="chat-panel">
          <div className="messages-area">
            {messages.map((message, index) => (
              <MessageBubble
                key={`${message.role}-${index}`}
                role={message.role}
                content={message.content}
              />
            ))}

            {isLoading && <TypingIndicator />}
            <div ref={messagesEndRef} />
          </div>

          <div className="composer-shell">
            <div className="composer">
              <textarea
                rows="1"
                className="composer-input"
                value={input}
                onChange={(event) => setInput(event.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask about routing, delays, fleet planning, warehousing, or shipment operations..."
              />

              <button
                type="button"
                className="send-button"
                onClick={() => sendMessage()}
                disabled={isLoading || !input.trim()}
              >
                <span>Send</span>
              </button>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
