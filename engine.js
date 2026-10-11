/* Vacuum math engine - pure arithmetic, every borrowed number labeled. */
(function (root) {
  "use strict";
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function article(n) { return /^(8|11|18)/.test(String(n)) ? "an" : "a"; }

  function binPlan(binL, perSessionL, sessionsWeek) {
    if (!(binL > 0) || !(perSessionL > 0) || !(sessionsWeek > 0)) return { error: "bin, pickup and pace must be positive" };
    var sessions = r1(binL / perSessionL);
    var emptiesYear = r1(sessionsWeek * 52 / sessions);
    return { binL: binL, perSessionL: perSessionL, sessionsWeek: sessionsWeek, sessions: sessions, emptiesYear: emptiesYear };
  }

  function bagPlan(bagL, perSessionL, sessionsWeek, bagPrice) {
    if (!(bagL > 0) || !(perSessionL > 0) || !(sessionsWeek > 0) || !(bagPrice > 0)) return { error: "bag, pickup, pace and price must be positive" };
    var sessions = r1(bagL / perSessionL);
    var bagsYear = r1(sessionsWeek * 52 / sessions);
    var costYear = r2(bagsYear * bagPrice);
    return { bagL: bagL, perSessionL: perSessionL, sessionsWeek: sessionsWeek, bagPrice: bagPrice, sessions: sessions, bagsYear: bagsYear, costYear: costYear };
  }

  function filterPlan(filterH, minSession, sessionsWeek, filterPrice) {
    if (!(filterH > 0) || !(minSession > 0) || !(sessionsWeek > 0) || !(filterPrice > 0)) return { error: "filter life, session length, pace and price must be positive" };
    var hoursWeek = minSession * sessionsWeek / 60;
    var weeks = r1(filterH / hoursWeek);
    var filtersYear = r1(52 / weeks);
    var costYear = r2(filtersYear * filterPrice);
    return { filterH: filterH, minSession: minSession, sessionsWeek: sessionsWeek, filterPrice: filterPrice, weeks: weeks, filtersYear: filtersYear, costYear: costYear };
  }

  function renderBin(r) {
    return article(r.binL) + " " + r.binL + " L bin picking up a labeled " + r.perSessionL + " liters a session fills after " + r.sessions + " sessions - about " + r.emptiesYear + " empties a year at " + r.sessionsWeek + " sessions a week.";
  }

  function renderBag(r) {
    return "A labeled " + r.bagL + " L bag at a labeled " + r.perSessionL + " liters a session lasts " + r.sessions + " sessions - about " + r.bagsYear + " bags and " + r.costYear + " a year at " + r.sessionsWeek + " sessions a week.";
  }

  function renderFilter(r) {
    return "A labeled " + r.filterH + "-hour filter at " + r.minSession + " minutes a session, " + r.sessionsWeek + " sessions a week, lasts about " + r.weeks + " weeks - about " + r.filtersYear + " filters and " + r.costYear + " a year.";
  }

  var api = { binPlan: binPlan, bagPlan: bagPlan, filterPlan: filterPlan,
              renderBin: renderBin, renderBag: renderBag, renderFilter: renderFilter };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.VacuumMath = api;
})(typeof window !== "undefined" ? window : this);
