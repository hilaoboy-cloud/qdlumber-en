#!/usr/bin/env python3
"""Build the Qingdao Lumber English static site.
Run: python3 gen_site.py
"""
import os, json, shutil
from urllib.parse import quote as _q

def quote(s): return _q(s)

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
     "Wood packaging with internal cushioning and structural support for servers, racks and precision electronics."),
    ("ev-battery-charging", "Battery & Charging Equipment",
     "Custom packaging configured for battery packs, charging stations and new energy transport requirements."),
    ("industrial-machinery-infrastructure", "Industrial Machinery & Infrastructure",
     "Heavy-duty wooden crates and engineered load-bearing bases for capital equipment and infrastructure."),
    ("high-voltage-insulators-power-transmission", "High Voltage Insulator & Power Transmission",
     "Custom crates with internal separation and cushioning configured for fragile glass, ceramic and porcelain insulators."),
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
    "description": "OEM manufacturer of custom wooden crates, pallets, skids and knock-down packaging kits for industrial equipment and export supply chains in Qingdao, China.",
    "contactPoint": [{
        "@type": "ContactPoint", "telephone": "+86-134-0510-1358",
        "email": EMAIL, "contactType": "sales", "areaServed": "Worldwide"
    }],
    "address": {"@type": "PostalAddress", "streetAddress": OFFICE[0],
                "addressLocality": "Qingdao", "addressCountry": "CN"},
}

def head(rel, slug, title, desc, extra=""):
    canon = CANON + ("/" if not slug else "/" + slug + "/")
    zh_url = CANON + "/zh/" + (slug + "/" if slug else "")
    home_preloads = ""
    if slug == "":
        home_preloads = f"""<link rel="preconnect" href="https://player.vimeo.com">
<link rel="preconnect" href="https://f.vimeocdn.com">
<link rel="preconnect" href="https://i.vimeocdn.com">
<link rel="dns-prefetch" href="https://player.vimeo.com">
<link rel="preload" as="image" href="{rel}assets/img/hero-poster.webp">"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{canon}">
<link rel="alternate" hreflang="zh" href="{zh_url}">
<link rel="alternate" hreflang="x-default" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{CANON}/assets/img/logo.webp">
<link rel="icon" type="image/webp" href="{rel}assets/img/favicon.webp">
<link rel="icon" type="image/png" href="{rel}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{rel}assets/img/favicon.png">
{home_preloads}
<link rel="stylesheet" href="{rel}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ORG_JSONLD, ensure_ascii=False)}</script>
{extra}</head>"""

