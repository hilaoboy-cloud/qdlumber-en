#!/usr/bin/env python3
"""Build the 9-page Qingdao Lumber English static site.
Run: python3 gen_site.py   (outputs into ~/workspace/qdlumber-en-rebuild/)
"""
import os, json, shutil

OUT = os.path.dirname(os.path.abspath(__file__))
CANON = "https://en.qdlumber.com"
WA_LINK = "https://wa.me/8613405101358"
EMAIL = "evan.chen@qdlumberco.com"

FACTORY = ("No. 1 Huayu Road, Jimo Development Zone, Qingdao, China",
           "+86 186 0261 9997", "Steven.Sung@qdlumberco.com")
OFFICE = ("1805, Qijian Building, No. 40 Hong Kong Middle Road, Qingdao, China",
          "+86 134 0510 1358", "evan.chen@qdlumberco.com")

INDUSTRIES = [
    ("data-servers-precision-electronics", "Data Server & Precision Electronics",
     "High-stability wooden packaging for servers, storage arrays and precision electronics."),
    ("ev-battery-charging", "EV Battery & Charging Station · UN38.3",
     "Heavy-duty, UN38.3-compliant packaging for lithium battery packs and charging stations."),
    ("industrial-machinery-infrastructure", "Industrial Machinery & Infrastructure",
     "Robust engineered crating for heavy machinery, electrical equipment and infrastructure."),
    ("high-voltage-insulators-power-transmission", "High Voltage Insulator & Power Transmission",
     "Specialized protective packaging for fragile glass, ceramic and porcelain insulators."),
]

WA_FILE = os.path.join(OUT, "assets", "whatsapp-float-button.html")
if os.path.exists(WA_FILE):
    with open(WA_FILE, encoding="utf-8") as f:
        WA_CODE = f.read()
else:
    WA_CODE = ""

ORG_JSONLD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Qingdao Lumber & Packaging Co., Ltd.",
    "url": CANON + "/",
    "logo": CANON + "/assets/img/logo.webp",
    "description": "U.S.-owned OEM manufacturer of custom wooden crates, knock-down crate kits and export packaging systems in Qingdao, China.",
    "contactPoint": [{
        "@type": "ContactPoint", "telephone": "+86-134-0510-1358",
        "email": EMAIL, "contactType": "sales", "areaServed": "Worldwide"
    }],
    "address": {"@type": "PostalAddress", "streetAddress": OFFICE[0],
                "addressLocality": "Qingdao", "addressCountry": "CN"},
}

def head(rel, slug, title, desc, extra=""):
    canon = CANON + ("/" if not slug else "/" + slug + "/")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{CANON}/assets/img/logo.webp">
<link rel="icon" type="image/webp" href="{rel}assets/img/logo.webp">
<link rel="stylesheet" href="{rel}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ORG_JSONLD, ensure_ascii=False)}</script>
{extra}</head>"""

def header(rel):
    ind_links = "\n".join(
        f'<a href="{rel}industries/{s}/">{n}</a>' for s, n, _ in INDUSTRIES)
    return f"""<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{rel}" aria-label="Qingdao Lumber &amp; Packaging — home">
      <img src="{rel}assets/img/logo.webp" alt="Qingdao Lumber &amp; Packaging logo" width="259" height="98"></a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="mainNav">
      <a class="nav-link" data-nav="home" href="{rel}">Home</a>
      <a class="nav-link" data-nav="solutions" href="{rel}solutions/">Solutions</a>
      <a class="nav-link" data-nav="capabilities" href="{rel}capabilities/">Capabilities</a>
      <a class="nav-link" data-nav="about" href="{rel}about/">About Us</a>
      <a class="nav-link" data-nav="case-studies" href="{rel}case-studies/">Case Study</a>
      <span class="has-drop"><a class="nav-link" data-nav="industries" href="{rel}industries/data-servers-precision-electronics/">Industries ▾</a>
        <span class="drop">{ind_links}</span></span>
      <a class="nav-cta" href="{rel}case-studies/#rfq">Get a Quote</a>
    </nav>
  </div>
</header>"""

def footer(rel):
    ind_links = "\n".join(
        f"<li><a href=\"{rel}industries/{s}/\">{n}</a></li>" for s, n, _ in INDUSTRIES)
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="{rel}assets/img/logo.webp" alt="Qingdao Lumber &amp; Packaging" width="200" height="76">
      <p>U.S.-owned OEM manufacturer of custom wooden crates, knock-down crate kits and export packaging systems — serving global industrial programs for 20+ years.</p>
      <div class="social-row">
        <a href="https://www.linkedin.com/company/qdlumber/" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
        <a href="https://www.youtube.com/@QingdaoLumberPackaging" aria-label="YouTube" target="_blank" rel="noopener">▶</a>
        <a href="{WA_LINK}" aria-label="WhatsApp" target="_blank" rel="noopener">WA</a>
      </div>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="{rel}">Home</a></li>
        <li><a href="{rel}solutions/">Solutions</a></li>
        <li><a href="{rel}capabilities/">Capabilities</a></li>
        <li><a href="{rel}about/">About Us</a></li>
        <li><a href="{rel}case-studies/">Case Study</a></li>
        <li><a href="{rel}case-studies/#rfq">Request a Quote</a></li>
      </ul>
    </div>
    <div>
      <h4>Industries</h4>
      <ul>{ind_links}</ul>
    </div>
    <div>
      <h4>Contact</h4>
      <p><strong style="color:#fff">Factory</strong><br>{FACTORY[0]}<br>
      Tel: <a href="tel:+8618602619997">{FACTORY[1]}</a><br>
      Email: <a href="mailto:{FACTORY[2]}">{FACTORY[2]}</a></p>
      <p style="margin-top:12px"><strong style="color:#fff">Office</strong><br>{OFFICE[0]}<br>
      Tel: <a href="tel:+8613405101358">{OFFICE[1]}</a><br>
      Email: <a href="mailto:{OFFICE[2]}">{OFFICE[2]}</a></p>
      <div style="margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,.1)">
        <span style="display:block;font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#fff;margin-bottom:6px">Our Network</span>
        <a href="http://www.marinelumberco.com" target="_blank" rel="noopener" style="display:block;font-size:13px;color:#8fa79b;margin-bottom:4px">Marine Lumber Co. ↗</a>
        <a href="https://marinedefensepackaging.com" target="_blank" rel="noopener" style="display:block;font-size:13px;color:#8fa79b;margin-bottom:4px">Marine Defense Packaging ↗</a>
        <a href="http://www.qdlumber.com" target="_blank" rel="noopener" style="display:block;font-size:13px;color:#8fa79b">Qingdao Lumber &amp; Packaging (China) ↗</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="yr">2026</span> Qingdao Lumber &amp; Packaging Co., Ltd. All rights reserved.</span>
    <span>ISPM-15 Compliant · Export-Ready Packaging</span>
  </div>
</footer>
{WA_CODE}
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def page(rel, slug, title, desc, body, extra_head=""):
    return head(rel, slug, title, desc, extra_head) + header(rel) + body + footer(rel)

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")

def cta_band(rel, title, text):
    return f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>{title}</h2>
  <p>{text}</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}case-studies/#rfq">Request a Quote</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={quote('Hello Qingdao Lumber, I would like to discuss my packaging project.')}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
</div></section>"""

