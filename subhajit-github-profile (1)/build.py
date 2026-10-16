import base64, hashlib, math, os, zipfile, shutil

SRC = '/mnt/user-data/uploads/Gemini_Generated_Image_vsqhl9vsqhl9vsqh.png'  # id portrait, embedded byte-for-byte
OUT = '/home/claude/pkg'
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/assets')
B64 = base64.b64encode(open(SRC, 'rb').read()).decode()

NAVY, BLUE, RED, INK, MUTED = '#070b16', '#247bff', '#ff354f', '#f4f6ff', '#aab5d1'
USER, NAME = 'subhajit-ghanta', 'SUBHAJIT'
LI = 'https://www.linkedin.com/in/subhajit-ghanta-745606380/'
GH = 'https://github.com/subhajit-ghanta'

BASE = '''.§d{font-family:"Bebas Neue","Oswald","Arial Narrow",Impact,"Helvetica Neue",Arial,sans-serif;font-weight:800;letter-spacing:.5px}
.§s{font-family:"Inter","Segoe UI",system-ui,-apple-system,Roboto,"Helvetica Neue",Arial,sans-serif}
.§m{font-family:ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
'''


def wrap(p, W, H, body, css, title, desc, defs=''):
    css = (BASE + css).replace('§', p)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{p}t {p}d">
<title id="{p}t">{title}</title><desc id="{p}d">{desc}</desc>
<defs><style>{css}</style>
<linearGradient id="{p}hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{RED}"/></linearGradient>
<linearGradient id="{p}acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{RED}"/></linearGradient>
<pattern id="{p}dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#fff" fill-opacity=".07"/></pattern>
<linearGradient id="{p}rimB" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}" stop-opacity=".28"/><stop offset=".4" stop-color="{BLUE}" stop-opacity="0"/></linearGradient>
<linearGradient id="{p}rimR" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="{RED}" stop-opacity=".26"/><stop offset=".4" stop-color="{RED}" stop-opacity="0"/></linearGradient>
<clipPath id="{p}frame"><rect width="{W}" height="{H}" rx="28"/></clipPath>
{defs}</defs>
<g clip-path="url(#{p}frame)"><rect width="{W}" height="{H}" fill="{NAVY}"/><rect width="{W}" height="{H}" fill="url(#{p}dots)"/>
{body}</g>
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="27.5" fill="none" stroke="url(#{p}hair)" stroke-width="1.5" stroke-opacity=".85"/>
</svg>'''


def portrait(p, x, y, w, r=20, src=(64, 20, 896, 840)):
    """Original PNG placed unmodified; only cropped by a clip (excludes the corner watermark)."""
    sx, sy, sw, sh = src
    sc = w / sw
    h = sh * sc
    cid = f'{p}pc'
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h:.2f}" rx="{r}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><image href="data:image/png;base64,{B64}" x="{x - sx * sc:.2f}" y="{y - sy * sc:.2f}" '
            f'width="{1024 * sc:.2f}" height="{1024 * sc:.2f}" preserveAspectRatio="none"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h:.2f}" fill="url(#{p}rimB)"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h:.2f}" fill="url(#{p}rimR)"/></g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h:.2f}" rx="{r}" fill="none" stroke="url(#{p}hair)" stroke-width="1.5"/>'), h


# ---------------------------------------------------------------- hero
def hero():
    p = 'hr'
    port, ph = portrait(p, 622, 64, 240)
    greet = "hello, world. I'm"
    chars = ''.join(
        f'<tspan class="{p}ch" style="animation-delay:{0.3 + i * 0.06:.2f}s">{"&#160;" if c == " " else c}</tspan>'
        for i, c in enumerate(greet))
    roles = ['Data Analyst', 'Machine Learning Engineer', 'Analytics · Machine Learning · Python']
    sizes = [30, 30, 25]
    rtxt = ''.join(
        f'<text class="{p}s {p}role {p}r{i + 1}" x="56" y="256" font-size="{sizes[i]}" font-weight="800" fill="{BLUE}" '
        f'style="animation-delay:{2.4 + i * 3.5:.1f}s">{r}</text>' for i, r in enumerate(roles))
    pitch = ["I'm passionate about Data Analytics, Machine Learning, and Python.",
             "I enjoy transforming raw data into meaningful insights and",
             "building intelligent solutions that solve real-world problems."]
    ptxt = ''.join(f'<text class="{p}s" x="56" y="{302 + 25 * i}" font-size="15" fill="{MUTED}">{t}</text>' for i, t in enumerate(pitch))
    css = '''