def header(rel, slug=""):
    ind_links = "\n".join(
        f'<a href="{rel}industries/{s}/">{n}</a>' for s, n, _ in INDUSTRIES)
    zh_target = f"{rel}zh/{slug + '/' if slug else ''}"
    return f"""<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{rel}" aria-label="Qingdao Lumber &amp; Packaging — home">
      <img src="{rel}assets/img/logo.webp" alt="Qingdao Lumber &amp; Packaging" width="259" height="98"></a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="mainNav">
      <a class="nav-link" data-nav="home" href="{rel}">Home</a>
      <a class="nav-link" data-nav="solutions" href="{rel}solutions/">Solutions</a>
      <a class="nav-link" data-nav="capabilities" href="{rel}capabilities/">Capabilities</a>
      <a class="nav-link" data-nav="about" href="{rel}about/">About Us</a>
      <a class="nav-link" data-nav="applications" href="{rel}applications/">Applications</a>
      <span class="has-drop"><a class="nav-link" data-nav="industries" href="{rel}industries/data-servers-precision-electronics/">Industries ▾</a>
        <span class="drop">{ind_links}</span></span>
      <a class="nav-cta" href="{rel}applications/#rfq">Request a Quote</a>
      <a class="lang-flag-toggle" href="{zh_target}" title="Switch to Chinese" aria-label="Switch to Chinese">
        <img src="{rel}assets/img/flag-cn.svg" alt="Chinese" width="26" height="19.5" class="flag-icon">
      </a>
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
      <img src="{rel}assets/img/logo-footer.webp" alt="Qingdao Lumber &amp; Packaging" width="200" height="75">
      <p>Qingdao Lumber &amp; Packaging manufactures custom wooden crates, pallets, skids and knock-down packaging kits for industrial equipment and global export supply chains.</p>
      <div class="social-row">
        <a href="https://www.linkedin.com/company/qdlumber/" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
        <a href="https://www.youtube.com/@QingdaoLumberPackaging" aria-label="YouTube" target="_blank" rel="noopener">▶</a>
        <a href="{WA_LINK}" aria-label="WhatsApp" target="_blank" rel="noopener">WA</a>
      </div>
    </div>
    <div>
      <h4>EXPLORE</h4>
      <ul>
        <li><a href="{rel}">Home</a></li>
        <li><a href="{rel}solutions/">Solutions</a></li>
        <li><a href="{rel}capabilities/">Capabilities</a></li>
        <li><a href="{rel}about/">About Us</a></li>
        <li><a href="{rel}applications/">Applications</a></li>
        <li><a href="{rel}applications/#rfq">Request a Quote</a></li>
      </ul>
    </div>
    <div>
      <h4>INDUSTRIES</h4>
      <ul>{ind_links}</ul>
    </div>
    <div>
      <h4>OUR NETWORK</h4>
      <ul>
        <li><a href="http://www.marinelumberco.com" target="_blank" rel="noopener">Marine Lumber Co. ↗</a></li>
        <li><a href="https://marinedefensepackaging.com" target="_blank" rel="noopener">Marine Defense Packaging ↗</a></li>
        <li><a href="http://www.qdlumber.com" target="_blank" rel="noopener">Qingdao Lumber &amp; Packaging (China) ↗</a></li>
      </ul>
    </div>
    <div>
      <h4>CONTACT</h4>
      <div class="footer-contact-block">
        <strong>Factory</strong>
        <span>{FACTORY[0]}</span><br>
        Tel: <a href="tel:+8618602619997">{FACTORY[1]}</a><br>
        Email: <a href="mailto:{FACTORY[2]}">{FACTORY[2]}</a>
      </div>
      <div class="footer-contact-block" style="margin-top:10px">
        <strong>Office</strong>
        <span>{OFFICE[0]}</span><br>
        Tel: <a href="tel:+8613405101358">{OFFICE[1]}</a><br>
        Email: <a href="mailto:{OFFICE[2]}">{OFFICE[2]}</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="yr">2026</span> Qingdao Lumber &amp; Packaging Co., Ltd. All rights reserved.</span>
    <span>ISPM 15 Treatment Support · Export Packaging Manufacturing</span>
  </div>
</footer>
{WA_CODE}
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def page(rel, slug, title, desc, body, extra_head=""):
    return head(rel, slug, title, desc, extra_head) + header(rel, slug) + body + footer(rel)

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
    <a class="btn btn-green" href="{rel}applications/#rfq">Request a Quote</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={quote('Hello Qingdao Lumber, I would like to discuss my packaging requirements.')}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
</div></section>"""

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

    pillars = [
        ("Built to Your Specifications",
         "We manufacture packaging to customer drawings, dimensions and project requirements."),
        ("Consistent Production",
         "Defined production processes and inspection procedures support repeat orders and consistent output."),
        ("Designed for Shipping",
         "Packaging configurations can be tailored to product dimensions, handling methods and shipping requirements."),
        ("Export Packaging Support",
         "ISPM 15-related treatment and marking requirements can be addressed according to the shipment and destination."),
    ]
    pillar_cards = "\n".join(
        f'''    <div class="tcard reveal"><h3 style="color:var(--g700);margin-bottom:8px">{t}</h3><p>{d}</p></div>'''
        for t, d in pillars)

    features = [
        ("values-precision.webp", "Wood packaging component fabrication in factory",
         "Custom-Built to Drawings",
         "Every wooden crate, pallet and base is manufactured to your specified dimensions, tolerances and load ratings."),
        ("values-efficiency.webp", "Production scheduling and packaging coordination",
         "Repeat OEM Programs",
         "Reliable manufacturing capacity supporting both scheduled recurring production and project-based batches."),
        ("values-accountability.webp", "ISPM 15 compliant heat-treated wood packaging ready for export",
         "Export Treatment Standards",
         "Solid wood packaging materials can be heat-treated and marked in accordance with ISPM 15 for international trade."),
        ("values-partnership.webp", "Project team reviewing packaging assembly and specifications",
         "Long-Term OEM Partnership",
         "Responsive communication, transparent project tracking and dedicated support for manufacturing supply chains."),
    ]
    feature_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in features)

    body = f"""
<section class="hero">
  <div class="hero-video-bg">
    <iframe src="https://player.vimeo.com/video/1190319624?background=1&autoplay=1&loop=1&byline=0&title=0&muted=1" frameborder="0" allow="autoplay; fullscreen" allowfullscreen loading="eager" fetchpriority="high"></iframe>
  </div>
  <div class="hero-overlay"></div>
  <div class="wrap hero-wrap">
    <div class="hero-content reveal in">
      <span class="hero-kicker">OEM WOOD PACKAGING MANUFACTURING</span>
      <h1 class="hero-title">Custom Wood Packaging for Industrial Supply Chains</h1>
      <p class="hero-sublead" style="font-weight:600;font-size:1.15rem;color:#e8f5e9;margin-bottom:12px">OEM Manufacturing Built to Your Specifications.</p>
      <p class="hero-lead">We manufacture custom wooden crates, pallets, skids and knock-down packaging kits for industrial equipment and export shipments. From customer drawings to repeat production, we focus on fit, consistency and practical shipping requirements.</p>
      <div class="hero-actions">
        <a class="btn btn-green" href="{rel}applications/#rfq">Request a Quote</a>
        <a class="btn btn-ghost" href="{rel}solutions/">Explore Our Solutions</a>
      </div>
    </div>
  </div>
</section>

<section style="padding:48px 0 0"><div class="wrap">
  <div class="grid g4">
{pillar_cards}
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">Manufacturing Built Around Your Supply Chain</h2>
  <p class="section-sub reveal">We support industrial manufacturers and equipment exporters with reliable wood packaging, repeatable quality control and export readiness.</p>
  <div class="grid g4">{feature_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Production Consistency &amp; Process Control</h2>
  <p class="section-sub reveal">From initial drawing review to container stowage, each step is aligned with customer requirements.</p>
  <div class="grid g2" style="max-width:960px;margin:0 auto">
    <div class="tcard reveal"><h3>Accurate Fit &amp; Structural Integrity</h3><p>Components are precision-cut and assembled to customer specifications, ensuring secure fit and dependable support during handling.</p></div>
    <div class="tcard reveal"><h3>Space &amp; Volume Optimization</h3><p>Knock-down crate kits and modular packaging configurations are designed to reduce shipping and storage volume where suitable.</p></div>
    <div class="tcard reveal"><h3>Standardized Inspection Procedures</h3><p>Defined quality checks cover lumber dimensions, fastener integrity, joint fit and IPPC marking clarity before dispatch.</p></div>
    <div class="tcard reveal"><h3>Reliable Batch Fulfillment</h3><p>Structured production schedules and responsive project coordination support dependable deliveries for continuous operations.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="text-align:center">
  <h2 class="section-title reveal">Manufacturing &amp; Packing Operations in Action</h2>
  <p class="section-sub reveal">Watch our automated woodworking, component prefabrication and packaging preparation in action at our Qingdao facility.</p>
  <div class="video-showcase reveal">
    <iframe src="https://www.youtube.com/embed/5F0zRgISQto?rel=0" title="Qingdao Lumber &amp; Packaging OEM Service" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">Wood Packaging Across Industrial Sectors</h2>
  <p class="section-sub reveal">Tailored configurations developed for industrial equipment, precision technology, power infrastructure and new energy programs.</p>
  <div class="grid g2">{ind_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Our Packaging Solutions</h2>
  <p class="section-sub reveal">Custom wooden crates · Knock-down crate kits · Pallets &amp; skids · Server crates · Export packaging preparation — built to customer drawings.</p>
  <div style="text-align:center" class="reveal">
    <a class="btn btn-green" href="{rel}solutions/">View All Solutions</a>
  </div>
</div></section>
""" + cta_band(rel, "Share Your Drawings or Requirements",
               "Tell us about your product, packaging requirements and shipment destination. We will review your inquiry and follow up regarding the next steps.")
    return page(rel, "", "Qingdao Lumber & Packaging | Custom Wood Packaging",
                "OEM manufacturer of custom wooden crates, pallets, skids and knock-down packaging kits for industrial equipment and export supply chains.", body)

