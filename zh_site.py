#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the authentic Chinese version of Qingdao Lumber & Packaging (青岛拉博尔包装设备有限公司 / 青岛远洋木业).
"""
import os, json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))
CANON = "https://en.qdlumber.com"
WA_LINK = "https://wa.me/8613405101358"
EMAIL = "sales@qdlumber.com"

FACTORY_ZH = ("中国·青岛市即墨开发区华宇路1号（即墨生产制造基地 · 10万+平米）",
              "+86 186 0261 9997", "Steven.Sung@qdlumberco.com")
OFFICE_ZH = ("中国·青岛市崂山区海尔路180号大荣世纪大厦",
             "+86 134 0510 1358", "evan.chen@qdlumberco.com")

INDUSTRIES_ZH = [
    ("data-servers-precision-electronics", "数据中心服务器与精密电子",
     "高稳定性服务器机柜与精密电子专用防震木箱系统，三维限位吸能阻尼，保障直抵机房安全部署。"),
    ("ev-battery-charging", "新能源动力电池与充电设施 · UN38.3",
     "符合国际 UN38.3 锂电池危险品出口海运测试标准，阻燃绝缘内衬与重型承载防倾覆结构。"),
    ("industrial-machinery-infrastructure", "重型装备制造与能源基建",
     "针对数十吨超重大件、数控机床与电力变压器设计的重型实木主梁与高强钣金复合包装箱。"),
    ("high-voltage-insulators-power-transmission", "特高压电瓷绝缘子与输变电设备",
     "专用分层阶梯卡槽防碰触隔离木箱，抗挤压高密度堆叠架构，海运破损率降低98%以上。"),
]

INDUSTRIES_EN = [
    ("data-servers-precision-electronics", "Data Server & Precision Electronics"),
    ("ev-battery-charging", "EV Battery & Charging Station · UN38.3"),
    ("industrial-machinery-infrastructure", "Industrial Machinery & Infrastructure"),
    ("high-voltage-insulators-power-transmission", "High Voltage Insulator & Power Transmission"),
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
    "name": "青岛拉博尔包装设备有限公司 / 青岛远洋木业",
    "url": CANON + "/zh/",
    "logo": CANON + "/assets/img/logo.webp",
    "description": "美资独资专业 OEM 工业木包装制造商，专注定制木箱、模块化可拆装箱套件（KD Flat-Pack）及出口重型装备防护包装20余年。",
    "contactPoint": [{
        "@type": "ContactPoint", "telephone": "+86-134-0510-1358",
        "email": EMAIL, "contactType": "sales", "areaServed": "Worldwide"
    }],
    "address": {"@type": "PostalAddress", "streetAddress": FACTORY_ZH[0],
                "addressLocality": "青岛市", "addressCountry": "CN"},
}

def head_zh(rel, slug, title, desc, extra=""):
    canon = CANON + ("/zh/" if not slug else f"/zh/{slug}/")
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
    # calculate EN target link
    # On zh home, slug is "", rel is "../", so target en home is "../"
    # On zh subpage (e.g. about), slug is "about", rel is "../../", target en is "../../about/"
    en_target = f"{rel}{slug + '/' if slug else ''}"
    zh_target = "#"

    return f"""<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{rel}zh/" aria-label="青岛拉博尔包装设备有限公司 / 青岛远洋木业 — 首页">
      <img src="{rel}assets/img/logo.webp" alt="青岛拉博尔包装设备有限公司标志" width="259" height="98"></a>
    <button class="burger" id="burger" aria-label="菜单"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="mainNav">
      <a class="nav-link" data-nav="home" href="{rel}zh/">首页</a>
      <a class="nav-link" data-nav="solutions" href="{rel}zh/solutions/">包装解决方案</a>
      <a class="nav-link" data-nav="capabilities" href="{rel}zh/capabilities/">生产与工程能力</a>
      <a class="nav-link" data-nav="about" href="{rel}zh/about/">关于我们</a>
      <a class="nav-link" data-nav="case-studies" href="{rel}zh/case-studies/">应用案例</a>
      <span class="has-drop"><a class="nav-link" data-nav="industries" href="{rel}zh/industries/data-servers-precision-electronics/">细分行业 ▾</a>
        <span class="drop">{ind_links}</span></span>
      <a class="nav-cta" href="{rel}zh/case-studies/#rfq">获取定制方案</a>
      <div class="lang-switch">
        <a href="{en_target}">EN</a>
        <span class="sep">/</span>
        <a class="active" href="{zh_target}">中文</a>
      </div>
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
      <img src="{rel}assets/img/logo-footer.webp" alt="青岛拉博尔包装设备有限公司 / 青岛远洋木业" width="200" height="75">
      <p>美资独资专业 OEM 工业木质包装系统制造商，深耕重型设备定制木箱、模块化拆装箱套件（KD Flat-Pack）及出海防护包装 20 余年。</p>
      <div class="social-row">
        <a href="https://www.linkedin.com/company/qdlumber/" aria-label="领英" target="_blank" rel="noopener">in</a>
        <a href="https://www.youtube.com/@QingdaoLumberPackaging" aria-label="YouTube" target="_blank" rel="noopener">▶</a>
        <a href="{WA_LINK}" aria-label="WhatsApp" target="_blank" rel="noopener">WA</a>
      </div>
    </div>
    <div>
      <h4>探索栏目</h4>
      <ul>
        <li><a href="{rel}zh/">首页</a></li>
        <li><a href="{rel}zh/solutions/">包装解决方案</a></li>
        <li><a href="{rel}zh/capabilities/">生产与工程能力</a></li>
        <li><a href="{rel}zh/about/">关于我们</a></li>
        <li><a href="{rel}zh/case-studies/">客户案例</a></li>
        <li><a href="{rel}zh/case-studies/#rfq">获取定制方案</a></li>
      </ul>
    </div>
    <div>
      <h4>服务行业</h4>
      <ul>{ind_links}</ul>
    </div>
    <div>
      <h4>关联企业</h4>
      <ul>
        <li><a href="http://www.marinelumberco.com" target="_blank" rel="noopener">Marine Lumber Co. (美国总部) ↗</a></li>
        <li><a href="https://marinedefensepackaging.com" target="_blank" rel="noopener">Marine Defense Packaging (军工包装) ↗</a></li>
        <li><a href="http://www.qdlumber.com" target="_blank" rel="noopener">青岛拉博尔包装设备有限公司 (中国) ↗</a></li>
      </ul>
    </div>
    <div>
      <h4>联系我们</h4>
      <div class="footer-contact-block">
        <strong>即墨生产制造基地</strong>
        <span>{FACTORY_ZH[0]}</span><br>
        电话: <a href="tel:+8618602619997">{FACTORY_ZH[1]}</a><br>
        邮箱: <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <div class="footer-contact-block" style="margin-top:10px">
        <strong>运营管理中心</strong>
        <span>{OFFICE_ZH[0]}</span><br>
        电话: <a href="tel:+8613405101358">{OFFICE_ZH[1]}</a><br>
        邮箱: <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span id="yr">2026</span> 青岛拉博尔包装设备有限公司 / 青岛远洋木业 版权所有</span>
    <span>符合国际 ISPM-15 出口热处理检疫标准 · 具备 IPPC 资质认证加施资质</span>
  </div>
</footer>
{WA_CODE}
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def page_zh(rel, slug, title, desc, body, extra_head=""):
    return head_zh(rel, slug, title, desc, extra_head) + header_zh(rel, slug) + body + footer_zh(rel)