.§ch{animation:§in .01s steps(1) both}
@keyframes §in{from{opacity:0}to{opacity:1}}
.§rise{animation:§up 1.1s cubic-bezier(.2,.8,.2,1) .9s both}
@keyframes §up{from{transform:translateY(120px)}to{transform:translateY(0)}}
.§bar{transform-box:fill-box;transform-origin:left center;animation:§grow .9s ease-out 1.7s both}
@keyframes §grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.§role{opacity:0;animation:§cyc 10.5s linear infinite backwards}
.§r1{opacity:1}
@keyframes §cyc{0%{opacity:0;transform:translateY(10px)}3%{opacity:1;transform:translateY(0)}30%{opacity:1}33.3%{opacity:0}100%{opacity:0}}
.§fade{animation:§fd .8s ease-out both}
@keyframes §fd{from{opacity:0}to{opacity:1}}
.§float{animation:§fl 7s ease-in-out 2s infinite}
@keyframes §fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
'''
    body = f'''
<circle cx="780" cy="130" r="150" fill="{BLUE}" fill-opacity=".10"/><circle cx="640" cy="390" r="120" fill="{RED}" fill-opacity=".08"/>
<text class="{p}m" x="56" y="76" font-size="19" fill="{MUTED}">{chars}</text>
<clipPath id="{p}nm"><rect x="40" y="100" width="540" height="112"/></clipPath>
<g clip-path="url(#{p}nm)"><g class="{p}rise"><text class="{p}d" x="56" y="192" font-size="104" textLength="450" lengthAdjust="spacingAndGlyphs" fill="{INK}">{NAME}</text></g></g>
<rect class="{p}bar" x="56" y="212" width="110" height="4" rx="2" fill="url(#{p}acc)"/>
{rtxt}
<g class="{p}fade" style="animation-delay:1.9s">{ptxt}</g>
<g class="{p}fade" style="animation-delay:2.2s">
<rect x="56" y="380" width="122" height="34" rx="17" fill="#0e1630" stroke="url(#{p}hair)" stroke-opacity=".8"/>
<path d="M76 389c-4 0-7 3-7 7 0 5 7 12 7 12s7-7 7-12c0-4-3-7-7-7z" fill="none" stroke="{BLUE}" stroke-width="1.8"/><circle cx="76" cy="396" r="2.5" fill="{RED}"/>
<text class="{p}m" x="92" y="402" font-size="14" fill="{INK}">Kolkata</text>
<rect x="190" y="380" width="360" height="34" rx="17" fill="#0e1630" stroke="url(#{p}hair)" stroke-opacity=".8"/>
<text class="{p}m" x="208" y="402" font-size="13" fill="{INK}">Data Analytics · Machine Learning · Python</text></g>
<g class="{p}float"><rect x="636" y="78" width="240" height="{ph:.2f}" rx="20" fill="none" stroke="{RED}" stroke-opacity=".55" stroke-width="1.5"/>
{port}</g>
<text class="{p}m" x="622" y="{64 + ph + 40:.0f}" font-size="14" fill="{MUTED}">@{USER}</text>'''
    return wrap(p, 900, 440, body, css, 'Subhajit, data analyst and machine learning engineer',
                'Animated intro: typed greeting, name reveal, cycling roles, pitch, location and portrait.')


# ---------------------------------------------------------------- about + interests
def about():
    p = 'ab'
    caps = ['Data Analytics &amp; Data Visualization', 'Machine Learning Model Development', 'Python Programming',
            'Data Cleaning &amp; Feature Engineering', 'SQL for Data Analysis']
    rows = ''.join(
        f'<rect x="56" y="{139 + 46 * i}" width="12" height="12" rx="3" fill="url(#{p}acc)"/>'
        f'<text class="{p}s" x="82" y="{151 + 46 * i}" font-size="18" font-weight="600" fill="{INK}">{c}</text>' for i, c in enumerate(caps))
    slides = [('Data', 'Exploration', 'Turning raw data into', 'meaningful insights.'),
              ('Open', 'Source', 'Building and sharing', 'code on GitHub.'),
              ('Real-world', 'problems', 'Intelligent solutions that', 'solve them.')]
    sl = ''
    for i, (a, b, l1, l2) in enumerate(slides):
        sl += (f'<g class="{p}sl {p}sl{i + 1}"><text class="{p}m" x="532" y="92" font-size="14" fill="{MUTED}">0{i + 1} / 03</text>'
               f'<text class="{p}d" x="532" y="158" font-size="50" fill="{INK}">{a}</text>'
               f'<text class="{p}d" x="532" y="210" font-size="50" fill="{BLUE if i != 1 else RED}">{b}</text>'
               f'<text class="{p}s" x="532" y="254" font-size="16" fill="{MUTED}">{l1}</text>'
               f'<text class="{p}s" x="532" y="278" font-size="16" fill="{MUTED}">{l2}</text></g>')
    bars = ''.join(
        f'<rect x="{532 + i * 106}" y="318" width="96" height="5" rx="2.5" fill="#1b2540"/>'
        f'<rect class="{p}pg {p}pg{i + 1}" x="{532 + i * 106}" y="318" width="96" height="5" rx="2.5" fill="url(#{p}acc)"/>' for i in range(3))
    css = '''