# ================= SOLUTIONS =================
def build_solutions():
    rel = "../"
    faq_json = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Can you manufacture packaging based on our technical drawings or samples?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. We manufacture custom wooden crates, skids, pallets and knock-down kits directly to customer drawings, dimensions and project specifications."}},
            {"@type": "Question", "name": "What types of industrial packaging solutions do you specialize in?",
             "acceptedAnswer": {"@type": "Answer", "text": "We provide custom wooden crates, server crates, knock-down crate kits, heavy-duty pallets and skids, precision wood components, and protective packaging accessories."}},
            {"@type": "Question", "name": "What information is needed to review an inquiry?",
             "acceptedAnswer": {"@type": "Answer", "text": "Product dimensions, weight, handling method, shipment destination, estimated quantities, and technical drawings or sketches if available."}},
            {"@type": "Question", "name": "How are export wood packaging requirements handled?",
             "acceptedAnswer": {"@type": "Answer", "text": "Applicable solid wood packaging materials can be heat-treated and marked in accordance with ISPM 15 standards, supporting necessary export phytosanitary documentation."}},
            {"@type": "Question", "name": "How do knock-down (flat-pack) crate kits assist with shipping costs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Knock-down crate kits ship flat, designed to reduce shipping and storage volume where suitable, and assemble securely on-site at destination."}}
        ]}
    extra = f'\n<script type="application/ld+json">{json.dumps(faq_json, ensure_ascii=False)}</script>'

    products = [
        ("solutions-wood-elements.webp", "Custom wooden crates built to specifications on factory floor",
         "Custom Wooden Crates", "Built to customer drawings, dimensions and load-bearing requirements."),
        ("solutions-server-crates.webp", "Wooden server crate with access ramp inside warehouse",
         "Server Crates", "Wooden packaging configured for server racks, power modules and data center equipment."),
        ("solutions-battery-crates.webp", "Wooden crate for battery packs and charging equipment",
         "Knock-Down Crate Kits", "Modular flat-pack crating kits convenient to transport and assemble at destination."),
        ("solutions-plywood-panels.webp", "Heavy-duty wooden skids and pallets in staging area",
         "Pallets &amp; Skids", "Engineered timber bases and heavy-duty skids for stable handling and transport."),
        ("solutions-cnc-parts.webp", "Precision-cut wood components and panels",
         "Wood Components", "Dimensioned timber, plywood panels and pre-cut parts processed to project specifications."),
        ("case-ev-charging.webp", "Protective packaging materials and foam inserts inside crate",
         "Protective Packaging", "Internal cushioning, foam inserts, barrier bags and corrosion protection configured per project needs."),
    ]
    product_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in products)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Solutions</div>
  <h1>Custom Wood Packaging Solutions</h1>
  <p class="lead">We provide custom wood packaging for industrial equipment, export shipments and recurring OEM programs. Solutions are developed around your product dimensions, handling requirements, shipment conditions and assembly needs.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">Packaging Products &amp; Configurations</h2>
  <p class="section-sub reveal">From individual custom crates to repeatable knock-down kits, each packaging structure is tailored to the physical characteristics of your product and logistics requirements.</p>
  <div class="grid g3">{product_cards}
  </div>

  <h2 class="section-title reveal" style="margin-top:56px">Structural Configurations &amp; Export Features</h2>
  <p class="section-sub reveal">Practical engineering details focused on load distribution, transit stability, space efficiency and export compliance.</p>

  <div class="split reveal" style="margin-bottom:32px">
    <div class="ph"><img src="{rel}assets/img/knockdown-kits-flatpack.webp" alt="Flat-pack wooden crate components stacked on pallets" loading="lazy" width="800" height="450"></div>
    <div class="split-content">
      <span class="kicker">Flat-Pack Architecture</span>
      <h3>Knock-Down (KD) Crate Kits</h3>
      <p><em>Flat-pack wooden crate systems engineered for space efficiency and fast on-site assembly.</em></p>
      <ul class="check-list">
        <li>Designed to reduce shipping and storage volume where suitable, lowering ocean freight and domestic transport costs.</li>
        <li>Pre-drilled and pre-fitted panels designed for accurate fit and secure assembly at destination.</li>
        <li>Suitable for recurring equipment programs, returnable loops, or projects requiring streamlined field crating.</li>
      </ul>
      <div class="split-meta"><span>Packaging Format:</span> Modular Flat-Pack Kits for Space-Efficient Stowage</div>
    </div>
  </div>

  <div class="split reveal" style="margin-bottom:32px">
    <div class="split-content">
      <span class="kicker">Structural Reinforcement</span>
      <h3>Reinforced Framing &amp; Hardware Integration</h3>
      <p><em>Heavy-duty timber frames integrated with structural steel brackets and corner hardware for high-load applications.</em></p>
      <ul class="check-list">
        <li>Designed for accurate fit and secure assembly, reinforcing key stress points during lifting and multi-modal transport.</li>
        <li>Configured with heavy-duty skids, lifting provisions, and forklift entry pockets for safe handling.</li>
        <li>Surface-treated hardware options including galvanizing or zinc plating available based on project needs.</li>
      </ul>
      <div class="split-meta"><span>Hardware Integration:</span> High-Strength Corner Brackets &amp; Lifting Hardware</div>
    </div>
    <div class="ph"><img src="{rel}assets/img/solutions-metal-components.webp" alt="Lifting frame moving wooden crate components in factory" loading="lazy" width="800" height="450"></div>
  </div>

  <div class="split reveal">
    <div class="ph"><img src="{rel}assets/img/solutions-fastening-systems.webp" alt="Fastening hardware and structural plates for wood crates" loading="lazy" width="800" height="956"></div>
    <div class="split-content">
      <span class="kicker">Export Compliance</span>
      <h3>Export Packaging Preparation &amp; ISPM 15 Support</h3>
      <p><em>Solid wood heat treatment and documentation to support international trade requirements.</em></p>
      <ul class="check-list">
        <li>Applicable solid wood packaging materials undergo certified heat treatment meeting ISPM 15 standards.</li>
        <li>Official IPPC stamps applied clearly on exterior crate surfaces for customs verification.</li>
        <li>Support applicable export documentation and destination-country phytosanitary requirements.</li>
      </ul>
      <div class="split-meta"><span>Export Readiness:</span> ISPM 15 Compliant Solid Wood &amp; IPPC Marking</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Frequently Asked Questions</h2>
  <p class="section-sub reveal">Common questions regarding customization, technical drawings, export standards and shipping requirements.</p>
  <div class="faq">
    <div class="faq-item reveal"><button class="faq-q">Can you manufacture packaging based on our technical drawings or samples?</button><div class="faq-a"><p>Yes. We manufacture custom wooden crates, skids, pallets and knock-down kits directly to customer drawings, dimensions and project specifications.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">What types of industrial packaging solutions do you specialize in?</button><div class="faq-a"><p>We provide custom wooden crates, server crates, knock-down crate kits, heavy-duty pallets and skids, precision wood components, and protective packaging accessories.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">What information is needed to review an inquiry?</button><div class="faq-a"><p>Product dimensions, weight, handling method, shipment destination, estimated quantities, and technical drawings or sketches if available.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">How are export wood packaging requirements handled?</button><div class="faq-a"><p>Applicable solid wood packaging materials can be heat-treated and marked in accordance with ISPM 15 standards, supporting necessary export phytosanitary documentation.</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">How do knock-down (flat-pack) crate kits assist with shipping costs?</button><div class="faq-a"><p>Knock-down crate kits ship flat, designed to reduce shipping and storage volume where suitable, and assemble securely on-site at destination.</p></div></div>
  </div>