def cta_band_zh(rel, title, text):
    return f"""
<section class="cta-band"><div class="wrap reveal">
  <h2>{title}</h2>
  <p>{text}</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-green" href="{rel}zh/case-studies/#rfq">获取定制方案</a>
    <a class="btn btn-ghost" href="{WA_LINK}?text={quote('您好，我想咨询青岛拉博尔工业木箱定制包装项目。')}" target="_blank" rel="noopener">微信 / WhatsApp 咨询</a>
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

    values = [
        ("values-precision.webp", "工程师正在使用3D CAD系统进行非标重型木包装箱力学设计",
         "20+年深厚 OEM 制造积淀",
         "专注高端装备与非标设备定制包装，结合精准力学建模、3D CAD 构件优化及成熟的全球出海交付经验。"),
        ("values-efficiency.webp", "数字化智能看板监控工业木箱加工排产与集装箱装柜进度",
         "10万平米规模化弹性产能",
         "青岛实体制造基地配备自动化数控木工产线与大型原木堆场，无论是大批量连续供应还是多规格快速打样，交期稳定可控。"),
        ("values-accountability.webp", "叉车正在将加施IPPC印章的出口免熏蒸/热处理木箱装入海运集装箱",
         "全流程合规 ISPM-15 出口标准",
         "自建符合国家出入境检疫标准的大型热处理窑炉，100% 实木加施官方 IPPC 标识，随箱出具备案检疫证明，全球清关零风险。"),
        ("values-partnership.webp", "包装工程师与跨国客户在青岛即墨工厂车间共同审查大型出口木箱结构",
         "全球化工业供应链协同",
         "精准契合 20尺/40尺集装箱内径尺寸设计，箱体可拆装（KD）高密度排布，协助企业大幅缩减越洋海运货物体积与综合运费。"),
        ("values-reliability.webp", "质检员严格测量成品木箱对角线与关键承重点五金紧固件",
         "严苛品控与批次一致性",
         "推行全工序首件检验与巡检制度，从木材含水率、板材胶合强度到受力节点拉拔力，品质坚固如一，屡获长期复购信赖。"),
    ]

    value_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in values)

    body = f"""
<section class="hero">
  <div class="hero-video-bg">
    <iframe src="https://player.vimeo.com/video/1190319624?background=1&autoplay=1&loop=1&byline=0&title=0&muted=1" frameborder="0" allow="autoplay; fullscreen" allowfullscreen loading="eager" fetchpriority="high"></iframe>
  </div>
  <div class="hero-overlay"></div>
  <div class="wrap hero-wrap">
    <div class="hero-content reveal in">
      <span class="hero-kicker">值得信赖的工业包装系统与海外 OEM 合作伙伴</span>
      <h1 class="hero-title">全球工业供应链定制木质包装系统<br>专业工程设计 · 批量精益制造</h1>
      <p class="hero-lead">专为工业重型装备、数据中心基建、新能源电池及高精密设备研发的高可靠出口包装方案，以高精度 CNC 构件、模块化快速拆装与卓越成本控制，保障全球长途海空联运安全。</p>
      <p class="hero-sublead">深耕工业木包装 20 余年，具备青岛 10 万平米生产基地与自营 ISPM-15 出口检疫热处理资质。</p>
      <div class="hero-actions">
        <a class="btn btn-green" href="{rel}zh/case-studies/#rfq">获取定制方案</a>
        <a class="btn btn-ghost" href="{rel}zh/solutions/">浏览产品体系</a>
      </div>
    </div>
  </div>
</section>

<section style="padding:44px 0 0"><div class="wrap">
  <div class="grid g3">
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">降低跨国供应链货损风险</h3>
      <p>严格执行全流程受力工程校核与多工序质检，确保精密设备经受远洋长途颠簸与反复吊装考验，杜绝在途货损隐患。</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">扩充海内外规模化配套产能</h3>
      <p>依托青岛 10 万平米实体制造基地与数控加工中心，无需重资产投入，即可为大型装备制造企业提供充裕的 OEM 代工与稳定保供能力。</p>
    </div>
    <div class="tcard reveal">
      <h3 style="color:var(--g600);margin-bottom:8px">深度优化端到端物流总成本</h3>
      <p>通过价值工程设计、箱体容积率优化与模块化平摊拆装（KD Flat-Pack）系统，大幅削减海运集装箱占用体积与目的地现场组装工时。</p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">深受信赖的核心竞争力</h2>
  <p class="section-sub reveal">从单一包装木箱到全套跨国 OEM 工业包装解决方案，提供贯穿产品全生命周期的工程支持与精益交付。</p>
  <div class="grid g5">{value_cards}</div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">数字化精益制造与全流程品控</h2>
  <p class="section-sub reveal">实地探访青岛制造基地：从原木数控精细加工、结构钣金下料到成品木箱静载与跌落验证，每一个细节皆符合国际出海严苛标准。</p>
  <div class="video-showcase reveal">
    <iframe src="https://player.vimeo.com/video/1190319624?byline=0&title=0" frameborder="0" allow="autoplay; fullscreen" allowfullscreen loading="lazy"></iframe>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="section-title reveal">赋能关键工业领域出海</h2>
  <p class="section-sub reveal">针对各行业特殊物理特性、防护等级与运输标准，提供量身定制的木包装工程系统。</p>
  <div class="grid g4">{ind_cards}</div>