from urllib.parse import quote as _q
def quote(s): return _q(s)

# ================= HOME =================
def build_home():
    rel = ""
    ind_cards = ""
    for s, n, d in INDUSTRIES:
        ind_cards += f"""
    <a class="tcard reveal" href="{rel}industries/{s}/" style="display:block">
      <h3>{n}</h3><p>{d}</p>
      <p style="margin-top:12px;font-weight:700;color:var(--g600)">Learn more →</p>
    </a>"""
    values = [
        ("values-precision.webp", "Engineer designing a custom wooden crate in 3D CAD software",
         "Proven OEM Expertise",
         "Consistent, high-precision packaging solutions backed by over two decades of experience in complex OEM projects."),
        ("values-efficiency.webp", "Digital logistics dashboard monitoring OEM packaging production and shipment schedules",
         "Scalable Production Capacity",
         "Flexible manufacturing supporting both high-volume production and customized OEM programs with reliable lead times."),
        ("values-accountability.webp", "Forklift loading ISPM-15 wooden crates into a shipping container for export",
         "Export-Ready Standards",
         "All solid woods are heat-treated and certified to meet international shipping regulations and customs requirements."),
        ("values-partnership.webp", "Qingdao Lumber engineer reviewing an export wooden crate with a client at the factory",
         "Global OEM Programs Support",
         "Designed to maximize container space and reduce shipping costs, with ISPM-15 compliant materials for seamless global export."),
        ("values-reliability.webp", "Two workers inspecting a finished large wooden crate before shipment",
         "Quality You Can Rely On",
         "Strict in-process inspection and disciplined execution — consistent quality you can depend on, shipment after shipment."),
    ]
    value_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in values)
    body = f"""
<section class="hero">
  <div class="hero-video-bg">
    <iframe src="https://player.vimeo.com/video/1190319624?background=1&autoplay=1&loop=1&byline=0&title=0&muted=1" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
  </div>
  <div class="hero-overlay"></div>
  <div class="wrap">
    <div class="hero-inner reveal in">
      <span class="kicker" style="color:#7bd88f">Your Reliable OEM Packaging Solutions Partner</span>
      <h1>Engineered OEM Packaging Systems for Global Supply Chains</h1>
      <p class="lead">High-performance wood packaging solutions designed for precision, cost efficiency, and reliable export — supporting industrial equipment and OEM programs worldwide.<br><span style="display:inline-block;margin-top:10px;font-size:0.95em;color:#c0dfcc">Built for OEM packaging programs requiring scalability, consistency, and cost control.</span></p>
      <div class="hero-actions">
        <a class="btn btn-green" href="{rel}case-studies/#rfq">Request a Quote</a>
        <a class="btn btn-ghost" href="{rel}solutions/">Explore Solutions</a>
      </div>
    </div>
  </div>
</section>

<section style="padding:44px 0 0"><div class="wrap">
  <div class="grid g3">
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">Reduce Supply Chain Risk</h3>
      <p>Ensure stable production, controlled quality, and reliable delivery — minimizing uncertainty across global OEM programs.</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">Scale Your Production Capacity</h3>
      <p>Expand your manufacturing capability in China without additional investment, supported by integrated production and export-ready operations.</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">Optimize Total Cost</h3>
      <p>Through value engineering, material optimization, and flat-pack designs, we reduce packaging cost, freight volume, and overall logistics expenses.</p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">Why Global OEMs Choose Us</h2>
  <p class="section-sub reveal">Precision manufacturing, disciplined process control, and export-ready logistics — backed by 20+ years of industrial OEM packaging expertise.</p>
  <div class="grid g5">{value_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Every Dimension. Every Joint. Every Component.<br>Built to Your Exact Specifications.</h2>
  <p class="section-sub reveal">Through controlled manufacturing processes and strict quality inspection, we ensure consistent precision — every time.</p>
  <div class="grid g2" style="max-width:960px;margin:0 auto">
    <div class="tcard reveal"><h3>Consistent On-Time Delivery. Zero-Defect Quality.</h3><p>Delivered through controlled processes and disciplined execution — ensuring reliability you can depend on, shipment after shipment.</p></div>
    <div class="tcard reveal"><h3>We Operate as an Extension of Your Team</h3><p>With transparent communication, responsive support, and disciplined execution, we align with your operations to support long-term OEM success.</p></div>
    <div class="tcard reveal"><h3>Optimized Designs for Cost-Efficient Logistics</h3><p>Engineered to reduce transportation costs, shorten lead times, and minimize material waste through efficient structural design and packaging optimization.</p></div>
    <div class="tcard reveal"><h3>Full Traceability from Raw Material to Final Delivery</h3><p>Every stage is tracked and controlled — ensuring transparency, accountability, and consistent quality across the entire production process.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="text-align:center">
  <h2 class="section-title reveal">Reliable Packaging Systems for Global Logistics</h2>
  <p class="section-sub reveal">Engineered to protect, perform, and scale across demanding international supply chains. Watch our automated manufacturing, precision processing, and rigorous quality inspection in action.</p>
  <div class="video-showcase reveal">
    <iframe src="https://www.youtube.com/embed/5F0zRgISQto?rel=0" title="Qingdao Lumber &amp; Packaging OEM Service" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">Built for High-Demand Industrial Applications</h2>
  <p class="section-sub reveal">Engineered packaging systems for the industries where failure is not an option.</p>
  <div class="grid g2">{ind_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Our Products</h2>
  <p class="section-sub reveal">Custom wooden crates · Knock-down crate kits · Server crates · Export packaging systems — all ISPM-15 compliant and built to your drawings.</p>
  <div style="text-align:center" class="reveal">
    <a class="btn btn-green" href="{rel}solutions/">See All Solutions</a>
  </div>
</div></section>
""" + cta_band(rel, "Tell Us What You're Shipping",
               "Send your drawings or dimensions — our engineering team will design the right crate for it, and reply within one business day.")
    return page(rel, "", "Qingdao Lumber & Packaging | Custom OEM Wooden Crates & Export Packaging",
                "Qingdao Lumber & Packaging designs and manufactures custom OEM wooden crates, knock-down crate kits and export packaging systems for global industrial programs. 20+ years, ISPM-15 compliant.", body)