</div></section>
""" + cta_band(rel, "Share Your Drawings or Requirements",
               "Tell us about your product, packaging requirements and shipment destination. We will review your inquiry and follow up regarding the next steps.")
    return page(rel, "solutions", "Custom Wooden Crates & Packaging Solutions",
                "Custom wood packaging solutions for industrial equipment, export shipments and repeat OEM programs — built to your drawings and shipping requirements.", body, extra)

# ================= CAPABILITIES =================
def build_capabilities():
    rel = "../"
    gallery = [
        ("laser-cutting-machine.webp", "Steel plate fabrication equipment"),
        ("cnc-router-plywood.webp", "CNC router processing plywood panels"),
        ("press-brake-bending.webp", "Forming sheet metal brackets"),
        ("robotic-welding-arm.webp", "Welding structural corner assemblies"),
        ("cnc-panel-saw.webp", "Precision panel saw cutting plywood"),
        ("punch-press-stamping.webp", "Punch press stamping hardware components"),
        ("powder-coating-line.webp", "Powder coating hardware components"),
        ("dip-coating-line.webp", "Anti-corrosion surface treatment tanks"),
    ]
    figs = "\n".join(
        f'    <figure class="reveal"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy" width="400" height="300"></figure>'
        for fn, alt in gallery)

    sections = [
        ("Custom Manufacturing", "capabilities-oem-engineering.webp", "Open custom wooden crate showing internal structure",
         "We manufacture wooden crates, pallets, skids and framing structures according to customer drawings, dimensions, load requirements and project specifications."),
        ("Wood Processing", "capabilities-wood-metal.webp", "Precision-cut wood components and corner joints",
         "Equipped with panel saws, CNC routers and multi-spindle boring equipment to process solid lumber and plywood panels with dimensional consistency."),
        ("Knock-Down Packaging", "capabilities-knockdown-systems.webp", "Flat-pack wooden crate kits stacked on pallet",
         "Modular flat-pack crating systems engineered for efficient container stowage, reduced shipping volume where suitable, and straightforward site assembly."),
        ("Quality Inspection", "capabilities-quality-assurance.webp", "Quality inspection of finished wooden crates",
         "Systematic in-process inspection covering wood moisture, dimensional verification, fastening integrity, IPPC mark clarity and structural alignment."),
        ("Export Packaging Preparation", "capabilities-logistics-support.webp", "Loading ISPM-15 wooden crates for shipment",
         "Heat treatment processing for solid wood in compliance with ISPM 15 standards, IPPC stamping, and coordination of export documentation."),
        ("Production &amp; Shipment Coordination", "values-efficiency.webp", "Production planning and shipment staging",
         "Production scheduling, batch tracking, container stowage planning and dispatch coordination to support ongoing customer shipping schedules."),
    ]
    sec_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for t, img, alt, d in sections)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Capabilities</div>
  <h1>Manufacturing Capabilities</h1>
  <p class="lead">Our manufacturing capabilities support custom wood packaging, precision-cut components and repeat OEM production. Available processes and specifications are confirmed according to project requirements.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">Manufacturing &amp; Operational Capabilities</h2>
  <p class="section-sub reveal">From technical drawing review through component cutting, assembly and export preparation, we focus on consistent execution.</p>
  <div class="grid g3">{sec_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">Processing &amp; Fabrication Equipment</h2>
  <p class="section-sub reveal">Our facility integrates automated woodworking machinery alongside structural metal processing to support diverse packaging configurations.</p>
  <div class="gallery">{figs}
  </div>
</div></section>

<section><div class="wrap" style="max-width:960px">
  <h2 class="section-title reveal">Project Review &amp; Manufacturing Workflow</h2>
  <p class="section-sub reveal">How we work with your team from initial requirement confirmation through repeat supply.</p>
  <div class="grid g2">
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">1. Specification &amp; Drawing Review</h3>
      <p>We review customer drawings, 3D CAD files or product dimensions, confirming material selections, load ratings and destination shipping conditions.</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">2. Process &amp; Material Planning</h3>
      <p>Lumber selection, cutting lists, fastener specifications and protective materials are scheduled to ensure batch consistency and dimensional accuracy.</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">3. In-Process Quality Checks</h3>
      <p>Dimensional tolerances, joint fit, fastener placement and structural integrity are verified at key production stages.</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">4. Export Readiness &amp; Dispatch</h3>
      <p>ISPM 15 heat treatment and IPPC stamping are completed, with container stowage and dispatch coordinated to project timelines.</p>
    </div>
  </div>
</div></section>
""" + cta_band(rel, "Share Your Drawings or Requirements",
               "Tell us about your product, packaging requirements and shipment destination. We will review your inquiry and follow up regarding the next steps.")
    return page(rel, "capabilities", "Wood Packaging Manufacturing Capabilities",
                "Wood packaging manufacturing capabilities in Qingdao, China: custom crates, wood processing, knock-down kits, quality inspection and export preparation.", body)

