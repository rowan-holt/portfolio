(async () => {
  const content = await siteReady;
  const timeline = document.getElementById("timeline");
  for (const entry of content.about.timeline) {
    const period = document.createElement("dt");
    period.textContent = entry.period;
    const text = document.createElement("dd");
    text.textContent = entry.text;
    const row = document.createElement("div");
    row.append(period, text);
    timeline.append(row);
  }
})();
