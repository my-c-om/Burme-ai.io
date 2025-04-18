// app.js
document.getElementById('convert-btn').addEventListener('click', async () => {
  const fileInput = document.getElementById('image-upload');
  
  if (!fileInput.files[0]) {
    alert("Please select an image first!");
    return;
  }

  // Show loading state
  const btn = document.getElementById('convert-btn');
  btn.disabled = true;
  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';

  // Send to backend
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  try {
    const response = await fetch('/convert', {
      method: 'POST',
      body: formData
    });
    
    const result = await response.json();
    document.getElementById('video-output').innerHTML = `
      <video controls autoplay class="result-video">
        <source src="${result.video_url}" type="video/mp4">
      </video>
    `;
  } catch (error) {
    console.error("Error:", error);
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<i class="fas fa-magic"></i> Convert to Video';
  }
});