.§sl{opacity:0;animation-duration:12s;animation-iteration-count:infinite;animation-timing-function:linear}
.§sl1{opacity:1;animation-name:§s1}.§sl2{animation-name:§s2}.§sl3{animation-name:§s3}
@keyframes §s1{0%{opacity:1}30%{opacity:1}33.3%{opacity:0}96.6%{opacity:0}100%{opacity:1}}
@keyframes §s2{0%,30%{opacity:0}33.3%{opacity:1}63.3%{opacity:1}66.7%{opacity:0}100%{opacity:0}}
@keyframes §s3{0%,63.3%{opacity:0}66.7%{opacity:1}96.6%{opacity:1}100%{opacity:0}}
.§pg{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation-duration:12s;animation-iteration-count:infinite;animation-timing-function:linear}
.§pg1{transform:scaleX(1);animation-name:§p1}.§pg2{animation-name:§p2}.§pg3{animation-name:§p3}
@keyframes §p1{0%{transform:scaleX(0)}33.3%{transform:scaleX(1)}99.9%{transform:scaleX(1)}100%{transform:scaleX(0)}}
@keyframes §p2{0%,33.3%{transform:scaleX(0)}66.6%{transform:scaleX(1)}99.9%{transform:scaleX(1)}100%{transform:scaleX(0)}}
@keyframes §p3{0%,66.6%{transform:scaleX(0)}100%{transform:scaleX(1)}}
.§in{animation:§fd .9s ease-out both}
@keyframes §fd{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}
'''
    body = f'''