# ================= SOLUTIONS =================
def build_solutions():
    rel = "../"
    faq_json = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Can you manufacture packaging based on our technical drawings or samples?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Send us your technical drawings, CAD files or samples, and our engineering team will design and manufacture crate systems built to your exact specifications."}},
            {"@type": "Question", "name": "What types of industrial packaging solutions do you specialize in?",
             "acceptedAnswer": {"@type": "Answer", "text": "We specialize in custom wooden crates, knock-down (flat-pack) crate kits, server crates, export packaging systems and structural metal components for industrial crating."}},
            {"@type": "Question", "name": "What information do you need to start an OEM packaging project?",
             "acceptedAnswer": {"@type": "Answer", "text": "Product dimensions and weight, fragility and handling requirements, shipment mode and destination, order quantities, and drawings or samples if available."}},
            {"@type": "Question", "name": "Are all solid wood materials ISPM-15 compliant for international shipping?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. 100% of our solid wood lumber and components undergo certified heat treatment and carry the official IPPC stamp, accompanied by full phytosanitary documentation to guarantee smooth customs clearance worldwide."}},
            {"@type": "Question", "name": "How do knockdown (flat-pack) crate kits reduce logistics and freight costs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Our flat-pack knockdown crate systems maximize container cubing efficiency by up to 60%, significantly lowering ocean freight and domestic transport costs while enabling fast, reliable on-site assembly at your destination facility."}}
        ]}
    extra = f'\n<script type="application/ld+json">{json.dumps(faq_json, ensure_ascii=False)}</script>'
    products = [
        ("solutions-wood-elements.webp", "Large structural timber panels staged on the factory floor for custom crate builds",
         "Custom Wooden Crates", "Built to your drawings — every dimension, every joint, every component."),
        ("solutions-server-crates.webp", "Wooden server crate with access ramp inside a warehouse",
         "Server Crates", "Shock-resistant crating for servers, racks and data center equipment."),
        ("solutions-battery-crates.webp", "Tall open-top wooden crate for battery units outdoors",
         "Battery & Energy Storage Crates", "UN38.3-compliant heavy-duty packaging for battery packs and charging stations."),
        ("solutions-plywood-panels.webp", "Precision cutting machine processing plywood panels",
         "Precision Panel Processing", "CNC-cut plywood panels with tight dimensional tolerances."),
        ("solutions-cnc-parts.webp", "CNC-machined wooden components for crate assembly",
         "CNC Wood Components", "Precision-machined wooden parts for engineered crate systems."),
    ]
    product_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in products)
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Solutions</div>
  <h1>Your Global OEM Partner for Industrial Wooden Packaging Solutions</h1>
  <p class="lead">Comprehensive industrial packaging solutions designed for strength, durability, and logistics efficiency — supporting complex global supply chain requirements across heavy industry, energy, and manufacturing sectors.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">Industrial Crating Solutions</h2>
  <p class="section-sub reveal">Heavy-duty engineered crating systems designed to protect large, sensitive, and high-value industrial equipment during global transportation. Built for structural strength, stability, and export compliance, our solutions perform reliably under complex logistics and handling conditions.</p>
  <div class="grid g3">{product_cards}
  </div>

  <h2 class="section-title reveal" style="margin-top:56px">Metal Components &amp; Knockdown Kit Systems</h2>
  <p class="section-sub reveal">Engineered wood and metal-based modular packaging systems designed for efficient assembly, structural strength, and optimized global logistics performance. Fully customized OEM solutions ensure precise fit, reduced shipping volume, and consistent performance across industrial applications.</p>

  <div class="split reveal" style="margin-bottom:56px">
    <div class="ph"><img src="{rel}assets/img/solutions-knockdown-kits.webp" alt="Flat-pack knockdown wooden crate kits with metal frames stacked in the factory" loading="lazy" width="800" height="600"></div>
    <div>
      <h3>Knockdown Crate Kits</h3>
      <p><em>Engineered OEM flat-pack packaging systems combining precision wood panels and structural metal components for efficient on-site assembly at destination.</em></p>
      <ul class="check-list">
        <li>Each kit includes pre-cut panels, reinforced frames, metal fittings, braces, and assembly hardware, ensuring fast installation and consistent structural performance across deployment.</li>
        <li>Optimized for container utilization — these systems reduce shipping volume and logistics costs while maintaining full structural strength and protection performance after assembly.</li>
      </ul>
    </div>
  </div>

  <div class="split reveal" style="margin-bottom:56px">
    <div>
      <h3>Structural Metal Components</h3>
      <p><em>High-strength engineered metal components designed for structural reinforcement in industrial crating systems.</em></p>
      <ul class="check-list">
        <li>Manufactured through precision laser cutting, forming, and welding — tight dimensional tolerances, high structural consistency, and reliable load-bearing performance.</li>
        <li>Designed for seamless integration with wooden crate structures, reinforcing key stress points during handling, stacking, and long-distance transportation.</li>
        <li>Built for demanding industrial and export environments: durable performance under vibration, dynamic loads, and multi-modal logistics conditions.</li>
      </ul>
    </div>
    <div class="ph"><img src="{rel}assets/img/solutions-metal-components.webp" alt="Yellow lifting frame moving wooden crate components in the factory" loading="lazy" width="800" height="450"></div>
  </div>

  <div class="split reveal">
    <div class="ph"><img src="{rel}assets/img/solutions-fastening-systems.webp" alt="Custom metal reinforcement plates for structural crate fastening" loading="lazy" width="800" height="956"></div>
    <div>
      <h3>Connection &amp; Fastening Systems</h3>
      <p><em>Custom-engineered sheet metal reinforcement plates designed for structural strengthening in industrial crate systems.</em></p>
      <ul class="check-list">
        <li>Manufactured in-house through precision laser cutting, bending, and welding — enhancing load distribution and structural rigidity at key connection points within wooden and hybrid crate assemblies.</li>
        <li>Strict dimensional control ensures accurate fitment and reliable integration with crate frames, improving overall stability during lifting, stacking, and long-distance transportation.</li>
      </ul>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Frequently Asked Questions</h2>
  <p class="section-sub reveal">Find answers to common questions about OEM customization, materials, production capacity, export standards, and packaging solutions.</p>
  <div class="faq">
    <div class="faq-item reveal"><button class="faq-q">Can you manufacture packaging based on our technical drawings or samples?</button><div class="faq-a"><p>Yes. Send us your technical drawings, CAD files or samples, and our engineering team will design and manufacture crate systems built to your exact specifications — every dimension, every joint, every component.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">What types of industrial packaging solutions do you specialize in?</button><div class="faq-a"><p>We specialize in custom wooden crates, knock-down (flat-pack) crate kits, server crates, export packaging systems, and structural metal components for industrial crating — all ISPM-15 compliant and export-ready.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">What information do you need to start an OEM packaging project?</button><div class="faq-a"><p>Product dimensions and weight, fragility and handling requirements, shipment mode and destination country, estimated order quantities, and any drawings or samples you already have. The more detail you share, the faster we can engineer the right solution.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">Are all solid wood materials ISPM-15 compliant for international shipping?</button><div class="faq-a"><p>Yes. 100% of our solid wood lumber and components undergo certified heat treatment and carry the official IPPC stamp, accompanied by full phytosanitary documentation to guarantee smooth customs clearance worldwide.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">How do knockdown (flat-pack) crate kits reduce logistics and freight costs?</button><div class="faq-a"><p>Our flat-pack knockdown crate systems maximize container cubing efficiency by up to 60%, significantly lowering ocean freight and domestic transport costs while enabling fast, reliable on-site assembly at your destination facility.</p></div></div>
  </div>