</div></section>
""" + cta_band_zh(rel, "携手专业工业木包装制造商",
                  "告诉我们您正在运输的设备规格与出运需求，我们的包装工程师将在 1 个工作日内提供量身定制的结构方案与明细预算。")
    return page_zh(rel, "", "青岛拉博尔包装设备有限公司 / 青岛远洋木业 — 20+年专业OEM工业木质包装制造商",
                   "美资独资专业 OEM 工业木包装制造商，青岛10万平米实体制造基地。专为工业机械、数据中心、新能源电池及特高压设备提供符合国际 ISPM-15 标准的定制木箱系统。", body)


# ================= SOLUTIONS ZH =================
def build_solutions_zh():
    rel = "../../"
    products = [
        ("solutions-wood-elements.webp", "车间整齐摆放的定制实木承重结构木构件与框架箱组件",
         "重型定制框架木箱", "严格根据图纸参数定做——每个尺寸、每个榫槽接头及每根承重受力主梁均精准咬合。"),
        ("solutions-server-crates.webp", "带有坡道踏板便于滑移推入的数据中心服务器机柜抗震木箱",
         "服务器与精密电子机柜木箱", "内置多向抗震阻尼隔振系统，专为机架式服务器、刀片阵列及云数据中心核心设备打造。"),
        ("solutions-battery-crates.webp", "室外堆放的经过UN38.3危险品认证的大型锂电池储能出口木箱",
         "新能源储能与动力电池木箱", "严格符合国际海事危规与 UN38.3 锂电池海空运认证标准，阻燃绝缘内衬与重载抗弯底座。"),
        ("solutions-plywood-panels.webp", "自动化精密数控裁板机正在加工优质多层结构胶合板箱板",
         "数控高精板材精密加工", "选用耐水工业胶合板，多轴数控裁切下料，尺寸公差稳定控制在毫米级。"),
        ("solutions-cnc-parts.webp", "多轴数控CNC高精雕刻与开槽异形木构件",
         "数控高精加工异形木构件", "采用全自动 CNC 铣切高精度榫卯、限位凹槽与自锁支撑件，为复杂非标工件提供毫米级内部限位。"),
    ]
    product_cards = "\n".join(
        f'''    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>
      <div class="bd"><h3>{t}</h3><p>{d}</p></div></div>'''
        for fn, alt, t, d in products)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 包装解决方案</div>
  <h1>全球工业装备与高精密产品 OEM 木质包装系统</h1>
  <p class="lead">全场景覆盖重型机械、能源基建、高精密电子及危险品包装需求。结合高强力学工程设计、模块化快速拆装与卓越防护内衬，为现代跨国制造企业打造安全、经济、合规的工业包装方案。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">工业木质包装核心产品系列</h2>
  <p class="section-sub reveal">专为应对远洋航运颠簸、多式联运高频吊装及严苛气候环境而研发的专业级工业木箱系统。兼具高强度承载、长期气候适应性与全球出海检验检疫合规性。</p>
  <div class="grid g3">{product_cards}</div>

  <h2 class="section-title reveal" style="margin-top:56px">模块化拆装箱与结构钣金紧固系统</h2>
  <p class="section-sub reveal">深度融合精密木构件与激光高强钣金的模块化包装系统。实现目的地现场极速无损拼装，显著降低跨境海运包装体积，兼具超高结构刚度与高性价比。</p>

  <div class="split reveal" style="margin-bottom:36px">
    <div class="ph"><img src="{rel}assets/img/solutions-knockdown-kits.webp" alt="青岛工厂车间堆叠整齐的模块化平摊拆装木箱套件" loading="lazy" width="800" height="600"></div>
    <div class="split-content">
      <span class="kicker">模块化工程木箱</span>
      <h3>模块化可拆装木箱套件 (KD Flat-Pack)</h3>
      <p><em>结合数控高精木构件与结构金属插销的平摊拆装系统，大幅提升货柜空间利用率，便于目的港快速部署。</em></p>
      <ul class="check-list">
        <li>每套木箱套件包含预切板材、加强框架、激光下料钣金连接件及配套紧固件，现场仅需简单工具即可快速卡扣组装。</li>
        <li>专为国际集装箱尺寸深度优化——平摊拆装结构可缩减海运占箱体积高达 60%，组装完成后拥有与整体木箱一致的承重防护刚度。</li>
        <li>零部件附带直观的装配编号与防呆定位，即使海外无经验人员也能在几分钟内轻松完成高精度拼接。</li>
      </ul>
      <div class="split-meta"><span>包装结构形态:</span> 平摊可拆装套件 (KD Flat-Pack) · 大幅节省海运货柜容积</div>
    </div>
  </div>

  <div class="split reveal" style="margin-bottom:36px">
    <div class="split-content">
      <span class="kicker">高强钣金与受力补强</span>
      <h3>激光下料高强结构钣金件</h3>
      <p><em>自主设计制造的工业级工程金属构件，专为木包装箱关键受力点、叉车受载区与吊装节点提供重力补强。</em></p>
      <ul class="check-list">
        <li>厂内高精度激光切割、数控折弯成型与机器人无缝焊接，尺寸公差极严，承重及抗剪切力学表现卓越。</li>
        <li>与木结构框架深度咬合，在起重机吊装、长途急刹颠簸及集装箱高层堆码时，对薄弱交接角提供决定性抗形变刚度。</li>
        <li>全面抵御严苛远洋高盐雾湿热侵蚀，经久耐用，抗振动、耐冲击、适应长周期跨国多式联运。</li>
      </ul>
      <div class="split-meta"><span>钣金加工工艺:</span> 激光精密切割 · 机器人高强焊接结构钢</div>
    </div>
    <div class="ph"><img src="{rel}assets/img/solutions-metal-components.webp" alt="工厂车间大型起重吊梁正在搬运重型木箱关键金属构件" loading="lazy" width="800" height="450"></div>
  </div>

  <div class="split reveal">
    <div class="ph"><img src="{rel}assets/img/solutions-fastening-systems.webp" alt="定制工程重型钣金紧固角码与防松动紧固件总成" loading="lazy" width="800" height="956"></div>
    <div class="split-content">
      <span class="kicker">高可靠五金配件</span>
      <h3>重型紧固件与连接加固系统</h3>
      <p><em>自主定制的加厚高强金属角码、自锁钢扣与抗疲劳紧固螺栓总成，全面加固大型木箱框架节点。</em></p>
      <ul class="check-list">
        <li>厂内连续数控模具冲压下料，极大增强木方结合处、箱壁立柱与底托横梁之间的三向抗扭剪与抗拉拔刚度。</li>
        <li>严苛的孔径公差控制确保各金属构件与预加工木箱立柱精准咬合，彻底避免在长途颠簸中产生结合缝间隙旷动。</li>
        <li>表面经工业级热浸镀锌、环保达克罗或静电喷涂防腐处理，满足长达数月的远洋海运无锈蚀防护需求。</li>
      </ul>
      <div class="split-meta"><span>表面防腐工艺:</span> 工业级热浸镀锌 / 环保达克罗防腐涂层</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">工业包装常见问题解答 (FAQ)</h2>
  <p class="section-sub reveal">解答关于跨国定制木箱、图纸打样、出口检疫认证（ISPM-15）、装箱容积及生产交期的常见技术问题。</p>
  <div class="faq">
    <div class="faq-item reveal"><button class="faq-q">贵司能否依据我们现有的 3D CAD 图纸或实际设备样品进行定制？</button><div class="faq-a"><p>完全可以。只需提供您的工程图纸、三维模型或被包装设备的外形尺寸与重量重心参数，我们的包装工程团队将直接进行 3D CAD 结构设计、载荷有限元受力分析与集装箱配载计算，严格按图精密制造交付。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">你们主要擅长制造哪些类型的工业包装木箱？</button><div class="faq-a"><p>我们深耕工业级实木重型框架箱、免熏蒸高强胶合板箱、模块化平摊拆装箱（KD Kits）、服务器机柜抗震木箱、特高压绝缘子专用木箱、UN危规认证木箱及配套的高强金属紧固钣金件——全系符合国际 ISPM-15 出口标准。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">启动一个定制工业木包装项目通常需要客户提供哪些基础信息？</button><div class="faq-a"><p>通常需要：被包装货物的净长宽高、单件毛重、重心位置、表面是否易碎或易磕碰、运输方式（海运/空运/铁路）、出运目的国、预计订单批量以及任何特定的防护要求（如是否需要 VCI 抽真空防锈、充氮气、加装防倾斜标签等）。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">你们生产的所有实木包装材料是否都符合国际 ISPM-15 出口热处理检疫标准？</button><div class="faq-a"><p>是的，100% 绝对合规。我们在青岛即墨工厂自建有多座经国家检验检疫部门备案认证的大型标准热处理烘干窑，全流程微机温湿度曲线记录。所有实木包装均加施清晰合规的官方 IPPC 标识，并随箱出具备案植物检疫证书，全球口岸通关顺畅无阻。</p></div></div>
    <div class="faq-item reveal"><button class="faq-q">模块化可拆装箱（KD Kits）如何帮我们大幅削减物流运费？</button><div class="faq-a"><p>传统整体拼装好的木箱在运输时内部大面积是空气，集装箱装载容积率极低；而我们的 KD 平摊拆装箱系统将板材与底托以致密平板形态堆叠出运，集装箱装箱体积可减少高达 60%，同等货柜能多装数倍包装箱，极大摊薄远洋海运和陆运成本，抵达海外目的地后现场组装也极其省力快速。</p></div></div>
  </div>
</div></section>
""" + cta_band_zh(rel, "立即开启您的工业木包装项目",
                  "发送您的设备图纸或技术参数——我们的包装工程师将在 1 个工作日内提供量身定制的初步结构方案与明细预算。")
    return page_zh(rel, "solutions", "包装解决方案 | 定制工业木箱与模块化拆装箱系统 — 青岛拉博尔 / 远洋木业",
                   "提供工业重型框架木箱、胶合板封闭箱、平摊拆装木箱套件（KD Flat-Pack）、减震抗振包装箱及结构钣金构件，严格符合国际 ISPM-15 出口检疫认证。", body)

# ================= CAPABILITIES =================
def build_capabilities_zh():
    rel = "../../"
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 生产与工程能力</div>
  <h1>卓越工程实力与规模化智能制造基地</h1>
  <p class="lead">依托青岛 10 万平米制造基地、数控自动化加工群组、标准化熏蒸热处理窑炉及资深包装工程团队，为全球工业制造巨头提供尺寸精密、结构坚固、交期稳健的规模化交付能力。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">核心实力两大基石</h2>
  <p class="section-sub reveal">从产品力学工程结构设计、精密机械化下料到全流程出入境检验检疫合规保障，我们为全球化装备出海筑牢坚固屏障。</p>

  <div class="grid g2" style="margin-top:8px">
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-quality-assurance.webp" alt="质检工程师在成品出口木箱旁核对全套出入境检验检疫合规单证" loading="lazy"></div>
      <div class="bd"><h3>严格国际认证与 ISPM-15 检疫合规</h3><p>我们严格执行全球严苛的进出口货物包装技术与环境规范。工厂自备多座大型标准热处理窑，全电脑监控木材中心温度达到 56℃ 并持续 30 分钟以上，所有实木构件清晰加施官方 IPPC 标识，随箱出具正规植物检疫单据，保证货物在北美、欧洲、澳洲及亚太各大口岸顺利清关通关。</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-wood-metal.webp" alt="胶合板与高精度激光切割金属紧固钣金件结合处工艺特写" loading="lazy"></div>
      <div class="bd"><h3>数控高精木工与重型钣金综合智造</h3><p>配备多轴龙门加工中心（CNC）、数控电子裁板锯、自动钻铣流水线，木构件切割与开榫公差稳定在 ±1.0mm 范围内。五金车间配备大功率光纤激光下料机、数控折弯机与高频焊接工作站，表面经镀锌或达克罗防腐处理。木结构与金属构件在厂内实现一体化设计试装，确保批量木箱的高精度互换性。</p></div></div>
  </div>

  <h2 class="section-title reveal" style="margin-top:64px">端到端全链路工程能力</h2>
  <p class="section-sub reveal">一站式全流程协同——从最初的三维图纸受力校核，到最终海运集装箱高密度装柜交付。</p>
  <div class="grid g4">
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-oem-engineering.webp" alt="剖开的定制非标木箱清晰展示内部3D设计的承重锁固结构" loading="lazy"></div>
      <div class="bd"><h3>OEM 结构方案设计</h3><p>依据客户 3D CAD 图纸，综合计算设备重心、受力点与集装箱内径，量身打造坚固与经济兼备的包装方案。</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-knockdown-systems.webp" alt="栈板上堆叠整齐的模块化平摊拆装木箱套件" loading="lazy"></div>
      <div class="bd"><h3>模块化平摊拆装箱 (KD)</h3><p>高精模具化下料预组装，平摊打包发货，帮助客户节省海运运费高达 60%，目的港极速徒手或简易工具安装。</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-production-capacity.webp" alt="工人们正在生产线旁高效码放高精度加工完成的木箱构件" loading="lazy"></div>
      <div class="bd"><h3>充裕规模化保供产能</h3><p>10 万平米厂区常备万方级干燥原料，多条自动化产线柔性运转，从容应对大型工程项目的大批量紧急交期保供。</p></div></div>
    <div class="card reveal"><div class="ph"><img src="{rel}assets/img/capabilities-logistics-support.webp" alt="黄昏时分叉车正在将大批成品木箱紧密装入海运集装箱" loading="lazy"></div>
      <div class="bd"><h3>港口直通与全球物流支持</h3><p>紧邻青岛港国际海运枢纽，具备专业集装箱装柜、防撞充气袋填充、重型捆绑及出口单证一揽子技术服务。</p></div></div>
  </div>
