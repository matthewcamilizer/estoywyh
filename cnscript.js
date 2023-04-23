const wrapper = document.querySelector(".wrapper"),
musicImg = wrapper.querySelector(".img-area img"),
musicName = wrapper.querySelector(".song-details .name"),
musicArtist = wrapper.querySelector(".song-details .artist"),
musicGenre = wrapper.querySelector(".song-details .genre"),
playPauseBtn = wrapper.querySelector(".play-pause"),
shareButton = wrapper.querySelector("#share"),

volumeControl = wrapper.querySelector("#vc"),
sliderShow = wrapper.querySelector(".slider_container")
volumeProgress = wrapper.querySelector(".volumee"),
volumeMute = wrapper.querySelector(".fa-volume-mute"),
volumeMax = wrapper.querySelector(".fa-volume-up"),
showCase = wrapper.querySelector(".sc"),
topBar = wrapper.querySelector(".top-bar"),
opVolume = wrapper.querySelector("#opvc"),
areaOption = wrapper.querySelector(".wrapperr"),
closeOptions = wrapper.querySelector("#close_op"),
musicOption = wrapper.querySelector("#zzy"),
muteArtist = wrapper.querySelector(".noat"),
onlyArtist = wrapper.querySelector(".oat"),
muteGenre = wrapper.querySelector(".nogenre"),
onlyGenre = wrapper.querySelector(".ogenre"),
allGenre = wrapper.querySelector(".showgenre"),
allArtist = wrapper.querySelector(".showat"),
resetLartist = wrapper.querySelector(".reset_artists"),
resetLgenre = wrapper.querySelector(".reset_genres"),
showLa = wrapper.querySelector(".showlat"),
showLg = wrapper.querySelector(".showlgenre"),
showDlg = wrapper.querySelector(".showdlgenre"),
showDla = wrapper.querySelector(".showdlat"),
resetDlartist = wrapper.querySelector(".reset_dlartists"),
resetDlgenre = wrapper.querySelector(".reset_dlgenres"),
setCanvas = document.querySelector("#video-background"),

prevBtn = wrapper.querySelector("#prev"),
nextBtn = wrapper.querySelector("#next"),
mainAudio = wrapper.querySelector("#main-audio"),
progressArea = wrapper.querySelector(".progress-area"),
progressBar = progressArea.querySelector(".progress-bar"),
musicList = wrapper.querySelector(".music-list"),
moreMusicBtn = wrapper.querySelector("#more-music"),
lyContainer = wrapper.querySelector('.lycontainer');
closemoreMusic = musicList.querySelector("#close"),
closeLyric = lyContainer.querySelector("#closelyric"),
now_playing = musicList.querySelector('.now-playing');
//dynamic title while playing
dynamicTitle = document.querySelector("title")
dynamicIcon = document.getElementById("ddicon");

lyricThreshold = document.querySelector(".threshold");
lyricContainer = document.querySelector("#lyrics");
lyricTitle = document.querySelector(".lytitle");
boardLyric = document.querySelector("#b");
boardGenre = document.querySelector("#c");


let musicIndex = Math.floor((Math.random() * allMusic.length) + 1);
isMusicPaused = true;


//const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

  //hover compliation
  //main player hover opacity:0.2 for every devices
  let PCtimeoutId;
  let PCisActive = false;
  
  function PCactivateBox() {
    wrapper.classList.remove('inactive');
    PCisActive = true;
  }
  function dePCactivateBox() {
    wrapper.classList.add('inactive');
    PCisActive = false;
  }
  function PCresetTimeout() {
    clearTimeout(PCtimeoutId);
    PCtimeoutId = setTimeout(() => {
      dePCactivateBox();
    }, 7500);
  }
  wrapper.addEventListener('mousedown', () => {
    PCactivateBox();
    PCresetTimeout();
  });
  wrapper.addEventListener('mousemove', () => {
    if (!PCisActive) {
      PCactivateBox();
    }
    PCresetTimeout();
  });
  wrapper.addEventListener('mouseleave', () => {
    PCresetTimeout();
  });
  PCresetTimeout();
  //volumebar disappear for every devices
  let PCVolumePCtimeoutId;
  let PCvolumeActive = false;
  function PCactivateVolume() {
      volumeProgress.classList.add("showw");
      voloumeActive = true;
      PCresetVolumeTimeout()
  }
  function dePCactivateVolume() {
    volumeProgress.classList.remove("showw");
    voloumeActive = false;
    PCresetVolumeTimeout()
  } 
  function PCresetVolumeTimeout() {
    clearTimeout(PCVolumePCtimeoutId);
    PCVolumePCtimeoutId = setTimeout(() => {
      dePCactivateVolume();
    }, 5000);
  }
  volumeProgress.addEventListener('mousedown', () => {
    PCactivateVolume();
    PCresetVolumeTimeout();
  });
  volumeProgress.addEventListener('mousemove', () => {
    if (!PCvolumeActive) {
      PCactivateVolume();
    }
    PCresetVolumeTimeout();
  });
  volumeProgress.addEventListener('mouseleave', () => {
    PCresetVolumeTimeout();
  });
  PCresetVolumeTimeout();
  //Option fly away for every devices
  let PCOptionPCtimeoutId, PCOptionActive = false;
  function PCactivateOption() {
    areaOption.classList.add("show");
    PCOptionActive = true;
    PCresetOptionTimeout()
  }
  function dePCactivateOption() {
    areaOption.classList.remove("show");
    PCOptionActive = false;
    PCresetOptionTimeout()
  }
  function PCresetOptionTimeout() {
  clearTimeout(PCOptionPCtimeoutId);
  PCOptionPCtimeoutId = setTimeout(() => {
    dePCactivateOption();
  }, 10000);
  }
  areaOption.addEventListener('mousedown', () => {
  PCactivateOption();
  PCresetOptionTimeout();
  });
  areaOption.addEventListener('mousemove', () => {
  if (!PCOptionActive) {
    PCactivateOption();
  }
  PCresetOptionTimeout();
  });
  areaOption.addEventListener('mouseleave', () => {
  PCresetOptionTimeout();
  });
  PCresetOptionTimeout();
  //Musiclist down for every devices
  let ListPCtimeoutId, ListPCActive = false;
  function PCactivateList() {
    musicList.classList.add("show");
    ListPCActive = true;
    PCresetListTimeout()
  }
  function dePCactivateList() {
  musicList.classList.remove("show");
  ListPCActive = false;
  PCresetListTimeout()
  }
  function PCresetListTimeout() {
  clearTimeout(ListPCtimeoutId);
  ListPCtimeoutId = setTimeout(() => {
    dePCactivateList();
  }, 15000);
  }
  musicList.addEventListener('mousedown', () => {
  PCactivateList();
  PCresetListTimeout();
  });
  musicList.addEventListener('mousemove', () => {
  if (!ListPCActive) {
    PCactivateList();
  }
  PCresetListTimeout();
  });
  musicList.addEventListener('mouseleave', () => {
  PCresetListTimeout();
  });
  PCresetListTimeout();


  //mobile
  let timeoutId;
let isActive = false;

function activateBox() {
  wrapper.classList.remove('inactive');
  isActive = true;
}
function deactivateBox() {
  wrapper.classList.add('inactive');
  isActive = false;
}
function resetTimeout() {
  clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    deactivateBox();
  }, 7500);
}
wrapper.addEventListener('touchstart', () => {
  activateBox();
  resetTimeout();
});
wrapper.addEventListener('touchmove', () => {
  if (!isActive) {
    activateBox();
  }
  resetTimeout();
});
wrapper.addEventListener('touchend', () => {
  resetTimeout();
});
resetTimeout();


