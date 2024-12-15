
    // Snail animation logic
    document.addEventListener("DOMContentLoaded", () => {
      const snail = document.querySelector('.snail');
      const slime = document.querySelector('.slime-trail');
      const snailSpeed = 44.4; // pixels/second
      let position = 0;
      let animationInterval;
  
      // Function to animate the snail
      const moveSnail = () => {
        position += snailSpeed / 10; // Update position every 100ms
        if (position > window.innerWidth) {
          clearInterval(animationInterval); // Stop animation once it reaches the end
          setTimeout(() => {
            position = 0; // Reset position after completing animation
            snail.style.transform = `translateX(${position}px)`; // Reset snail
            slime.style.width = '0'; // Reset slime trail
          }, 500); // Delay to show end position briefly before reset
          return;
        }
        snail.style.transform = `translateX(${position}px)`;
        slime.style.width = `${position + 50}px`; // Update slime trail length
      };
  
      // Start animation on click
      snail.addEventListener('click', () => {
        if (animationInterval) return; // Prevent multiple intervals
        animationInterval = setInterval(moveSnail, 100);
  
        // Disable further clicks during animation
        snail.style.pointerEvents = 'none';
  
        // Re-enable clicking after animation ends
        setTimeout(() => {
          snail.style.pointerEvents = 'auto';
        }, (window.innerWidth / (snailSpeed / 10)) * 100); // Calculate total animation time
      });
    });
  

function makeIframeFullscreen() {
  const iframe = document.getElementById('tychos-simulator');
  const button = document.getElementById('dive-button');
  
  // Smooth transition effect using CSS
  iframe.style.transition = 'transform 0.4s ease, width 0.4s ease, height 0.4s ease';
  iframe.style.transform = 'scale(1.3)';
  iframe.style.boxShadow = '0 0 20px rgba(0, 0, 0, 0.5)';

  // Remove button interaction while transitioning
  button.disabled = true;

  // After the animation, request fullscreen
  setTimeout(() => {
    if (iframe.requestFullscreen) {
      iframe.requestFullscreen();
    } else if (iframe.webkitRequestFullscreen) { // Safari
      iframe.webkitRequestFullscreen();
    } else if (iframe.msRequestFullscreen) { // IE/Edge
      iframe.msRequestFullscreen();
    }

    // Cleanup: Restore styles after fullscreen
    iframe.style.transition = '';
    iframe.style.transform = '';
    iframe.style.boxShadow = '';
    button.disabled = false;
  }, 600); // Match transition duration
}
  