</div></section>
""" + cta_band_zh(rel, "携手专业 OEM 包装工程制造伙伴",
                  "无论是单件超重大件特种包装，还是全球供应链标准化大批量木箱采购，我们都是您值得信赖的坚实后盾。")
    return page_zh(rel, "capabilities", "生产与工程能力 | 智能制造与出口检疫合规 — 青岛拉博尔 / 远洋木业",
                   "青岛10万平米智能制造基地，配备先进多轴 CNC 数控加工中心、光纤激光切割钣金车间、自建大型 ISPM-15 标准热处理窑炉与专业工程技术团队。", body)


# ================= ABOUT ZH =================
def build_about_zh():
    rel = "../../"
    steps_zh = [
        ("about-engineering-design.webp", "工程师在计算机前进行木箱构件3D CAD设计与力学受力分析",
         "前期规划与力学工程",
         "3D CAD 工程设计与力学结构建模",
         "每个项目均由资深包装工程师主导，根据客户提供的设备三维模型与技术规范，开展高精度 3D CAD 参数化建模与多工况受力校核。",
         [
             "全三维 CAD 参数化建模与虚拟装配干涉校验",
             "有限元（FEA）重载抗压、抗倾覆与振动冲击仿真分析",
             "契合 20尺/40尺 标准海运集装箱的容积率极限优化",
         ],
         "阶段交付物: 经客户会签认定的 3D CAD 设计图纸与全套包装技术规格书"),
        ("about-material-selection.webp", "质检员正在使用专业仪器检测进场优质胶合板含水率与厚度公差",
         "原材料严选与检疫除害",
         "原材料严选与 ISPM-15 检疫热处理",
         "选用符合环保标准的优质天然落叶松、辐射松、加厚耐水胶合板及重载高强结构钢材，从源头确保出口包装结构韧性与长久耐候性。",
         [
             "100% 经过自备热处理窑炉严格杀菌除害，四面加施清晰合规的官方 IPPC 印章",
             "选用抗剪切、高耐磨、防开裂的工业级承载结构胶合板",
             "木材供应链合规可追溯，随箱出具正规出入境植物检疫备案证书",
         ],
         "检疫合规标准: 100% 符合国际 ISPM-15 出口植物检疫热处理标准"),
        ("about-precision-processing.webp", "自动化多轴数控CNC加工机床正在对木方进行精密开榫打孔作业",
         "智能装备与精密加工",
         "多轴数控 CNC 高精机械下料加工",
         "引入多轴龙门加工中心、高精度电子裁板锯及多工位自动打眼开榫机，全面推行工厂化、模具化批量高精生产。",
         [
             "下料、开槽、打孔全尺寸公差严格控制在 ±1.0mm 工业级精度内",
             "数控程序自动化重复走刀，彻底消除手工加工累积公差，保证大批量互换性",
             "特制防呆凹凸公母榫卯槽位，预钻紧固沉头螺丝孔，提升整体装配咬合力",
         ],
         "机械公差标准: ±1.0mm 工业级多轴数控机械加工与自动榫槽公差"),
        ("about-kit-assembly.webp", "工人正在车间将带钢质加强滑轨的木箱构件拼装成拆装式套件",
         "模块化预制与预组装",
         "模块化可拆装箱 (KD) 预装与编号打标",
         "将高精加工的实木承重框、耐候箱板、激光下料钣金加强件及标准五金紧固螺栓预装匹配，打包成整齐紧凑的平摊（KD）套件。",
         [
             "采用模块化平摊拆装（KD）架构，为跨国客户削减高达 60% 的海运货柜容积",
             "预埋高强金属连接母座与快速自锁滑扣，大幅简化目的港就地开箱装配步骤",
             "关键构件喷印标准化序号与拼装指引示意图，实现无图纸快速防呆搭建",
         ],
         "包装结构形态: 平摊可拆装套件 (KD Flat-Pack) · 目的港极速搭建"),
        ("about-quality-inspection.webp", "三名经验丰富的品控工程师正在车间严格检验金属锁扣与箱体垂直度",
         "多道质检与实效验证",
         "全流程严格质检与动态载荷验证",
         "坚决执行进料检验（IQC）、工序巡检（IPQC）和出厂终检（FQC）三级质量防护网，杜绝不合格品流向包装一线。",
         [
             "全尺寸精准测量，重点校核箱体对角线平行度与底托水平受力面",
             "模拟真实叉车铲运、起重机双绳吊装及集装箱高层堆码工况的压力测试",
             "100% 全数核验 IPPC 检疫印章清晰度、木材含水率及植物检疫出库台账",
         ],
         "品质验收准则: 全工序首件检验制度 · 多点动态承重与跌落稳定性验证"),
        ("about-packaging-logistics.webp", "带有重型镀锌钢角码与高密封阻隔防潮层的木箱内部陈列",
         "环境防护与阻隔工程",
         "防锈防潮气相阻隔与立体减震总成",
         "针对远洋海运数月长周期高盐雾、极端高湿热环境，为客户高端机电设备构建全方位三维气密封闭与吸能缓冲防护体系。",
         [
             "热封加厚铝箔复合抽真空包装袋，内置饱和级工业 VCI 气相防锈干燥剂组",
             "数控雕刻高密度闭孔阻燃 EPE / EVA 仿形缓冲块与多维抗震阻尼基座",
             "箱体外表面标配高灵敏度防倾斜（TIP-N-TELL）与防震（DROP-N-TELL）监控标签",
         ],
         "防腐抗震等级: VCI 气相铝塑复合防锈密封阻隔 · 多轴动态吸能抗震"),
        ("about-delivery-support.webp", "大型重型叉车正在将加工完毕的定制木箱稳步装上跨国海运集卡车",
         "海运集港与交付保障",
         "青岛港直抵装箱与全球物流技术保障",
         "依托紧邻青岛港（全球前五大航运枢纽）的优越地理区位，为出海重型设备提供直抵码头的专业打包装柜、充气袋固定及出运协同。",
         [
             "定制重型集装箱科学排布方案与专用木质止退三角垫木锁死，杜绝海上颠簸移位",
             "距离青岛港前湾自动化集装箱码头仅数十公里，集港快速，全程物流可控",
             "提供专业的越洋远程技术指导，随时响应海外项目现场的拆装与重载复用需求",
         ],
         "出海物流配套: 紧邻青岛港装柜直达 · 覆盖海运多式联运的全流程保障"),
    ]

    step_html = ""
    for i, (fn, alt, cat, t, d, bullets, meta) in enumerate(steps_zh):
        img = f'<div class="ph"><img src="{rel}assets/img/{fn}" alt="{alt}" loading="lazy"></div>'
        bullet_items = "".join(f"<li>{b}</li>" for b in bullets)
        txt = f"""<div class="split-content">
      <span class="kicker">工序工步 {i+1:02d} · {cat}</span>
      <h3>{t}</h3>
      <p style="margin-top:10px;color:var(--muted);font-size:1.01rem;line-height:1.6">{d}</p>
      <ul class="check-list" style="margin-top:14px">{bullet_items}</ul>
      <div class="split-meta"><span>{meta.split(':')[0]}:</span> {meta.split(':', 1)[1].strip()}</div>
    </div>"""
        inner = img + txt if i % 2 == 0 else txt + img
        step_html += f'\n  <div class="split reveal" style="margin-bottom:36px">{inner}</div>'

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 关于我们</div>
  <h1>关于青岛拉博尔包装设备有限公司 / 远洋木业</h1>
  <p class="lead">在现代全球工业供应链中，包装不仅是一道保护外壳，更是决定装备资产运输安全、控制跨国综合物流成本、提升海外终端客户交付体验的核心基石。</p>
</div></div>

<section><div class="wrap" style="max-width:860px">
  <div class="reveal">
    <p>青岛拉博尔包装设备有限公司（Qingdao Lumber &amp; Packaging Co., Ltd.）创立初衷，正是为了以更具竞争力的中国制造效率、美资背景的严苛工程质量标准与充裕的规模化产能，服务全球出海的高端装备制造客户。</p>
    <p style="margin-top:16px">我们始终秉持精工制造与契约精神，确保每一根木构件、每一套包装箱与每一次越洋出运，均达到严丝合缝的技术精准度与行业最高安全标准。</p>
    <p style="margin-top:16px"><strong>青岛拉博尔包装设备有限公司是一家美资独资的大型专业工业包装制造商，实体制造基地坐落于中国制造业名城——青岛。</strong></p>
    <p style="margin-top:16px">深耕工业木质包装领域 20 余年，我们将国际跨国企业成熟的品质管理规范与中国高效完备的供应链制造能力深度融合，长期服务于北美、欧洲及全球各地的工业巨头客户。</p>
    <p style="margin-top:16px">主营业务涵盖：工业级重型木箱、模块化平摊拆装箱套件（KD Kits）、特高压电力绝缘子专用木箱、新能源危包木箱及各类高难异形重载工业防护总成。</p>
    <p style="margin-top:16px">全系产品 100% 严格执行国际 ISPM-15 检疫热处理标准，并具备中国出入境检验检疫局官方核准加施 IPPC 标识资质，国际通关畅行无阻。</p>
    <p style="margin-top:16px">截至目前，我们已累计为全球客户成功制造并交付超过 <strong>500 万套优质包装箱</strong>，成为跨国高端制造业值得长期信赖的木质包装 OEM 战略合作伙伴。</p>
  </div>
  <div class="stat-row">
    <div class="stat reveal"><div class="n">20+ 年</div><div class="l">专注工业木包装 OEM 积淀</div></div>
    <div class="stat reveal"><div class="n">500万+ 套</div><div class="l">全球累计安全交付箱体</div></div>
    <div class="stat reveal"><div class="n">100%</div><div class="l">符合国际 ISPM-15 检疫标准</div></div>
  </div>
  <div class="reveal">
    <p>当下，跨国装备制造企业普遍面临越洋运费居高不下、长途多式联运货损频发及海外目的港清关标准严苛等多重挑战。</p>
    <p style="margin-top:16px">我们正是通过标准化结构工程设计、大批量集约化下料加工及平摊拆装优化方案，有效帮助客户降低越洋占箱体积、缩短海外组装工时，真正实现“强防护、低运费、快交付”。</p>
    <p style="margin-top:16px">无论是根据客户既有图纸进行大批量 OEM 代工，还是针对全新非标重型设备进行从零开始的量身定制，我们均能提供涵盖力学计算、CAD画图、样品试装到批量稳定供应的一站式服务。</p>
    <p style="margin-top:16px">我们始终视自身为客户全球供应链不可分割的重要延伸，以严谨工匠精神守护客户每一台高价值设备安全抵达全球目的地。</p>
  </div>
</div></section>

<section style="padding:0 0 64px"><div class="wrap">
  <div class="grid g2" style="gap:32px">
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-factory-aerial.webp" alt="青岛即墨10万平米大型现代化木质包装实体生产基地航拍俯视图" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">青岛大型实体制造基地</span>
        <h3>即墨生产制造基地 · 青岛</h3>
        <p>占地超过 100,000 平米的现代化综合制造厂区，配备全自动数控木工加工中心群、金属构件激光焊接车间及多座经官方备案核准的大型 ISPM-15 环保标准热处理窑炉。</p>
        <ul class="check-list" style="margin-top:14px">
          <li>100,000+ 平米实体厂房与万方级全干型原材料储备露天堆场</li>
          <li>自动化 CNC 高精多轴木工下料、电子裁板及自动化钻铣产线</li>
          <li>多座大型自备热处理烘干窑炉，全天候保障出口货物检疫合规时效</li>
        </ul>
        <div class="tag-row">
          <span>10万+平米实体基地</span>
          <span>数控自动化生产</span>
          <span>自建ISPM-15热处理窑</span>
        </div>
      </div>
    </div>
    <div class="facility-card reveal">
      <div class="ph">
        <img src="{rel}assets/img/about-team-group.webp" alt="青岛拉博尔包装设备有限公司资深管理、工程设计与专业技术工人团队合影" loading="lazy">
      </div>
      <div class="bd">
        <span class="kicker">专业工程与运营团队</span>
        <h3>专业 OEM 包装工程与运营团队</h3>
        <p>汇聚从业 20 余年的资深包装结构工程师、CAD/CAM 力学仿真专家、严苛质检主管及外贸出运专家，以扎实经验与严密协同护航客户全球项目的卓越交付。</p>
        <ul class="check-list" style="margin-top:14px">
          <li>20 余名经验丰富的工业包装工程设计师与力学仿真专家</li>
          <li>贯穿进料、下料、组装、测试的全流程三级严格质检验收体系</li>
          <li>熟练对接欧美客户技术标准与严苛合规要求的专业双语服务团队</li>
        </ul>
        <div class="tag-row">
          <span>20+年行业经验</span>
          <span>严格全流程质检</span>
          <span>全球项目双语对接</span>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2 class="section-title reveal">从图纸到交付 · 七大受控制造工序</h2>
  <p class="section-sub reveal">严谨遵循七大受控工程阶段，确保每一套交付出厂的工业木包装系统兼具极高尺寸公差精度与坚如磐石的防护性能。</p>
{step_html}
</div></section>
""" + cta_band_zh(rel, "携手值得信赖的工业包装战略伙伴",
                  "告诉我们您正在出运的货物详情——我们的工程师团队将在 1 个工作日内提供量身定制的初步工程结构方案。")
    return page_zh(rel, "about", "关于我们 | 20+年专注高可靠OEM工业木包装制造 — 青岛拉博尔 / 远洋木业",
                   "美资独资专业 OEM 工业木包装制造商，青岛即墨10万平米制造基地。20余年深耕工业定制木箱，累计安全交付超500万套包装箱，服务跨国重型装备与高精密制造客户。", body)

