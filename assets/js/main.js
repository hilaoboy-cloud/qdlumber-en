/* Qingdao Lumber EN / ZH — interactions */
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
      var isSub = (key !== "home") && (path.indexOf("/" + key) !== -1 || (key === "applications" && path.indexOf("/case-studies") !== -1));
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

  /* RFQ form: formsubmit.co AJAX with mailto fallback */
  var form = document.getElementById("rfqForm");
  if (form) {
    var isZh = document.documentElement.lang === "zh" || location.pathname.indexOf("/zh") !== -1;

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

      var nameMsg = isZh ? "请填写您的姓名" : "Please enter your full name.";
      var emailMsg = isZh ? "请填写有效的企业邮箱" : "Please enter a valid business email.";
      var companyMsg = isZh ? "请填写您的公司名称" : "Please enter your company name.";
      var countryMsg = isZh ? "请填写所在国家或地区" : "Please enter your country / region.";
      var needMsg = isZh ? "请填写您的产品与包装要求（至少10个字符）" : "Please describe your product and packaging requirements (at least 10 characters).";

      var fullName    = check("fName", function(v){ return v.length >= 1; }, nameMsg);
      var email       = check("fEmail", function(v){ return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }, emailMsg);
      var company     = check("fCompany", function(v){ return v.length >= 2; }, companyMsg);
      var country     = check("fCountry", function(v){ return v.length >= 1; }, countryMsg);
      var dimensions  = document.getElementById("fDimensions") ? document.getElementById("fDimensions").value.trim() : "";
      var quantity    = document.getElementById("fQuantity") ? document.getElementById("fQuantity").value.trim() : "";
      var destination = document.getElementById("fDestination") ? document.getElementById("fDestination").value.trim() : "";
      var need        = check("fNeed", function(v){ return v.length >= 10; }, needMsg);

      if (!ok) {
        var bad = form.querySelector(".field.invalid input, .field.invalid textarea");
        if (bad) bad.focus();
        return;
      }

      var note = document.getElementById("formNote");
      function showNote(t){ if (note){ note.classList.add("show"); note.textContent = t; } }

      var successMsg = isZh
        ? "感谢您的咨询，您的信息已提交。我们将评估您的询价，并与您沟通后续事宜。"
        : "Thank you — your inquiry has been sent. We will review your inquiry and follow up regarding the next steps.";
      var fallbackMsg = isZh
        ? "自动提交遇到问题，已为您唤起本地邮件客户端。我们将评估您的询价，并与您沟通后续事宜。"
        : "Something went wrong sending automatically — your email client has been opened instead. We will review your inquiry and follow up regarding the next steps.";

      function mailtoFallback(){
        var subject = encodeURIComponent((isZh ? "[网站询价] " : "Website RFQ — ") + company + " / " + fullName);
        var body = encodeURIComponent(
          (isZh ? "姓名: " : "Full Name: ") + fullName + "\n" +
          (isZh ? "邮箱: " : "Business Email: ") + email + "\n" +
          (isZh ? "公司: " : "Company: ") + company + "\n" +
          (isZh ? "国家/地区: " : "Country / Region: ") + (country || "—") + "\n" +
          (isZh ? "尺寸与重量: " : "Dimensions & Weight: ") + (dimensions || "—") + "\n" +
          (isZh ? "预计数量: " : "Estimated Quantity: ") + (quantity || "—") + "\n" +
          (isZh ? "出运目的地: " : "Shipping Destination: ") + (destination || "—") + "\n\n" +
          (isZh ? "产品与包装要求:\n" : "Product & Packaging Requirements:\n") + need + "\n\n" +
          (isZh ? "(来自青岛拉博尔包装网站询价表单)" : "(Sent from Qingdao Lumber & Packaging website RFQ form)")
        );
        window.location.href = "mailto:evan.chen@qdlumberco.com?subject=" + subject + "&body=" + body;
        showNote(fallbackMsg);
      }

      var btn = form.querySelector('button[type="submit"]');
      var btnDefaultText = isZh ? "提交询价" : "Submit Inquiry";
      var btnSendingText = isZh ? "正在提交…" : "Submitting…";
      if (btn) { btn.disabled = true; btn.textContent = btnSendingText; }

      fetch("https://formsubmit.co/ajax/evan.chen@qdlumberco.com", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          "Full Name": fullName,
          "Business Email": email,
          "Company": company,
          "Country / Region": country || "—",
          "Dimensions & Weight": dimensions || "—",
          "Estimated Quantity": quantity || "—",
          "Shipping Destination": destination || "—",
          "Requirements": need,
          _subject: (isZh ? "[网站询价] " : "Website RFQ — ") + company + " / " + fullName,
          _template: "table"
        })
      }).then(function(res){
        if (!res.ok) throw new Error("bad response");
        return res.json();
      }).then(function(){
        form.reset();
        showNote(successMsg);
      }).catch(function(){
        mailtoFallback();
      }).finally(function(){
        if (btn) { btn.disabled = false; btn.textContent = btnDefaultText; }
      });
    });

    ["fName","fEmail","fCompany","fCountry","fNeed"].forEach(function(id){
      var el = document.getElementById(id);
      if (el) el.addEventListener("input", function(){
        el.closest(".field").classList.remove("invalid");
      });
    });
  }
})();