# ================= ABOUT US =================
def build_about():
    rel = "../"
    phase1_steps = [
        ("01", "Requirement Review",
         "Confirming equipment dimensions, weight, handling methods, shipment routes and destination requirements.",
         "Scope &amp; transport conditions checklist", "➔"),
        ("02", "Drawing &amp; Specification Review",
         "Reviewing customer drawings and technical specifications to establish manufacturing parameters.",
         "CAD validation &amp; joint tolerances", "➔"),
        ("03", "Material &amp; Process Planning",
         "Selecting suitable timber, plywood, fasteners, protective liners and production schedules.",
         "Lumber cutting bill &amp; batch schedule", "➔"),
    ]
    phase2_steps = [
        ("04", "Manufacturing &amp; Assembly",
         "Precision cutting, panel processing, framing and component assembly according to verified drawings.",
         "CNC sawing &amp; framing prefabrication", "➔"),
        ("05", "Quality Inspection",
         "Verifying dimensional accuracy, fastener placement, structural strength and IPPC mark clarity.",
         "Dimensional checks &amp; in-process QA records", "➔"),
    ]
    phase3_steps = [
        ("06", "Packing &amp; Shipment Preparation",
         "Protective wrapping, labeling, export documentation coordination and container loading preparation.",
         "ISPM 15 treatment &amp; container staging", "➔"),
        ("07", "Delivery Coordination",
         "Coordinating dispatch and logistics handover according to agreed project schedules.",
         "Carrier handover &amp; dispatch fulfillment", "✓"),
    ]

    all_steps = [
        ("01", "Requirement Review", "Dimensions & Load"),
        ("02", "Drawing Review", "CAD & Tolerances"),
        ("03", "Process Planning", "Materials & Schedule"),
        ("04", "Fabrication", "Cutting & Assembly"),
        ("05", "Quality QA", "In-Process Verification"),
        ("06", "Packing Prep", "ISPM 15 & Packing"),
        ("07", "Delivery", "Dispatch & Handover"),
    ]

    pipeline_steps = "\n".join(
        f'''    <div class="pipeline-step">
      <div class="p-num">{n}</div>
      <div class="p-title">{t}</div>
      <div class="p-sub">{sub}</div>
    </div>'''
        for n, t, sub in all_steps)

    def render_phase_cards(cards):
        out = []
        for n, t, d, deliverable, arrow in cards:
            arrow_cls = "step-arrow done" if arrow == "✓" else "step-arrow"
            out.append(f'''      <div class="flow-step-card reveal">
        <div class="card-head">
          <span class="step-num">{n}</span>
          <span class="{arrow_cls}">{arrow}</span>
        </div>
        <h4>{t}</h4>
        <p>{d}</p>
        <div class="card-deliverable">{deliverable}</div>
      </div>''')
        return "\n".join(out)

    p1_html = render_phase_cards(phase1_steps)
    p2_html = render_phase_cards(phase2_steps)
    p3_html = render_phase_cards(phase3_steps)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / About Us</div>
  <h1>About Qingdao Lumber &amp; Packaging</h1>
  <p class="lead">Custom wood packaging manufacturing and repeat OEM program support in Qingdao, China.</p>
</div></div>

<section><div class="wrap" style="max-width:960px">
  <div class="reveal" style="font-size:1.1rem;line-height:1.75">
    <p>Qingdao Lumber &amp; Packaging supports industrial customers with custom wood packaging and OEM manufacturing in China.</p>
    <p style="margin-top:16px">We work with customer drawings, product specifications and shipping requirements to produce packaging for industrial equipment and export shipments. Our focus is on practical manufacturing, consistent production and responsive project coordination.</p>
    <p style="margin-top:16px">As part of a broader business network, we work to support customer requirements through clear communication and long-term supply relationships.</p>
  </div>
</div></section>

<section style="padding:0 0 64px"><div class="wrap">
  <div class="grid g2" style="gap:32px">
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-factory-aerial.webp" alt="Qingdao Lumber &amp; Packaging manufacturing facility in Jimo, Qingdao" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">PRODUCTION FACILITY</span>
        <h3>Jimo Production Base · Qingdao</h3>
        <p>Dedicated wood packaging manufacturing facility in Jimo, Qingdao, equipped with automated cutting lines, CNC routing equipment, component assembly bays, and certified ISPM 15 heat treatment kilns.</p>
        <ul class="check-list" style="margin-top:14px">
          <li>Automated panel saws and CNC precision routing equipment</li>
          <li>Certified heat treatment kilns for export compliance</li>
          <li>Dedicated assembly and container staging areas</li>
        </ul>
        <div class="tag-row">
          <span>Wood Processing</span>
          <span>Assembly Bays</span>
          <span>ISPM 15 Treatment</span>
        </div>
      </div>
    </div>
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-team-group.webp" alt="Qingdao Lumber &amp; Packaging production and project team group photo" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">OPERATIONS &amp; PROJECT SUPPORT</span>
        <h3>Manufacturing &amp; Project Team</h3>
        <p>Experienced production staff, machine operators, quality inspectors and project coordinators focused on technical drawing compliance, consistent fabrication and responsive customer communication.</p>
        <ul class="check-list" style="margin-top:14px">
          <li>Technical drawing and specification review</li>
          <li>In-process quality inspection across production stages</li>
          <li>Export packaging documentation and logistics coordination</li>
        </ul>
        <div class="tag-row">
          <span>Drawing Review</span>
          <span>Quality Inspection</span>
          <span>Project Support</span>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div style="text-align:center;max-width:820px;margin:0 auto">
    <span class="kicker">END-TO-END PROCESS CONTROL</span>
    <h2 class="section-title reveal">Manufacturing &amp; Project Workflow</h2>
    <p class="section-sub reveal">A structured 7-stage flowchart ensuring drawing compliance, batch consistency, and export readiness from inquiry to delivery.</p>
  </div>

  <div class="flowchart-wrap">
    <!-- Visual Pipeline Diagram -->
    <div class="pipeline-track reveal">
{pipeline_steps}
    </div>

    <!-- Phase 1: Engineering & Planning -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">PHASE 1</span>
        <h3>Project Engineering &amp; Review</h3>
      </div>
      <div class="flow-cards-row c3">
{p1_html}
      </div>
    </div>

    <!-- Phase 2: Manufacturing & Quality -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">PHASE 2</span>
        <h3>Fabrication &amp; Quality Control</h3>
      </div>
      <div class="flow-cards-row c2">
{p2_html}
      </div>
    </div>

    <!-- Phase 3: Export & Logistics -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">PHASE 3</span>
        <h3>Export Packaging &amp; Logistics</h3>
      </div>
      <div class="flow-cards-row c2">
{p3_html}
      </div>
    </div>
  </div>
