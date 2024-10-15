import { useEffect, useState } from "react";
import { BASE_URL, LOCAL_URL, USERS } from "./config";
import axios from "axios";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);

  const fetchUsers = async () => {
    const response = await axios.get(`${BASE_URL}${USERS.USERS}`);
    setUsers(response.data.users);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <>
      <div>
        {users.map((user, index) => (
          <div key={index}>
            <span>{user}</span>
            <br />
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