</div></section>
""" + cta_band(rel, "Start Your OEM Packaging Project",
               "Send us your drawings or product details — our engineers will respond within one business day.")
    return page(rel, "solutions", "Packaging Solutions | Custom Wooden Crates & Crating Systems",
                "Industrial crating solutions, knock-down crate kits and structural metal components engineered for strength, durability and logistics efficiency.", body, extra)

# ================= CAPABILITIES =================
def build_capabilities():
    rel = "../"
    gallery = [
        ("laser-cutting-machine.webp", "Gantry laser cutting machine cutting steel plate with sparks"),
        ("cnc-router-plywood.webp", "Gantry CNC machining center cutting plywood panels"),
        ("press-brake-bending.webp", "Worker operating a press brake to bend sheet metal components"),
        ("robotic-welding-arm.webp", "Industrial robotic arm welding a steel frame"),
        ("cnc-panel-saw.webp", "Electronic panel saw with touchscreen control console"),
        ("punch-press-stamping.webp", "Close-up of punch press stamping die with springs and guide pillars"),
        ("powder-coating-line.webp", "Red powder-coated parts hanging on an overhead conveyor coating line"),
        ("dip-coating-line.webp", "Large gantry dip-coating equipment with steel parts over treatment tanks"),
    ]
    figs = "\n".join(
        f'    <figure class="reveal"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy" width="400" height="300"></figure>'
        for fn, alt in gallery)
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Capabilities</div>
  <h1>Manufacturing &amp; Engineering Capabilities</h1>
  <p class="lead">Combining precision fabrication, controlled production systems, and scalable manufacturing capacity to deliver consistent quality, reliable output, and efficient supply for global OEM packaging programs.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">What We Do Best</h2>
  <p class="section-sub reveal">We deliver integrated OEM packaging solutions by combining precision manufacturing, custom engineering, and efficient global logistics. From individual components to complete knockdown crate systems, we ensure quality, consistency, and scalable performance for international industrial packaging programs.</p>

  <div class="grid g2" style="margin-top:8px">
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-quality-assurance.webp" alt="Quality inspector holding a checklist beside finished wooden crates" loading="lazy"></div>
      <div class="bd"><h3>Certifications &amp; Compliance</h3><p>We comply with international packaging and export standards to support global shipping requirements. All wood materials are ISPM-15 certified and properly heat-treated, with full documentation support for international logistics.</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-wood-metal.webp" alt="Close-up of metal fasteners on the edge of plywood crate panels" loading="lazy"></div>
      <div class="bd"><h3>Advanced Manufacturing Processes</h3><p>Our manufacturing capabilities include CNC machining, precision cutting, drilling, and routing for wood components. For metal fabrication, we use laser cutting, forming, bending, and robotic welding processes. Surface treatments such as polishing, galvanizing, and coating enhance durability and corrosion resistance. These integrated processes ensure every component meets exact specifications and performs reliably under real-world logistics conditions.</p></div></div>
  </div>

  <h2 class="section-title reveal" style="margin-top:64px">Integrated Capabilities</h2>
  <p class="section-sub reveal">One partner for the full journey — from engineering review to container loading.</p>
  <div class="grid g4">
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-oem-engineering.webp" alt="Open custom-built wooden crate showing its engineered internal structure" loading="lazy"></div>
      <div class="bd"><h3>OEM Engineering</h3><p>Crate systems engineered from your drawings for strength, stability and logistics efficiency.</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-knockdown-systems.webp" alt="Flat-pack wooden crate kits stacked on a pallet" loading="lazy"></div>
      <div class="bd"><h3>Knockdown Crate Systems</h3><p>Flat-pack kits with metal frames for efficient on-site assembly and lower freight cost.</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-production-capacity.webp" alt="Worker stacking freshly cut wooden boards in the factory" loading="lazy"></div>
      <div class="bd"><h3>Scalable Production Capacity</h3><p>Flexible manufacturing supporting high-volume OEM programs with reliable lead times.</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-logistics-support.webp" alt="Forklift loading crates into a shipping container at dusk" loading="lazy"></div>
      <div class="bd"><h3>Global Logistics Support</h3><p>Export-ready packing, container loading and ISPM-15 documentation for worldwide delivery.</p></div></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Inside Our Factory</h2>
  <p class="section-sub reveal">Integrated wood and metal fabrication under one roof — from CNC-cut panels to robotic welding and surface treatment.</p>
  <div class="gallery">{figs}
  </div>
</div></section>

<section><div class="wrap" style="max-width:860px">
  <h2 class="section-title reveal">Delivering More Than Manufacturing</h2>
  <p class="section-sub reveal">By combining integrated production, disciplined process control, and global logistics capability, we deliver more than manufacturing — we deliver reliable outcomes. Our solutions help customers reduce risk, control costs, and scale global operations with confidence.</p>
  <div class="frost reveal" style="background:var(--g50);border:1px solid var(--line);backdrop-filter:none;text-align:center">
    <h3 style="margin-bottom:10px">Contact Us</h3>
    <p style="color:var(--muted);margin-bottom:18px">We are ready to support your OEM packaging requirements with customized, efficient, and export-ready solutions. Your inquiry is important to us — our engineering team will respond promptly.</p>
    <a class="btn btn-green" href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</div></section>
""" + cta_band(rel, "Put Our Capabilities to Work",
               "Send your drawings — we'll engineer the crate system your program needs.")
    return page(rel, "capabilities", "Capabilities | Custom Wooden Packaging Manufacturing & Engineering",
                "CNC machining, precision cutting, laser-cut metal fabrication and ISPM-15 compliant processes delivering consistent OEM packaging quality at scale.", body)

