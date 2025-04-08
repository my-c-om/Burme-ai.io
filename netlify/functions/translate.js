const axios = require('axios');

exports.handler = async (event) => {
  try {
    const { text, targetLang } = JSON.parse(event.body);
    
    const response = await axios.post('https://api.segmind.com/v1/myanmar-translate', {
      text,
      target_lang: targetLang
    }, {
      headers: {
        'x-api-key': process.env.SEGMIND_API_KEY,
        'Content-Type': 'application/json'
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ translation: response.data.translated_text })
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