</div></section>
""" + cta_band(rel, "Work With an OEM Packaging Partner",
               "Tell us about your product, packaging requirements and shipment destination. We will review your inquiry and follow up regarding the next steps.")
    return page(rel, "about", "About Qingdao Lumber & Packaging",
                "Qingdao Lumber & Packaging supports industrial customers with custom wood packaging, precision components and OEM manufacturing in China.", body)

# ================= APPLICATIONS (CASE STUDIES) =================
def build_applications():
    rel = "../"
    cases = [
        ("Server &amp; Data Center Equipment",
         "Export and domestic shipping of rack servers, computing clusters and high-value electronics.",
         "Vibration cushioning, internal stability during multi-modal transit, and ramp access for safe uncrating.",
         "Custom timber frame with shock-mitigating foam inserts and integrated entry ramp.",
         "Tailored wooden crates supplied per project batch schedules.",
         "case-data-server.webp", "Tall wooden server crate with caution markings"),

        ("High-Voltage Insulators",
         "Bulk international shipment of fragile glass, ceramic and porcelain insulator discs.",
         "Separation between components, impact mitigation, and heavy stacking strength during sea freight.",
         "Compartmentalized crate structure with protective dividers preventing component-to-component contact.",
         "Reinforced export crates configured for containerized ocean transit.",
         "case-glass-insulator.webp", "Wooden crates packed with stacked glass insulators"),

        ("Industrial Machinery",
         "Capital equipment transport including machine tools, industrial printers, pumps and compressors.",
         "High load-bearing capacity, forklift access, and structural rigidity for irregular centers of gravity.",
         "Heavy-duty hardwood skids, reinforced corner framing, and customized internal blocking.",
         "Custom-engineered machinery crates manufactured to equipment weight and dimensions.",
         "case-industrial-printer.webp", "Custom wooden crate for industrial printer equipment"),

        ("Energy Equipment",
         "Battery enclosures, EV charging stations, transformers and electrical distribution units.",
         "Secure base anchoring, moisture barrier protection, and compliance with destination transport requirements.",
         "Engineered base framing with weather barrier wrap and bolted internal tie-down brackets.",
         "Project-specific crates configured according to product dimensions and transport mode.",
         "case-ev-charging.webp", "Wooden crate housing energy equipment"),

        ("Knock-Down Packaging Kits",
         "Recurring OEM equipment manufacturing requiring space-efficient component supply.",
         "Compact shipping volume before assembly and quick, standardized assembly at destination facility.",
         "Pre-drilled plywood and timber panels with metal corner brackets for flat-pack transport.",
         "Flat-pack KD kits delivered in bulk, designed to reduce shipping volume where suitable.",
         "case-server-rack-kd.webp", "Flat-pack server rack kit with metal corner brackets"),

        ("Custom Export Crating",
         "International break-bulk and containerized cargo requiring certified wood packaging.",
         "Full ISPM 15 compliance, IPPC stamps, durable transit protection under rough sea conditions.",
         "Heat-treated solid lumber and plywood construction with weather-resistant internal liners.",
         "Export-ready wooden crates delivered with required phytosanitary treatment marks.",
         "case-relocation-liftvan.webp", "Export wooden crates ready for shipping"),
    ]

    def case_card(title, bg, req, config, scope, img, alt):
        return f"""
    <div class="card reveal"><div class="ph portrait"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd">
        <span class="kicker">Application Example</span>
        <h3 style="margin-bottom:10px">{title}</h3>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>Context:</strong> {bg}</p>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>Packaging Requirements:</strong> {req}</p>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>Configuration:</strong> {config}</p>
        <p style="font-size:.9rem;color:var(--muted)"><strong>Delivered Scope:</strong> {scope}</p>
      </div></div>"""

    cards = "\n".join(case_card(*c) for c in cases)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / Applications</div>
  <h1>Packaging Applications</h1>
  <p class="lead">Examples of wood packaging applications across industrial and technology sectors. Each configuration is adapted to the product, handling method and shipping requirements.</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">Application Examples Across Sectors</h2>
  <p class="section-sub reveal">A representative overview of wood packaging configurations developed to customer specifications.</p>
  <div class="grid g3">{cards}
  </div>
</div></section>

<section id="rfq"><div class="wrap">
  <h2 class="section-title reveal">Request a Wood Packaging Quote</h2>
  <p class="section-sub reveal">Tell us about your product, packaging requirements and shipment destination. Drawings, dimensions, weight and estimated quantities will help us review your request.</p>
  <form class="rfq reveal" id="rfqForm" novalidate>
    <div class="form-grid">
      <div class="field"><label for="fName">Full Name *</label><input id="fName" name="full_name" type="text" autocomplete="name" required><span class="err"></span></div>
      <div class="field"><label for="fEmail">Business Email *</label><input id="fEmail" name="email" type="email" autocomplete="email" required><span class="err"></span></div>
      <div class="field"><label for="fCompany">Company *</label><input id="fCompany" name="company" type="text" autocomplete="organization" required><span class="err"></span></div>
      <div class="field"><label for="fCountry">Country / Region *</label><input id="fCountry" name="country" type="text" autocomplete="country-name" required><span class="err"></span></div>
      <div class="field"><label for="fDimensions">Dimensions &amp; Weight (Optional)</label><input id="fDimensions" name="dimensions_weight" type="text" placeholder="e.g. 1200 x 800 x 1000 mm, 450 kg"></div>
      <div class="field"><label for="fQuantity">Estimated Quantity (Optional)</label><input id="fQuantity" name="quantity" type="text" placeholder="e.g. 50 units / month or batch total"></div>
      <div class="field full"><label for="fDestination">Shipping Destination (Optional)</label><input id="fDestination" name="destination" type="text" placeholder="e.g. Port of Los Angeles, USA / Rotterdam, Netherlands"></div>
      <div class="field full"><label for="fNeed">Product &amp; Packaging Requirements *</label><textarea id="fNeed" name="requirements" rows="5" placeholder="Describe your product, handling requirements, drawings availability, or specific packaging standards..." required></textarea><span class="err"></span></div>
    </div>
    <div style="margin-top:22px;text-align:center">
      <button class="btn btn-green" type="submit" style="min-width:220px">Submit Inquiry</button>
    </div>
    <div class="form-note" id="formNote" role="status"></div>
    <p style="margin-top:14px;font-size:.9rem;color:var(--g700);text-align:center;font-weight:500">We will review your inquiry and follow up regarding the next steps.</p>
    <p style="margin-top:8px;font-size:.85rem;color:var(--muted);text-align:center">Prefer email? Write to <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="{WA_LINK}" target="_blank" rel="noopener">chat on WhatsApp</a>.</p>
  </form>
</div></section>
"""
    return page(rel, "applications", "Industrial Wood Packaging Applications",
                "Examples of wood packaging applications across servers, insulators, industrial machinery and energy equipment, with custom RFQ inquiry form.", body)

