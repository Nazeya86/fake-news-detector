import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [news, setNews] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', {
        news: news,
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error:', error);
      setPrediction('Error connecting to the backend.');
    }
  };

  const fillSampleNews = (type) => {
    const realNews = `The Prime Minister announced new initiatives to support sustainable farming and green technology adoption across rural communities.`;
    const fakeNews = `NASA confirms Earth will be hit by a giant asteroid next week, wiping out all life on the planet.`;

    setNews(type === 'real' ? realNews : fakeNews);
    setPrediction(''); // Clear old prediction
  };

  return (
    <div className="container">
      <h1 className="title">📰 Fake News Detector</h1>
      
      <div className="sample-buttons">
        <button className="sample-button real-sample" onClick={() => fillSampleNews('real')}>
          Sample Real News
        </button>
        <button className="sample-button fake-sample" onClick={() => fillSampleNews('fake')}>
          Sample Fake News
        </button>
      </div>

      <form onSubmit={handleSubmit} className="form">
        <textarea
          placeholder="Enter news content here..."
          value={news}
          onChange={(e) => setNews(e.target.value)}
          className="textarea"
          rows={6}
        />
        <button type="submit" className="button">Check</button>
      </form>

      {prediction && (
        <div className="result-container">
          <h2 className="result-title">Prediction:</h2>
          <p className={`result-text ${prediction === 'Fake' ? 'fake' : 'real'}`}>
            {prediction === 'Fake' ? '❌ Fake News' : '✅ Real News'}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