# ================= ABOUT =================
def build_about():
    rel = "../"
    steps = [
        ("about-engineering-design.webp", "3D CAD design drawing of wooden crate components",
         "Engineering Design", "Every project starts with engineering — our team designs crate systems in 3D CAD from your drawings and specifications."),
        ("about-material-selection.webp", "Worker measuring a stack of plywood sheets",
         "Material Selection", "Certified timber and ISPM-15 compliant materials, selected and inspected for strength and export readiness."),
        ("about-precision-processing.webp", "CNC machine control panel in the factory",
         "Precision Processing", "CNC machining, precision cutting and drilling — every component produced to exact tolerances."),
        ("about-kit-assembly.webp", "Crate kit assembly with metal rails and fasteners",
         "Kit Assembly", "Panels, frames, metal fittings and fasteners are matched and pre-assembled into complete knockdown kits."),
        ("about-quality-inspection.webp", "Three workers inspecting metal tooling and fixtures",
         "Quality Inspection", "Strict quality inspection at every stage — dimensional checks, structural verification and export compliance."),
        ("about-packaging-logistics.webp", "Wooden crate with metal plates and protective packaging materials",
         "Packaging &amp; Logistics", "Export-ready packing with protective materials, moisture barriers and complete shipping documentation."),
        ("about-delivery-support.webp", "Forklift loading a finished wooden crate onto a truck",
         "Delivery &amp; Support", "Container loading and global delivery, with responsive support from order to arrival."),
    ]
    step_html = ""
    for i, (fn, alt, t, d) in enumerate(steps):
        img = f'<div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>'
        txt = (f'<div><span class="kicker">Step {i+1:02d}</span><h3>{t}</h3>'
               f'<p style="margin-top:10px">{d}</p></div>')
        inner = img + txt if i % 2 == 0 else txt + img
        step_html += f'\n  <div class="split reveal" style="margin-bottom:48px">{inner}</div>'
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / About Us</div>
  <h1>About Qingdao Lumber &amp; Packaging</h1>
  <p class="lead">In today's global supply chains, packaging is no longer just protection — it is a critical part of operational stability, cost control, and delivery efficiency.</p>
</div></div>

