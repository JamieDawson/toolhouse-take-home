import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState(""); //Stores data from textarea
  const [responseText, setResponseText] = useState(""); //Stores data from response
  const [loading, setLoading] = useState(false); //Stores loading state depending if we are waiting for a response.

  //The function that is tricked when we submit the form
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Send the request to the backend.
      const res = await axios.post("http://localhost:5000/generate-code", {
        content: inputText,
      });
      console.log(res);

      //Checks if the return value is either response or tool_call_code!
      if (res.data.response) {
        console.log("Content found");
        setResponseText(res.data.response);
      } else if (res.data.tool_call_code) {
        console.log("Tool_call found");
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