<text class="{p}d" x="56" y="92" font-size="52" textLength="330" lengthAdjust="spacingAndGlyphs" fill="{INK}">What I work on</text>
<g class="{p}in">{rows}</g>
<rect x="500" y="40" width="360" height="320" rx="24" fill="#0b1226"/><rect x="500" y="40" width="360" height="320" rx="24" fill="url(#{p}dots)"/>
<rect x="500.75" y="40.75" width="358.5" height="318.5" rx="23.5" fill="none" stroke="url(#{p}hair)" stroke-width="1.5" stroke-opacity=".85"/>
{sl}{bars}'''
    return wrap(p, 900, 400, body, css, 'What Subhajit works on',
                'Capabilities list beside a three-slide carousel: data exploration, open source, real-world problems.')


# ---------------------------------------------------------------- stack
ICONS = [('Python', 'Py', '#3776ab', '#fff'), ('Pandas', 'Pd', '#2b1a8f', '#fff'), ('NumPy', 'Np', '#4d77cf', '#fff'),
         ('Scikit-learn', 'sk', '#f7931e', '#1a1204'), ('SQL', 'SQL', '#5b6b86', '#fff'), ('MySQL', 'My', '#00758f', '#fff'),
         ('Power BI', 'BI', '#f2c811', '#1a1204'), ('Matplotlib', 'Mp', '#11557c', '#fff'), ('Django', 'Dj', '#0c6b4a', '#fff'),
         ('Git', 'Git', '#f05032', '#fff')]


def chips(p, x0, y0, maxw, items, d0):
    x, y, out = x0, y0, []
    for i, t in enumerate(items):
        w = len(t) * 8 + 28
        if x + w > x0 + maxw:
            x, y = x0, y + 40
        out.append(f'<g class="{p}chip" style="animation-delay:{d0 + i * 0.06:.2f}s"><rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="#0e1630" '
                   f'stroke="url(#{p}hair)" stroke-opacity=".7"/><text class="{p}m" x="{x + w / 2}" y="{y + 20}" text-anchor="middle" font-size="13" fill="{INK}">{t}</text></g>')
        x += w + 8
    return ''.join(out), y + 30


def _table(rx, ry, N=2000):
    pts = [(rx * math.cos(2 * math.pi * k / N), ry * math.sin(2 * math.pi * k / N)) for k in range(N + 1)]
    cum = [0]
    for k in range(N):
        cum.append(cum[-1] + math.dist(pts[k], pts[k + 1]))
    return pts, [c / cum[-1] for c in cum]


def _at(rx, ry, rot, f, tab):
    pts, cum = tab
    f %= 1
    lo, hi = 0, len(cum) - 1
    while hi - lo > 1:
        m = (lo + hi) // 2
        if cum[m] <= f:
            lo = m
        else:
            hi = m
    u = (f - cum[lo]) / (cum[hi] - cum[lo])
    x = pts[lo][0] + (pts[hi][0] - pts[lo][0]) * u
    y = pts[lo][1] + (pts[hi][1] - pts[lo][1]) * u
    th = math.radians(rot)
    return x * math.cos(th) - y * math.sin(th), x * math.sin(th) + y * math.cos(th)


def stack():
    p = 'st'
    cx, cy = 450, 282
    defs = ''
    for i, (n, m, c, fg) in enumerate(ICONS):
        w = len(n) * 7.4 + 26
        defs += (f'<g id="{p}i{i}"><rect x="{-w / 2:.1f}" y="-14" width="{w:.1f}" height="28" rx="14" fill="{c}" stroke="#fff" stroke-opacity=".3"/>'
                 f'<text class="{p}s" y="4.5" text-anchor="middle" font-size="12" font-weight="800" fill="{fg}">{n}</text></g>')
    # geometry verified for >=13 px clearance between all labelled pills over the whole loop (arc-length motion)
    orbits = [(381.57, 149.66, -11.32, [0, 3, 4, 8], 0.6751, BLUE), (236.52, 92.76, -13.01, [1, 7, 6], 0.2138, RED),
              (117.22, 45.98, -21.23, [2, 5, 9], 0.4459, '#ffffff')]
    rings = moving = static = ''
    for rx, ry, rot, idx, f0, col in orbits:
        rings += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" fill="none" stroke="{col}" stroke-opacity=".5" stroke-dasharray="3 8"/>'
        tab = _table(rx, ry)
        for k, ic in enumerate(idx):
            ex, ey = _at(rx, ry, rot, f0 + k / len(idx), tab)
            dx, dy = -2 * ex, -2 * ey
            px, py = cx + ex, cy + ey
            path = f'M0 0 a{rx} {ry} {rot} 1 1 {dx:.2f} {dy:.2f} a{rx} {ry} {rot} 1 1 {-dx:.2f} {-dy:.2f}'
            moving += (f'<g transform="translate({px:.2f} {py:.2f})"><use href="#{p}i{ic}"/>'
                       f'<animateMotion begin="0s" dur="48s" repeatCount="indefinite" path="{path}"/></g>')
            static += f'<use href="#{p}i{ic}" x="{px:.2f}" y="{py:.2f}"/>'
    cols = [('Languages and databases', ['Python', 'SQL', 'MySQL'], 56), ('Data and ML libraries', ['Pandas', 'NumPy', 'Scikit-learn', 'Matplotlib'], 340),
            ('BI, web and tooling', ['Power BI', 'Django', 'Git'], 624)]
    chipsvg = ''
    for j, (h, items, x0) in enumerate(cols):
        g, _ = chips(p, x0, 530, 240, items, 1.0 + j * 0.3)
        chipsvg += f'<text class="{p}s" x="{x0}" y="514" font-size="15" font-weight="700" fill="{MUTED}">{h}</text>{g}'
    css = '''