//volumebar disappear for every devices
let VolumetimeoutId;
let volumeActive = false;
function activateVolume() {
    volumeProgress.classList.add("showw");
    voloumeActive = true;
    resetVolumeTimeout()
}
function deactivateVolume() {
  volumeProgress.classList.remove("showw");
  voloumeActive = false;
  resetVolumeTimeout()
}
function resetVolumeTimeout() {
  clearTimeout(VolumetimeoutId);
  VolumetimeoutId = setTimeout(() => {
    deactivateVolume();
  }, 5000);
}
volumeProgress.addEventListener('touchstart', () => {
  activateVolume();
  resetVolumeTimeout();
});
volumeProgress.addEventListener('touchmove', () => {
  if (!volumeActive) {
    activateVolume();
  }
  resetVolumeTimeout();
});
volumeProgress.addEventListener('touchend', () => {
  resetVolumeTimeout();
});
resetVolumeTimeout();
let OptiontimeoutId, OptionActive = false;
function activateOption() {
  areaOption.classList.add("show");
  OptionActive = true;
  resetOptionTimeout()
}
function deactivateOption() {
  areaOption.classList.remove("show");
  OptionActive = false;
  resetOptionTimeout()
}
function resetOptionTimeout() {
clearTimeout(OptiontimeoutId);
OptiontimeoutId = setTimeout(() => {
  deactivateOption();
}, 10000);
}
areaOption.addEventListener('touchstart', () => {
activateOption();
resetOptionTimeout();
});
areaOption.addEventListener('touchmove', () => {
if (!OptionActive) {
  activateOption();
}
resetOptionTimeout();
});
areaOption.addEventListener('touchend', () => {
resetOptionTimeout();
});
resetOptionTimeout();
let ListtimeoutId, ListActive = false;
function activateList() {
  musicList.classList.add("show");
  ListActive = true;
  resetListTimeout()
}
function deactivateList() {
musicList.classList.remove("show");
ListActive = false;
resetListTimeout()
}
function resetListTimeout() {
clearTimeout(ListtimeoutId);
ListtimeoutId = setTimeout(() => {
  deactivateList();
}, 15000);
}
musicList.addEventListener('touchstart', () => {
activateList();
resetListTimeout();
});
musicList.addEventListener('touchmove', () => {
if (!ListActive) {
  activateList();
}
resetListTimeout();
});
musicList.addEventListener('touchend', () => {
resetListTimeout();
});
resetListTimeout();




shareButton.addEventListener("click",()=>{
  navigator.clipboard.writeText(window.location.href + "&t=" + mainAudio.currentTime);
})




let timeStamp = 0;
window.addEventListener("hashchange", () => {
  const urlHash = window.location.hash.slice(1).toLowerCase();// get hash from URL and convert to lowercase
  let [hash, timestampStr] = decodeURIComponent(urlHash).split("&t=");
  if (urlHash) { // if hash is present, try to load song by id
    function convertTimeToSeconds() {
      if (/^\d+$/.test(timestampStr)) { // check if timestampStr is a single integer
        timestampStr = parseInt(timestampStr, 10);
      } else {
      const [minutesStr, secondsStr] = timestampStr.split(":");
      const minutes = parseInt(minutesStr, 10) || 0;
      const seconds = parseFloat(secondsStr, 0) || 0;
      timestampStr = minutes * 60 + seconds;
      }
    }
    convertTimeToSeconds()

    const song = allMusic.find((song) => song.hash.toLowerCase() === hash);
    timeStamp = parseFloat(timestampStr, 0) || 0;
    if (song) {
      loadMusic(allMusic.indexOf(song) + 1);
      musicIndex = allMusic.indexOf(song) + 1;
    } else {
      loadMusic(musicIndex); // fallback to default musicIndex if song with id is not found
    }
  } else { // no hash present, so load default musicIndex
    loadMusic(musicIndex);
  }
  progressBar.style.width = 0;
  playPauseBtn.querySelector("i").innerText = "play_arrow";
  wrapper.classList.remove("paused");
  musicImg.classList.remove('rotate');
  void musicImg.offsetWidth;
});

window.addEventListener("load", () => {
  const urlHash = window.location.hash.slice(1).toLowerCase(); // get hash from URL and convert to lowercase

  if (urlHash) { // if hash is present, try to load song by id
    let [hash, timestampStr] = decodeURIComponent(urlHash).split("&t=");
    const song = allMusic.find((song) => song.hash.toLowerCase() === hash);
    if (song) {
      loadMusic(allMusic.indexOf(song) + 1);
      musicIndex = allMusic.indexOf(song) + 1; 
      if (timestampStr){
      function convertTimeToSeconds() {
        if (/^\d+$/.test(timestampStr)) { // check if timestampStr is a single integer
          timestampStr = parseInt(timestampStr, 10);
        } else {
        const [minutesStr, secondsStr] = timestampStr.split(":");
        const minutes = parseInt(minutesStr, 10) || 0;
        const seconds = parseFloat(secondsStr, 0) || 0;
        timestampStr = minutes * 60 + seconds;
        }
      }
      convertTimeToSeconds()
      const timestamp = parseFloat(timestampStr, 0) || 0;
      mainAudio.currentTime = timestamp;
    }
    } else {
      loadMusic(musicIndex); // fallback to default musicIndex if song with id is not found
    }
    //refresh without hash
    history.replaceState(null, null, ' '); // remove the hash from the URL

  } else { // no hash present, so load default musicIndex
    loadMusic(musicIndex); 
     
  }
  history.replaceState('', '', `#${allMusic[musicIndex - 1 ].hash}`);
  playingSong();
});

// ZZY required
let likedArtists = [], dislikedArtists = [], likedGenres = [], dislikedGenres = [], fnlikedArtists = [], fnlikedGenres = [], fplikedGenres = [], fplikedArtists = [];

allArtist.addEventListener("click",()=>{
  let ATA = [];
  for (let i = 0; i < allMusic.length; i++){
    ATA.push(allMusic[i].artist);
  }
  const fakeshow = new Set(ATA);
  const show = Array.from(fakeshow).sort((a,b) => a.localeCompare(b)).join(', ');
  alert("每个歌手由逗号和空格隔开:\n\n" + show);
})
allGenre.addEventListener("click",()=>{
  let ATG = [];
  for (let i = 0; i < allMusic.length; i++){
    ATG.push(allMusic[i].genre);
  }
  const fakeshow = new Set(ATG);
  const show = Array.from(fakeshow).sort((a,b) => a.localeCompare(b)).join(', ');
  alert("每个风格由逗号和空格隔开:\n\n" + show);
})

let enterLikeArtists = [], enterLikeGenres = [], oastoredValue = [], ogstoredValue = [], nastoredValue = [], ngstoredValue = [];
let enterDislikesa = [], enterDislikesg = [];

onlyArtist.addEventListener("click", ()=>{
  enterLikeArtists = prompt("输入你想听的歌手，用逗号隔开，不区分大小写", oastoredValue);
  if (enterLikeArtists) {
    oastoredValue = enterLikeArtists;
    likedArtists = enterLikeArtists.split(',').map(artist => artist.trim());
    fnlikedArtists = likedArtists.map(artist => artist.toLowerCase());
    fplikedArtists = likedArtists.map(artist => artist.toLowerCase());
  }
  else {
    if (oastoredValue.length === 0) {
      enterLikeArtists = [];
    }
    else {
      enterLikeArtists = oastoredValue;
      likedArtists = enterLikeArtists.split(',').map(artist => artist.trim());
      fnlikedArtists = likedArtists.map(artist => artist.toLowerCase());
      fplikedArtists = likedArtists.map(artist => artist.toLowerCase());
    }
  }
});
muteArtist.addEventListener("click",()=>{
  enterDislikesa = prompt("输入你不想听的歌手，用逗号隔开，不区分大小写", nastoredValue);
  if (enterDislikesa) {
    nastoredValue = enterDislikesa;
    dislikedArtists = enterDislikesa.split(',').map(artist => artist.trim());
  }
  else {
    if (nastoredValue.length === 0){
      enterDislikesa = [];
    }
    else {
      enterDislikesa = nastoredValue;
      dislikedArtists = enterDislikesa.split(',').map(artist => artist.trim());
    }
  }
})

