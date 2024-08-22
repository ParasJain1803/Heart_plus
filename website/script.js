document.addEventListener("DOMContentLoaded", function () {
  // Responsive menu toggle
  const menuIcon = document.getElementById("menu-icon");
  const navLinks = document.getElementById("nav-links");

  menuIcon.addEventListener("click", function () {
    navLinks.classList.toggle("active");
  });

  // GSAP Animations
  gsap.to("header", { duration: 1.5, y: 0, ease: "bounce" });

  gsap.to("nav ul li", {
    duration: 1,
    opacity: 1,
    stagger: 0.3,
    delay: 1.5,
    ease: "power2.inOut",
  });

  gsap.to(".hero", { duration: 2, opacity: 1, delay: 2 });

  gsap.to(".cta-buttons .btn", {
    duration: 0.8,
    scale: 1,
    delay: 3,
    ease: "elastic.out(1, 0.3)",
    stagger: 0.2,
  });

  gsap.to(".about", {
    duration: 1.5,
    opacity: 1,
    x: 0,
    delay: 2.5,
    ease: "power2.out",
  });

  gsap.to("footer", {
    duration: 1.5,
    opacity: 1,
    delay: 3.5,
    ease: "power2.inOut",
  });
});
