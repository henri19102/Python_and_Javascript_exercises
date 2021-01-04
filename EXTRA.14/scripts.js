document.addEventListener("DOMContentLoaded", function() { startplayer(); }, false);
var player;

const timeElapsed = document.getElementById('time-elapsed');
const duration = document.getElementById('duration');

function startplayer() 
{
 player = document.getElementById('video_player');
 player.controls = false;
}
function play_vid()
{
 player.play();
}
function pause_vid()
{
 player.pause();
}
function stop_vid() 
{
 player.pause();
 player.currentTime = 0;
}
function change_vol()
{
 player.volume=document.getElementById("change_vol").value;
}