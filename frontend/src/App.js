import React, { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    const res = await fetch("/api/chat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();

    // Handle both possible response formats
    const aiReply = data.data?.reply || data.reply || "No response";

    setChat([
      ...chat,
      { role: "User", text: message },
      { role: "AI", text: aiReply },
    ]);

    setMessage("");
  };

  const resetChat = async () => {
    await fetch("/api/reset/", { method: "POST" });
    setChat([]);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Chat System</h2>

      <div
        style={{
          border: "1px solid gray",
          padding: "10px",
          height: "300px",
          overflowY: "scroll",
        }}
      >
        {chat.map((c, i) => (
          <p key={i}>
            <b>{c.role}:</b> {c.text}
          </p>
        ))}
      </div>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{ width: "80%" }}
      />

      <button onClick={sendMessage}>Send</button>
      <button onClick={resetChat}>Reset</button>
    </div>
  );
}

export default App;