.§chip{animation:§pop .5s ease-out both}
@keyframes §pop{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.§stat{display:none}
@media (prefers-reduced-motion:reduce){.§stat{display:inline}.§mv{display:none}}
'''
    body = f'''
<text class="{p}d" x="56" y="84" font-size="52" textLength="190" lengthAdjust="spacingAndGlyphs" fill="{INK}">Tech stack</text>
{rings}
<circle cx="{cx}" cy="{cy}" r="52" fill="{BLUE}" fill-opacity=".14"/><circle cx="{cx}" cy="{cy}" r="36" fill="#0e1630" stroke="url(#{p}hair)" stroke-width="1.5"/>
<text class="{p}m" x="{cx}" y="{cy + 6}" text-anchor="middle" font-size="18" font-weight="700" fill="{INK}">f(x)</text>
<g class="{p}mv">{moving}</g><g class="{p}stat">{static}</g>
{chipsvg}'''
    return wrap(p, 900, 620, body, css, "Subhajit's tech stack",
                'Ten labelled technologies on three tilted orbits, with the same stack grouped into chips.', defs)


# ---------------------------------------------------------------- id dashboard
def idcard():
    p = 'id'
    port, ph = portrait(p, 170, 252, 240)
    h = hashlib.sha256(USER.encode()).digest()
    bars, x = '', 170
    for i in range(48):
        w = 2 + (h[i % 32] >> (i % 5)) % 3
        if i % 2 == 0:
            bars += f'<rect x="{x}" y="568" width="{w}" height="24" fill="{INK}"/>'
        x += w + 1
        if x > 408:
            break
    repos = [('microworkers-notifier', 'Python', 74), ('Customer-Churn', 'Power BI', 82), ('smart-Route-system', 'JavaScript', 96)]
    rrows = ''.join(
        f'<text class="{p}m" x="540" y="{452 + 50 * i}" font-size="16" fill="{INK}">{n}</text>'
        f'<rect x="{860 - w}" y="{434 + 50 * i}" width="{w}" height="26" rx="13" fill="#0e1630" stroke="url(#{p}hair)" stroke-opacity=".7"/>'
        f'<text class="{p}s" x="{860 - w / 2}" y="{452 + 50 * i}" text-anchor="middle" font-size="12" font-weight="700" fill="{MUTED}">{l}</text>'
        f'<line x1="540" y1="{468 + 50 * i}" x2="860" y2="{468 + 50 * i}" stroke="#1b2540"/>' for i, (n, l, w) in enumerate(repos))
    defs = f'''<linearGradient id="{p}metal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a859f"/><stop offset=".5" stop-color="#eef1f8"/><stop offset="1" stop-color="#6f7a95"/></linearGradient>
<linearGradient id="{p}strap" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="#1a4fb0"/><stop offset="1" stop-color="{RED}"/></linearGradient>
<linearGradient id="{p}card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101a36"/><stop offset="1" stop-color="#0a1020"/></linearGradient>
<linearGradient id="{p}foil" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9cc4ff" stop-opacity="0"/><stop offset=".5" stop-color="#cfe0ff" stop-opacity=".38"/><stop offset="1" stop-color="#ff9aa9" stop-opacity="0"/></linearGradient>
<clipPath id="{p}cc"><rect x="140" y="176" width="300" height="420" rx="22"/></clipPath>'''
    css = '''
.§drop{animation:§dr 1.1s cubic-bezier(.2,.9,.3,1.05) both}
@keyframes §dr{from{transform:translateY(-660px)}to{transform:translateY(0)}}
.§swing{transform-origin:290px 20px;animation:§damp 5s ease-out .9s both,§sway 5.4s ease-in-out 5.9s infinite}
@keyframes §damp{0%{transform:rotate(0)}8%{transform:rotate(9deg)}20%{transform:rotate(-6.5deg)}34%{transform:rotate(4.4deg)}48%{transform:rotate(-3deg)}62%{transform:rotate(2.3deg)}78%{transform:rotate(-1.9deg)}100%{transform:rotate(1.7deg)}}
@keyframes §sway{0%,100%{transform:rotate(1.7deg)}50%{transform:rotate(-1.7deg)}}
.§foil{animation:§sweep 7s ease-in-out 3s infinite}
@keyframes §sweep{0%,55%{transform:translateX(0)}100%{transform:translateX(430px)}}
.§fade{animation:§fd .9s ease-out 1.4s both}
@keyframes §fd{from{opacity:0}to{opacity:1}}
'''
    body = f'''
<g class="{p}fade"><text class="{p}s" x="540" y="228" font-size="22" font-weight="800" fill="{INK}">Repository snapshot</text>
<text class="{p}d" x="540" y="350" font-size="140" fill="{BLUE}">7</text>
<text class="{p}s" x="626" y="306" font-size="20" font-weight="700" fill="{INK}">repositories</text>
<text class="{p}m" x="626" y="332" font-size="13" fill="{MUTED}">as of 17 Oct 2026</text>
<text class="{p}s" x="540" y="404" font-size="15" font-weight="700" fill="{MUTED}">Featured projects</text>{rrows}</g>
<g class="{p}drop"><g class="{p}swing">
<rect x="264" y="-70" width="52" height="196" fill="url(#{p}strap)"/><line x1="272" y1="-70" x2="272" y2="126" stroke="#fff" stroke-opacity=".28" stroke-dasharray="4 5"/><line x1="308" y1="-70" x2="308" y2="126" stroke="#fff" stroke-opacity=".28" stroke-dasharray="4 5"/>
<rect x="270" y="116" width="40" height="26" rx="5" fill="url(#{p}metal)"/><rect x="260" y="138" width="60" height="32" rx="11" fill="url(#{p}metal)"/><rect x="277" y="147" width="26" height="11" rx="5.5" fill="{NAVY}"/>
<path d="M290 170v22" stroke="url(#{p}metal)" stroke-width="5" stroke-linecap="round"/>
<rect x="140" y="176" width="300" height="420" rx="22" fill="url(#{p}card)"/>
<g clip-path="url(#{p}cc)"><rect x="140" y="176" width="300" height="40" fill="url(#{p}acc)" fill-opacity=".9"/></g>
<rect x="266" y="190" width="48" height="10" rx="5" fill="{NAVY}"/>
<text class="{p}m" x="170" y="238" font-size="12" fill="{MUTED}">Analytics · ML · Python</text>
{port}
<text class="{p}d" x="170" y="520" font-size="40" textLength="150" lengthAdjust="spacingAndGlyphs" fill="{INK}">{NAME}</text>
<text class="{p}m" x="170" y="540" font-size="13" fill="{BLUE}">@{USER}</text>
<text class="{p}s" x="170" y="560" font-size="13" font-weight="600" fill="{MUTED}">Data Analyst · ML Engineer</text>
{bars}
<rect x="140.75" y="176.75" width="298.5" height="418.5" rx="21.5" fill="none" stroke="url(#{p}hair)" stroke-width="1.5"/>
<g clip-path="url(#{p}cc)"><g class="{p}foil"><rect transform="skewX(-18)" x="100" y="150" width="70" height="470" fill="url(#{p}foil)"/></g></g>
</g></g>'''
    return wrap(p, 900, 640, body, css, 'Subhajit\'s ID card',
                'A lanyard ID card drops in, settles into a gentle swing, beside a dated repository snapshot.', defs)


# ---------------------------------------------------------------- connect
def connect():
    p = 'cn'
    port, ph = portrait(p, 56, 100, 250)

    def card(y, mark, bg, fg, title, url, d):
        return (f'<g class="{p}fade" style="animation-delay:{d}s"><rect x="410" y="{y}" width="430" height="108" rx="22" fill="#0b1226"/>'
                f'<rect x="410.75" y="{y + .75}" width="428.5" height="106.5" rx="21.5" fill="none" stroke="url(#{p}hair)" stroke-width="1.5" stroke-opacity=".85"/>'
                f'<rect x="436" y="{y + 26}" width="56" height="56" rx="14" fill="{bg}"/>'
                f'<text class="{p}s" x="464" y="{y + 63}" text-anchor="middle" font-size="26" font-weight="800" fill="{fg}">{mark}</text>'
                f'<text class="{p}s" x="512" y="{y + 50}" font-size="24" font-weight="800" fill="{INK}">{title}</text>'
                f'<text class="{p}m" x="512" y="{y + 76}" font-size="11" fill="{MUTED}">{url}</text>'
                f'<g class="{p}nudge" style="animation-delay:{d}s"><path d="M806 {y + 42}l12 12-12 12" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g></g>')
    chev = ''.join(f'<g class="{p}nudge" style="animation-delay:{i * .25}s"><path d="M{334 + i * 20} 203l14 14-14 14" fill="none" stroke="{BLUE if i < 2 else RED}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>' for i in range(3))
    css = '''
.§nudge{animation:§nd 1.6s ease-in-out infinite}
@keyframes §nd{0%,100%{transform:translateX(0)}50%{transform:translateX(9px)}}
.§fade{animation:§fd .8s ease-out both}
@keyframes §fd{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
'''
    body = f'''
<text class="{p}d" x="410" y="72" font-size="50" textLength="250" lengthAdjust="spacingAndGlyphs" fill="{INK}">Let's connect</text>
{port}{chev}
{card(112, 'in', '#0a66c2', '#fff', 'LinkedIn', 'linkedin.com/in/subhajit-ghanta-745606380', 0.3)}
{card(240, 'GH', '#161b22', '#fff', 'GitHub', 'github.com/subhajit-ghanta', 0.6)}'''
    return wrap(p, 900, 380, body, css, 'Connect with Subhajit', 'Portrait with nudging arrows pointing to LinkedIn and GitHub cards.')


files = {'hero': hero, 'about-life': about, 'stack': stack, 'id-dashboard': idcard, 'connect': connect}
for n, f in files.items():
    open(f'{OUT}/assets/{n}.svg', 'w', encoding='utf-8').write(f())

readme = f'''<div align="center">

![Intro](./assets/hero.svg?v=1)

![About](./assets/about-life.svg?v=1)

![Stack](./assets/stack.svg?v=1)

![ID](./assets/id-dashboard.svg?v=1)

![Connect](./assets/connect.svg?v=1)

</div>

## Featured projects

| Project | What it does | Built with |
| --- | --- | --- |
| [microworkers-notifier]({GH}/microworkers-notifier) | Telegram notifier for Microworkers jobs | Python |
| [Customer-Churn]({GH}/Customer-Churn) | Customer Churn Analysis Dashboard built using Microsoft Power BI | Power BI |
| [smart-Route-system]({GH}/smart-Route-system) | Smart Route System | JavaScript |

## Connect

- [LinkedIn]({LI})
- [GitHub]({GH})
'''
open(OUT + '/README.md', 'w', encoding='utf-8').write(readme)

preview = '''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Profile preview</title>
<style>body{margin:0;font:14px system-ui,sans-serif}section{padding:24px;display:grid;gap:20px;justify-items:center}img{max-width:100%;height:auto;display:block}
.dark{background:#0d1117;color:#e6edf3}.light{background:#fff;color:#24292f}</style>
<section class="dark"><p>GitHub dark</p>@IMGS@</section><section class="light"><p>GitHub light</p>@IMGS@</section>'''
imgs = ''.join(f'<img src="assets/{n}.svg?v=1" alt="{n}" width="900">' for n in files)
open(OUT + '/preview.html', 'w').write(preview.replace('@IMGS@', imgs))
shutil.copy(__file__, OUT + '/build.py')

zp = '/mnt/user-data/outputs/subhajit-github-profile.zip'
os.makedirs('/mnt/user-data/outputs', exist_ok=True)
if os.path.exists(zp):
    os.remove(zp)
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(OUT):
        for fn in fs:
            full = os.path.join(root, fn)
            z.write(full, os.path.relpath(full, OUT))
for n in files:
    print(n, os.path.getsize(f'{OUT}/assets/{n}.svg') // 1024, 'KB')
