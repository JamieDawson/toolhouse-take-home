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

      if (res.data.response) {
        setResponseText(res.data.response);
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
          paddingLeft: "60px", // Padding on the left
          maxWidth: "60%", // Set max width to prevent it from being too wide
        }}
      >
        {responseText}
      </div>
    </div>
  );
}

export default App;

/*
"Generate Two Sum code."
        "Make the two arguements array called nums=[2,7,11,15] and target=9."
        "After posting the code, give a basic explination on how the code works"
*/
