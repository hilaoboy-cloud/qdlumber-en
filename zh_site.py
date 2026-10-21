#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the authentic Chinese version of Qingdao Lumber & Packaging (青岛拉博尔包装).
"""
import os, json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))
ZH_OUT = os.path.join(OUT, "zh")
CANON = "https://en.qdlumber.com"
WA_LINK = "https://wa.me/8613405101358"
EMAIL = "evan.chen@qdlumberco.com"

FACTORY_ZH = ("中国·青岛市即墨开发区华宇路1号",
              "+86 186 0261 9997", "Steven.Sung@qdlumberco.com")
OFFICE_ZH = ("中国·青岛市市南区香港中路40号旗舰大厦1805室",
             "+86 134 0510 1358", "evan.chen@qdlumberco.com")

INDUSTRIES_ZH = [
    ("data-servers-precision-electronics", "数据中心服务器与精密电子",
     "为服务器、机柜、存储系统及精密电子设备提供定制木箱，并根据产品特点与运输要求配置内部支撑和缓冲结构。"),
    ("ev-battery-charging", "新能源电池与充电设备",
     "为电池包、充电设备及相关产品提供定制包装，根据产品特点及适用的运输要求确定承载结构和防护配置。"),
    ("industrial-machinery-infrastructure", "工业机械与基础设施设备",
     "根据设备尺寸、重量、吊装位置及运输条件，为工业机械提供定制重型木箱与木质底座。"),
    ("high-voltage-insulators-power-transmission", "高压绝缘子与输配电设备",
     "为玻璃、陶瓷及瓷质绝缘子提供定制木箱，根据产品形状和易损部位配置内部隔离、支撑与缓冲结构，降低装卸和运输过程中的碰损风险。"),
]

WA_FILE = os.path.join(OUT, "assets", "whatsapp-float-button.html")
if os.path.exists(WA_FILE):
    with open(WA_FILE, encoding="utf-8") as f:
        WA_CODE = f.read()
else:
    WA_CODE = ""

ORG_JSONLD_ZH = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "青岛拉博尔包装设备有限公司",
    "alternateName": "Qingdao Lumber & Packaging Co., Ltd.",
    "url": CANON + "/zh/",
    "logo": CANON + "/assets/img/logo.webp",
    "description": "面向工业供应链的定制木质包装制造商，按客户图纸与要求提供木箱、木托盘、木质底座及拆装式包装套件 OEM 制造服务。",
    "contactPoint": [{
        "@type": "ContactPoint", "telephone": "+86-134-0510-1358",
        "email": EMAIL, "contactType": "sales", "areaServed": "Worldwide"
    }],
    "address": {"@type": "PostalAddress", "streetAddress": OFFICE_ZH[0],
                "addressLocality": "青岛", "addressRegion": "山东", "addressCountry": "CN"},
}

def head_zh(rel, slug, title, desc, extra=""):
    canon = CANON + "/zh/" + (slug + "/" if slug else "")
    en_url = CANON + ("/" if not slug else "/" + slug + "/")
    home_preloads = ""
    if slug == "":
        home_preloads = f"""<link rel="preconnect" href="https://player.vimeo.com">
<link rel="preconnect" href="https://f.vimeocdn.com">
<link rel="preconnect" href="https://i.vimeocdn.com">
<link rel="dns-prefetch" href="https://player.vimeo.com">
<link rel="preload" as="image" href="{rel}assets/img/hero-poster.webp">"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="zh" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
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
<script type="application/ld+json">{json.dumps(ORG_JSONLD_ZH, ensure_ascii=False)}</script>
{extra}</head>"""

def header_zh(rel, slug=""):
    ind_links = "\n".join(
        f'<a href="{rel}zh/industries/{s}/">{n}</a>' for s, n, _ in INDUSTRIES_ZH)
    en_target = f"{rel}{slug + '/' if slug else ''}"
    return f"""<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{rel}zh/" aria-label="青岛拉博尔包装 — 首页">
      <img src="{rel}assets/img/logo.webp" alt="青岛拉博尔包装" width="259" height="98"></a>
    <button class="burger" id="burger" aria-label="导航菜单"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="mainNav">
      <a class="nav-link" data-nav="home" href="{rel}zh/">首页</a>
      <a class="nav-link" data-nav="solutions" href="{rel}zh/solutions/">包装解决方案</a>
      <a class="nav-link" data-nav="capabilities" href="{rel}zh/capabilities/">制造能力</a>
      <a class="nav-link" data-nav="about" href="{rel}zh/about/">关于我们</a>
      <a class="nav-link" data-nav="applications" href="{rel}zh/applications/">包装应用</a>
      <span class="has-drop"><a class="nav-link" data-nav="industries" href="{rel}zh/industries/data-servers-precision-electronics/">服务行业 ▾</a>
        <span class="drop">{ind_links}</span></span>
      <a class="nav-cta" href="{rel}zh/applications/#rfq">获取报价</a>
      <a class="lang-flag-toggle" href="{en_target}" title="Switch to English" aria-label="切换至英文版">
        <img src="{rel}assets/img/flag-us.svg" alt="English" width="26" height="19.5" class="flag-icon">
      </a>
    </nav>
  </div>