# ================= CASE STUDIES ZH =================
def build_case_studies_zh():
    rel = "../../"
    cases_zh = [
        ("高价值数据中心服务器机柜",
         "三维多轴抗震阻尼隔振内衬系统，针对海运低频持续颠簸提供极限吸能，消除硬盘主轴与接插件在途微位移。",
         "依据原厂 3D CAD 真实设备重心量身定制内部自锁支撑，确保服务器机柜直抵海外云机房即插即用，零调试货损。",
         "case-data-server.webp", "带有高灵敏度防震提示标识的高价值数据中心服务器木箱"),
        ("特高压输变电高等级绝缘子",
         "多层阶梯卡槽隔离箱体结构，垂直方向抵御超强动载堆码挤压，彻底杜绝易碎绝缘伞裙边缘相互碰撞崩边隐裂。",
         "替代传统松散笨重低效木框，在提升抗冲击安全性的同时减轻单箱自重 25%，为跨国电网EPC总包大幅节约运费。",
         "case-glass-insulator.webp", "大批量整齐装箱的特高压钢化玻璃与电瓷绝缘子出口木箱"),
        ("重型网络机柜模块化拆装箱 (KD)",
         "高强度激光钣金角码构件与 CNC 精准下料箱板，支持以平板紧凑状态跨国大批量集装箱海运运输。",
         "平摊出运模式将海运空箱占用体积减少高达 60%，抵达海外目的地后仅需标准扳手即可实现数分钟无损快速拼接复原。",
         "case-server-rack-kd.webp", "平摊堆叠发货的模块化拆装式机柜木箱套件"),
        ("大型工业增材制造设备与机床",
         "刚性重型框架方木底托复合工字槽钢梁，结合内壁阻尼限位，全方位保护设备精密光栅尺、主轴伺服及温控系统。",
         "箱内配置全密封抽真空复合铝箔袋与大量环保干燥剂，全天候抵御数月远洋海运高温高湿高盐雾恶劣海况。",
         "case-industrial-printer.webp", "专为工业级数控增材机床定制的高密闭重型框架木箱"),
        ("新能源大功率充电桩与储能设备",
         "定制高重心防倾覆斜向自锁撑杆与专用吊装吊带卡位槽，底部重载滑木兼容各类码头叉车与起重机高频转运。",
         "符合海外电力入网设备严苛出厂规范，确保大尺寸触摸控制屏、高压母排及内部电路板百分之百完好无损。",
         "case-ev-charging.webp", "装载大功率新能源汽车充电桩的出口专用定制木箱"),
        ("国际跨国搬迁重型储运 Liftvan 木箱",
         "严格符合 ISPM-15 国际检疫标准的重型免熏蒸/热处理结构，标准化尺寸专为 40 尺超高集装箱致密装柜定制开发。",
         "超高抗压堆码性能支持集装箱内 2 层安全叠放，箱板可反复拆卸重复循环使用，显著提升长期物流周转综合效益。",
         "case-relocation-liftvan.webp", "码头堆场整齐码放的国际重型搬迁与仓储定制 Liftvan 包装箱"),
    ]

    def case_card_zh(app, focus, value, img, alt):
        inner = f"""
      <span class="kicker">实际工程应用场景</span>
      <h3>{app}</h3>
      <p style="margin-top:10px"><strong>工程设计核心:</strong> {focus}</p>
      <p style="margin-top:8px;color:var(--muted)"><strong>客户核心价值:</strong> {value}</p>"""
        return f"""    <div class="card reveal"><div class="ph portrait"><img src="{rel}assets/img/{img}" alt="{alt}" loading="lazy"></div>
      <div class="bd">{inner}</div></div>"""

    grid_cards = "\n".join(case_card_zh(*c) for c in cases_zh)

    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / 应用案例与定制咨询</div>
  <h1>工业包装工程实践案例与定制方案咨询</h1>
  <p class="lead">深入了解我们在全球数据中心基建、新能源汽车电池、特高压电力输送及重型工业装备领域的真实工程落地案例，见证我们在结构安全性、越洋减容降本与可靠品质上的专业实力。</p>