onlyGenre.addEventListener("click", ()=>{
  enterLikeGenres = prompt("输入你想听的风格，用逗号隔开，不区分大小写", ogstoredValue);
  if (enterLikeGenres) {
    ogstoredValue = enterLikeGenres;
    likedGenres = enterLikeGenres.split(',').map(genre => genre.trim());
    fplikedGenres = likedGenres.map(genre => genre.toLowerCase());
    fnlikedGenres = likedGenres.map(genre => genre.toLowerCase());
  }
  else {
    if (ogstoredValue.length === 0){
      enterLikeGenres = [];
    }
    else { 
      enterLikeGenres = ogstoredValue;    
      likedGenres = enterLikeGenres.split(',').map(genre => genre.trim());
      fplikedGenres = likedGenres.map(genre => genre.toLowerCase());
      fnlikedGenres = likedGenres.map(genre => genre.toLowerCase()); 
    }
  }
})
muteGenre.addEventListener("click",()=>{
  enterDislikesg = prompt("输入你不想听的风格，用逗号隔开，不区分大小写", ngstoredValue);
  if (enterDislikesg) {
    ngstoredValue = enterDislikesg;
    dislikedGenres = enterDislikesg.split(',').map(genre => genre.trim());
  }
  else {
    if (ngstoredValue.length === 0){
      enterDislikesg = [];
    }
    else {
      enterDislikesg = ngstoredValue;
      dislikedGenres = enterDislikesg.split(',').map(genre => genre.trim());
    }
  }
})

showLa.addEventListener("click", ()=>{
  if (likedArtists.length > 0){
    let ATA = [];
    for (let i = 0; i < likedArtists.length; i++){
      ATA.push(likedArtists[i]);
    }
    alert('这是你想听的歌手，由逗号和空格隔开:\n\n' + ATA.join(', '));
  }
  else {
    alert("你还没输入想听的歌手");
  }
})
showDla.addEventListener("click", ()=>{
  if (dislikedArtists.length > 0){
    let ATA = [];
    for (let i = 0; i < dislikedArtists.length; i++){
      ATA.push(dislikedArtists[i]);
    }
    alert('这是你输入的不想听的歌手，由逗号和空格隔开:\n\n' + ATA.join(', '));
  }
  else {
    alert("你还没输入不想听的歌手");
  }
})

showLg.addEventListener("click",()=>{
  if (likedGenres.length > 0){
    let ATA = [];
    for (let i = 0; i < likedGenres.length; i++){
      ATA.push(likedGenres[i]);
    }
    alert('这是你输入的想听风格，由逗号和空格隔开:\n\n' + ATA.join(', '));
  }
  else {
    alert("你还没输入想听的风格");
  }
})
showDlg.addEventListener("click",()=>{
  if (dislikedGenres.length > 0){
    let ATA = [];
    for (let i = 0; i < dislikedGenres.length; i++){
      ATA.push(dislikedGenres[i]);
    }
    alert('这是你输入的不想听的风格，由逗号和空格隔开:\n\n' + ATA.join(', '));
  }
  else {
    alert("你还没输入不想听的风格");
  }
})

resetLartist.addEventListener("click",()=>{
  if (likedArtists.length > 0){
    likedArtists = [];
    oastoredValue = [];
    enterLikeArtists = [];
    alert("你已清空想听的歌手!");
  }
  else{
    alert("你还没输入想听的歌手");
  }
})
resetDlartist.addEventListener("click",()=>{
  if (dislikedArtists.length > 0){
    dislikedArtists = [];
    nastoredValue = [];
    enterDislikesa = [];
    alert("你已清空不想听的歌手!");
  }
  else{
    alert("你还没输入不想听的歌手");
  }
})

resetLgenre.addEventListener("click",()=>{
  if (likedGenres.length > 0){
    likedGenres = [];
    ogstoredValue = [];  
    enterLikeGenres = [];
    alert("你已清空想听的风格!");
  }
  else{
    alert("你还没输入想听的风格");
  }
})
resetDlgenre.addEventListener("click",()=>{
  if (dislikedGenres.length > 0){
    dislikedGenres = [];
    ngstoredValue = [];
    enterDislikesg = [];
    alert("你已清空不想听的风格!");
  }
  else{
    alert("你还没输入不想听的风格");
  }
})