# ================= INDUSTRY PAGES =================
INDUSTRY_FEATURE_IMAGES = {
    "data-servers-precision-electronics": ("case-data-server.webp", "Custom wooden crate designed for servers and electronics"),
    "ev-battery-charging": ("solutions-battery-crates.webp", "Custom wooden crate for battery packs and charging equipment"),
    "industrial-machinery-infrastructure": ("case-industrial-printer.webp", "Engineered wooden crate for industrial machinery"),
    "high-voltage-insulators-power-transmission": ("case-glass-insulator.webp", "Reinforced wooden crates for high-voltage glass and ceramic insulators"),
}

def industry_page(slug, short, h1, title, desc, intro_paras, approach, solutions, challenges, scope, objective):
    rel = "../../"
    paras = "\n".join(f"    <p style=\"margin-top:14px\">{p}</p>" for p in intro_paras)
    sol = "\n".join(f"      <li>{s}</li>" for s in solutions)
    cha = "\n".join(f"      <li>{c}</li>" for c in challenges)
    sco = "\n".join(f"      <li>{s}</li>" for s in scope)
    wa_text = quote(f"Hello Qingdao Lumber, I would like to discuss packaging for {short}.")
    img_fn, img_alt = INDUSTRY_FEATURE_IMAGES.get(slug, ("knockdown-kits-flatpack.webp", short))
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}">Home</a> / <a href="{rel}industries/data-servers-precision-electronics/">Industries</a> / {short}</div>
  <h1>{h1}</h1>
  <p class="lead">{objective}</p>
</div></div>

<section><div class="wrap">
  <div class="split reveal" style="margin-bottom:20px">
    <div class="ph"><img src="{rel}assets/img/{img_fn}" alt="{img_alt}" loading="lazy"></div>
    <div class="split-content">
      <span class="kicker">Industry Packaging Overview</span>
      <h3 style="margin-bottom:14px">{short}</h3>
      {paras}
      <div class="split-meta"><span>Compliance &amp; Export:</span> ISPM 15 Treatment Support · Configured to Transport Requirements</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap" style="max-width:960px">
  <h2 class="section-title reveal">Packaging Configuration &amp; Features</h2>
  <p class="section-sub reveal">{approach}</p>
  <h3 class="reveal" style="margin:34px 0 6px">Key Packaging Features</h3>
  <ul class="check-list reveal">{sol}</ul>
</div></section>

<section><div class="wrap" style="max-width:960px">
  <div class="grid g2">
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">Shipping Requirements Addressed</h3>
      <ul class="check-list">{cha}</ul></div>
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">Typical Applications</h3>
      <ul class="check-list">{sco}</ul></div>
  </div>
</div></section>
"""
    cta = f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>Discuss Your {short} Packaging Requirements</h2>
  <p>Tell us about your equipment dimensions, weight and shipping destination. We will review your inquiry and follow up regarding the next steps.</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}applications/#rfq">Request a Quote</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={wa_text}" target="_blank" rel="noopener">Chat on WhatsApp</a>
  </div>
</div></section>"""
    return page(rel, "industries/" + slug, title, desc, body + cta)