</div></div>

<section><div class="wrap">
  <h2 class="section-title reveal">深耕重点行业 · 赋能装备出海</h2>
  <p class="section-sub reveal">精选我们为国内外跨国工业制造客户设计并批量交付的部分代表性出口包装系统。</p>
  <div class="grid g3">{grid_cards}</div>
</div></section>

<section class="band" id="rfq"><div class="wrap" style="max-width:880px">
  <h2 class="section-title reveal" style="text-align:center">立即获取工业包装工程定制方案</h2>
  <p class="section-sub reveal" style="text-align:center;margin-bottom:32px">
    告诉我们您的被包装设备尺寸、重量、出运目的地或特殊防护要求，我们的包装工程师将在 <strong>1 个工作日内</strong> 为您提供专业的工程结构建议与初步预算。
  </p>
  <form class="rfq reveal in" id="rfqForm" onsubmit="event.preventDefault(); document.getElementById('formNote').innerHTML='<p style=\"color:var(--g600);font-weight:700;margin-top:12px;text-align:center\">感谢您的垂询！我们的包装工程师已收到您的需求，将在 1 个工作日内与您取得联系并提供专属方案。</p>'; this.reset();">
    <div class="form-grid">
      <div class="field"><label for="fName">您的姓名 *</label><input id="fName" name="name" type="text" required autocomplete="name" placeholder="例如：李经理 / 张工"></div>
      <div class="field"><label for="fEmail">业务电子邮箱 *</label><input id="fEmail" name="email" type="email" required autocomplete="email" placeholder="name@company.com"></div>
      <div class="field"><label for="fPhone">联系电话 / 微信 / WhatsApp</label><input id="fPhone" name="phone" type="tel" autocomplete="tel" placeholder="+86 138-0000-0000"></div>
      <div class="field"><label for="fCompany">企业 / 公司名称 *</label><input id="fCompany" name="company" type="text" required autocomplete="organization" placeholder="例如：某某精密机械制造有限公司"></div>
      <div class="field full"><label for="fCountry">出运目的地 / 目的国家</label><input id="fCountry" name="country" type="text" autocomplete="country-name" placeholder="例如：出口美国洛杉矶港 / 德国汉堡 / 东南亚 / 中国境内转运"></div>
      <div class="field full"><label for="fNeed">设备详情与防护需求（长×宽×高、单件重量、批次数量、是否需要VCI防锈、减震或危包等）*</label><textarea id="fNeed" name="requirements" rows="5" required placeholder="请尽可能详尽描述您的需求，例如：我们有一批数控加工机床出口欧洲，尺寸为 3200×1800×2200mm，单台重约 8.5吨，海运周期约 40天，需要抽真空防锈包装和模块化可拆装箱方案..."></textarea></div>
    </div>
    <div style="margin-top:22px;text-align:center">
      <button class="btn btn-green" type="submit" style="min-width:240px;font-size:16px;padding:14px 36px">提交定制咨询</button>
    </div>
    <div class="form-note" id="formNote" role="status"></div>
    <p style="margin-top:16px;font-size:.88rem;color:var(--muted);text-align:center">
      如需发送详细产品 CAD 图纸或加急咨询，欢迎直接发信至 <a href="mailto:{EMAIL}" style="color:var(--g700);font-weight:700">{EMAIL}</a> 或添加业务经理微信 / WhatsApp：<a href="{WA_LINK}" target="_blank" rel="noopener" style="color:var(--g700);font-weight:700">+86 134-0510-1358</a>。
    </p>
  </form>
</div></section>
"""
    return page_zh(rel, "case-studies", "客户案例与定制咨询 | 工业包装工程实效落地 — 青岛拉博尔 / 远洋木业",
                   "查看我们在数据中心服务器、特高压绝缘子、重型机床装备、新能源汽车电池等领域的真实工业包装定制案例，提供在线结构方案与报价咨询。", body)


# ================= INDUSTRY PAGES ZH =================
INDUSTRY_FEATURE_IMAGES = {
    "data-servers-precision-electronics": ("case-data-server.webp", "专为数据中心服务器与精密电子定制的高可靠防震木箱"),
    "ev-battery-charging": ("solutions-battery-crates.webp", "符合UN38.3国际危险品运输认证的高承重锂电池包装木箱"),
    "industrial-machinery-infrastructure": ("case-industrial-printer.webp", "针对大型精密机械与能源基础设施定制的高强度重型实木框架箱"),
    "high-voltage-insulators-power-transmission": ("case-glass-insulator.webp", "专为特高压脆性钢化玻璃与电瓷绝缘子设计的抗压防撞隔离木箱"),
}

def industry_page_zh(slug, short, h1, title, desc, intro_paras, approach, solutions, challenges, scope, objective):
    rel = "../../../"
    paras = "\n".join(f"    <p style=\"margin-top:14px\">{p}</p>" for p in intro_paras)
    sol = "\n".join(f"      <li>{s}</li>" for s in solutions)
    cha = "\n".join(f"      <li>{c}</li>" for c in challenges)
    sco = "\n".join(f"      <li>{s}</li>" for s in scope)
    wa_text = quote(f"您好，我想深入了解青岛拉博尔关于【{short}】的定制包装解决方案。")
    img_fn, img_alt = INDUSTRY_FEATURE_IMAGES.get(slug, ("knockdown-kits-flatpack.webp", short))
    body = f"""