function loadMusic(indexNumb) {
  mainAudio.src = `static/sla/songs/${allMusic[indexNumb - 1].src}.mp3`;
  mainAudio.currentTime = timeStamp;




  jsmediatags.read(mainAudio.src, {
    onSuccess: function(tag) {
      // Set the metadata fields in your music player using the tag information
      musicName.innerText = tag.tags.title;
      musicArtist.innerText = tag.tags.artist;
      musicGenre.innerText = tag.tags.genre;  
      //dynamic title while playing
      dynamicTitle.textContent =tag.tags.artist + ` - ` + tag.tags.title;
      lyricTitle.textContent =tag.tags.artist + ` - ` + tag.tags.title; 
      lyricThreshold.style.width= "92%";
      // Set the image source for your music player
      var image = tag.tags.picture;
      if (image) {
        var base64String = "";
        for (var i = 0; i < image.data.length; i++) {
          base64String += String.fromCharCode(image.data[i]);
        }
        var base64 = "data:" + image.format + ";base64," + window.btoa(base64String);
        musicImg.src = base64;
      }

      const cretedCSS = document.querySelector("#newCSS");
      if (cretedCSS){document.head.removeChild(cretedCSS);}
      const ToRemove = lyricContainer.querySelectorAll(`[song]:not([song*="${tag.tags.title}"])`);
      if(ToRemove){
        for(let o=0;o<ToRemove.length;o++){
          ToRemove[o].remove();
        }
      }
      fetch(`static/sla/lyrics/${allMusic[indexNumb - 1].src}.json`)
      .then(response => response.json())
      .then(data => {
        // check if scroll or create .empty
        const hasScrolled  = new Array(data[tag.tags.title]['lyrics'].length).fill(false);
        const created  = new Array(data[tag.tags.title]['lyrics'].length).fill(false);
        for (let i = 0; i < data[tag.tags.title]['lyrics'].length; i++) {
          let subly = `<div class=lyct id="${i}" song=${tag.tags.title} >
              <div class=lyrics id="lyric-${i}">${data[tag.tags.title]['lyrics'][i].text}</div>
              <div id="shinely-${i}">${data[tag.tags.title]['lyrics'][i].text}</div>
            </div>`;
          lyricContainer.insertAdjacentHTML("beforeend", subly);
        }

        lyricContainer.scrollTop = 0;
        mainAudio.addEventListener('timeupdate', () => {
          const currentTime = mainAudio.currentTime;
          let foundCurrentLyric = false;
          let currentLyricIndex = 0;
            for (let i = 0; i < data[tag.tags.title]['lyrics'].length; i++) {
              if (currentTime >= data[tag.tags.title]['lyrics'][i].start && currentTime <= data[tag.tags.title]['lyrics'][i].end) {
                currentLyricIndex = i;
                foundCurrentLyric = true;
                const animationDuration = data[tag.tags.title]['lyrics'][i].end - data[tag.tags.title]['lyrics'][i].start + 0.2;
                document.body.style.setProperty('--animation-duration', animationDuration + 's');
              }
            }
    
            for (let j = 0; j < data[tag.tags.title]['lyrics'].length; j++){
            const lyricElem = document.getElementById(`lyric-${j}`);
            const lyct = document.getElementById(`${j}`);
            const shine = document.getElementById(`shinely-${j}`);  
            if (j === currentLyricIndex && foundCurrentLyric) {
                lyricElem.classList.add('highlight');
                lyricElem.classList.remove('played');
                lyct.classList.add('cu');
                lyct.classList.remove('played');
                lyricElem.setAttribute('data-text', lyricElem.textContent);
                shine.classList.add('shinely');
    
                let anishine = document.querySelector(".shinely");
                if(wrapper.classList.contains('paused')){anishine.style.animationPlayState = "running";}
                else{anishine.style.animationPlayState = "paused";}  
    
                let duration = data[tag.tags.title]['lyrics'][j].end - data[tag.tags.title]['lyrics'][j].start;
                let currentTime = mainAudio.currentTime - data[tag.tags.title]['lyrics'][j].start;
                let percentage = currentTime / duration;
                shine.scrollLeft = (lyricElem.scrollWidth - lyricElem.clientWidth) * percentage;
                lyricElem.scrollLeft = (lyricElem.scrollWidth - lyricElem.clientWidth) * percentage;
                
    
                let CurrentLyric = document.querySelector('.cu');
                let lyel = document.querySelector('.lyct');
                let VisibleLyricAboveQuality = Math.floor(CurrentLyric.offsetTop / lyel.offsetHeight);
    
                //the quality of visible lyrics
                let ScollThreshold = Math.floor((lyricContainer.offsetHeight / 2 - CurrentLyric.offsetHeight) / lyel.offsetHeight);
    
                if (VisibleLyricAboveQuality >= ScollThreshold && !hasScrolled[j]){
                  lyricContainer.scrollTop += CurrentLyric.offsetHeight;
                  console.log(lyricContainer.scrollTop);
                  hasScrolled[j] = true;
                }
              // If we've scrolled to the bottom and there are still more lyrics, create a new empty div
              if (lyricContainer.scrollTop >= lyricContainer.scrollHeight - lyricContainer.offsetHeight && j < lyrics.length - 2 
                && !created[j]) {
                  const emptyLyricElem = document.createElement('div');
                  emptyLyricElem.classList.add('empty');
                  lyricContainer.appendChild(emptyLyricElem);
                  var emp = `.empty{
                    position: relative;
                    width: 100%;
                    min-height: 2em;
                  }`;
                  var style = document.createElement("style");
                  style.appendChild(document.createTextNode(emp));
                  document.head.appendChild(style);
                  created[j] = true;
                } 
              }
            if (j < currentLyricIndex) {
                  hasScrolled[j] = false;
                shine.classList.remove('shinely');
                lyricElem.classList.add('played');
                lyricElem.classList.remove('highlight');
                lyct.classList.add('played');
                lyct.classList.remove('cu');
              }
            if (j > currentLyricIndex) {
                shine.classList.remove('shinely');
                lyricElem.classList.remove('played');
                lyricElem.classList.remove('highlight');
                lyct.classList.remove('played');
                lyct.classList.remove('cu');
              }
            }
          });
    
    
        for (let i = 0; i < data[tag.tags.title]['lyrics'].length; i++) {
          let dylyric = document.getElementById(`${i}`);
          dylyric.addEventListener("click", ()=>{
            if(dylyric.classList.contains('cu')){if(wrapper.classList.contains('paused')){pauseMusic();}else{playMusic();}}
            else{mainAudio.currentTime = data[tag.tags.title]['lyrics'][i].start;playMusic();}
          });
        }
    
        mainAudio.addEventListener("ended", ()=>{
          for(let j=0;j<data[tag.tags.title]['lyrics'].length;j++){
            const lyricElem = document.getElementById(`lyric-${j}`);
            const lyct = document.getElementById(`${j}`);
            lyricElem.classList.remove('played');
            lyct.classList.remove('played');
          }
    
        let empty = document.querySelectorAll(".empty");for(let i=0;i<empty.length;i++){lyricContainer.removeChild(empty[i]);}
    
        let ScrollInterval;
        ScrollInterval = setInterval(function(){
          lyricContainer.scrollTop -= 50;
          if (lyricContainer.scrollTop === 0){clearInterval(ScrollInterval);}
        }, 40); 
        })
      })
      .catch(error => {
        lyricContainer.innerHTML="";
        const cretedCSS = document.querySelector("#newCSS");
        var newcss = `
        #lyrics{
          display: flex;
          align-items: center;
          justifyContent: center;
        } 
        .what{
          padding-left: 8px;
        }
        `;
        var style = document.createElement("style");
        if (cretedCSS){
          document.head.removeChild(cretedCSS);
          {
            style.setAttribute("id","newCSS");
            style.appendChild(document.createTextNode(newcss));
            document.head.appendChild(style);
            let what = `<div class="what" id="wt">Lyrics came to visit Elon Musk</div>` 
            lyricContainer.insertAdjacentHTML("beforeend",what);
          }
        }
        else{
            style.setAttribute("id","newCSS");
            style.appendChild(document.createTextNode(newcss));
            document.head.appendChild(style);
            let what = `<div class="what" id="wt">Lyrics came to visit Elon Musk</div>` 
            lyricContainer.insertAdjacentHTML("beforeend",what);
          }
          lyricThreshold.style.width= "100%";
          console.error('Error fetching JSON data:', error);
      });

    },
    onError: function(error) {if(error){throw(error);}}
  });

  dynamicIcon.setAttribute("href", `static/sla/images/${allMusic[indexNumb - 1].src}.ico`);
  now_playing.textContent = (indexNumb) + " / " + allMusic.length;
  if(allMusic[indexNumb - 1].canvas){
    setCanvas.src = `static/sla/canvas/${allMusic[indexNumb - 1].src}.mp4`; 
    document.body.style.marginTop= "5rem";
    document.body.style.display= "flex";
    document.body.style.alignItems= "top";
    document.body.style.justifyContent= "center";
    document.body.style.minHeight= "100vh";
    document.body.style.background= "linear-gradient(to bottom right, #e3b2f8, #93d0f8, #f3ea96)";
    document.body.style.backgroundSize= "1000%";
    document.body.style.animation= "atl 15s ease-in-out infinite";
    // Create the @keyframes atl animation
    var keyframes = `
    @keyframes atl {
      0% {
        background-position: 0 100%;
      }
      25% {
        background-position: 50% 100%;
      }
      50% {
        background-position: 100% 100%;
      }
      75% {
        background-position: 50% 100%;
      }
      100% {
        background-position: 0 100%;
      }
    }
  `;
  // Append the @keyframes atl animation to the stylesheet
  const canvasCSS = document.querySelector("#canvasCSS");
  if (canvasCSS){
    document.head.removeChild(canvasCSS);
    var style = document.createElement('style');
    style.setAttribute("id","canvasCSS");
    style.appendChild(document.createTextNode(keyframes));
    document.head.appendChild(style);
  }
  else{
    var style = document.createElement('style');
    style.setAttribute("id","canvasCSS");
    style.appendChild(document.createTextNode(keyframes));
    document.head.appendChild(style);
    }
  }
  else{setCanvas.src = "";
  random_bg_color();
  }
  //dynamic URL while playing
  history.pushState('', '', `#${allMusic[indexNumb - 1].hash}`);
}


boardGenre.addEventListener("click",()=>{
  musicGenre.classList.toggle("show");
  if(boardGenre.classList.contains("fa-bars")){boardGenre.classList.replace("fa-bars", "fa-list");}
  else{boardGenre.classList.replace("fa-list", "fa-bars");}
});

boardLyric.addEventListener("click",()=>{
  lyContainer.classList.add("show");
});

closeLyric.addEventListener("click",()=>{
  lyContainer.classList.remove("show");
});


function random_bg_color(){
  let hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
  let a;

  function populate(a){
      for(let i=0; i<6; i++){
          let x = Math.round(Math.random() * 15);
          let y = hex[x];
          a += y;
      }
      return a;
  }
  let Color1 = populate('#'), Color2 = populate('#'), Color3 = populate('#'), Color4 = populate('#');
  var angle = 'to bottom right';
  let gradient = 'linear-gradient(' + angle + ',' + Color1 + ', ' + Color2 + ', ' + Color3 + ', ' + Color4 + ")";
  document.body.style.background = gradient;
  document.body.style.display= "flex";
  document.body.style.alignItems = "top";
  document.body.style.justifyContent = "center";
  document.body.style.minHeight = "100vh";
  document.body.style.backgroundSize = "700%";
  document.body.style.animation= "atl 15s ease-in-out infinite";
    // Create the @keyframes atl animation
    var keyframes = `
    @keyframes atl {
      0% {
        background-position: 0 100%;
      }
      25% {
        background-position: 50% 100%;
      }
      50% {
        background-position: 100% 100%;
      }
      75% {
        background-position: 50% 100%;
      }
      100% {
        background-position: 0 100%;
      }
    }
  `;

  // Append the @keyframes atl animation to the stylesheet
  const bgCSS = document.querySelector("#bgCSS");
  var style = document.createElement('style');
  if(bgCSS)
  {
    document.head.removeChild(bgCSS);  
    style.setAttribute("id","bgCSS");
    style.appendChild(document.createTextNode(keyframes));
    document.head.appendChild(style);
  }
  else 
  {
    style.setAttribute("id","bgCSS");
    style.appendChild(document.createTextNode(keyframes));
    document.head.appendChild(style);
  }
}