def build_industries():
    pages = {}

    pages["data-servers-precision-electronics"] = industry_page(
        "data-servers-precision-electronics", "Servers & Precision Electronics",
        "Wood Packaging for Servers & Precision Electronics",
        "Server & Data Center Wooden Crates",
        "Custom wooden crating for servers, racks, storage systems and sensitive electronic equipment, with internal supports and cushioning configured to the product and shipping requirements.",
        ["Data servers, storage arrays, telecommunications racks and sensitive electronic systems require stable protection against transit shock, vibration and moisture during international shipment.",
         "Packaging configurations must provide consistent fit across batch deliveries, accommodating equipment dimensions, rack-mount rails, and convenient unloading at destination facilities."],
        "Custom wooden crating for servers, racks, storage systems and sensitive electronic equipment, with internal supports and cushioning configured to the product and shipping requirements.",
        ["Custom-dimensioned wooden crates built for rackmount servers, power modules and electronics",
         "Internal cushioning and foam inserts configured according to product weight and sensitivity",
         "Anti-static liners and moisture barrier foil packaging available based on project needs",
         "Integrated ramp options on tall crates for convenient uncrating and equipment rollout",
         "Heat-treated solid lumber in accordance with ISPM 15 standards for export shipments"],
        ["Mitigating vibration and transit shock during road, sea and air transport",
         "Configuring internal padding to avoid contact on sensitive bezel surfaces or connector ports",
         "Facilitating convenient site uncrating without requiring specialized heavy machinery",
         "Maintaining consistent dimensions across repeat OEM deliveries"],
        ["Rack-mounted servers and compute nodes",
         "Data storage arrays and drive enclosures",
         "Network switches and telecommunications cabinets",
         "Power distribution units (PDUs) and uninterruptible power supplies (UPS)",
         "High-value industrial automation controllers"],
        "Custom wooden crating for servers, racks, storage systems and sensitive electronic equipment, with internal supports and cushioning configured to the product and shipping requirements.")

    pages["ev-battery-charging"] = industry_page(
        "ev-battery-charging", "Battery & Charging Equipment",
        "Wood Packaging for Battery & Charging Equipment",
        "Battery & Charging Equipment Packaging",
        "Custom packaging for battery packs, charging stations and related equipment, with structural support and protective features specified according to the product and applicable transport requirements.",
        ["Lithium battery packs, energy storage enclosures and high-power charging stations present distinct packaging demands related to heavy unit weight, structural stability and transport compliance.",
         "Packaging designs must incorporate substantial load-bearing skids, secure hold-down anchoring, and internal insulation features configured to the specific equipment model and shipping route."],
        "Custom packaging for battery packs, charging stations and related equipment, with structural support and protective features specified according to the product and applicable transport requirements.",
        ["Reinforced heavy-duty bases designed to support high concentrated weight",
         "Internal wooden blocking and non-conductive cushioning to secure components in position",
         "Heavy-duty crate framing with bolted access panels for straightforward loading and unloading",
         "Packaging structures configured to support project-specific transport standards and carrier guidelines",
         "ISPM 15 compliant heat treatment for all solid wood materials used in export shipments"],
        ["Accommodating heavy, concentrated loads with reinforced skid bases and lifting points",
         "Securing large charging cabinets against lateral tipping during vessel movement",
         "Protecting powder-coated surfaces, digital display screens and charging cables during transit",
         "Supporting project-specific dangerous goods documentation and carrier handling criteria"],
        ["Lithium-ion battery packs and module assemblies",
         "Commercial vehicle and industrial battery units",
         "DC fast charging stations and power conversion cabinets",
         "AC wallboxes and commercial charging pedestals",
         "Energy storage system (ESS) sub-assemblies"],
        "Custom packaging for battery packs, charging stations and related equipment, with structural support and protective features specified according to the product and applicable transport requirements.")

    pages["industrial-machinery-infrastructure"] = industry_page(
        "industrial-machinery-infrastructure", "Industrial Machinery & Infrastructure",
        "Wood Packaging for Industrial Machinery",
        "Industrial Machinery Wooden Crates",
        "Heavy-duty wooden crates and bases tailored to machinery dimensions, weight, lifting points and shipping conditions.",
        ["Industrial machine tools, heavy rotating equipment, pumps and power infrastructure components are capital-intensive assets requiring robust mechanical protection.",
         "Packaging must withstand multi-modal shipping, heavy lifting by crane or forklift, and outdoor staging while preventing shifting or structural distortion during transit."],
        "Heavy-duty wooden crates and bases tailored to machinery dimensions, weight, lifting points and shipping conditions.",
        ["High-capacity timber skids engineered for forklift handling and crane rigging",
         "Custom internal blocking, tie-down brackets and bracing aligned with equipment anchoring points",
         "Full wooden sheathing or open-slat framing options based on transport route and protection needs",
         "Moisture barrier bags, desiccants and rust-inhibiting VCI film configured for ocean voyages",
         "Certified ISPM 15 heat treatment and visible IPPC stamps on exterior framing"],
        ["Securing machinery with offset centers of gravity and irregular mounting footprints",
         "Preventing mechanical distortion, surface abrasion and component shifting under dynamic shipping loads",
         "Providing clearly marked lifting points and forklift pockets for safe site handling",
         "Protecting bare metal components against saltwater air and moisture during long sea transits"],
        ["CNC machine tools and sheet metal processing equipment",
         "Industrial pumps, compressors and hydraulic power units",
         "Electric motors, generators and distribution transformers",
         "Mining, construction and heavy material handling assemblies",
         "Valves, actuators and pipeline infrastructure components"],
        "Heavy-duty wooden crates and bases tailored to machinery dimensions, weight, lifting points and shipping conditions.")

    pages["high-voltage-insulators-power-transmission"] = industry_page(
        "high-voltage-insulators-power-transmission", "Insulators & Power Equipment",
        "Wood Packaging for Insulators & Power Equipment",
        "Wooden Crates for Electrical Insulators",
        "Custom crates for glass, ceramic and porcelain insulators, with internal separation, support and cushioning configured to help reduce impact damage during handling and transport.",
        ["High-voltage glass, ceramic and composite insulators are inherently brittle components that require specialized protection during bulk handling, sea freight and overland delivery.",
         "Even minor chipping or hairline cracks can compromise electrical insulation performance. Packaging must isolate individual units, absorb transit shocks and support high-density container stacking."],
        "Custom crates for glass, ceramic and porcelain insulators, with internal separation, support and cushioning configured to help reduce impact damage during handling and transport.",
        ["Compartmentalized wooden crate frames with custom internal dividers to prevent insulator contact",
         "Layered cushioning and shock-absorbing inserts configured for fragile porcelain and glass sheds",
         "Rigid exterior frames engineered to withstand multi-tier stacking inside ocean containers",
         "Ventilated framing configurations to minimize internal condensation during ocean transit",
         "ISPM 15 certified solid wood materials with official IPPC markings for international delivery"],
        ["Preventing chipping, surface cracking and breakage of brittle insulator bodies during transit",
         "Isolating stacked discs so individual units do not transmit point loads to adjacent components",
         "Ensuring rigid crate dimensions that stack securely without crushing lower tiers in container transit",
         "Facilitating straightforward unloading and inventory counting at utility project staging yards"],
        ["High-voltage porcelain suspension and station post insulators",
         "Toughened glass insulator strings and disc units",
         "Composite and silicone rubber high-voltage insulators",
         "Transformer bushings and high-voltage surge arresters",
         "Substation electrical switchgear accessories"],
        "Custom crates for glass, ceramic and porcelain insulators, with internal separation, support and cushioning configured to help reduce impact damage during handling and transport.")

    return pages

# ================= SEO FILES =================
def build_seo():
    urls = ["", "solutions/", "capabilities/", "about/", "applications/"] + \
           ["industries/" + s + "/" for s, _, _ in INDUSTRIES]
    zh_urls = ["zh/", "zh/solutions/", "zh/capabilities/", "zh/about/", "zh/applications/"] + \
              ["zh/industries/" + s + "/" for s, _, _ in INDUSTRIES]
    all_urls = urls + zh_urls
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in all_urls:
        sm.append(f"  <url><loc>{CANON}/{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u in ('', 'zh/') else '0.8'}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {CANON}/sitemap.xml\n")

# ================= LEGACY REDIRECTS =================
def build_redirects():
    redirects = [
        ("home/index.html", f"{CANON}/"),
        ("2/index.html", f"{CANON}/capabilities/"),
        ("3/index.html", f"{CANON}/about/"),
        ("case-study/index.html", f"{CANON}/applications/"),
        ("case-study-more/index.html", f"{CANON}/applications/"),
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
    print("--- Building English Site ---")
    write("index.html", build_home())
    write("solutions/index.html", build_solutions())
    write("capabilities/index.html", build_capabilities())
    write("about/index.html", build_about())
    write("applications/index.html", build_applications())
    # Keep case-studies/ accessible with identical content as well
    write("case-studies/index.html", build_applications())

    for slug, html in build_industries().items():
        write(f"industries/{slug}/index.html", html)
    build_redirects()

    # Generate Chinese Site
    try:
        import zh_site
        zh_site.generate_chinese_site()
    except Exception as e:
        print("Error generating Chinese site:", e)

    build_seo()
    print("done.")

if __name__ == "__main__":
    main()