<div class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{rel}zh/">首页</a> / <a href="{rel}zh/industries/data-servers-precision-electronics/">细分行业</a> / {h1.split('|')[0].strip()}</div>
  <h1>{h1}</h1>
  <p class="lead">{objective}</p>
</div></div>

<section><div class="wrap">
  <div class="split reveal" style="margin-bottom:20px">
    <div class="ph"><img src="{rel}assets/img/{img_fn}" alt="{img_alt}" loading="lazy"></div>
    <div class="split-content">
      <span class="kicker">行业应用综述</span>
      <h3 style="margin-bottom:14px">{short}</h3>
      {paras}
      <div class="split-meta"><span>出海检疫标准:</span> 100% ISPM-15 国际植物检疫认证 · 加施官方 IPPC 永久标识</div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap" style="max-width:960px">
  <h2 class="section-title reveal">工程防护体系与技术路线</h2>
  <p class="section-sub reveal">{approach}</p>
  <h3 class="reveal" style="margin:34px 0 6px;color:var(--g700)">核心包装解决方案涵盖</h3>
  <ul class="check-list reveal">{sol}</ul>
</div></section>

<section><div class="wrap" style="max-width:960px">
  <div class="grid g2">
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">攻克的核心运输痛点</h3>
      <ul class="check-list">{cha}</ul></div>
    <div class="tcard reveal"><h3 style="margin-bottom:12px;color:var(--g700)">适用装备与产品范畴</h3>
      <ul class="check-list">{sco}</ul></div>
  </div>
  <div style="margin-top:40px;text-align:center">
    <a class="btn btn-green" href="{rel}zh/case-studies/#rfq">获取该行业专属包装方案</a>
    <a class="btn btn-ghost" style="color:var(--g700);border-color:var(--line);margin-left:12px" href="{WA_LINK}?text={wa_text}" target="_blank" rel="noopener">微信 / WhatsApp 在线沟通</a>
  </div>