<section><div class="wrap" style="max-width:860px">
  <div class="reveal">
    <p>Qingdao Lumber &amp; Packaging was established to support this demand with reliable OEM manufacturing, precise engineering execution, and scalable production capability.</p>
    <p style="margin-top:16px">We ensure that every component, system, and shipment is delivered with consistency and full alignment to customer requirements.</p>
    <p style="margin-top:16px"><strong>Qingdao Lumber &amp; Packaging Co., Ltd. is a U.S.-owned OEM packaging manufacturer with full-scale production facilities in Qingdao, China.</strong></p>
    <p style="margin-top:16px">For 20+ years, we have combined international quality expectations with efficient manufacturing capabilities to serve industrial clients across North America, Europe, and global markets.</p>
    <p style="margin-top:16px">We specialize in custom knockdown crate systems, export packaging crates, and industrial protective packaging solutions.</p>
    <p style="margin-top:16px">All products are ISPM-15 compliant and fully prepared for international shipment.</p>
    <p style="margin-top:16px">To date, we have delivered over <strong>5 million crate sets</strong>, supporting global industrial and technology supply chains with stable and scalable OEM production.</p>
  </div>
  <div class="stat-row">
    <div class="stat reveal"><div class="n">20+</div><div class="l">Years of OEM expertise</div></div>
    <div class="stat reveal"><div class="n">5M+</div><div class="l">Crate sets delivered</div></div>
    <div class="stat reveal"><div class="n">100%</div><div class="l">ISPM-15 compliant materials</div></div>
  </div>
  <div class="reveal">
    <p>Our customers face increasing cost pressure, supply chain complexity, and the need for consistent quality across global operations.</p>
    <p style="margin-top:16px">We design OEM packaging systems that address these challenges through standardized engineering, scalable production, and optimized logistics performance.</p>
    <p style="margin-top:16px">We manufacture precision-cut wood components and fully integrated knockdown crate systems based on customer drawings and technical requirements.</p>
    <p style="margin-top:16px">Each OEM kit includes structural elements, metal fittings, fasteners, and protective materials, all matched and assembled into complete transport-ready systems for efficient deployment.</p>
    <p style="margin-top:16px">We operate as an integrated extension of our customers' supply chain, supporting OEM programs with structured processes, repeatable quality, and reliable global delivery.</p>
    <p style="margin-top:16px">From engineering review to final shipment, every stage is managed with precision and consistency.</p>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">From Drawing to Delivery</h2>
  <p class="section-sub reveal">Seven controlled stages take every OEM packaging program from engineering review to final shipment.</p>
{step_html}
</div></section>
""" + cta_band(rel, "Work With an OEM Packaging Partner",
               "Tell us what you're shipping — we'll engineer the right crate for it.")
    return page(rel, "about", "About Us | Qingdao Lumber & Packaging — 20+ Years OEM Expertise",
                "U.S.-owned OEM packaging manufacturer in Qingdao, China. 20+ years serving industrial clients across North America, Europe and global markets. 5M+ crate sets delivered.", body)

# ================= CASE STUDIES =================
def build_case_studies():
    rel = "../"
    cases = [
        ("High-value IT &amp; data center equipment",
         "Shock-resistant internal support system designed to stabilize sensitive server components during global transit.",
         "100% custom-built to customer drawings, ensuring safe handling, vibration protection, and reliable international delivery.",
         "case-data-server.webp", "Tall wooden server crate with CAUTION markings for data center equipment"),
        ("High-voltage utility equipment",
         "Reinforced timber-frame crate structure designed for stacking strength and impact resistance in bulk export shipping.",
         "Lower cost alternative to traditional packaging while improving durability, space efficiency, and logistics performance.",
         "case-glass-insulator.webp", "Wooden crates packed with stacked glass high-voltage insulators"),
        ("Heavy IT infrastructure transport",
         "Reinforced steel bracket system with CNC-cut precision panels for maximum load stability and secure assembly.",
         "Flat-pack KD structure reduces shipping costs while enabling fast on-site assembly and reuse capability.",
         "case-server-rack-kd.webp", "Flat-pack server rack kit with yellow steel support brackets"),
        ("Additive manufacturing &amp; industrial machinery",
         "Rigid frame structure with pallet integration designed for vibration control and long-distance transport safety.",
         "Ensures climate stability, structural protection, and consistent global delivery performance.",
         "case-industrial-printer.webp", "Custom wooden crate for an industrial printer"),
        ("Energy infrastructure equipment",
         "Custom-fit internal reinforcement system designed to eliminate movement and absorb transport shocks.",
         "Ensures installation-ready delivery with full protection across global shipping routes.",
         "case-ev-charging.webp", "Wooden crate housing an EV charging station"),
        ("High-volume relocation logistics",
         "ISPM-15 compliant reinforced KD structure designed for maximum container efficiency and repeat usage.",
         "Flat-pack system reduces freight cost while improving stacking strength and operational efficiency.",
         None, None),
    ]
    def case_card(app, focus, value, img, alt):
        inner = f"""
      <span class="kicker">Application</span>
      <h3>{app}</h3>
      <p style="margin-top:10px"><strong>Engineering Focus:</strong> {focus}</p>
      <p style="margin-top:8px;color:var(--muted)"><strong>Key Value:</strong> {value}</p>"""
        if img:
            return f"""
    <div class="card reveal"><div class="ph portrait"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd">{inner}
      </div></div>"""
        return f"""
    <div class="tcard reveal">{inner}
    </div>"""
    cards = "\n".join(case_card(*c) for c in cases)
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Case Study</div>
  <h1>Engineered Packaging in the Real World</h1>
  <p class="lead">Real-world applications demonstrating engineered packaging solutions that ensure structural reliability, logistics efficiency, and consistent execution across international industries.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">Proven Across Industries</h2>
  <p class="section-sub reveal">A selection of OEM packaging programs we have engineered and delivered.</p>
  <div class="grid g3">{cards}
  </div>
</div></section>

<section class="band"><div class="wrap" style="max-width:860px;text-align:center">
  <h2 class="section-title reveal">Engineering Standards</h2>
  <p class="section-sub reveal"><strong>Supporting OEM packaging programs worldwide.</strong><br>We partner with packaging companies, industrial manufacturers, and logistics providers to deliver scalable OEM packaging solutions across North America, Europe, and global markets.<br><br>Additional case studies and application examples are available upon request. Contact us to discuss your OEM packaging requirements and engineering needs.</p>
</div></section>

<section id="rfq"><div class="wrap">
  <h2 class="section-title reveal">Request a Quote</h2>
  <p class="section-sub reveal">Tell us what you're shipping — our engineering team will respond within one business day.</p>
  <form class="rfq reveal" id="rfqForm" novalidate>
    <div class="form-grid">
      <div class="field"><label for="fFirst">First Name *</label><input id="fFirst" name="first_name" type="text" autocomplete="given-name"><span class="err"></span></div>
      <div class="field"><label for="fLast">Last Name *</label><input id="fLast" name="last_name" type="text" autocomplete="family-name"><span class="err"></span></div>
      <div class="field"><label for="fEmail">Email *</label><input id="fEmail" name="email" type="email" autocomplete="email"><span class="err"></span></div>
      <div class="field"><label for="fPhone">Phone</label><input id="fPhone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="fCompany">Company *</label><input id="fCompany" name="company" type="text" autocomplete="organization"><span class="err"></span></div>
      <div class="field"><label for="fCountry">Country</label><input id="fCountry" name="country" type="text" autocomplete="country-name"></div>
      <div class="field full"><label for="fNeed">What are you shipping? Dimensions, weight, quantities, destination… *</label><textarea id="fNeed" name="requirements" rows="5"></textarea><span class="err"></span></div>
    </div>
    <div style="margin-top:22px;text-align:center">
      <button class="btn btn-green" type="submit" style="min-width:220px">Send Inquiry</button>
    </div>
    <div class="form-note" id="formNote" role="status"></div>
    <p style="margin-top:16px;font-size:.85rem;color:var(--muted);text-align:center">Prefer email? Write to <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="{WA_LINK}" target="_blank" rel="noopener">chat on WhatsApp</a>.</p>
  </form>
</div></section>
"""
    return page(rel, "case-studies", "Case Studies | Engineered OEM Packaging Applications",
                "Real-world engineered packaging applications across data centers, energy, industrial machinery and infrastructure — plus a direct RFQ form.", body)

# ================= INDUSTRY PAGES =================
def industry_page(slug, short, h1, title, desc, intro_paras, approach, solutions, challenges, scope, objective):
    rel = "../../"
    paras = "\n".join(f"    <p style=\"margin-top:14px\">{p}</p>" for p in intro_paras)
    sol = "\n".join(f"      <li>{s}</li>" for s in solutions)
    cha = "\n".join(f"      <li>{c}</li>" for c in challenges)
    sco = "\n".join(f"      <li>{s}</li>" for s in scope)
    wa_text = quote(f"Hello Qingdao Lumber, I'd like to discuss packaging for {short}.")
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / <a href="{rel}industries/data-servers-precision-electronics/">Industries</a> / {h1.split('|')[0].strip()}</div>
  <h1>{h1}</h1>
  <p class="lead">{objective}</p>
</div></div>

<section><div class="wrap" style="max-width:880px">
  <div class="reveal">{paras}</div>
</div></section>

<section class="band"><div class="wrap" style="max-width:880px">
  <h2 class="section-title reveal">Engineering Approach</h2>
  <p class="section-sub reveal">{approach}</p>
  <h3 class="reveal" style="margin:34px 0 6px">Key Solutions Include</h3>
  <ul class="check-list reveal">{sol}</ul>
</div></section>

<section><div class="wrap" style="max-width:880px">
  <div class="grid g2">
    <div class="reveal"><h3 style="margin-bottom:6px">Real-World Challenges Addressed</h3>
      <ul class="check-list">{cha}</ul></div>
    <div class="reveal"><h3 style="margin-bottom:6px">Application Scope</h3>
      <ul class="check-list">{sco}</ul></div>
  </div>
