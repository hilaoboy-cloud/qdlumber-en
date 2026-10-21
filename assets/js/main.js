/* Qingdao Lumber EN — interactions */
(function(){
  "use strict";

  /* mobile nav */
  var burger = document.getElementById("burger"),
      nav = document.getElementById("mainNav");
  if (burger && nav) {
    burger.addEventListener("click", function(){ nav.classList.toggle("open"); });
    nav.addEventListener("click", function(e){
      if (e.target.tagName === "A") nav.classList.remove("open");
    });
  }

  /* active nav link */
  try {
    var path = location.pathname.replace(/\/+$/,"") || "/";
    var links = document.querySelectorAll("#mainNav a.nav-link[data-nav]");
    links.forEach(function(a){
      var key = a.getAttribute("data-nav");
      var isHome = (key === "home") && (path === "/" || path === "" || path.endsWith("/index.html") || path.endsWith("/qdlumber-en") || path.endsWith("/zh"));
      var isSub = (key !== "home") && (path.indexOf("/" + key) !== -1);
      if (isHome || isSub) {
        a.classList.add("active");
      }
    });
  } catch(e){}

  /* FAQ accordion */
  document.querySelectorAll(".faq-item .faq-q").forEach(function(btn){
    btn.addEventListener("click", function(){
      var item = btn.parentElement,
          ans = item.querySelector(".faq-a"),
          open = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(function(o){
        o.classList.remove("open");
        o.querySelector(".faq-a").style.maxHeight = null;
      });
      if (!open) {
        item.classList.add("open");
        ans.style.maxHeight = ans.scrollHeight + "px";
      }
    });
  });

  /* reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, {threshold: .12});
    document.querySelectorAll(".reveal").forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function(el){ el.classList.add("in"); });
  }

  /* footer year */
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  /* RFQ form: formsubmit.co AJAX, mailto fallback.
     NOTE: formsubmit requires a one-time activation email to be confirmed
     by the mailbox owner before submissions are delivered. */
  var form = document.getElementById("rfqForm");
  if (form) {
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var ok = true;
      function check(id, test, msg){
        var el = document.getElementById(id);
        if (!el) return "";
        var wrap = el.closest(".field");
        var val = el.value.trim();
        var valid = test(val);
        wrap.classList.toggle("invalid", !valid);
        var err = wrap.querySelector(".err");
        if (err && msg) err.textContent = msg;
        if (!valid) ok = false;
        return val;
      }
      var firstName = check("fFirst", function(v){ return v.length >= 1; }, "Please enter your first name.");
      var lastName  = check("fLast",  function(v){ return v.length >= 1; }, "Please enter your last name.");
      var email     = check("fEmail", function(v){ return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }, "Please enter a valid email address.");
      var company   = check("fCompany", function(v){ return v.length >= 2; }, "Please enter your company name.");
      var country   = document.getElementById("fCountry") ? document.getElementById("fCountry").value.trim() : "";
      var need      = check("fNeed", function(v){ return v.length >= 10; }, "Please describe your requirements (at least 10 characters).");
      var phone     = document.getElementById("fPhone") ? document.getElementById("fPhone").value.trim() : "";
      if (!ok) {
        var bad = form.querySelector(".field.invalid input, .field.invalid textarea");
        if (bad) bad.focus();
        return;
      }
      var note = document.getElementById("formNote");
      function showNote(t){ if (note){ note.classList.add("show"); note.textContent = t; } }
      function mailtoFallback(){
        var subject = encodeURIComponent("Website RFQ — " + company + " / " + firstName + " " + lastName);
        var body = encodeURIComponent(
          "First Name: " + firstName + "\nLast Name: " + lastName +
          "\nEmail: " + email + "\nCompany: " + company +
          "\nCountry: " + (country || "—") + "\nPhone: " + (phone || "—") +
          "\n\nRequirements:\n" + need +
          "\n\n(Sent from the Qingdao Lumber & Packaging website RFQ form)"
        );
        window.location.href = "mailto:Evan.chen@qdlumberco.com?subject=" + subject + "&body=" + body;
        showNote("Something went wrong sending automatically — your email client has been opened instead. We usually reply within one business day.");
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      fetch("https://formsubmit.co/ajax/Evan.chen@qdlumberco.com", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          "First Name": firstName,
          "Last Name": lastName,
          email: email,
          company: company,
          country: country || "—",
          phone: phone || "—",
          requirements: need,
          _subject: "Website RFQ — " + company + " / " + firstName + " " + lastName,
          _template: "table"
        })
      }).then(function(res){
        if (!res.ok) throw new Error("bad response");
        return res.json();
      }).then(function(){
        form.reset();
        showNote("Thank you — your inquiry has been sent. We usually reply within one business day.");
      }).catch(function(){
        mailtoFallback();
      }).finally(function(){
        if (btn) { btn.disabled = false; btn.textContent = "Send Inquiry"; }
      });
    });
    ["fFirst","fLast","fEmail","fCompany","fNeed"].forEach(function(id){
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", function(){
        el.closest(".field").classList.remove("invalid");
      });
    });
  }
})();