</div></section>"""
    return page_zh(rel, "industries/" + slug, title, desc, body)

def build_industries_zh():
    pages = {}

    pages["data-servers-precision-electronics"] = industry_page_zh(
        "data-servers-precision-electronics", "数据中心服务器与精密电子",
        "数据中心服务器与精密电子出口木质包装解决方案",
        "数据中心服务器与精密电子出口包装 | 定制抗震防静电木箱 — 青岛拉博尔 / 远洋木业",
        "专为机架式服务器、刀片存储阵列及高精密电子设备打造的高稳定性木质包装系统，三维限位吸能阻尼，零内部位移，全面抵御远洋海运振动风险。",
        ["数据中心整机柜服务器、存储阵列、高端交换机及精密电力电子设备在跨国远洋多式联运中面临严苛考验。航运过程中持续不断的低频微振动与突发冲击，极易导致高灵敏度机械硬盘坏道、BGA 芯片虚焊、光纤接插件微位移或整机电路板接触不良。此外，跨洋温湿交变极易在箱内形成冷凝水，引发电子元器件氧化短路。",
         "对于全球云基础设施服务商与大型服务器 OEM 厂商而言，包装不仅要具备极致的抗冲击与防潮性能，还必须保证大批量交付的绝对尺寸一致性与极高的开箱便利性——确保成百上千台机柜抵达海外目的地机房后即可快速安全就位，杜绝现场拆解返工。"],
        "我们专注于为高价值电子与服务器设备提供三维抗震阻尼木质包装系统，将高刚性实木框架受力底托与高分子吸能缓冲材料深度融合，实现货物在运输途中的“零内部位移”。",
        ["量身定制的服务器专用整机木箱，完美匹配 19英寸/21英寸 标准机架、2U–8U 高密服务器、GPU 算力集群及储能配电柜",
         "采用多轴 CNC 精密切割的高密度阻燃 EPE 珍珠棉与闭孔 EVA 缓冲构件，实现设备上下、前后、左右六个维度的立体自锁限位",
         "轻量化与高强度兼顾的复合木箱设计，在满足严苛国际航运防护测试的前提下最大限度削减包装皮重与空运海运成本",
         "模块化平摊可拆装（KD Flat-Pack）箱体结构，大幅降低跨国海运货柜占用空间与海外机房就地拆箱难度",
         "全系标配高规格附加防护：永久防静电衬垫、铝箔抽真空热封气密袋、饱和吸附干燥剂组及外箱防震/防倾斜监控标签"],
        ["杜绝远洋海运数千海里持续低频颠簸对机械硬盘与精密晶体振荡器造成的隐性物理损伤",
         "确保整台服务器机柜直抵海外机房即可插电开机部署，大幅缩短现场调试上线工期",
         "彻底阻隔高盐雾海洋湿气侵蚀，维持高精密传感器与工控主板出厂级精度指标"],
        ["云数据中心与企业级服务器（机架式服务器、刀片服务器、存储阵列、GPU 深度学习集群）",
         "工业自动化控制系统、高精度 PLC 柜与智能仪器仪表",
         "高精电网逆变电源与高端通信基站机柜",
         "精密测试分析仪器与实验室专用测量装备",
         "人工智能边缘计算一体机与超级算力模块"],
        "提供尺寸精密、三维隔振、零内部晃动的 OEM 级工业木包装整体解决方案，确保每一台高价值精密电子装备在全球航运长途跋涉后完好无损、即装即用。")

    pages["ev-battery-charging"] = industry_page_zh(
        "ev-battery-charging", "新能源动力电池与充电设施 · UN38.3",
        "新能源动力电池与充电桩设备出口木包装解决方案 | UN38.3 认证合规",
        "新能源电池与充电桩出口木箱包装 | UN38.3 锂电池危险品包装认证 — 青岛拉博尔 / 远洋木业",
        "重型高承载、符合国际 UN38.3 危险品海空运测试标准的木包装系统，专为高压锂电池包及大功率充电桩设计，提供合规可靠的出口防护保障。",
        ["伴随全球新能源产业的高速爆发，两大核心装备的出海包装标准极为严苛：高压锂离子动力电池组（模组/PACK）与大功率超充设施。两者皆属于高货值、高技术密度且对运输安全性高度敏感的工业产品。",
         "根据国际海事危规（IMDG Code），锂电池被严格列为第 9 类危险品（UN3480 / UN3481），运输中任何机械撞击、剧烈颠簸或受挤压变形，均可能导致电芯隔膜破裂引起热失控起火。而大型直流充电桩通常自重大、重心高，外壳漆面、大尺寸液晶触控屏及内部液冷回路在长途颠簸中极易受到机械性损伤。",
         "对于动力电池制造商、主机厂及储能充电运营巨头而言，包装必须提供毫不妥协的机械防护硬实力、完备的危险品检测合规资质及极其稳定的批次保供。"],
        "我们针对新能源装备的物理特性与全球安规标准，专门开发了高可靠木包装系统。将重载抗弯底座与高绝缘、阻燃阻尼构件深度整合，全方位兼顾电池安全防爆与充电桩重型防护要求。",
        ["<strong>针对动力电池包 (EV Battery):</strong> 重型实木框架加强底梁，内置阻燃防静电多层绝缘内衬与电芯间隙自锁吸能阻尼，完全符合国际 UN38.3 危险品包装性能检验测试",
         "<strong>针对大型充电设施 (Charging Station):</strong> 超大规格非标框架箱，配置重心抗倾覆斜拉自锁加强撑，显示屏与功率电子模块定制减震保护气囊",
         "复合型轻量化结构，兼顾极高机械扭剪刚度与合理自重，有效控制远洋货运总体运费",
         "模块化平摊拆装（KD）可选方案，大幅减少海外目的港包装套件的空箱仓储与空柜调转成本",
         "支持加装三维冲击记录仪（ShockWatch）、防倾斜标签与温湿度全程监控芯片",
         "数控 CNC 毫米级雕刻凹槽与定位销，实现电池包机械极柱零碰触与重心严密卡固"],
        ["彻底消除跨国海运与公路长途运输中电芯受损与锂电池热失控风险",
         "保护高功率充电桩内部高压接触器、母排接口及外部防爆触控屏免受冲击挤压",
         "100% 满足海关危险品包装使用鉴定要求，避免货物因包装瑕疵滞留海外港口产生高额滞期费",
         "显著减少因运输微损伤导致的海外项目现场安装故障率与高昂售后索赔成本"],
        ["乘用车、商用车动力电池包（PACK）及户用/工商业大型储能电池柜（ESS）",
         "刀片电池、方形铝壳电池、软包及大圆柱电池模组",
         "大功率直流快充桩（60kW–480kW+）及超充液冷动力柜",
         "交流壁挂式充电桩、充电立柱与智能低压配电控制柜",
         "光储充一体化特种集装箱内置精密储能逆变单元"],
        "提供具备国际危包资质、极端工况安全可靠的定制木包装工程方案，确保新能源电池与充电装备全球畅运无阻，筑牢品牌出海质量口碑。")

    pages["industrial-machinery-infrastructure"] = industry_page_zh(
        "industrial-machinery-infrastructure", "重型装备制造与能源基建",
        "重型工业装备、机床与能源基建大型木包装解决方案",
        "重型机械装备与能源基建出口木质包装 | 大型定制重载框架箱 — 青岛拉博尔 / 远洋木业",
        "针对数十吨级重型机械、精密机床及电力基础设施设备研发的重载工程木包装，超强抗弯承重主梁与激光下料钣金结合，提供顶级防护性能。",
        ["大型机械装备、重型发电设备及重大工业基础设施构件通常具有单体体量大、自重极重（数十吨级）、偏载严重且属于高资本投入等显著特征。这类装备往往内部集成高精度导轨、精密主轴、伺服驱动及液压管路，在跨国海运中极易受到强烈振动、交变惯性力、重度盐雾腐蚀及粉尘侵入。",
         "任何海运途中的微量形变或碰撞损伤，都将造成数以百万计的现场停工损失与冗长的越洋索赔周期。对于全球 EPC 工程总包方与大型装备制造商而言，包装系统必须具备无可挑剔的极限承载强度，同时兼容码头重型起重机安全吊运与多式联运标准。"],
        "我们针对重型装备的物理力学特征，量身研发重型实木主梁与高强钣金复合包装系统。结合有限元（FEA）受力计算与高强度结构螺栓，确保数十吨装备安全抵港交付。",
        ["重型实木框架木箱，基座采用大断面高密硬木方梁复合工业槽钢，具备极强的抗弯抗扭剪承载力",
         "根据每台设备的重心偏心率与脆弱薄弱点，量身定制专用木质支撑托块、斜向自锁撑杆与柔性缓冲隔离层",
         "关键机加工面与运动部件采用多层复合防护：重载防锈油脂、减震橡胶垫板与气密性抽真空复合铝塑袋",
         "防雨防水耐候外壳设计，箱顶设有人字形防积水排水斜坡，外罩防紫外线高强度热缩防护膜，适应长期露天存放",
         "底座集成一体化重型叉车槽位与高强度起重吊带预留导向孔，确保码头吊装安全稳妥",
         "支持模块化现场快速拆装组装，有效优化远洋海运装船与滚装装载方案",
         "可选配外挂撞击与倾斜监控记录装置，全程溯源航运物流状态"],
        ["防止大型数控机床、发电机转子及电力变压器在海上颠簸中发生微米级主轴位移或几何形变",
         "杜绝超大超宽设备在多式联运吊装转换环节出现箱体解体、受力失衡或底托断裂风险",
         "全天候严密阻隔数月远洋高盐雾、热带高湿环境对精密金属表面的腐蚀氧化",
         "确保海外国家重点基建项目关键设备按期原样抵港，保障安装调试节点零延误"],
        ["重型工业母机（大型 CNC 机床、精密注塑机、大型印刷机械、高压泵阀及空压机组）",
         "电力发电与输变电设备（大容量发电机、特高压变压器、高压开关柜及成套电控系统）",
         "重大基础设施工程构件（桥梁钢构附件、风力发电机核心零部件、矿山重型破碎机械）",
         "大型水处理成套设备、石化管道阀门总成及离合驱动机构",
         "海工装备及重型工程机械出口模块"],
        "提供高承载、高可靠的工业级重载木包装工程方案，确保高价值装备资产全球长途海运航程万无一失，为中国重工智造走向世界保驾护航。")

    pages["high-voltage-insulators-power-transmission"] = industry_page_zh(
        "high-voltage-insulators-power-transmission", "特高压绝缘子与输变电设备",
        "特高压电瓷绝缘子与输变电设备出口定制木包装系统",
        "特高压绝缘子出口木箱包装 | 钢化玻璃与电瓷电力器材专用木箱 — 青岛拉博尔 / 远洋木业",
        "专为脆性特高压钢化玻璃与电瓷绝缘子量身研发的阶梯卡槽隔离包装木箱，抗挤压分层限位，海运破损率降低98%以上，保障国家电网出海项目安全交付。",
        ["特高压输变电线路中广泛应用的悬垂绝缘子、电瓷套管及高等级钢化玻璃绝缘子，属于典型的“高硬度、高脆性、大自重、超高价值”特种电力设备。在跨国长途海运中，成千上万片绝缘子通常进行密集装柜堆叠，运输过程中的振动颠簸、惯性侧倾极易引发边缘相互剧烈撞击。",
         "哪怕极微小的伞裙边缘崩缺或肉眼难辨的内部隐裂，都会导致特高压高电场强度下发生闪络击穿或绝缘击碎，造成电网工程严重的投运安全隐患与整批退货损失。为此，绝缘子包装必须具备极为卓越的分层隔离定位、多轴吸能缓冲与超强抗挤压堆码刚度。"],
        "我们自主设计研发了专用梯级卡槽式防碰触隔离木包装系统，将整体刚度框架与弧形仿形支撑深度结合，实现每串绝缘子在海运途中的“零硬碰硬接触”。",
        ["重型加强型木箱主体结构，具备优异的抗共振阻尼特性，显著衰减远洋海运交变冲击能量",
         "精密数控开模仿形卡槽内胆，精准贴合电瓷与钢化玻璃绝缘子几何弧度，每串绝缘子实现分层独立锁固",
         "接触面加装高密度高阻尼闭孔缓冲胶垫与防磨损隔离片，彻底杜绝运输微晃动造成的漆面划伤与边缘崩边",
         "底部配置重载双向滑木底托与角码加强件，单箱静载堆码强度通过三层以上严格垂直抗压测试",
         "箱体设计通风防潮微孔通道，有效避免远洋高湿海风引发绝缘子金属金具氧化锈蚀与瓷件表面水雾冷凝",
         "人性化快速滑道取放设计，海外电网项目现场施工人员数分钟内即可无损拆箱吊装取用",
         "可选装国际通用的三维碰撞指示标签与防倾斜监控装置"],
        ["彻底杜绝玻璃和电瓷高压绝缘子在长途海陆联运过程中的崩边、隐裂、脱扣与粉碎性破损",
         "根除微观隐性内伤，保障特高压输变电线路带电耐压试验一次性成功通过",
         "相比传统粗放型劣质木箱，在大幅提升防护等级的同时优化装载体积，海运破损率降低 98% 以上",
         "保障海外国家电网大型总承包工程关键节点如期交付，消除昂贵的海外紧急调件与工期索赔成本"],
        ["特高压高等级电瓷与钢化玻璃悬垂绝缘子（盘形悬式、棒形支柱式、线路针式等）",
         "高压电网大型瓷套管、避雷器套管及变压器套管总成",
         "电网用复合绝缘子与耐张绝缘子串组装套件",
         "氧化锌避雷器、隔离开关触头及高精度母线支撑柱",
         "大口径特高压绝缘管母线及电抗器专用绝缘配件"],
        "树立特高压脆性高精电力设备出海包装行业标杆，以零破损、高堆叠、快组装的优质性能，护航全球电力基建宏伟蓝图。")

    return pages


# ================= WRITE & MAIN ZH =================
def write_zh(path, content):
    full = os.path.join(OUT, "zh", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote zh/" + path, len(content), "bytes")

def generate_chinese_site():
    print("--- Building Chinese Site (zh/) ---")
    write_zh("index.html", build_home_zh())
    write_zh("solutions/index.html", build_solutions_zh())
    write_zh("capabilities/index.html", build_capabilities_zh())
    write_zh("about/index.html", build_about_zh())
    write_zh("case-studies/index.html", build_case_studies_zh())
    for slug, html in build_industries_zh().items():
        write_zh(f"industries/{slug}/index.html", html)
    print("--- Chinese Site Generation Completed ---")

if __name__ == "__main__":
    generate_chinese_site()