</header>"""

def footer_zh(rel):
    ind_links = "\n".join(
        f"<li><a href=\"{rel}zh/industries/{s}/\">{n}</a></li>" for s, n, _ in INDUSTRIES_ZH)
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="{rel}assets/img/logo-footer.webp" alt="青岛拉博尔包装" width="200" height="75">
      <p>青岛拉博尔包装面向工业客户提供定制木箱、木托盘、木质底座及拆装式木箱套件，服务工业设备与全球出口供应链。</p>
      <div class="social-row">
        <a class="s-li" href="https://www.linkedin.com/company/qdlumber/" aria-label="领英 LinkedIn" target="_blank" rel="noopener"><svg width="15" height="15" viewBox="0 0 448 512" fill="currentColor" aria-hidden="true"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.3 0-55.7 37.7-55.7 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.7-48.3 87.9-48.3 94 0 111.3 61.9 111.3 142.3V448z"/></svg></a>
        <a class="s-yt" href="https://www.youtube.com/@QingdaoLumberPackaging" aria-label="YouTube 官方视频" target="_blank" rel="noopener"><svg width="17" height="17" viewBox="0 0 576 512" fill="currentColor" aria-hidden="true"><path d="M549.655 124.083c-6.281-23.65-24.787-42.156-48.437-48.437C458.54 64 288 64 288 64S117.46 64 74.782 75.646c-23.65 6.281-42.156 24.787-48.437 48.437C14.7 166.762 14.7 256 14.7 256s0 89.238 11.645 131.917c6.281 23.65 24.787 42.156 48.437 48.437C117.46 448 288 448 288 448s170.54 0 213.218-11.646c23.65-6.281 42.156-24.787 48.437-48.437C561.3 345.238 561.3 256 561.3 256s0-89.238-11.645-131.917zM232 336V176l144 80-144 80z"/></svg></a>
        <a class="s-wa" href="{WA_LINK}" aria-label="WhatsApp 即时咨询" target="_blank" rel="noopener"><svg width="16" height="16" viewBox="0 0 448 512" fill="currentColor" aria-hidden="true"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg></a>
      </div>
    </div>
    <div>
      <h4>快速导航</h4>
      <ul>
        <li><a href="{rel}zh/">首页</a></li>
        <li><a href="{rel}zh/solutions/">包装解决方案</a></li>
        <li><a href="{rel}zh/capabilities/">制造能力</a></li>
        <li><a href="{rel}zh/about/">关于我们</a></li>
        <li><a href="{rel}zh/applications/">包装应用</a></li>
        <li><a href="{rel}zh/applications/#rfq">获取报价</a></li>
      </ul>
    </div>
    <div>
      <h4>服务行业</h4>
      <ul>{ind_links}</ul>
    </div>
    <div>
      <h4>联系我们</h4>
      <div class="footer-contact-block">
        <strong>生产基地</strong>
        <span>{FACTORY_ZH[0]}</span><br>
        电话: <a href="tel:+8618602619997">{FACTORY_ZH[1]}</a><br>
        邮箱: <a href="mailto:{FACTORY_ZH[2]}">{FACTORY_ZH[2]}</a>
      </div>
      <div class="footer-contact-block" style="margin-top:10px">
        <strong>运营中心</strong>
        <span>{OFFICE_ZH[0]}</span><br>
        电话: <a href="tel:+8613405101358">{OFFICE_ZH[1]}</a><br>
        邮箱: <a href="mailto:{OFFICE_ZH[2]}">{OFFICE_ZH[2]}</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="yr">2026</span> 青岛拉博尔包装设备有限公司 保留所有权利。</span>
    <span>支持 ISPM 15 处理要求 · 出口木质包装制造</span>
  </div>
</footer>
{WA_CODE}
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def page_zh(rel, slug, title, desc, body, extra_head=""):
    return head_zh(rel, slug, title, desc, extra_head) + header_zh(rel, slug) + body + footer_zh(rel)

def write_zh(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote [ZH]", path, len(content), "bytes")

def cta_band_zh(rel, title, text):
    return f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>{title}</h2>
  <p>{text}</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}zh/applications/#rfq">获取报价</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={quote('您好，我想咨询木质包装与OEM定制需求。')}" target="_blank" rel="noopener">WhatsApp 在线沟通</a>
  </div>
</div></section>"""

