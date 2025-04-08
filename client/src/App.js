import React, { useState } from 'react';
import { Button, TextField, Box, Typography } from '@mui/material';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const handleTranslate = async () => {
    try {
      const response = await fetch('/.netlify/functions/translate', {
        method: 'POST',
        body: JSON.stringify({ text: inputText, targetLang: 'my' })
      });
      const data = await response.json();
      setOutputText(data.translation);
    } catch (error) {
      console.error('Translation error:', error);
    }
  };

  return (
    <Box sx={{ maxWidth: 800, margin: 'auto', p: 4 }}>
      <Typography variant="h4" gutterBottom>
        Burma.ai Translator
      </Typography>
      <TextField
        fullWidth
        multiline
        rows={4}
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter English text"
        sx={{ mb: 2 }}
      />
      <Button variant="contained" onClick={handleTranslate}>
        Translate to Myanmar
      </Button>
      <TextField
        fullWidth
        multiline
        rows={4}
        value={outputText}
        placeholder="Myanmar translation"
        sx={{ mt: 2 }}
        InputProps={{ readOnly: true }}
      />
    </Box>
  );
}

export default App;
