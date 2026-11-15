(() => {
  "use strict";
  const counts = { inspect: 0, report: 0, learn: 0 };
  const byId = (id) => document.getElementById(id);
  const learning = byId("learning");
  function render() {
    byId("inspectCount").textContent = counts.inspect;
    byId("reportCount").textContent = counts.report;
    byId("learnCount").textContent = counts.learn;
  }
  byId("inspectBtn").addEventListener("click", () => {
    counts.inspect += 1;
    counts.learn += 1;
    learning.hidden = false;
    byId("feedback").textContent = "Good practice: pause, inspect the sender and context, avoid unexpected links, and verify independently.";
    render();
    learning.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  byId("reportBtn").addEventListener("click", () => {
    counts.report += 1;
    byId("feedback").textContent = "In a real organization, report the message through the approved security channel. This demo sends no report.";
    render();
  });
  byId("resetBtn").addEventListener("click", () => {
    counts.inspect = counts.report = counts.learn = 0;
    learning.hidden = true;
    byId("feedback").textContent = "";
    render();
  });
  render();
})();