# ================= HOME ZH =================
def build_home_zh():
    rel = "../"
    ind_cards = ""
    for s, n, d in INDUSTRIES_ZH:
        ind_cards += f"""
    <a class="tcard reveal" href="{rel}zh/industries/{s}/" style="display:block">
      <h3>{n}</h3><p>{d}</p>
      <p style="margin-top:12px;font-weight:700;color:var(--g600)">了解更多 →</p>
    </a>"""

    pillars = [
        ("按图纸与技术要求定制",
         "根据客户图纸、尺寸及项目要求生产木质包装。"),
        ("注重批次一致性",
         "通过明确的生产流程与检验要求，支持重复订单及稳定的批量交付。"),
        ("兼顾运输与装卸需求",
         "根据产品尺寸、装卸方式及运输要求，选择合适的包装结构。"),
        ("出口木质包装支持",
         "根据货物出运及目的地要求，落实适用的 ISPM 15 处理与标识要求。"),
    ]
    pillar_cards = "\n".join(
        f'''    <div class="tcard reveal"><h3 style="color:var(--g700);margin-bottom:8px">{t}</h3><p>{d}</p></div>'''
        for t, d in pillars)

    features = [
        ("values-precision.webp", "按图纸精准制造木质包装部件",
         "按图纸与技术要求定制",
         "根据客户提供的图纸、尺寸公差与承载要求，精准完成木箱、木托盘与底座加工。"),
        ("values-efficiency.webp", "排产协同与批量生产执行",
         "注重批次一致性",
         "成熟的木质包装制造流程与出厂检验，支持持续性 OEM 项目与批量稳定交付。"),
        ("values-accountability.webp", "出口木包装热处理与标识规范",
         "出口木质包装支持",
         "实木包装材料可严格按照国际植物检疫标准（ISPM 15）进行热处理并施加 IPPC 标识。"),
        ("values-partnership.webp", "项目团队对接客户包装需求",
         "长期 OEM 伙伴合作",
         "沟通清晰、响应迅速，根据客户供应链节奏提供持续、稳定的包装制造配套。"),
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
      <span class="hero-kicker">面向工业供应链的定制木质包装</span>
      <h1 class="hero-title">面向工业供应链的定制木质包装</h1>
      <p class="hero-sublead" style="font-weight:600;font-size:1.15rem;color:#e8f5e9;margin-bottom:12px">按客户图纸与要求提供 OEM 木质包装制造服务。</p>
      <p class="hero-lead">我们为工业设备及出口运输提供定制木箱、木托盘、木质底座及拆装式包装套件。从图纸对接到批量生产，我们注重尺寸匹配、批次一致性与实际运输需求。</p>
      <div class="hero-actions">
        <a class="btn btn-green" href="{rel}zh/applications/#rfq">获取报价</a>
        <a class="btn btn-ghost" href="{rel}zh/solutions/">了解包装方案</a>
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
  <h2 class="section-title reveal">围绕工业客户需求构建的制造服务</h2>
  <p class="section-sub reveal">专注工业设备木包装加工与出口配套，注重生产过程控制与持续稳定交付。</p>
  <div class="grid g4">{feature_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">注重生产过程控制与批次一致性</h2>
  <p class="section-sub reveal">从图纸审核、下料加工到装箱出运，各环节严格落实技术要求与检验规程。</p>
  <div class="grid g2" style="max-width:960px;margin:0 auto">
    <div class="tcard reveal"><h3>尺寸精准与部件匹配</h3><p>按照客户技术要求完成精准切割与预装配，注重部件匹配及组装稳固性，确保现场装配顺畅。</p></div>
    <div class="tcard reveal"><h3>兼顾运输与仓储空间</h3><p>提供拆装式木箱套件与平板化包装结构，在适用情况下减少运输与仓储占用空间，节约综合物流成本。</p></div>
    <div class="tcard reveal"><h3>规范的质量检验流程</h3><p>覆盖材料规格、含水率、紧固件牢固度、箱体尺寸及 IPPC 标识规范性检验，把控出厂质量。</p></div>
    <div class="tcard reveal"><h3>可靠的批量交付协同</h3><p>根据客户出运计划制定排产计划，配合集装箱装载与陆海运发货，保障项目节点准时交付。</p></div>
  </div>
</div></section>

<section><div class="wrap" style="text-align:center">
  <h2 class="section-title reveal">木材加工与装箱作业现场</h2>
  <p class="section-sub reveal">观看我们在青岛即墨基地的自动化下料锯切、部件预制、木箱组装与出运准备实况。</p>
  <div class="video-showcase reveal">
    <iframe src="https://www.youtube.com/embed/5F0zRgISQto?rel=0" title="青岛拉博尔包装制造实况" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">覆盖多个重点工业制造领域</h2>
  <p class="section-sub reveal">为服务器精密设备、新能源储能设施、大型工业机械及电网输变电设备提供匹配的木包装方案。</p>
  <div class="grid g2">{ind_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">主要产品类别</h2>
  <p class="section-sub reveal">定制木箱 · 拆装式木箱套件 · 木托盘与木质底座 · 服务器木箱 · 出口包装配套 — 按客户图纸加工制造。</p>
  <div style="text-align:center" class="reveal">
    <a class="btn btn-green" href="{rel}zh/solutions/">查看全部包装方案</a>
  </div>
</div></section>
""" + cta_band_zh(rel, "提交图纸或技术要求",
                  "请介绍您的产品、包装要求及出运目的地。我们将评估您的询价，并与您沟通后续事宜。")
    return page_zh(rel, "", "青岛拉博尔包装｜定制木质包装与 OEM 制造",
                   "青岛拉博尔包装面向工业供应链提供定制木箱、木托盘、木质底座及拆装式木箱套件 OEM 制造服务，注重尺寸匹配、批次一致性与出口运输需求。", body)

# ================= SOLUTIONS ZH =================
def build_solutions_zh():
    rel = "../../"
    faq_json = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "是否可以根据客户图纸或技术要求定制生产？",
             "acceptedAnswer": {"@type": "Answer", "text": "可以。我们严格依据客户提供的工程图纸、3D模型、尺寸公差及承重要求生产各类木箱、木托盘及木质底座。"}},
            {"@type": "Question", "name": "公司主要提供哪些类别的工业木质包装？",
             "acceptedAnswer": {"@type": "Answer", "text": "主要包括定制木箱、服务器木箱、拆装式木箱套件（KD）、重型木托盘与滑橇底座、木质加工件及内装防护辅料。"}},
            {"@type": "Question", "name": "发起包装询价需要提供哪些基础信息？",
             "acceptedAnswer": {"@type": "Answer", "text": "建议提供包装物外形尺寸、重量、吊运或叉装方式、出运目的地、预计订单批次，以及现有的技术图纸或草图。"}},
            {"@type": "Question", "name": "实木包装材料如何满足出口检疫要求？",
             "acceptedAnswer": {"@type": "Answer", "text": "适用的实木材料可严格执行 ISPM 15 国际植物检疫标准进行热处理，加施清晰规范的 IPPC 标识，并协助提供出口相关文件。"}},
            {"@type": "Question", "name": "拆装式木箱套件（KD）如何帮助降低运输成本？",
             "acceptedAnswer": {"@type": "Answer", "text": "拆装式木箱采用平板化出运，在适用情况下减少空箱运输与仓储占用空间，运抵目的地后可便捷组装使用。"}}
        ]}
    extra = f'\n<script type="application/ld+json">{json.dumps(faq_json, ensure_ascii=False)}</script>'

    products = [
        ("solutions-wood-elements.webp", "按图纸生产的工业重型木箱",
         "定制木箱", "根据客户图纸、尺寸及承载要求定制生产，适配重型设备与复杂外形。"),
        ("solutions-server-crates.webp", "带坡道的数据中心服务器木箱",
         "服务器木箱", "为服务器、机柜及数据中心设备配置的木箱包装，支持缓震与便捷装卸。"),
        ("solutions-battery-crates.webp", "拆装式平摊包装木箱套件",
         "拆装式木箱套件", "模块化平板运输木箱套件，便于集装箱运输，到货后可在现场便捷组装。"),
        ("solutions-plywood-panels.webp", "重型承载木托盘与滑橇底座",
         "木托盘与木质底座", "针对重型设备设计的承重底座与托盘，满足叉车、吊装搬运及运输稳定性要求。"),
        ("solutions-cnc-parts.webp", "规格木材与胶合板加工件",
         "木质加工件", "按客户技术规格精密加工的规格木方、胶合板裁切件及预钻孔装配辅件。"),
        ("case-ev-charging.webp", "箱内缓冲衬垫与防护包装辅料",
         "防护包装", "根据项目具体要求配置内部缓冲垫块、EVA/EPE泡沫、防潮铝箔袋及固定限位构件。"),
    ]
    product_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in products)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 包装解决方案</div>
  <h1>定制木质包装解决方案</h1>
  <p class="lead">我们为工业设备、出口运输及持续性 OEM 项目提供定制木质包装。根据产品尺寸、装卸要求、运输条件及现场组装需求，确定合适的包装方案。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">主要产品类别与包装形式</h2>
  <p class="section-sub reveal">从单套非标重型木箱到大批量拆装式包装套件，依据设备物理特性与物流场景提供匹配的结构。</p>
  <div class="grid g3">{product_cards}
  </div>

  <h2 class="section-title reveal" style="margin-top:56px">结构特点与出口配套</h2>
  <p class="section-sub reveal">注重受力分布、运输稳定性、空间利用与出口合规要求的实用结构方案。</p>

  <div class="split reveal" style="margin-bottom:32px">
    <div class="ph"><img src="{rel}assets/img/knockdown-kits-flatpack.webp" alt="平板堆叠的拆装式木箱套件" loading="lazy" width="800" height="450"></div>
    <div class="split-content">
      <span class="kicker">平板化出运结构</span>
      <h3>拆装式木箱套件（KD）</h3>
      <p><em>便于集装箱运输并在目的地现场快速装配的木箱包装系统。</em></p>
      <ul class="check-list">
        <li>在适用情况下减少运输与仓储占用空间，降低整箱空运及海运物流成本。</li>
        <li>预加工、预钻孔面板设计，注重部件匹配及组装稳固性，现场组装快捷可靠。</li>
        <li>适用于持续性设备批量出口、循环包装或需现场快速装箱的工业场景。</li>
      </ul>
      <div class="split-meta"><span>包装形态:</span> 平板化拆装套件 · 优化集装箱空间利用</div>
    </div>
  </div>

  <div class="split reveal" style="margin-bottom:32px">
    <div class="split-content">
      <span class="kicker">结构稳固性</span>
      <h3>结构加固与金属构件</h3>
      <p><em>根据重型设备承载与吊运要求，配置高强度木质主梁与金属加固件。</em></p>
      <ul class="check-list">
        <li>注重部件匹配及组装稳固性，在重点受力节点与转角处配置金属护角或加强角铁。</li>
        <li>底座配置重型滑橇、叉车进叉孔及起重吊装点，方便码头及现场安全装卸。</li>
        <li>金属构件可选镀锌或防锈喷涂等表面处理，适应海运高盐雾环境。</li>
      </ul>
      <div class="split-meta"><span>配件加固:</span> 高强度护角与起吊受力构件配套</div>
    </div>
    <div class="ph"><img src="{rel}assets/img/solutions-metal-components.webp" alt="工厂内起吊搬运木质构件" loading="lazy" width="800" height="450"></div>
  </div>

  <div class="split reveal">
    <div class="ph"><img src="{rel}assets/img/solutions-fastening-systems.webp" alt="木箱加固件与固定金属附件" loading="lazy" width="800" height="956"></div>
    <div class="split-content">
      <span class="kicker">出口合规支持</span>
      <h3>出口木包装准备与 ISPM 15 处理</h3>
      <p><em>严格落实实木材料热处理与标识规范，支持海运出口通关要求。</em></p>
      <ul class="check-list">
        <li>用于出口的适真实木材料经正规热处理，达到 ISPM 15 检疫处理要求。</li>
        <li>在箱体外部清晰加施官方认可的 IPPC 标识，便于海关及口岸快速核验。</li>
        <li>协助准备适用的出口文件并满足目的地国家对木质包装材料的植物检疫要求。</li>
      </ul>
      <div class="split-meta"><span>出口合规:</span> 支持 ISPM 15 热处理与 IPPC 标识规范</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">常见问题解答</h2>
  <p class="section-sub reveal">关于 OEM 制造、图纸对接、出口检疫与运输要求的常见咨询。</p>
  <div class="faq">
    <div class="faq-item reveal"><button class="faq-q">是否可以根据客户图纸或技术要求定制生产？</button><div class="faq-a"><p>可以。我们严格依据客户提供的工程图纸、3D模型、尺寸公差及承重要求生产各类木箱、木托盘及木质底座。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">公司主要提供哪些类别的工业木质包装？</button><div class="faq-a"><p>主要包括定制木箱、服务器木箱、拆装式木箱套件（KD）、重型木托盘与滑橇底座、木质加工件及内装防护辅料。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">发起包装询价需要提供哪些基础信息？</button><div class="faq-a"><p>建议提供包装物外形尺寸、重量、吊运或叉装方式、出运目的地、预计订单批次，以及现有的技术图纸或草图。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">实木包装材料如何满足出口检疫要求？</button><div class="faq-a"><p>适用的实木材料可严格执行 ISPM 15 国际植物检疫标准进行热处理，加施清晰规范的 IPPC 标识，并协助提供出口相关文件。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">拆装式木箱套件（KD）如何帮助降低运输成本？</button><div class="faq-a"><p>拆装式木箱采用平板化出运，在适用情况下减少空箱运输与仓储占用空间，运抵目的地后可便捷组装使用。</p></div></div>
  </div>
</div></section>
""" + cta_band_zh(rel, "提交图纸或技术要求",
                  "请介绍您的产品、包装要求及出运目的地。我们将评估您的询价，并与您沟通后续事宜。")
    return page_zh(rel, "solutions", "定制木箱与工业木质包装解决方案",
                   "为工业设备、出口运输及持续性 OEM 项目提供定制木质包装服务，涵盖定制木箱、拆装式木箱套件、木托盘底座及出口检疫合规支持。", body, extra)

# ================= CAPABILITIES ZH =================
def build_capabilities_zh():
    rel = "../../"
    gallery = [
        ("laser-cutting-machine.webp", "钣金激光切割加工设备"),
        ("cnc-router-plywood.webp", "数控雕刻机裁切胶合板板材"),
        ("press-brake-bending.webp", "数控折弯机加工金属连接件"),
        ("robotic-welding-arm.webp", "焊接机械臂加工转角结构件"),
        ("cnc-panel-saw.webp", "数控精密往复裁板锯开料"),
        ("punch-press-stamping.webp", "冲床加工五金冲压件"),
        ("powder-coating-line.webp", "金属构件表面喷塑涂装生产线"),
        ("dip-coating-line.webp", "金属配件表面防锈浸塑水箱"),
    ]
    figs = "\n".join(
        f'    <figure class="reveal"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy" width="400" height="300"></figure>'
        for fn, alt in gallery)

    sections = [
        ("定制生产", "capabilities-oem-engineering.webp", "展示内部结构的定制木箱箱体",
         "根据客户技术图纸、尺寸规格与承重指标，生产符合实际设备运输与防护要求的非标木质包装。"),
        ("木材加工", "capabilities-wood-metal.webp", "木构件精准锯切与钻孔加工",
         "拥有精密裁板锯、数控雕刻机及多轴钻孔设备，可加工实木板材、胶合板组件及预制榫槽配件。"),
        ("拆装式包装", "capabilities-knockdown-systems.webp", "平板化拆装式木箱套件堆放",
         "生产便于集装箱装载与集约化运输的平板拆装木箱套件，在适用情况下减少运费，目的地组装便捷。"),
        ("质量检验", "capabilities-quality-assurance.webp", "质检人员核对成品木箱技术规格",
         "建立规范的检验流程，对木材含水率、下料尺寸公差、紧固件排布、箱体方正度及 IPPC 标识逐项复核。"),
        ("出口包装准备", "capabilities-logistics-support.webp", "装载出口木箱入集装箱",
         "依据 ISPM 15 标准落实实木热处理，规范加施 IPPC 标识，并协助准备出口报关所需的木质包装证明材料。"),
        ("生产与出运协调", "values-efficiency.webp", "排产计划与出运装车调度",
         "做好订单批次排产、集装箱配载测算与承运调度，与客户物流计划无缝对接，保障稳定准时交付。"),
    ]
    sec_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for t, img, alt, d in sections)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 制造能力</div>
  <h1>制造能力</h1>
  <p class="lead">我们提供定制木质包装、按规格加工的木质部件及重复性 OEM 批量生产服务。具体加工工艺与技术要求根据项目需求确认。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">主要制造环节与配套能力</h2>
  <p class="section-sub reveal">从图纸审核、板材下料、组装加工到出厂检验与出口配套，注重执行质量与批次稳定性。</p>
  <div class="grid g3">{sec_cards}
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">加工制造设备与车间配置</h2>
  <p class="section-sub reveal">配备木材机械化锯切、数控雕刻加工及钣金构件配套设备，满足多样化包装箱体的制造需求。</p>
  <div class="gallery">{figs}
  </div>
</div></section>

<section><div class="wrap" style="max-width:960px">
  <h2 class="section-title reveal">项目对接与制造流程</h2>
  <p class="section-sub reveal">从前期技术要求确认到后期稳定批量交付的标准化作业步骤。</p>
  <div class="grid g2">
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">1. 需求与图纸审核</h3>
      <p>认真核对客户提供的设备图纸、CAD 尺寸及运输条件，明确选材要求、承载结构与出运目的地要求。</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">2. 材料与工艺规划</h3>
      <p>合理编制板材木方开料单、紧固件规格及内装衬垫清单，确保材料利用率与生产批次一致性。</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">3. 过程检验与组装</h3>
      <p>在下料、开槽、钻孔及组装各个环节落实公差检查，确保部件尺寸与受力结构符合规范。</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g700)">4. 出口检疫与出运配套</h3>
      <p>落实实木 ISPM 15 处理与 IPPC 标识，配合集装箱拼箱或整箱配载，协助办理出运所需文件。</p>
    </div>
  </div>
</div></section>
""" + cta_band_zh(rel, "提交图纸或技术要求",
                  "请介绍您的产品、包装要求及出运目的地。我们将评估您的询价，并与您沟通后续事宜。")
    return page_zh(rel, "capabilities", "木质包装制造能力",
                   "青岛拉博尔包装的制造能力：定制生产、木材加工、拆装式木箱套件、质量检验与出口包装配套服务。", body)

# ================= ABOUT ZH =================
def build_about_zh():
    rel = "../../"
    phase1_steps = [
        ("01", "需求确认",
         "与客户沟通包装设备尺寸、单重、重心位置、装卸方式及运输目的地等基础信息。",
         "产物输出：设备参数与出运工况清单", "➔"),
        ("02", "图纸审核",
         "审核客户提供的图纸与技术要求，确认材质要求、承载结构及接口配合尺寸。",
         "产物输出：CAD图纸公差复核与受力确认", "➔"),
        ("03", "工艺规划",
         "确定用木方、胶合板、紧固件及缓冲辅料清单，排定加工工艺与生产批次计划。",
         "产物输出：板材木方开料单与生产排期", "➔"),
    ]
    phase2_steps = [
        ("04", "生产组装",
         "按照图纸规格完成精确下料、锯切、开槽、钻孔及箱体框架预制组装。",
         "产物输出：数控精密切割与箱体构件预制", "➔"),
        ("05", "质量检验",
         "检查箱体尺寸公差、紧固连接牢固度、木材含水率及 IPPC 标识规范性。",
         "产物输出：尺寸公差复检与全工序质检记录", "➔"),
    ]
    phase3_steps = [
        ("06", "包装准备",
         "按要求配置防潮膜、缓冲衬垫，落实标识贴附及集装箱配载装载准备。",
         "产物输出：ISPM 15 热处理与集装箱配载装载", "➔"),
        ("07", "交付协调",
         "根据客户出运节点安排物流承运与现场交接，保障项目按计划准时推进。",
         "产物输出：物流承运交接与准时发运交付", "✓"),
    ]

    all_steps = [
        ("01", "需求确认", "尺寸与工况"),
        ("02", "图纸审核", "CAD公差复核"),
        ("03", "工艺规划", "开料与排产"),
        ("04", "生产组装", "精密切割预制"),
        ("05", "质量检验", "全工序质检"),
        ("06", "包装准备", "热处理与打包"),
        ("07", "交付协调", "准时发运交接"),
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
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 关于我们</div>
  <h1>关于青岛拉博尔包装</h1>
  <p class="lead">面向工业客户提供定制木质包装及 OEM 制造服务。</p>
</div></div>

<section><div class="wrap" style="max-width:960px">
  <div class="reveal" style="font-size:1.1rem;line-height:1.75">
    <p>青岛拉博尔包装面向工业客户，提供定制木质包装及 OEM 制造服务。</p>
    <p style="margin-top:16px">我们根据客户图纸、产品规格及运输要求，为工业设备和出口货物生产相应的木质包装。我们注重生产执行、批次一致性及及时的项目沟通与协调。</p>
    <p style="margin-top:16px">依托相关企业网络，我们通过清晰的沟通与长期供应合作，支持客户的包装需求。</p>
  </div>
</div></section>

<section style="padding:0 0 64px"><div class="wrap">
  <div class="grid g2" style="gap:32px">
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-factory-aerial.webp" alt="青岛拉博尔包装即墨生产制造基地" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">实体生产基地</span>
        <h3>即墨生产制造基地 · 青岛</h3>
        <p>位于青岛即墨的实体木包装制造基地，配备数控裁板锯、数控雕刻加工中心、木箱预装配工位及标准出口木材热处理烘干窑。</p>
        <ul class="check-list" style="margin-top:14px">
          <li>机械化精密锯切与数控木工加工工位</li>
          <li>正规合规的出口木材热处理烘房设施</li>
          <li>充足的室内组装车间与集装箱配载装卸区</li>
        </ul>
        <div class="tag-row">
          <span>实体制造</span>
          <span>数控木工</span>
          <span>ISPM 15 热处理</span>
        </div>
      </div>
    </div>
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-team-group.webp" alt="青岛拉博尔包装制造与项目执行团队合影" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">专业执行团队</span>
        <h3>制造与项目执行团队</h3>
        <p>经验丰富的木工技师、设备操作工、质检人员与外贸项目协调专员，注重技术图纸落地执行、质量把控与顺畅沟通。</p>
        <ul class="check-list" style="margin-top:14px">
          <li>严格依据客户图纸与技术标准生产</li>
          <li>落实全工序质量检验与尺寸复核</li>
          <li>支持多语言技术沟通与出口海运协调</li>
        </ul>
        <div class="tag-row">
          <span>图纸复核</span>
          <span>质量检验</span>
          <span>项目协同</span>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div style="text-align:center;max-width:820px;margin:0 auto">
    <span class="kicker">全流程受控执行</span>
    <h2 class="section-title reveal">制造与项目协作流程</h2>
    <p class="section-sub reveal">从图纸对接到出运交付的七个标准化协作阶段，确保图纸符合性、批次一致性与出口合规。</p>
  </div>

  <div class="flowchart-wrap">
    <!-- 顶层流程示意图 -->
    <div class="pipeline-track reveal">
{pipeline_steps}
    </div>

    <!-- Phase 1: Engineering & Planning -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">阶段一</span>
        <h3>前期规划与技术确认 · Engineering &amp; Review</h3>
      </div>
      <div class="flow-cards-row c3">
{p1_html}
      </div>
    </div>

    <!-- Phase 2: Manufacturing & Quality -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">阶段二</span>
        <h3>精益制造与品质核验 · Fabrication &amp; QA</h3>
      </div>
      <div class="flow-cards-row c2">
{p2_html}
      </div>
    </div>

    <!-- Phase 3: Export & Logistics -->
    <div class="flow-phase-block reveal">
      <div class="flow-phase-head">
        <span class="flow-phase-tag">阶段三</span>
        <h3>出口包装与交付协同 · Export &amp; Logistics</h3>
      </div>
      <div class="flow-cards-row c2">
{p3_html}
      </div>
    </div>
  </div>
</div></section>
""" + cta_band_zh(rel, "提交图纸或技术要求",
                  "请介绍您的产品、包装要求及出运目的地。我们将评估您的询价，并与您沟通后续事宜。")
    return page_zh(rel, "about", "关于青岛拉博尔包装",
                   "青岛拉博尔包装面向工业客户提供定制木质包装及 OEM 制造服务，注重图纸尺寸匹配、批次一致性与出口运输需求。", body)

# ================= APPLICATIONS ZH =================
def build_applications_zh():
    rel = "../../"
    cases = [
        ("服务器与数据中心设备",
         "机柜式服务器、高密度算力服务器及高端精密电子设备的国内外长途运输。",
         "减少运输振动冲击，箱内有效稳固，并配置斜坡以便目的地安全移机部署。",
         "采用定制木构件外框结合减震缓冲材料，箱体配置辅助装卸斜坡板。",
         "按批次生产提供匹配的成套服务器木箱包装。",
         "case-data-server.webp", "带有操作警示标识的高位服务器木箱"),

        ("高压绝缘子",
         "玻璃、陶瓷及瓷质特高压电瓷绝缘子盘式串的大宗海运出口。",
         "防止碰损微裂纹，组件相互隔离，并具备优异的抗压多层集装箱堆码能力。",
         "设计阶梯隔离卡槽隔板木箱，消除绝缘子片之间的硬接触碰伤。",
         "交付结构牢固的重型海运木箱，适配集装箱堆叠出运。",
         "case-glass-insulator.webp", "整齐摆放高压玻璃绝缘子的出口木箱"),

        ("工业机械设备",
         "数控机床、工业印刷设备、大功率水泵及压缩机等机械设备的出口与转运。",
         "满足高承重要求，重心不对称设备的稳固锁紧，并方便叉车与吊具起吊。",
         "采用重型硬木滑橇底座，结合转角角铁加固与箱内设备锚固木撑。",
         "依据设备外形尺寸与单重定制生产的重型工业包装箱。",
         "case-industrial-printer.webp", "为大型工业打印机制造的专用实木木箱"),

        ("能源设备",
         "储能电池集装箱组件、电动汽车充电桩、变压器及配电电控柜出运。",
         "箱底牢固承托抗侧倾，配置防潮防雨包装膜，满足陆海联运防护要求。",
         "重型实木主梁底座，配套防潮密封包装膜及螺栓拉杆锁固附件。",
         "根据具体设备外形与运输条件确认的定制木箱结构。",
         "case-ev-charging.webp", "装载新能源充电设施的重型木箱包装"),

        ("拆装式包装套件",
         "持续性工业 OEM 设备出口项目，要求在发货前节省仓储及海运体积。",
         "组装前具备极高堆码密度，运抵现场后通过标准五金件快速装配成箱。",
         "数控精准预开孔胶合板及木质围板，配套金属转角锁扣五金件。",
         "批量出运平板化拆装包装套件，在适用情况下减少运输占用空间。",
         "case-server-rack-kd.webp", "带金属角码的平板拆装式机柜包装套件"),

        ("定制出口木箱",
         "机械大件与成套设备的集装箱海运及件杂货散货海运出口。",
         "全面符合 ISPM 15 植物检疫要求，具备规范清晰的 IPPC 标识与防潮防盐雾保护。",
         "选用符合标准的热处理实木及胶合板复合结构，加贴防潮防雨内衬。",
         "完成热处理并加施 IPPC 标识的成套出口木箱。",
         "case-relocation-liftvan.webp", "整齐码放的出口木箱准备装车装船"),
    ]

    def case_card_zh(title, bg, req, config, scope, img, alt):
        return f"""
    <div class="card reveal"><div class="ph portrait"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd">
        <span class="kicker">包装应用示例</span>
        <h3 style="margin-bottom:10px">{title}</h3>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>应用背景:</strong> {bg}</p>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>包装需求:</strong> {req}</p>
        <p style="font-size:.9rem;margin-bottom:6px"><strong>采用结构:</strong> {config}</p>
        <p style="font-size:.9rem;color:var(--muted)"><strong>实际交付:</strong> {scope}</p>
      </div></div>"""

    cards = "\n".join(case_card_zh(*c) for c in cases)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 包装应用</div>
  <h1>包装应用案例</h1>
  <p class="lead">展示木质包装在工业设备及科技产品领域的典型应用。具体包装结构根据产品特点、装卸方式与运输要求进行调整。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">典型工业领域包装应用示例</h2>
  <p class="section-sub reveal">展示依据客户实际设备规格与出运需求定制生产的木包装方案。</p>
  <div class="grid g3">{cards}
  </div>
</div></section>

<section id="rfq"><div class="wrap">
  <h2 class="section-title reveal">获取木质包装报价</h2>
  <p class="section-sub reveal">请介绍您的产品、包装要求及出运目的地。提供图纸、尺寸、重量和预计数量，有助于我们评估您的需求。</p>
  <form class="rfq reveal" id="rfqForm" novalidate>
    <div class="form-grid">
      <div class="field"><label for="fName">姓名 *</label><input id="fName" name="full_name" type="text" autocomplete="name" required><span class="err"></span></div>
      <div class="field"><label for="fEmail">工作邮箱 *</label><input id="fEmail" name="email" type="email" autocomplete="email" required><span class="err"></span></div>
      <div class="field"><label for="fCompany">公司名称 *</label><input id="fCompany" name="company" type="text" autocomplete="organization" required><span class="err"></span></div>
      <div class="field"><label for="fCountry">国家 / 地区 *</label><input id="fCountry" name="country" type="text" autocomplete="country-name" required><span class="err"></span></div>
      <div class="field"><label for="fDimensions">尺寸与重量 (选填)</label><input id="fDimensions" name="dimensions_weight" type="text" placeholder="例如：1200 x 800 x 1000 毫米，450 千克"></div>
      <div class="field"><label for="fQuantity">预计数量 (选填)</label><input id="fQuantity" name="quantity" type="text" placeholder="例如：每月 50 套 或 单批次总量"></div>
      <div class="field full"><label for="fDestination">出运目的地 (选填)</label><input id="fDestination" name="destination" type="text" placeholder="例如：青岛港 / 美国洛杉矶港 / 德国汉堡"></div>
      <div class="field full"><label for="fNeed">产品与包装要求 *</label><textarea id="fNeed" name="requirements" rows="5" placeholder="请简要介绍您的设备特点、是否有图纸、包装特殊要求、交期计划等…" required></textarea><span class="err"></span></div>
    </div>
    <div style="margin-top:22px;text-align:center">
      <button class="btn btn-green" type="submit" style="min-width:220px">提交询价</button>
    </div>
    <div class="form-note" id="formNote" role="status"></div>
    <p style="margin-top:14px;font-size:.9rem;color:var(--g700);text-align:center;font-weight:500">我们将评估您的询价，并与您沟通后续事宜。</p>
    <p style="margin-top:8px;font-size:.85rem;color:var(--muted);text-align:center">如需直接沟通，欢迎发送邮件至 <a href="mailto:{EMAIL}">{EMAIL}</a> 或通过 <a href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp 在线联系</a>。</p>
  </form>
</div></section>
"""
    return page_zh(rel, "applications", "工业木质包装应用",
                   "展示木质包装在服务器、电网绝缘子、工业机床及储能设备领域的典型应用示例，提供木包装在线询价与需求对接服务。", body)

# ================= INDUSTRY PAGES ZH =================
def industry_page_zh(slug, short, h1, title, desc, intro_paras, approach, solutions, challenges, scope, objective):
    rel = "../../../"
    paras = "\n".join(f"    <p style=\"margin-top:14px\">{p}</p>" for p in intro_paras)
    sol = "\n".join(f"      <li>{s}</li>" for s in solutions)
    cha = "\n".join(f"      <li>{c}</li>" for c in challenges)
    sco = "\n".join(f"      <li>{s}</li>" for s in scope)
    wa_text = quote(f"您好，我想了解关于{short}的木质包装方案。")
    img_map = {
        "data-servers-precision-electronics": ("case-data-server.webp", "服务器精密电子专用木箱"),
        "ev-battery-charging": ("solutions-battery-crates.webp", "电池包与充电设施定制包装木箱"),
        "industrial-machinery-infrastructure": ("case-industrial-printer.webp", "大型工业设备专用实木木箱"),
        "high-voltage-insulators-power-transmission": ("case-glass-insulator.webp", "特高压绝缘子出口木箱"),
    }
    img_fn, img_alt = img_map.get(slug, ("knockdown-kits-flatpack.webp", short))
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / <a href="{rel}zh/industries/data-servers-precision-electronics/">服务行业</a> / {short}</div>
  <h1>{h1}</h1>
  <p class="lead">{objective}</p>
</div></div>

<section><div class="wrap">
  <div class="split reveal" style="margin-bottom:20px">
    <div class="ph"><img src="{rel}assets/img/{img_fn}" alt="{img_alt}" loading="lazy"></div>
    <div class="split-content">
      <span class="kicker">行业包装概览</span>
      <h3 style="margin-bottom:14px">{short}</h3>
      {paras}
      <div class="split-meta"><span>出口与合规:</span> 支持 ISPM 15 处理要求 · 依据运输要求配置</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap" style="max-width:960px">
  <h2 class="section-title reveal">包装结构与防护配置</h2>
  <p class="section-sub reveal">{approach}</p>
  <h3 class="reveal" style="margin:34px 0 6px">关键防护配置</h3>
  <ul class="check-list reveal">{sol}</ul>
</div></section>

<section><div class="wrap" style="max-width:960px">
  <div class="grid g2">
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">应对的运输痛点</h3>
      <ul class="check-list">{cha}</ul></div>
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">典型适用范围</h3>
      <ul class="check-list">{sco}</ul></div>
  </div>
</div></section>
"""
    cta = f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>咨询{short}包装方案</h2>
  <p>请介绍您的设备尺寸、单重及出运要求。我们将评估您的询价，并与您沟通后续事宜。</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}zh/applications/#rfq">获取报价</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={wa_text}" target="_blank" rel="noopener">WhatsApp 在线沟通</a>
  </div>
