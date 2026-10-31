(async () => {
  const content = await siteReady;

  const links = document.getElementById("category-links");
  for (const [id, label] of Object.entries(content.categories)) {
    const link = document.createElement("a");
    link.href = `work.html?category=${id}`;
    link.textContent = label;
    const item = document.createElement("li");
    item.append(link);
    links.append(item);
  }

  const photos = await loadJson(PHOTOS_FILE);
  const photo = photos.find((p) => p.id === content.home.hero_photo_id)
    || photos.find((p) => p.category === "portrait")
    || photos[0];
  if (!photo) return;

  const img = document.createElement("img");
  img.src = photo.file;
  img.width = photo.width;
  img.height = photo.height;
  img.alt = photo.title || content.site.name;
  img.fetchPriority = "high";
  document.getElementById("hero").append(img);
})();
