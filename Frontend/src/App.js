import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [responseText, setResponseText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/generate-code", {
        content: inputText,
      });

      if (res.data.response) {
        setResponseText(res.data.response);
      } else if (res.data.error) {
        setResponseText(res.data.error);
      }
    } catch (error) {
      console.error("Error sending request:", error);
      setResponseText("Error processing the request.");
    }
  };

  return (
    <div className="App">
      <h1>Send Sentence to Backend</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Enter the sentence you want to send to the backend"
          rows={5}
          style={{ width: "100%", padding: "10px" }}
        />
        <button type="submit">Send to Backend</button>
      </form>
      <h2>Response:</h2>
      <pre>{responseText}</pre>
    </div>
  );
}

export default App;
