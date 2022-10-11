const body = document.querySelector('body')
const sidebarToggle = document.querySelector('#sidebarToggle')
const closedClass = 'with-closed-sidebar'

// Only show icons (closed) or full sidebar (open)
function toggleSidebar() {
    body.classList.toggle(closedClass)
    sidebarToggle.classList.toggle('flip')
    
    // Save state to cookie, so it doesn't change on reload
    if (body.classList.contains(closedClass)) {
        setCookie('sidebar', 'closed');
    }
    else {
        setCookie('sidebar', 'open');
    }
};

const mediaQuery = window.matchMedia('(max-width: 768px)');

// Pretty much the same as @media query in CSS.
// This is used to make things easier - only a CSS class is toggled.
function handleTabletChange(e) {
    if (e.matches) {
        body.classList.add(closedClass)
    }
    else {
        body.classList.remove(closedClass)
    }
}
mediaQuery.addListener(handleTabletChange);
