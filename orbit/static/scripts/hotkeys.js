// Sidebar navigation hotkeys
document.onkeydown = keydown; 

function keydown (evt) { 
    if (!evt) evt = event;
    if (evt.altKey && evt.key === 'ArrowUp') {
        window.location.href+='/↑';
    }
    else if (evt.altKey && evt.key === 'ArrowDown') { 
        window.location.href+='/↓';
    }
}