</div></section>
"""
    cta = f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>Discuss Your {short} Packaging Project</h2>
  <p>Send your product details — our engineers will design the protection your equipment deserves.</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}case-studies/#rfq">Request a Quote</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={wa_text}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
</div></section>"""
    return page(rel, "industries/" + slug, title, desc, body + cta)

def build_industries():
    pages = {}

    pages["data-servers-precision-electronics"] = industry_page(
        "data-servers-precision-electronics", "Data Server & Precision Electronics",
        "Data Server &amp; Precision Electronics Packaging",
        "Data Server & Precision Electronics Packaging | Custom Wooden Crates",
        "High-stability wooden packaging systems for data servers, storage arrays and precision electronics — zero internal movement, superior vibration resistance.",
        ["Data servers, storage arrays, high-end electronics, and precision electrical systems face extreme challenges during global transportation. Even minor vibration, impact, or internal movement can cause hard drive failures, solder joint damage, sensor misalignment, or complete system instability. Humidity fluctuations, electrostatic discharge, and repeated handling during sea, air, and multi-modal shipping only increase these risks.",
         "For OEMs and cloud infrastructure providers, packaging must also deliver absolute consistency and repeatability across large production batches — ensuring every unit arrives ready for immediate deployment with minimal on-site troubleshooting or rework."],
        "We specialize in designing high-stability wooden packaging systems for data servers and sensitive electronics, combining robust structural integrity with advanced internal protection engineering.",
        ["Custom-fitted server crates tailored for rack-mounted equipment, 2U–8U servers, GPU clusters, and storage arrays",
         "Precision internal blocking and cushioning systems using CNC-cut wood components, high-density foam, and EPE liners to eliminate movement in all three axes",
         "Lightweight yet high-strength hybrid crate designs that meet international transport standards while reducing shipping weight and cost",
         "Knock-down (flat-pack) crate systems for significantly lower return shipping and storage volume",
         "Optional integrated protections: anti-static linings, moisture barrier systems, humidity indicators, and shock monitoring labels"],
        ["Preventing hard drive and SSD damage from long-haul ocean freight vibration",
         "Ensuring entire server racks arrive deployment-ready, dramatically reducing on-site installation time",
         "Maintaining calibration accuracy for precision instruments and measurement equipment after international transit"],
        ["Data servers and cloud infrastructure hardware (rack servers, storage systems, switches, GPU servers)",
         "Industrial control systems and PLCs",
         "High-precision electronics and power systems",
         "Test & measurement instruments",
         "AI servers and edge computing equipment"],
        "Deliver zero internal movement, superior vibration resistance, and consistent OEM-grade protection for global shipments — ensuring every piece of sensitive equipment arrives in perfect condition, on time, and ready for immediate deployment.")

    pages["ev-battery-charging"] = industry_page(
        "ev-battery-charging", "EV Battery & Charging Station",
        "EV Battery &amp; Charging Station Packaging Solutions | UN38.3 Compliant",
        "EV Battery & Charging Station Packaging Solutions | UN38.3 Compliant",
        "Heavy-duty, UN38.3-compliant wooden packaging for lithium-ion battery packs and EV charging stations — certified protection for new energy products.",
        ["The rapid growth of new energy vehicles has created demanding packaging requirements for two critical product categories: high-voltage lithium-ion battery packs and EV charging stations. Both are high-value, technically complex, and sensitive to transport risks.",
         "EV battery packs face extreme safety and regulatory challenges — any impact or vibration can damage cells, trigger thermal runaway, or compromise the BMS. Charging stations, on the other hand, contain delicate power electronics, high-voltage components, large touchscreens, and cooling systems that are easily damaged by shock, moisture, or improper handling during global shipping.",
         "For battery manufacturers, automotive OEMs, and charging infrastructure providers, packaging must deliver uncompromising protection, full regulatory compliance, and consistent quality for international deliveries."],
        "We engineer heavy-duty wooden packaging systems tailored specifically for new energy products, combining superior structural strength with precision internal protection to meet the unique demands of both batteries and charging equipment.",
        ["<strong>For EV Batteries:</strong> Reinforced heavy-duty crates with high-load-bearing bases, multi-layer anti-vibration blocking, fire-retardant linings, electrical insulation, and UN38.3 compliant designs",
         "<strong>For Charging Stations:</strong> Oversized custom crates with tailored internal bracing, shock-absorbing cushioning for screens and power modules, weather-resistant barriers, and reinforced lifting points",
         "Hybrid structures balancing extreme rigidity with optimized weight",
         "Knock-down (flat-pack) options for reduced return shipping and storage costs",
         "Integrated monitoring solutions (shock, tilt, and humidity sensors)",
         "Precision CNC-cut blocking systems ensuring zero internal movement"],
        ["Preventing cell damage and thermal runaway risks in lithium battery packs during ocean and road transport",
         "Protecting sensitive power electronics, touchscreens, and connectors in charging stations from impact and moisture",
         "Ensuring safe handling and compliance for heavy, high-value new energy equipment across complex global supply chains",
         "Reducing on-site installation issues and costly warranty claims"],
        ["Lithium-ion battery packs for passenger EVs, commercial vehicles, and energy storage systems (ESS)",
         "Blade, prismatic, pouch, and cylindrical battery modules",
         "DC Fast Chargers (60kW–360kW+) and liquid-cooled charging systems",
         "AC Wallboxes, charging piles, and power distribution cabinets",
         "Integrated charging + energy storage solutions"],
        "Provide certified, high-reliability wooden packaging solutions that ensure the safe, damage-free transport of EV batteries and charging stations worldwide. We help new energy companies achieve zero-transport-damage performance, full regulatory compliance, faster project deployment, and enhanced brand reputation in the global market.")

    pages["industrial-machinery-infrastructure"] = industry_page(
        "industrial-machinery-infrastructure", "Industrial Machinery & Infrastructure",
        "Industrial Machinery &amp; Infrastructure Equipment Wooden Packaging",
        "Industrial Machinery & Infrastructure Equipment Wooden Packaging",
        "Heavy-duty engineered wooden packaging for industrial machinery and infrastructure equipment — maximum structural protection for capital-intensive cargo.",
        ["Industrial machinery, heavy electrical equipment, and critical infrastructure components are typically large, heavy, and highly capital-intensive. These products often contain precision mechanical parts, sensitive electronics, delicate instruments, and complex assemblies that are vulnerable to severe vibration, impact, moisture, dust, and shifting during long-distance international transportation.",
         "Any damage during transit can result in costly repairs, project delays, and safety risks. For manufacturers and EPC contractors, packaging must provide maximum structural protection while enabling safe, efficient loading, unloading, and on-site installation across challenging global supply chains."],
        "We design robust, custom-engineered wooden packaging systems specifically built for heavy industrial and infrastructure equipment. Our solutions combine superior load-bearing strength with intelligent internal protection to ensure equipment arrives in perfect condition.",
        ["Heavy-duty reinforced wooden crates with steel corner protectors and high-strength bases",
         "Custom internal blocking, bracing, and shock-absorbing systems tailored to each machine's center of gravity and weak points",
         "Multi-layer protection for sensitive components using high-density foam, rubber isolators, and anti-vibration mounts",
         "Weatherproof and moisture-barrier designs suitable for sea freight and outdoor storage",
         "Integrated forklift pockets, lifting eyes, and reinforced handling points for safe site operations",
         "Modular knock-down structures for optimized shipping volume and cost efficiency",
         "Optional shock and tilt monitoring devices"],
        ["Protecting precision components in CNC machines, generators, and transformers from transit vibration and impact",
         "Preventing deformation or misalignment of large structural equipment during multi-modal transport",
         "Ensuring safe handling and timely delivery for time-critical infrastructure projects",
         "Reducing damage claims and costly on-site rectification"],
        ["Industrial machinery (CNC machines, injection molding equipment, printing presses, pumps, and compressors)",
         "Power generation and distribution equipment (generators, transformers, switchgear, and control panels)",
         "Infrastructure components (bridge sections, wind power parts, mining equipment, and heavy valves)",
         "Large electrical and mechanical systems",
         "Oil & gas and heavy engineering equipment"],
        "Deliver heavy-duty, high-reliability wooden packaging solutions that guarantee the safe, damage-free transport of valuable industrial and infrastructure equipment worldwide. We help manufacturers and project owners minimize transport risks, accelerate project timelines, and protect their reputation for quality delivery.")

    pages["high-voltage-insulators-power-transmission"] = industry_page(
        "high-voltage-insulators-power-transmission", "High Voltage Insulator & Power Transmission",
        "High Voltage Insulator &amp; Power Transmission Packaging",
        "High Voltage Insulator & Power Transmission Packaging | Custom Wooden Crates",
        "Specialized protective wooden packaging for fragile glass, ceramic and porcelain high-voltage insulators — maximum safety for power grid projects.",
        ["High-voltage insulators, glass and ceramic components, porcelain bushings, and power transmission equipment are inherently fragile, heavy, and extremely valuable. These products are highly susceptible to impact, vibration, pressure, and chipping during international transportation. Even minor surface damage or micro-cracks can render high-voltage insulators unusable, leading to costly rejections, project delays, and safety risks in power grid construction.",
         "For manufacturers of insulators and electrical infrastructure components, packaging must provide superior shock absorption, stable positioning, and reliable protection while meeting stringent international transport standards."],
        "We specialize in reinforced wooden crate systems engineered specifically for the protection of fragile glass, ceramic, and porcelain high-voltage components. Our crates combine excellent structural rigidity and superior shock resistance with weight-efficient design.",
        ["Reinforced wooden crate structures that provide outstanding impact absorption and reduce resonance vibration",
         "Precision custom internal blocking and cushioning tailored to the shape and fragility of insulators",
         "Multi-layer protection using high-density foam, rubber pads, and anti-abrasion separators to prevent chipping and cracking",
         "Reinforced base and corner structures for heavy loads and safe handling",
         "Ventilated designs to prevent moisture condensation on ceramic and glass surfaces",
         "Modular and knock-down configurations for cost-efficient return logistics",
         "Optional shock and tilt monitoring systems"],
        ["Preventing chipping, cracking, and breakage of glass and ceramic high-voltage insulators during long-haul sea and land transport",
         "Minimizing micro-damage that could cause electrical failure under high voltage",
         "Reducing packaging weight while maintaining superior protection compared to traditional heavy crates",
         "Ensuring safe, damage-free delivery to global power grid and substation projects"],
        ["High-voltage porcelain and glass insulators (suspension, post, pin, and station post types)",
         "Ceramic bushings and transformer components",
         "Glass and ceramic power transmission components",
         "Surge arresters and other fragile electrical infrastructure products",
         "Large-diameter porcelain housings and specialty insulators"],
        "Deliver specialized protective crate packaging solutions that set the industry standard for protecting fragile yet critical high-voltage glass and ceramic insulators. We ensure maximum safety, minimum damage, and reliable global delivery, helping power transmission manufacturers achieve superior product integrity and customer satisfaction on international projects.")
    return pages

