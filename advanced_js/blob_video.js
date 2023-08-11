// Decode base64 video data
const videoBytes = atob(response.file);
var byteNumbers = new Array(videoBytes.length);
console.info(byteNumbers);

//116544281
for (var i = 0; i < videoBytes.length; i++) {
  byteNumbers[i] = videoBytes.charCodeAt(i);
}

//The Uint8Array represents an array of 8-bit unsigned integers, 
//which is suitable for representing binary data like video or audio.
var byteArray = new Uint8Array(byteNumbers);

// Create video blob
const videoBlob = new Blob([byteArray], { type: 'video/mp4' });

// Create video URL
const videoURL = URL.createObjectURL(videoBlob);

// Set video player source
var videoPlayer = document.querySelector('#video-player');
videoPlayer.src = videoURL;