//play music function
function playMusic(){
  wrapper.classList.add("paused");
  musicImg.classList.remove('rotatee');
  musicImg.classList.add('rotate');
  playPauseBtn.querySelector("i").innerText = "pause";
  mainAudio.play();
  showCase.textContent = "正在播放...";
}
// Jan 6th

musicImg.addEventListener("click", ()=>{
  const isMusicPlay = wrapper.classList.contains("paused");
  //if isPlayMusic is true then call pauseMusic else call playMusic
  isMusicPlay ? pauseMusic() : playMusic();
  playingSong();
});

//pause music function
function pauseMusic(){
  wrapper.classList.remove("paused");
  musicImg.classList.add('rotatee');
  playPauseBtn.querySelector("i").innerText = "play_arrow";
  mainAudio.pause();
  showCase.textContent = "你好呀!";
}


let AorG = true, agcheck = [];
function checkag(){
  //check like
  if (enterLikeArtists.length > 0 && enterLikeGenres.length === 0 && enterDislikesa.length === 0 && enterDislikesg.length === 0){
    let artists = enterLikeArtists.split(',').map(a => a.trim().toLowerCase());
    agcheck = allMusic.filter(la =>{
      return artists.includes(la.artist.toLowerCase());
    })
  }
  if (enterLikeArtists.length === 0 && enterLikeGenres.length > 0 && enterDislikesa.length === 0 && enterDislikesg.length === 0){
    const genres = enterLikeGenres.split(',').map(g => g.trim().toLowerCase());
    agcheck = allMusic.filter(lg => {
      return genres.includes(lg.genre.toLowerCase());
    })
        
  }
  if (enterLikeArtists.length > 0 && enterLikeGenres.length > 0 && enterDislikesa.length === 0 && enterDislikesg.length === 0){
  agcheck = allMusic.filter(ag => {
    return enterLikeArtists.toLowerCase().includes(ag.artist.toLowerCase()) && enterLikeGenres.toLowerCase().includes(ag.genre.toLowerCase());
  })
  }
  if (enterLikeArtists.length > 0 && enterDislikesg.length > 0 && enterDislikesa.length === 0 && enterLikeGenres.length === 0){
    agcheck = allMusic.filter(ladg => {
      return enterLikeArtists.toLowerCase().includes(ladg.artist.toLowerCase()) && !(enterDislikesg.toLowerCase().includes(ladg.genre.toLowerCase()));
    })
  }
  //check dislike
  if (enterDislikesa.length > 0 && enterDislikesg.length > 0 && enterLikeArtists.length === 0 && enterLikeGenres.length === 0) {
    agcheck = allMusic.filter(dag => {
      return !(enterDislikesa.toLowerCase().includes(dag.artist.toLowerCase()) && enterDislikesg.toLowerCase().includes(dag.genre.toLowerCase()));
    })
  }
  if (enterDislikesa.length === 0 && enterDislikesg.length > 0 && enterLikeArtists.length === 0 && enterLikeGenres.length === 0) {
    agcheck = allMusic.filter(dag => {
      return !(enterDislikesg.toLowerCase().includes(dag.genre.toLowerCase()));
    })
  }
  if (enterDislikesa.length > 0 && enterDislikesg.length === 0 && enterLikeArtists.length === 0 && enterLikeGenres.length === 0) {
    agcheck = allMusic.filter(dag => {
      return enterDislikesa.toLowerCase().includes(dag.artist.toLowerCase());
    })
  }  
  if (enterDislikesa.length > 0 && enterLikeGenres.length > 0 && enterDislikesg.length === 0 && enterLikeArtists.length === 0) {
    const likeGenres = enterLikeGenres.split(',').map(g => g.trim().toLowerCase());
    agcheck = allMusic.filter(dalg => {
      const songGenres = dalg.genre.toLowerCase().split(',');
      return likeGenres.every(g => songGenres.includes(g)) && !(enterDislikesa.toLowerCase().includes(dalg.artist.toLowerCase()));
    });
  } 
  if (enterLikeArtists.length === 0 && enterLikeGenres.length === 0 && enterDislikesa.length === 0 && enterDislikesg.length === 0){
    agcheck = [];
  }   
}

let isnextACalled = false, isnextGCalled = false; 
//next music function
function nextMusic(){
  checkag();
  //skip artists
  let isLike = false, isLikeg = false;
  if (((likedArtists.length > 0 || dislikedArtists.length > 0) && agcheck.length > 0) && !isnextGCalled){
      //skip while like True
      if (likedArtists.length > 0){
         
       if (fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())){
        let count = 0,bcount=0, counta = 0, countb = 0;        
         
        if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            count++;
             
          }
        }
        //same artist skips genres
        else {
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          let check = false, pcheck = false;
          if (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counta < allMusic.length && !check){
              while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counta < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                counta++;
                 
                let countin = 0;
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countin++;
                   
                }
                 
              }
              check = true;
            }
          if (fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countb < allMusic.length && !pcheck){
                let countain = 0, countin = 0, countinn = 0,checka = false, checkb = false, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
                if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length && !checka){
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countin++;
                   
                  while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countain < allMusic.length){
                    musicIndex++;
                    musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                    countain++;
                     
                  }
                }
                checka = true;
                }
                if (fndislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countinn < allMusic.length && !checkb){
                  while (fndislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countinn < allMusic.length){
                    musicIndex++;
                    musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                    countinn++;
                     
                    while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counta < allMusic.length){
                      musicIndex++;
                      musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                      counta++;
                       
                    }
                  }
                checkb = true;
                }
                pcheck = true;
              }  
          }
        }
      else if (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())){
        let count = 0, countin = 0
         
        if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            count++;
             
          }
        }
        //different artists skip genres
        else{
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          let checkifb = false, countb = 0, countab = 0, checkd = false, checke = false, countbb = 0, countaa = 0, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
          if (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !checkd){ 
            while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
              musicIndex++;
              musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
              count++;
               
              while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countin++;
                 
              }
            }
            checkd = true;
          }
          if (fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !checke){
            while (fndislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countaa < allMusic.length){
              musicIndex++;
              musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
              countaa++;
               
              while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countbb < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countbb++;
                 
              }
            }
            checke = true;
          }
          if(fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !checkifb){
            while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countab < allMusic.length){
              musicIndex++;
              musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
              countab++;
               
              while (!fnlikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countb < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countb++;
                 
              }
            }
            checkifb = true;
          }
           
        }
      }
    isLike =true;
    }
      //skip while dis True
      if (dislikedArtists.length > 0 && !isLike){
        let fdislikedArtists = dislikedArtists.map(artist => artist.toLowerCase());
         
        if (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())) {
          let counter = 0;
           
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex++;
              musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            }

          }
          //same genre skip artist
          else {
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            let check = false,countdg = 0, countbg = 0, pcheck = false, countg = false, gcheck = false, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
            if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !check){
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countg < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countg++;
                   
                  let countin = 0;
                  while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countin < allMusic.length){
                    musicIndex++;
                    musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                    countin++;
                     
                  }
                   
                }
                 
                check = true;
              }
            if (fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !pcheck){
                  let countin = 0, countag=0, countinn = 0,checka = false, checkb = false;
                  if (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinn < allMusic.length && !checkb){
                    while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinn < allMusic.length){
                      musicIndex++;
                      musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                      countinn++;
                       
                      while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countag < allMusic.length){
                        musicIndex++;
                        musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                        countag++;
                         
                      }
                    }
                     
                  checkb = true;
                  }
                  pcheck = true;
              }  
            if (fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !gcheck){
              while(fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && countbg < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countbg++;
                 
                while(fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countdg < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countdg++;
                   
                }
              }
              gcheck = true;
               
            }
             
          }//taylor swift
      }
        //skip while dis not True 
        else if (!fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())) {
          let counter = 0;
           
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex - 1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex++;
              musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
              counter++;
            }
          }
          //different genres skip
          else{
            musicIndex++;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            let checkd = false, count=0, countin=0, checke = false, countbb = 0, countaa = 0, countdg = 0, countbg = 0, gcheck = false, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
            if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !checkd){ 
              while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                count++;
                 
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countin++;
                   
                }
              }
              checkd = true;
            }
            if (fdislikedArtists.includes(allMusic[musicIndex - 1].artist.toLowerCase()) && !checke){
              while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countaa < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countaa++;
                 
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countbb < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countbb++;
                   
                }
              }
              checke = true;
            }            
            if (fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !gcheck){
              while(fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && countbg < allMusic.length){
                musicIndex++;
                musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                countbg++;
                 
                while(fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countdg < allMusic.length){
                  musicIndex++;
                  musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
                  countdg++;
                   
                }
              }
              gcheck = true;
               
            }
             
          }
        }
    }
      loadMusic(musicIndex);
      musicImg.classList.remove('rotate');
      void musicImg.offsetWidth;
      musicImg.classList.add('rotate');
      playMusic();
      playingSong();
       
       
      isnextACalled = true;
}  
  //skip genres
  if (((likedGenres.length > 0 || dislikedGenres.length > 0) && agcheck.length > 0) && !isnextACalled) {
      //skip while like True
      if (likedGenres.length > 0 ){
         
        if (fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase())){
        let count = 0;
         
        musicIndex++;
        musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
        while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          count++;
        }
      }
      else if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase())){
        let count = 0;
         
        musicIndex++;
        musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
        while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          count++;
        }
      }
    isLikeg = true;
  }
      //skip while dis True 
      if (dislikedGenres.length > 0 && !isLikeg){
         
        let fdislikedgenres = dislikedGenres.map(genre => genre.toLowerCase());
        let fdislikedartists = dislikedArtists.map(artist => artist.toLowerCase());
        if (fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase())) {
        let counter = 0;
         
        musicIndex++;
        musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
        while (fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && counter < allMusic.length) {
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
        }
      }
      //skip while dis not True 
      else if (!fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase())) {
        let counter = 0;
         
        musicIndex++;
        musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
        while (fdislikedgenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && counter < allMusic.length) {
          musicIndex++;
          musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
          counter++;
        }
      }
    }
      loadMusic(musicIndex);
      musicImg.classList.remove('rotate');
      void musicImg.offsetWidth;
      musicImg.classList.add('rotate');
      playMusic();
      playingSong();
       
       
      isnextGCalled = true;
}   
  if (agcheck.length == 0 || (likedArtists.length == 0 && dislikedArtists.length == 0 && likedGenres.length == 0 && dislikedGenres.length == 0))
  {
    musicIndex++;
    musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
    loadMusic(musicIndex);
    musicImg.classList.remove('rotate');
    void musicImg.offsetWidth;
    musicImg.classList.add('rotate');
    playMusic();
    playingSong();
     
  }
   
   
   
   
  if (timeStamp != 0 ) {
    mainAudio.currentTime = 0;
    timeStamp = 0;
  }
  isnextACalled = false; 
  isnextGCalled = false;
  AorG = true;
}


