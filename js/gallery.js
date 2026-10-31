(async () => {
  const content = await siteReady;
  const filters = document.getElementById("filters");
  const gallery = document.getElementById("gallery");
  const status = document.getElementById("status");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const closeBtn = document.getElementById("lightbox-close");
  const prevBtn = document.getElementById("lightbox-prev");
  const nextBtn = document.getElementById("lightbox-next");

  filters.setAttribute("aria-label", content.work.filter_label);
  closeBtn.setAttribute("aria-label", content.lightbox.close);
  prevBtn.setAttribute("aria-label", content.lightbox.prev);
  nextBtn.setAttribute("aria-label", content.lightbox.next);

  let photos;
  try {
    photos = await loadJson(PHOTOS_FILE);
  } catch (error) {
    status.textContent = content.work.error;
    status.hidden = false;
    return;
  }

  const options = { all: content.work.all, ...content.categories };
  const requested = new URLSearchParams(location.search).get("category");
  let category = Object.hasOwn(options, requested) ? requested : "all";
  let visible = [];
  let index = 0;
  let opener = null;

  const altText = (photo) => photo.title || content.categories[photo.category] || "";

  function renderFilters() {
    for (const button of filters.children) {
      button.setAttribute("aria-pressed", String(button.dataset.category === category));
    }
  }

  function renderGallery() {
    visible = category === "all" ? photos : photos.filter((p) => p.category === category);
    gallery.replaceChildren(...visible.map((photo, i) => {
      const img = document.createElement("img");
      img.src = photo.thumb;
      img.width = photo.width;
      img.height = photo.height;
      img.alt = altText(photo);
      img.loading = "lazy";
      img.decoding = "async";
      const button = document.createElement("button");
      button.type = "button";
      button.append(img);
      button.addEventListener("click", () => openLightbox(i, button));
      const item = document.createElement("li");
      item.append(button);
      return item;
    }));
    status.textContent = content.work.empty;
    status.hidden = visible.length > 0;
  }

  for (const [id, label] of Object.entries(options)) {
    const button = document.createElement("button");
    button.type = "button";
    button.dataset.category = id;
    button.textContent = label;
    button.addEventListener("click", () => {
      category = id;
      const url = new URL(location.href);
      if (id === "all") url.searchParams.delete("category");
      else url.searchParams.set("category", id);
      history.replaceState(null, "", url);
      renderFilters();
      renderGallery();
    });
    filters.append(button);
  }

  function showPhoto(i) {
    index = (i + visible.length) % visible.length;
    const photo = visible[index];
    lightboxImg.src = photo.file;
    lightboxImg.width = photo.width;
    lightboxImg.height = photo.height;
    lightboxImg.alt = altText(photo);
    const heading = [photo.title, photo.year].filter(Boolean).join(", ");
    lightboxCaption.textContent = [heading, photo.caption].filter(Boolean).join(" · ");
    const single = visible.length < 2;
    prevBtn.hidden = single;
    nextBtn.hidden = single;
  }

  function openLightbox(i, button) {
    opener = button;
    showPhoto(i);
    lightbox.showModal();
  }

  closeBtn.addEventListener("click", () => lightbox.close());
  prevBtn.addEventListener("click", () => showPhoto(index - 1));
  nextBtn.addEventListener("click", () => showPhoto(index + 1));
  lightbox.addEventListener("close", () => {
    lightboxImg.removeAttribute("src");
    if (opener) opener.focus();
  });
  // ESC는 dialog가 기본으로 처리한다
  lightbox.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") showPhoto(index - 1);
    if (event.key === "ArrowRight") showPhoto(index + 1);
  });

  let touchX = null;
  let touchY = null;
  lightbox.addEventListener("touchstart", (event) => {
    touchX = event.changedTouches[0].clientX;
    touchY = event.changedTouches[0].clientY;
  }, { passive: true });
  lightbox.addEventListener("touchend", (event) => {
    if (touchX === null) return;
    const dx = event.changedTouches[0].clientX - touchX;
    const dy = event.changedTouches[0].clientY - touchY;
    touchX = null;
    if (Math.abs(dx) < 50 || Math.abs(dx) < Math.abs(dy)) return;
    showPhoto(dx < 0 ? index + 1 : index - 1);
  }, { passive: true });

  renderFilters();
  renderGallery();
})();