</div></section>"""
    return page_zh(rel, "industries/" + slug, title, desc, body + cta)

def build_industries_zh():
    pages = {}

    pages["data-servers-precision-electronics"] = industry_page_zh(
        "data-servers-precision-electronics", "服务器与精密电子",
        "服务器与数据中心设备木箱",
        "服务器与数据中心设备木箱",
        "为服务器、机柜、存储系统及精密电子设备提供定制木箱，并根据产品特点与运输要求配置内部支撑和缓冲结构。",
        ["数据中心服务器、机架式存储设备及高端电子仪表在多式联运过程中对冲击与震动敏感。",
         "包装方案需确保批量加工尺寸精准一致，兼顾现场快速拆装与斜坡安全卸载需求。"],
        "为服务器、机柜、存储系统及精密电子设备提供定制木箱，并根据产品特点与运输要求配置内部支撑和缓冲结构。",
        ["按服务器机柜尺寸量身定制的高刚性木箱外壳",
         "依据设备重量与易损点配置防震缓冲泡沫垫块",
         "按项目需求提供防静电内衬及铝箔防潮真空袋包装",
         "高位机柜包装箱可选配一体化下卸斜坡板，方便现场设备移出",
         "用于出口的实木材料执行 ISPM 15 热处理与标识标准"],
        ["降低公路与海运中持续微震对电子元器件的影响",
         "避免硬性接触刮伤面板或损坏接口部件",
         "方便机房现场在无重型机械配合下安全开箱取机",
         "支持 OEM 批量供应中的尺寸匹配与互换性"],
        ["机架式服务器与计算节点",
         "数据存储磁盘阵列柜",
         "交换机与通信机柜",
         "精密电源与不间断电源（UPS）主机",
         "工业自动化控制机柜"],
        "为服务器、机柜、存储系统及精密电子设备提供定制木箱，并根据产品特点与运输要求配置内部支撑和缓冲结构。")

    pages["ev-battery-charging"] = industry_page_zh(
        "ev-battery-charging", "电池与充电设备",
        "电池与充电设备包装",
        "电池与充电设备包装",
        "为电池包、充电设备及相关产品提供定制包装，根据产品特点及适用的运输要求确定承载结构和防护配置。",
        ["锂电池包、工商业储能设备及高压直流充电桩具有自重偏重、重心高及严格的运输规范要求。",
         "包装结构需具备强化承托底座、牢靠固定构件与绝缘防护，并根据具体电池型号和出运方式确认合规要求。"],
        "为电池包、充电设备及相关产品提供定制包装，根据产品特点及适用的运输要求确定承载结构和防护配置。",
        ["加厚重型滑橇式底梁，满足高集中载荷承托与叉车装卸",
         "箱内配置限位木档与防晃支撑，避免运输中发生侧移",
         "根据具体电池包要求配置绝缘垫块与缓冲阻燃材料",
         "箱体框架支持螺栓固定与快速拆卸面板，方便吊装入箱",
         "出口实木用料符合国际 ISPM 15 植物检疫处理要求"],
        ["重型电池包在急刹车及海运摇摆状态下的稳固限位",
         "大功率户外充电桩箱体表面防刮花与防倾覆支撑",
         "方便现场叉车与行车吊具的安全起吊操作",
         "配合承运人及港口对特定型号货物的运输要求进行结构优化"],
        ["新能源乘用车与商用车锂动力电池包",
         "工商业储能系统（ESS）电池箱体",
         "直流快充桩与大功率分体充电电源柜",
         "交流充电桩与车载充电机辅件",
         "光储充一体化控制设备配电柜"],
        "为电池包、充电设备及相关产品提供定制包装，根据产品特点及适用的运输要求确定承载结构和防护配置。")

    pages["industrial-machinery-infrastructure"] = industry_page_zh(
        "industrial-machinery-infrastructure", "工业机械与基础设施",
        "工业机械设备木箱",
        "工业机械设备木箱",
        "根据设备尺寸、重量、吊装位置及运输条件，为工业机械提供定制重型木箱与木质底座。",
        ["重型机床、大型旋转动力机械及电网输变电核心构件多属于高价值大件设备，外形不规则且重心偏移明显。",
         "包装需承受长距离多程转运颠簸，具备坚固的起吊和拖拽受力点，并做好防潮防锈措施。"],
        "根据设备尺寸、重量、吊装位置及运输条件，为工业机械提供定制重型木箱与木质底座。",
        ["高强度承重木托盘与底座，预留加宽叉槽与吊装孔位",
         "箱内定制异形阻挡木块及螺栓压紧装置，牢固锁定设备基座",
         "可选全封闭胶合板结构或加固实木花格结构",
         "海运出口配置真空防潮袋、干燥剂及气相防锈（VCI）内衬",
         "箱体主受力构件采用优质木材并完成出口检疫热处理"],
        ["妥善解决偏心设备在装卸搬运中的倾斜与晃动问题",
         "防止精密导轨与主轴在运输途中受外力碰擦变形",
         "清晰标明起吊点与重心标志，杜绝野蛮装卸隐患",
         "抵御远洋海运高湿高盐雾对裸露金属表面的侵蚀"],
        ["数控加工中心、车床、铣床与折弯设备",
         "大功率工业泵组、风机与空气压缩机",
         "工业电机、变压器与输配电控制成套设备",
         "矿山机械、工程机械核心配套零部件",
         "大口径工业阀门与管道压力设备"],
        "根据设备尺寸、重量、吊装位置及运输条件，为工业机械提供定制重型木箱与木质底座。")

    pages["high-voltage-insulators-power-transmission"] = industry_page_zh(
        "high-voltage-insulators-power-transmission", "电力绝缘子与输变电",
        "电力绝缘子专用木箱",
        "电力绝缘子专用木箱",
        "为玻璃、陶瓷及瓷质绝缘子提供定制木箱，根据产品形状和易损部位配置内部隔离、支撑与缓冲结构，降低装卸和运输过程中的碰损风险。",
        ["高压悬式玻璃绝缘子、瓷瓶及套管质地坚硬但脆性大，在海运和堆叠时易受挤压碰缺或震动微裂。",
         "包装必须做到伞裙互不硬性碰触，同时木箱外框需要有极佳的承重刚度以支持多层集装箱内堆叠。"],
        "为玻璃、陶瓷及瓷质绝缘子提供定制木箱，根据产品形状和易损部位配置内部隔离、支撑与缓冲结构，降低装卸和运输过程中的碰损风险。",
        ["内部定制阶梯卡槽隔板，将绝缘子盘片依次牢固限位",
         "接触部位加衬缓冲护垫，降低海运颠簸冲击",
         "高强度实木外框柱脚结构，保障集装箱内多层牢固堆码",
         "通风排湿结构设计，减少海上温差引起的绝缘件表面冷凝水",
         "实木材料符合 ISPM 15 出口检疫规范并加施 IPPC 标识"],
        ["杜绝长途海运中绝缘子组件之间的相互撞击与边缘掉瓷",
         "消除底层木箱在集装箱重载堆码下的结构变形挤压",
         "便于港口堆场、电网工地现场高效清点与装卸搬运",
         "保证绝缘子按技术标准安全运抵变电站或输电线路施工现场"],
        ["特高压悬式盘形玻璃与瓷质绝缘子串",
         "变电站支柱绝缘子与穿墙套管",
         "复合绝缘子与硅橡胶输变电配件",
         "高压避雷器及互感器绝缘外套",
         "电网工程成套绝缘绝缘紧固件箱"],
        "为玻璃、陶瓷及瓷质绝缘子提供定制木箱，根据产品形状和易损部位配置内部隔离、支撑与缓冲结构，降低装卸和运输过程中的碰损风险。")

    return pages

def generate_chinese_site():
    print("--- Building Chinese Site (/zh/) ---")
    write_zh("zh/index.html", build_home_zh())
    write_zh("zh/solutions/index.html", build_solutions_zh())
    write_zh("zh/capabilities/index.html", build_capabilities_zh())
    write_zh("zh/about/index.html", build_about_zh())
    write_zh("zh/applications/index.html", build_applications_zh())
    # Keep case-studies/ accessible with identical content as well
    write_zh("zh/case-studies/index.html", build_applications_zh())

    for slug, html in build_industries_zh().items():
        write_zh(f"zh/industries/{slug}/index.html", html)

if __name__ == "__main__":
    generate_chinese_site()