# ================= SEO FILES =================
def build_seo():
    urls = ["", "solutions/", "capabilities/", "about/", "case-studies/"] + \
           ["industries/" + s + "/" for s, _, _ in INDUSTRIES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{CANON}/{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u == '' else '0.8'}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {CANON}/sitemap.xml\n")

# ================= LEGACY REDIRECTS =================
def build_redirects():
    redirects = [
        ("home/index.html", f"{CANON}/"),
        ("2/index.html", f"{CANON}/capabilities/"),
        ("3/index.html", f"{CANON}/about/"),
        ("case-study/index.html", f"{CANON}/case-studies/"),
        ("case-study-more/index.html", f"{CANON}/case-studies/"),
        ("industries/electronics-precision/index.html", f"{CANON}/industries/data-servers-precision-electronics/"),
        ("industries/1/index.html", f"{CANON}/industries/data-servers-precision-electronics/"),
        ("industries-ev-battery-charging/index.html", f"{CANON}/industries/ev-battery-charging/"),
        ("industries-industrial-infra/index.html", f"{CANON}/industries/industrial-machinery-infrastructure/"),
        ("industries-power-electrical/index.html", f"{CANON}/industries/high-voltage-insulators-power-transmission/"),
    ]
    for path, target in redirects:
        content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting...</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<script>window.location.replace('{target}');</script>
</head>
<body>
<p>Redirecting to <a href="{target}">{target}</a>...</p>
</body>
</html>"""
        write(path, content)

# ================= MAIN =================
def main():
    write("index.html", build_home())
    write("solutions/index.html", build_solutions())
    write("capabilities/index.html", build_capabilities())
    write("about/index.html", build_about())
    write("case-studies/index.html", build_case_studies())
    for slug, html in build_industries().items():
        write(f"industries/{slug}/index.html", html)
    build_redirects()
    build_seo()
    # copy images already in assets/img (populated by image pipeline)
    print("done.")

if __name__ == "__main__":
    main()
