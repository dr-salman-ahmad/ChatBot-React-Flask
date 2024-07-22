// src/Chat.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Form, Button, Card } from 'react-bootstrap';


const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    setMessages([
      { id: 1, text: 'Hi! How can I assist you today?', sender: 'bot' },
    ]);
  }, []);

  const sendMessage = async () => {
    const userMessage = { id: messages.length + 1, text: input, sender: 'user' };
    setMessages([...messages, userMessage]);
    setInput('');

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', {
        messages: [{ role: 'user', content: input }],
      });
      const botMessage = {
        id: messages.length + 2,
        text: response.data.response,
        sender: 'bot',
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container>
      <Row className="justify-content-md-center mt-4">
        <Col md={8}>
          <Card>
            <Card.Header as="h5">Chatbot</Card.Header>
            <Card.Body style={{ height: '400px', overflowY: 'auto' }}>
              {messages.map((message) => (
                <div key={message.id} className={`d-flex ${message.sender === 'bot' ? 'justify-content-start' : 'justify-content-end'} mb-2`}>
                  <div
                    className={`p-2 rounded ${message.sender === 'bot' ? 'bg-info' : 'bg-light'}`}
                    style={{
                      maxWidth: '70%',
                      borderRadius: '20px',
                      padding: '10px',
                      backgroundColor: message.sender === 'bot' ? '#cce5ff' : '#f8f9fa',
                      color: message.sender === 'bot' ? '#004085' : '#212529',
                    }}
                  >
                    {message.text}
                  </div>
                </div>
              ))}
            </Card.Body>
            <Card.Footer>
              <Form.Group className="mb-3" controlId="formMessage">
                <Form.Control
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
                  placeholder="Type your message here"
                />
              </Form.Group>
              <Button variant="primary" onClick={sendMessage}>Send</Button>
            </Card.Footer>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Chat;