let isprevGCalled = false, isprevACalled = false;
//prev music function
function prevMusic(){
  checkag();
  // skip artists
  let isLike = false, isLikeg = false;
  if (((likedArtists.length > 0 || dislikedArtists.length > 0) && agcheck.length > 0) && !isprevGCalled) {
      //skip while like True
      if (likedArtists.length > 0){
         
        //same artists skip
        if (fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())){
          let count = 0;
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)) {
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
               
            }
          }
          else{
            let check = false, pcheck = false;
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            let countcount = 0;
            if(!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !check){
              while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countcount < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countcount++;
                 
                let countint = 0, artistFound = false; //ChatGPT solution
                while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !artistFound && countint < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countint++;
                   
                  if (fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())) {
                    artistFound = true;
                  }
                }
              }
              check = true;
            }
            if (fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !pcheck){
              let countin = 0,countinnn=0, checkif = false, countinn = 0, checkiff = false, fpdislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
              if (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !checkif){
                while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countin++;
                   
                }
                checkif = true;
              }
              if (fpdislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !checkiff){
                while (fpdislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countinn < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countinn++;
                                 
                  while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinnn < allMusic.length){
                    musicIndex--;
                    musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                    countinnn++;
                  }
                }
                checkiff = true;
              }
              pcheck = true;
            }
          }
        }
        else if (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())){
           
          let count = 0;
           
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)) {
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
               
            }
          }  
          //different artists skip genres
          else{
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            let checkifb = false, checkif = false, checkiff = false, countb = 0, counta = 0, countab = 0,countinn = 0, countinnn = 0, fpdislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
            if(!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !checkif){
              while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                count++;
                 
                while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && counta < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  counta++;
                   
                }
              }
               
              checkif = true;
            }
            if (fpdislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !checkiff){
              while (fpdislikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countinn < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countinn++;
                               
                while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinnn < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countinnn++;
                }
              }
               
              checkiff = true;
            }
            if(fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && !checkifb){
              while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countab < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countab++;
                 
                while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countb < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countb++;
                   
                }
              }
              checkifb = true;
            }
             
          }
        }
        isLike = true;
      }

      //skip while dis True
      if (dislikedArtists.length > 0 && !isLike){
        let fdislikedArtists = dislikedArtists.map(artist => artist.toLowerCase());
         
        if (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())) {
          let counter = 0;
           
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            }

          }
          //same genre skip artist
          else {
            musicIndex--;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            let check = false, countbg = 0, pcheck = false, countg = false, countdg = 0, gcheck = false, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
            if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !check){
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countg < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countg++;
                   
                  let countin = 0;
                  while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countin < allMusic.length){
                    musicIndex--;
                    musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                    countin++;
                     
                  }
                   
                }
                 
                check = true;
              }
            if (fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !pcheck){
                  let countin = 0, countag=0, countinn = 0,checka = false, checkb = false;
                  if (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinn < allMusic.length && !checkb){
                    while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countinn < allMusic.length){
                      musicIndex--;
                      musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                      countinn++;
                       
                      while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countag < allMusic.length){
                        musicIndex--;
                        musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                        countag++;
                         
                      }
                    }
                     
                  checkb = true;
                  }
                  pcheck = true;
                }  
            if (fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !gcheck){
              while(fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && countbg < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countbg++;
                 
                while(fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countdg < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countdg++;
                   
                }
              }
              gcheck = true;
               
            }
             
          }//taylor swift
      }
        //skip while dis not True 
        else if (!fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase())) {
          let counter = 0;
           
          if (!(likedGenres.length > 0 || dislikedGenres.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex - 1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              counter++;
            }
          }
          //different genres skip
          else{
            musicIndex--;
            musicIndex > allMusic.length ? musicIndex = 1 : musicIndex = musicIndex;
            let checkd = false, count=0, countin=0, checke = false, countbb = 0, countaa = 0, countbg = 0, countdg = 0, gcheck = false, fndislikedGenres = dislikedGenres.map(genre => genre.toLowerCase());
            if (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && !checkd){ 
              while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                count++;
                 
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countin < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countin++;
                   
                }
              }
              checkd = true;
            }
            if (fdislikedArtists.includes(allMusic[musicIndex - 1].artist.toLowerCase()) && !checke){
              while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countaa < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countaa++;
                 
                while (!fnlikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && countbb < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countbb++;
                   
                }
              }
              checke = true;
            }
            if (fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && !gcheck){
              while(fndislikedGenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && countbg < allMusic.length){
                musicIndex--;
                musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                countbg++;
                 
                while(fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && countdg < allMusic.length){
                  musicIndex--;
                  musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
                  countdg++;
                   
                }
              }
              gcheck = true;
               
            }
             
          }
        }
    }
      loadMusic(musicIndex);
      musicImg.classList.remove('rotate');
      void musicImg.offsetWidth;
      musicImg.classList.add('rotate');
      playMusic();
      playingSong();
       
       
      isprevACalled = true;
} 
  // skip genres
  if (((likedGenres.length > 0 || dislikedGenres.length > 0) && agcheck.length > 0) && !isprevACalled){
      //skip while like True
      if (likedGenres.length > 0){
         
        if (fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase())){
          let count = 0;
           
          if (!(likedArtists.length > 0 || dislikedArtists.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
            }
          }
          else{
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
               
            }
             
          }
        }
        else if (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase())){
          let count = 0;
           
          if (!(likedArtists.length > 0 || dislikedArtists.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedGenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
            }
          }
          else {
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (!fplikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && count < allMusic.length){
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              count++;
               
            }
             
          }
        }
     isLikeg = true;
    }
  
      //skip while dis True
      if (dislikedGenres.length > 0 && !isLikeg){
         
        let fdislikedgenres = dislikedGenres.map(genre => genre.toLowerCase());
        if (fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase())) {
          let counter = 0;
           
          if (!(likedArtists.length > 0 || dislikedArtists.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            }
          }
          else{
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex-1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              counter++;
               
            }
             
          }
        }
        //skip while dis not True 
        else if (!fdislikedgenres.includes(allMusic[musicIndex-1].genre.toLowerCase())) {
          let counter = 0;
           
          if (!(likedArtists.length > 0 || dislikedArtists.length > 0)){
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedgenres.includes(allMusic[musicIndex - 1].genre.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              counter++;
            }      
          }
          else{
            musicIndex--;
            musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
            while (fdislikedArtists.includes(allMusic[musicIndex - 1].artist.toLowerCase()) && counter < allMusic.length) {
              musicIndex--;
              musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
              counter++;
               
            }  
             
          }    
        }
    }
      loadMusic(musicIndex);
      musicImg.classList.remove('rotate');
      void musicImg.offsetWidth;
      musicImg.classList.add('rotate');
      playMusic();
      playingSong();
       
       
      isprevGCalled = true;
} 
    if (agcheck.length == 0 || (likedArtists.length == 0 && dislikedArtists.length == 0 && likedGenres.length == 0 && dislikedGenres.length == 0))
  {
    musicIndex--;
    musicIndex < 1 ? musicIndex = allMusic.length : musicIndex = musicIndex;
    loadMusic(musicIndex);
    musicImg.classList.remove('rotate');
    void musicImg.offsetWidth;
    musicImg.classList.add('rotate');
    playMusic();
    playingSong();
     
  }
   
   
   
   
  if (timeStamp != 0 ) {
    mainAudio.currentTime = 0;
    timeStamp = 0;
  } 
  isprevGCalled = false;
  isprevACalled = false;
  AorG = true;
}

