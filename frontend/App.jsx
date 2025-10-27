import { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [response, setResponse] = useState(null);

  const sendRequest = async () => {
    const res = await fetch("http://localhost:8000/user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, age: Number(age) }),
    });
    const data = await res.json();
    setResponse(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>백엔드 연동 예제</h2>
      <input placeholder="이름" value={name} onChange={(e) => setName(e.target.value)} />
      <input placeholder="나이" value={age} onChange={(e) => setAge(e.target.value)} />
      <button onClick={sendRequest}>전송</button>

      {response && (
        <div style={{ marginTop: 20 }}>
          <p>서버 응답: {response.message}</p>
          <p>성인 여부: {response.is_adult ? "성인" : "미성년자"}</p>
        </div>
      )}
    </div>
  );
}

export default App;