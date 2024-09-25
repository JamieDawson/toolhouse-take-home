import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [responseText, setResponseText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/generate-code", {
        content: inputText,
      });
      console.log(res);

      if (res.data.response) {
        console.log("Content got called");
        setResponseText(res.data.response);
      } else if (res.data.tool_call_code) {
        console.log("Tool call got called");
        const parsedToolCall = JSON.parse(res.data.tool_call_code);
        setResponseText(parsedToolCall.code_str);
      } else if (res.data.error) {
        setResponseText(res.data.error);
      }
    } catch (error) {
      console.error("Error sending request:", error);
      setResponseText("Error processing the request.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Request code!</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Enter the sentence you want to send to the backend"
          rows={5}
          style={{ width: "60%", padding: "10px" }}
        />
        <br />
        <button type="submit">Send to Backend</button>
      </form>

      {loading && <p>Your code is loading. This might take a few seconds...</p>}

      <h2>Response:</h2>
      <div
        style={{
          whiteSpace: "pre-wrap",
          wordWrap: "break-word",
          paddingLeft: "60px",
          maxWidth: "80%", // Limit the width to prevent overflow
          overflow: "auto", // Add scroll if necessary
          boxSizing: "border-box", // Include padding in width calculation
        }}
      >
        <pre style={{ margin: 0 }}>
          <code>{responseText}</code>
        </pre>
      </div>
    </div>
  );
}

export default App;