// play or pause button event
playPauseBtn.addEventListener("click", ()=>{
  const isMusicPlay = wrapper.classList.contains("paused");
  //if isPlayMusic is true then call pauseMusic else call playMusic
  isMusicPlay ? pauseMusic() : playMusic();
  playingSong();
});

//prev music button event
prevBtn.addEventListener("click", ()=>{
  const isMusicPlay = wrapper.classList.contains("paused");
  if(mainAudio.currentTime > 5){
    mainAudio.currentTime = 0; //setting audio current time to 0
    const existingLyric = document.querySelector("#lyrics");
    if(existingLyric){
      for(let j=0;j<existingLyric.length;j++){
        const lyricElem = document.getElementById(`lyric-${j}`);
        const lyct = document.getElementById(`${musicName}-${j}`);
        lyricElem.classList.remove('played');
        lyct.classList.remove('played');
      }
    
      let empty = document.querySelectorAll(".empty");for(let i=0;i<empty.length;i++){lyricContainer.removeChild(empty[i]);}
      let ScrollInterval;
      ScrollInterval = setInterval(function(){
        lyricContainer.scrollTop -= 50;
        if (lyricContainer.scrollTop === 0){clearInterval(ScrollInterval);}
      }, 40); 
    }

    isMusicPlay ? pauseMusic() : playMusic();
    loadMusic(musicIndex); //calling loadMusic function with argument, in the argument there is a index of current song

    playMusic(); //calling playMusic function
  }
  else{let getText = repeatBtn.innerText; //getting this tag innerText
      switch(getText){
      case "repeat":
        prevMusic(); //calling prevMusic function
        break;
      case "repeat_one":
        prevMusic(); //calling prevMusic function
        break;
      case "shuffle":
        let randIndex = Math.floor((Math.random() * allMusic.length) + 1); //genereting random index/numb with max range of array length
        let count = 0;
        do{
          randIndex = Math.floor((Math.random() * allMusic.length) + 1);
        }while(musicIndex == randIndex && count < allMusic.length); //this loop run until the next random number won't be the same of current musicIndex
        musicIndex = randIndex; //passing randomIndex to musicIndex
        loadMusic(musicIndex);
        if (timeStamp != 0 ) {
          mainAudio.currentTime = 0;
          timeStamp = 0;
        }
        count++;
        musicImg.classList.remove('rotate');
        void musicImg.offsetWidth;
        musicImg.classList.add('rotate');
        playMusic();
        playingSong();
        break;
      }
  
  }
prevBtn.setAttribute("title", "Previous");
});

//next music button event
nextBtn.addEventListener("click", ()=>{

let getText = repeatBtn.innerText; //getting this tag innerText
switch(getText){
  case "repeat":
    nextMusic(); //calling nextMusic function
    break;
  case "repeat_one":
    nextMusic(); //calling nextMusic function
    break;
  case "shuffle":
    let randIndex = Math.floor((Math.random() * allMusic.length) + 1); //genereting random index/numb with max range of array length
    let count = 0;
    do{
      randIndex = Math.floor((Math.random() * allMusic.length) + 1);
    }while(musicIndex == randIndex && count < allMusic.length); //this loop run until the next random number won't be the same of current musicIndex
    musicIndex = randIndex; //passing randomIndex to musicIndex
    loadMusic(musicIndex);
    if (timeStamp != 0 ) {
      mainAudio.currentTime = 0;
      timeStamp = 0;
    }
    count++;
    musicImg.classList.remove('rotate');
    void musicImg.offsetWidth;
    musicImg.classList.add('rotate');
    playMusic();
    playingSong();
    break;
}
nextBtn.setAttribute("title", "Next");
});

// update progress bar width according to music current time
mainAudio.addEventListener("timeupdate", (e)=>{
  const currentTime = e.target.currentTime; //getting playing song currentTime
  const duration = e.target.duration; //getting playing song total duration
  let progressWidth = (currentTime / duration) * 100;
  progressBar.style.width = `${progressWidth}%`;
  let musicCurrentTime = wrapper.querySelector(".current-time"),
  musicDuartion = wrapper.querySelector(".max-duration");
  mainAudio.addEventListener("loadeddata", ()=>{
    // update song total duration
    let mainAdDuration = mainAudio.duration, totalMin = Math.floor(mainAdDuration / 60), totalSec = Math.floor(mainAdDuration % 60);
    if(totalSec < 10){ //if sec is less than 10 then add 0 before it
      totalSec = `0${totalSec}`;
    }
    musicDuartion.innerText = `${totalMin}:${totalSec}`;
  });
  // update playing song current time
  let currentMin = Math.floor(currentTime / 60), currentSec = Math.floor(currentTime % 60);
  if(currentSec < 10){ //if sec is less than 10 then add 0 before it
    currentSec = `0${currentSec}`;
  }
  musicCurrentTime.innerText = `${currentMin}:${currentSec}`;
});

// update playing song currentTime on according to the progress bar width
progressArea.addEventListener("click", (e)=>{
  const isMusicPlay = wrapper.classList.contains("paused");
  let progressWidth = progressArea.clientWidth; //getting width of progress bar
  let clickedOffsetX = e.offsetX; //getting offset x value
  let songDuration = mainAudio.duration; //getting song total duration

  mainAudio.currentTime = (clickedOffsetX / progressWidth) * songDuration;
  isMusicPlay ? playMusic() : pauseMusic();
  playingSong();
});

