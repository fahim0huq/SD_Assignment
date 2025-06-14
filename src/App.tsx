import './App.css';
import React, { useState, useEffect, type ChangeEvent, type FormEvent } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

interface FormData {
  name: string;
  email: string;
}

function App() {
  const [count, setCount] = useState<number>(0);
  const [users, setUsers] = useState<User[]>([]);
  const [formData, setFormData] = useState<FormData>({ name: '', email: '' });
  const [submitted, setSubmitted] = useState<FormData | null>(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then((data: User[]) => setUsers(data.slice(0, 10)));
  }, []);

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setSubmitted(formData);
    setFormData({ name: '', email: '' });
  };

  return (
    <div className="container">
      <div className="navbar">
        <h1>React Lab Demo</h1>
      </div>

      <div className="greeting">
        <h2>Hello, Fahim!</h2>
        <p>Button clicked {count} times.</p>
        <button onClick={() => setCount(count + 1)}>Click Me</button>
      </div>

      <h3 className="section-title">Users (Fetched from API)</h3>
      <div className="card-container">
        {users.map(user => (
          <div className="card" key={user.id}>
            <h4>{user.name}</h4>
            <p>{user.email}</p>
          </div>
        ))}
      </div>

      <h3 className="section-title">Submit a Form</h3>
      <div className="form-section">
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            placeholder="Your name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Your email"
            value={formData.email}
            onChange={handleInputChange}
            required
          />
          <button type="submit">Submit</button>
        </form>

        {submitted && (
          <div className="submitted">
            <p><strong>Name:</strong> {submitted.name}</p>
            <p><strong>Email:</strong> {submitted.email}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
