// scripts/app.js
document.querySelector('button').addEventListener('click', async () => {
  const fileInput = document.querySelector('input[type="file"]');
  if (!fileInput.files.length) return alert("Please select an image!");

  const formData = new FormData();
  formData.append('image', fileInput.files[0]);

  try {
    const response = await fetch('/convert', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    
    const videoOutput = document.getElementById('video-output');
    videoOutput.innerHTML = `<video src="${data.video_url}" controls></video>`;
  } catch (error) {
    console.error("Error:", error);
  }
});