//change loop, shuffle, repeat icon onclick
const repeatBtn = wrapper.querySelector("#repeat-plist");
repeatBtn.addEventListener("click", ()=>{
  let getText = repeatBtn.innerText; //getting this tag innerText
  switch(getText){
    case "repeat":
      repeatBtn.innerText = "repeat_one";
      repeatBtn.setAttribute("title", "song Loop");
      break;
    case "repeat_one":
      repeatBtn.innerText = "shuffle";
      repeatBtn.setAttribute("title", "shuffle");
      break;
    case "shuffle":
      repeatBtn.innerText = "repeat";
      repeatBtn.setAttribute("title", "playlist loop");
      break;
  }
});

//code for what to do after song ended
mainAudio.addEventListener("ended", ()=>{
  // we'll do according to the icon means if user has set icon to
  // loop song then we'll repeat the current song and will do accordingly
  let getText = repeatBtn.innerText; //getting this tag innerText
  switch(getText){
    case "repeat":
      nextMusic(); //calling nextMusic function
      break;
    case "repeat_one":
      mainAudio.currentTime = 0; //setting audio current time to 0
      loadMusic(musicIndex); //calling loadMusic function with argument, in the argument there is a index of current song
      playMusic(); //calling playMusic function
      break;
    case "shuffle":
      let randIndex = Math.floor((Math.random() * allMusic.length) + 1); //genereting random index/numb with max range of array length
      let count = 0;
      do{
        randIndex = Math.floor((Math.random() * allMusic.length) + 1);
      }while(musicIndex == randIndex && count < allMusic.length); //this loop run until the next random number won't be the same of current musicIndex
      musicIndex = randIndex; //passing randomIndex to musicIndex
      loadMusic(musicIndex);
      if (timeStamp != 0 ) {
        mainAudio.currentTime = 0;
        timeStamp = 0;
      }
      count++;
      musicImg.classList.remove('rotate');
      void musicImg.offsetWidth;
      musicImg.classList.add('rotate');
      playMusic();
      playingSong();
      break;
  }
});

//show music list onclick of music icon
moreMusicBtn.addEventListener("click", ()=>{
  musicList.classList.toggle("show");
});
closemoreMusic.addEventListener("click", ()=>{
  moreMusicBtn.click();
});

musicImg.addEventListener("click", ()=>{
    let getText = musicImg.innerText; //getting this tag innerText
      switch(getText){
        case "rotate":
          wrapper.classList.remove("paused");
          musicImg.classList.add('rotatee');
          playPauseBtn.querySelector("i").innerText = "play_arrow";
          mainAudio.pause();
          break;
        case "rotatee":
          wrapper.classList.add("paused");
          musicImg.classList.remove('rotatee');
          musicImg.classList.add('rotate');
          playPauseBtn.querySelector("i").innerText = "pause";
          mainAudio.play();
          break;
      }
});

function setVolume(){
  mainAudio.volume = volumeProgress.value / 100;
}

volumeProgress.oninput = function () {
    var value = (this.value - this.min) / (this.max - this.min) * 100
    this.style.background = 'linear-gradient(to left, #6b8dff 0%, #ff2a5f '
        + value + '%,  #fff ' + value + '%, #fff 100%)'
}

//show volume control
volumeControl.addEventListener("click", ()=>{
  volumeProgress.classList.toggle("showw");
});

const ulTag = wrapper.querySelector("ul");
// let create li tags according to array length for list
for (let i = 0; i < allMusic.length; i++) {
  mainAudio.src = `static/sla/songs/${allMusic[i].src}.mp3`;
  jsmediatags.read(mainAudio.src, {
    onSuccess: function(tag) {
      let liTag = `<li li-index="${i + 1}">
                <div class="roww">
                  <span id="scrolla">${tag.tags.title}</span>
                  <p id="scrollb">${tag.tags.artist}</p>
                  <p id="scrollb">${tag.tags.genre}</p>
                </div>
                <span id="${allMusic[i].src}" class="audio-duration"></span>
                <audio class="${allMusic[i].src}" src="static/sla/songs/${allMusic[i].src}.mp3"></audio>
              </li>`;
      ulTag.insertAdjacentHTML("beforeend", liTag); //inserting the li inside ul tag
      let liAudioDuartionTag = ulTag.querySelector(`#${allMusic[i].src}`);
      let liAudioTag = ulTag.querySelector(`.${allMusic[i].src}`);
      liAudioTag.addEventListener("loadeddata", ()=>{
        let duration = liAudioTag.duration;
        let totalMin = Math.floor(duration / 60);
        let totalSec = Math.floor(duration % 60);
        if(totalSec < 10){ //if sec is less than 10 then add 0 before it
          totalSec = `0${totalSec}`;
        };
        liAudioDuartionTag.innerText = `${totalMin}:${totalSec}`; //passing total duation of song
        liAudioDuartionTag.setAttribute("t-duration", `${totalMin}:${totalSec}`); //adding t-duration attribute with total duration value
      });

    },
    onError: function(error) {
      
    }
  });

}

//play particular song from the list onclick of li tag
function playingSong(){
  const allLiTag = ulTag.querySelectorAll("li");

  for (let j = 0; j < allLiTag.length; j++) {
    let audioTag = allLiTag[j].querySelector(".audio-duration");

    if(allLiTag[j].classList.contains("playing")){
      allLiTag[j].classList.remove("playing");
      let adDuration = audioTag.getAttribute("t-duration");
      audioTag.innerText = adDuration;
    }

    //if the li tag index is equal to the musicIndex then add playing class in it
    if(allLiTag[j].getAttribute("li-index") == musicIndex){
      allLiTag[j].classList.add("playing");
      if(wrapper.classList.contains("paused")){
        audioTag.innerText = "正在播放";
      }
    }

    allLiTag[j].setAttribute("onclick", "clicked(this)");
  }
}

//particular li clicked function
function clicked(element){
  let getLiIndex = element.getAttribute("li-index");
  musicIndex = getLiIndex; //updating current song index with clicked li index
  loadMusic(musicIndex);
  musicImg.classList.remove('rotate');
  void musicImg.offsetWidth;
  musicImg.classList.add('rotate');
  mainAudio.currentTime = 0;
  playMusic();
  playingSong();
}

musicOption.addEventListener("click", ()=>{
  areaOption.classList.toggle("show");
});

closeOptions.addEventListener("click", ()=>{
   musicOption.click();
});

function random_webkit_color() {
  let a, hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e'];
  function populate(a) {
      for (let i = 0; i < 6; i++) {
          let x = Math.round(Math.random() * 14);
          let y = hex[x];
          a += y;
      }
      return a;
  }
  let Color1 = populate('#');
  let Color2 = populate('#');
  var angle = 'to left';
  let gradient = 'linear-gradient(' + angle + ',' + Color1 + ', ' + Color2 + ")";
  volumeProgress.style.background = gradient;
}

opVolume.addEventListener("click", ()=>{
  volumeProgress.classList.toggle("showw");
});


let isDragging = false;
progressArea.addEventListener('mousedown', () => {
  isDragging = true;
});
progressArea.addEventListener('mouseleave', () => {
  isDragging = false;
});
progressArea.addEventListener('mousemove', (e) => {
  if (isDragging) {
    const xPos = e.clientX - progressArea.getBoundingClientRect().left;
    const percent = xPos / progressArea.offsetWidth;
    progressBar.style.width = `${percent * 100}%`;
  }
});

let MisDragging = false;
progressArea.addEventListener('touchstart', () => {
  MisDragging = true;
});
progressArea.addEventListener('touchend', () => {
  MisDragging = false;
});
progressArea.addEventListener('touchmove', (e) => {
  if (MisDragging) {
    const xPos = e.touches[0].clientX - progressArea.getBoundingClientRect().left;
    const percent = xPos / progressArea.offsetWidth;
    progressBar.style.width = `${percent * 100}%`;
  }
});