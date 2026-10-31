// 모든 페이지 공통: 문구 불러오기, 머리글·바닥글 그리기
const CONTENT_FILE = "content/ko.json";
const PHOTOS_FILE = "data/photos.json";

function lookup(content, path) {
  return path.split(".").reduce((value, key) => value[key], content);
}

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

function renderChrome(content) {
  const current = document.body.dataset.page;
  const pages = { home: "index.html", work: "work.html", about: "about.html", contact: "contact.html" };

  const skip = document.createElement("a");
  skip.className = "skip-link";
  skip.href = "#main";
  skip.textContent = content.site.skip;

  const header = document.createElement("header");
  header.className = "site-header";
  const name = document.createElement("a");
  name.className = "site-name";
  name.href = "index.html";
  name.textContent = content.site.name;
  const nav = document.createElement("nav");
  nav.className = "site-nav";
  nav.setAttribute("aria-label", content.nav.label);
  const list = document.createElement("ul");
  for (const [page, href] of Object.entries(pages)) {
    const link = document.createElement("a");
    link.href = href;
    link.textContent = content.nav[page];
    if (page === current) link.setAttribute("aria-current", "page");
    const item = document.createElement("li");
    item.append(link);
    list.append(item);
  }
  nav.append(list);
  header.append(name, nav);
  document.body.prepend(skip, header);

  const footer = document.createElement("footer");
  footer.className = "site-footer";
  footer.textContent = content.site.footer;
  document.querySelector("main").after(footer);
}

function applyText(content) {
  for (const el of document.querySelectorAll("[data-text]")) {
    el.textContent = lookup(content, el.dataset.text);
  }
  for (const el of document.querySelectorAll("[data-list]")) {
    for (const text of lookup(content, el.dataset.list)) {
      const item = document.createElement("li");
      item.textContent = text;
      el.append(item);
    }
  }
}

// 각 페이지 스크립트는 이 값을 기다려 문구를 받는다
const siteReady = loadJson(CONTENT_FILE).then((content) => {
  document.documentElement.lang = content.lang;
  const description = document.createElement("meta");
  description.name = "description";
  description.content = content.site.description;
  document.head.append(description);
  renderChrome(content);
  applyText(content);
  return content;
});
