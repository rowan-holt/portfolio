(async () => {
  const { contact } = await siteReady;
  const email = document.getElementById("contact-email");
  email.href = `mailto:${contact.email}`;
  email.textContent = contact.email;
  const instagram = document.getElementById("contact-instagram");
  instagram.href = contact.instagram_url;
  instagram.textContent = contact.instagram_handle;
})();
