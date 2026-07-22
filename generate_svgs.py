import sys
import xml.etree.ElementTree as ET

def build_svg(theme="dark"):
    is_dark = (theme == "dark")
    
    # Palette definition
    if is_dark:
        bg_main = "#030712"
        panel_bg = "url(#panelGradientDark)"
        panel_border = "rgba(255, 255, 255, 0.08)"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_accent_label = "#38BDF8"
        ascii_grad_start = "#22D3EE"
        ascii_grad_mid = "#A855F7"
        ascii_grad_end = "#10B981"
        accent_grad_1 = "#7C3AED"
        accent_grad_2 = "#22D3EE"
        accent_grad_3 = "#10B981"
        pill_bg = "rgba(255, 255, 255, 0.04)"
        pill_border = "rgba(255, 255, 255, 0.12)"
        pill_text = "#E2E8F0"
        titlebar_bg = "rgba(15, 23, 42, 0.75)"
        titlebar_text = "#94A3B8"
        grid_stroke = "rgba(255, 255, 255, 0.03)"
        aura_opacity_purple = "0.18"
        aura_opacity_cyan = "0.18"
        aura_opacity_emerald = "0.14"
        card_shadow = "0 20px 50px rgba(0,0,0,0.6)"
        row_bg = "rgba(255, 255, 255, 0.03)"
    else:
        bg_main = "#FFFFFF"
        panel_bg = "url(#panelGradientLight)"
        panel_border = "rgba(15, 23, 42, 0.08)"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        text_accent_label = "#0284C7"
        ascii_grad_start = "#2563EB"
        ascii_grad_mid = "#06B6D4"
        ascii_grad_end = "#10B981"
        accent_grad_1 = "#2563EB"
        accent_grad_2 = "#06B6D4"
        accent_grad_3 = "#10B981"
        pill_bg = "rgba(15, 23, 42, 0.04)"
        pill_border = "rgba(15, 23, 42, 0.12)"
        pill_text = "#1E293B"
        titlebar_bg = "rgba(241, 245, 249, 0.9)"
        titlebar_text = "#475569"
        grid_stroke = "rgba(15, 23, 42, 0.03)"
        aura_opacity_purple = "0.08"
        aura_opacity_cyan = "0.08"
        aura_opacity_emerald = "0.06"
        card_shadow = "0 15px 35px rgba(15,23,42,0.08)"
        row_bg = "rgba(15, 23, 42, 0.03)"

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610">
  <defs>
    <!-- Fonts & Keyframe Styles -->
    <style>
    <![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

      .font-sans {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; }}
      .font-mono {{ font-family: 'Fira Code', Consolas, Monaco, 'Courier New', monospace; }}

      /* Floating background auras */
      .float-bg-1 {{
        animation: floatAura1 12s ease-in-out infinite alternate;
      }}
      .float-bg-2 {{
        animation: floatAura2 15s ease-in-out infinite alternate;
      }}
      @keyframes floatAura1 {{
        0% {{ transform: translate(0px, 0px) scale(1); }}
        50% {{ transform: translate(30px, -20px) scale(1.08); }}
        100% {{ transform: translate(-20px, 25px) scale(0.95); }}
      }}
      @keyframes floatAura2 {{
        0% {{ transform: translate(0px, 0px) scale(1); }}
        50% {{ transform: translate(-25px, 30px) scale(1.1); }}
        100% {{ transform: translate(20px, -15px) scale(0.92); }}
      }}

      /* ASCII Floating Animation */
      .ascii-float {{
        animation: floatASCII 5s ease-in-out infinite alternate;
      }}
      @keyframes floatASCII {{
        0% {{ transform: translateY(0px); }}
        100% {{ transform: translateY(-6px); }}
      }}

      /* ASCII Line Reveal */
      .ascii-line {{
        opacity: 0;
        animation: asciiReveal 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      @keyframes asciiReveal {{
        from {{ opacity: 0; transform: translateY(4px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      /* Typing Animation (Cycling Phrases) */
      .typing-phrase {{
        opacity: 0;
        clip-path: inset(0 100% 0 0);
        animation: cycleType 20s steps(24, end) infinite;
      }}
      .phrase-1 {{ animation-delay: 0s; }}
      .phrase-2 {{ animation-delay: 4s; }}
      .phrase-3 {{ animation-delay: 8s; }}
      .phrase-4 {{ animation-delay: 12s; }}
      .phrase-5 {{ animation-delay: 16s; }}

      @keyframes cycleType {{
        0% {{ opacity: 1; clip-path: inset(0 100% 0 0); }}
        3% {{ opacity: 1; clip-path: inset(0 0% 0 0); }}
        17% {{ opacity: 1; clip-path: inset(0 0% 0 0); }}
        19% {{ opacity: 1; clip-path: inset(0 100% 0 0); }}
        20% {{ opacity: 0; clip-path: inset(0 100% 0 0); }}
        100% {{ opacity: 0; clip-path: inset(0 100% 0 0); }}
      }}

      .cursor-blink {{
        animation: blink 0.75s infinite;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      /* Sequential Row Reveal */
      .seq-row {{
        opacity: 0;
        animation: seqFade 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      .seq-1 {{ animation-delay: 0.20s; }}
      .seq-2 {{ animation-delay: 0.32s; }}
      .seq-3 {{ animation-delay: 0.44s; }}
      .seq-4 {{ animation-delay: 0.56s; }}
      .seq-5 {{ animation-delay: 0.68s; }}

      @keyframes seqFade {{
        from {{ opacity: 0; transform: translateY(6px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}

      /* Skill Pills Hover & Glow Animation */
      .skill-pill {{
        transition: transform 0.25s ease, filter 0.25s ease;
        cursor: pointer;
      }}
      .skill-pill:hover {{
        transform: translateY(-2px) scale(1.04);
        filter: drop-shadow(0 4px 12px rgba(34, 211, 238, 0.35));
      }}

      /* Border Shimmer Animation */
      .border-shimmer {{
        stroke-dasharray: 200 800;
        animation: shimmerMove 8s linear infinite;
      }}
      @keyframes shimmerMove {{
        0% {{ stroke-dashoffset: 1000; }}
        100% {{ stroke-dashoffset: 0; }}
      }}

      /* Scanline Effect */
      .scanline {{
        animation: scanlineSweep 6s linear infinite;
      }}
      @keyframes scanlineSweep {{
        0% {{ transform: translateY(0px); opacity: 0; }}
        10% {{ opacity: 0.25; }}
        90% {{ opacity: 0.25; }}
        100% {{ transform: translateY(500px); opacity: 0; }}
      }}

      /* Pulse Dot */
      .pulse-dot {{
        animation: pulseGlow 2s ease-in-out infinite alternate;
      }}
      @keyframes pulseGlow {{
        0% {{ opacity: 0.4; transform: scale(0.92); }}
        100% {{ opacity: 1; transform: scale(1.15); }}
      }}
    ]]>
    </style>

    <!-- Gradients -->
    <linearGradient id="panelGradientDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" stop-opacity="0.88" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0.94" />
    </linearGradient>

    <linearGradient id="panelGradientLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.94" />
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0.97" />
    </linearGradient>

    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_grad_1}">
        <animate attributeName="stop-color" values="{accent_grad_1};{accent_grad_2};{accent_grad_3};{accent_grad_1}" dur="9s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="{accent_grad_2}">
        <animate attributeName="stop-color" values="{accent_grad_2};{accent_grad_3};{accent_grad_1};{accent_grad_2}" dur="9s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="{accent_grad_3}">
        <animate attributeName="stop-color" values="{accent_grad_3};{accent_grad_1};{accent_grad_2};{accent_grad_3}" dur="9s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="asciiGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ascii_grad_start}">
        <animate attributeName="stop-color" values="{ascii_grad_start};{ascii_grad_mid};{ascii_grad_end};{ascii_grad_start}" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="{ascii_grad_mid}">
        <animate attributeName="stop-color" values="{ascii_grad_mid};{ascii_grad_end};{ascii_grad_start};{ascii_grad_mid}" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <linearGradient id="shimmerGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_grad_1}" stop-opacity="0" />
      <stop offset="50%" stop-color="{accent_grad_2}" stop-opacity="0.8" />
      <stop offset="100%" stop-color="{accent_grad_3}" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="glassReflection" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.12" />
      <stop offset="35%" stop-color="#FFFFFF" stop-opacity="0.02" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0" />
    </linearGradient>

    <!-- Radial Background Auras -->
    <radialGradient id="auraPurple" cx="20%" cy="20%" r="60%">
      <stop offset="0%" stop-color="{accent_grad_1}" stop-opacity="{aura_opacity_purple}" />
      <stop offset="100%" stop-color="{accent_grad_1}" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="auraCyan" cx="80%" cy="30%" r="55%">
      <stop offset="0%" stop-color="{accent_grad_2}" stop-opacity="{aura_opacity_cyan}" />
      <stop offset="100%" stop-color="{accent_grad_2}" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="auraEmerald" cx="50%" cy="85%" r="50%">
      <stop offset="0%" stop-color="{accent_grad_3}" stop-opacity="{aura_opacity_emerald}" />
      <stop offset="100%" stop-color="{accent_grad_3}" stop-opacity="0" />
    </radialGradient>

    <!-- Glow Filter -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.35" />
    </filter>

    <!-- Tech Grid Pattern -->
    <pattern id="techGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="1" />
      <circle cx="24" cy="24" r="1" fill="{grid_stroke}" />
    </pattern>

    <!-- Left Panel Clip Path for Scanline -->
    <clipPath id="leftPanelClip">
      <rect x="0" y="43" width="430" height="519" rx="0" />
    </clipPath>
  </defs>

  <!-- Canvas Base Frame -->
  <rect x="0" y="0" width="1180" height="610" rx="20" ry="20" fill="{bg_main}" />

  <!-- Ambient Radial Glow Auras -->
  <g class="float-bg-1">
    <rect x="0" y="0" width="1180" height="610" rx="20" fill="url(#auraPurple)" />
  </g>
  <g class="float-bg-2">
    <rect x="0" y="0" width="1180" height="610" rx="20" fill="url(#auraCyan)" />
  </g>
  <rect x="0" y="0" width="1180" height="610" rx="20" fill="url(#auraEmerald)" />

  <!-- Tech Grid Background -->
  <rect x="0" y="0" width="1180" height="610" rx="20" fill="url(#techGrid)" />

  <!-- Floating Particle Dust -->
  <g class="particles">
    <circle cx="140" cy="480" r="2" fill="{accent_grad_2}" opacity="0.6">
      <animate attributeName="cy" values="520;80;520" dur="14s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.1;0.8;0.1" dur="14s" repeatCount="indefinite" />
    </circle>
    <circle cx="380" cy="420" r="1.5" fill="{accent_grad_1}" opacity="0.5">
      <animate attributeName="cy" values="460;40;460" dur="16s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.2;0.9;0.2" dur="16s" repeatCount="indefinite" />
    </circle>
    <circle cx="620" cy="540" r="2.5" fill="{accent_grad_3}" opacity="0.5">
      <animate attributeName="cy" values="540;100;540" dur="13s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.1;0.7;0.1" dur="13s" repeatCount="indefinite" />
    </circle>
    <circle cx="890" cy="460" r="2" fill="{accent_grad_2}" opacity="0.6">
      <animate attributeName="cy" values="500;60;500" dur="15s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.3;0.9;0.3" dur="15s" repeatCount="indefinite" />
    </circle>
    <circle cx="1080" cy="500" r="1.8" fill="{accent_grad_1}" opacity="0.5">
      <animate attributeName="cy" values="520;90;520" dur="12s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.2;0.8;0.2" dur="12s" repeatCount="indefinite" />
    </circle>
  </g>

  <!-- Outer Frame Shimmer Border -->
  <rect x="1" y="1" width="1178" height="608" rx="19" fill="none" stroke="{panel_border}" stroke-width="1.5" />
  <rect x="1" y="1" width="1178" height="608" rx="19" fill="none" stroke="url(#shimmerGradient)" stroke-width="2" class="border-shimmer" />


  <!-- ============================================================ -->
  <!-- LEFT PANEL: ASCII ART PORTRAIT                               -->
  <!-- ============================================================ -->
  <g transform="translate(24, 24)" filter="url(#softShadow)">
    <!-- Panel Background Frame -->
    <rect x="0" y="0" width="430" height="562" rx="16" fill="{panel_bg}" stroke="{panel_border}" stroke-width="1" />
    <rect x="0" y="0" width="430" height="562" rx="16" fill="url(#glassReflection)" />

    <!-- Left Titlebar -->
    <path d="M 0 16 A 16 16 0 0 1 16 0 L 414 0 A 16 16 0 0 1 430 16 L 430 42 L 0 42 Z" fill="{titlebar_bg}" />
    <line x1="0" y1="42" x2="430" y2="42" stroke="{panel_border}" stroke-width="1" />

    <!-- Window Control Buttons -->
    <circle cx="22" cy="21" r="5.5" fill="#FF5F56" />
    <circle cx="38" cy="21" r="5.5" fill="#FFBD2E" />
    <circle cx="54" cy="21" r="5.5" fill="#27C93F" />

    <!-- Titlebar Text & Status -->
    <text x="76" y="25" class="font-mono" font-size="11" font-weight="600" fill="{titlebar_text}">ascii_avatar.sh</text>
    <circle cx="360" cy="21" r="4" fill="{accent_grad_3}" class="pulse-dot" filter="url(#neonGlow)" />
    <text x="372" y="25" class="font-mono" font-size="10" font-weight="600" fill="{accent_grad_3}">ONLINE</text>

    <!-- Scanline Sweep Effect -->
    <g clip-path="url(#leftPanelClip)">
      <rect x="0" y="43" width="430" height="8" fill="url(#shimmerGradient)" opacity="0.3" class="scanline" />
    </g>

    <!-- ASCII Art Container (Nested Outer Position + Inner Float + Line-by-Line Reveal) -->
    <g transform="translate(20, 68)">
      <g class="ascii-float">
        <g fill="url(#asciiGradient)" class="font-mono" font-size="10.5" font-weight="600" letter-spacing="0.5">
          <!-- 23 Clean Monospace Cyber ASCII Art Lines -->
          <text x="15" y="16" class="ascii-line" style="animation-delay: 0.04s;">.------------------------------------.</text>
          <text x="15" y="31" class="ascii-line" style="animation-delay: 0.08s;">| [SYS::DEV_MATRIX v4.2] ONLINE      |</text>
          <text x="15" y="46" class="ascii-line" style="animation-delay: 0.12s;">+------------------------------------+</text>
          <text x="15" y="61" class="ascii-line" style="animation-delay: 0.16s;">|                                    |</text>
          <text x="15" y="76" class="ascii-line" style="animation-delay: 0.20s;">|         .---.        .---.         |</text>
          <text x="15" y="91" class="ascii-line" style="animation-delay: 0.24s;">|        /     \  /\  /     \        |</text>
          <text x="15" y="106" class="ascii-line" style="animation-delay: 0.28s;">|       |  (o)  |/  \|  (o)  |       |</text>
          <text x="15" y="121" class="ascii-line" style="animation-delay: 0.32s;">|        \     / \  / \     /        |</text>
          <text x="15" y="136" class="ascii-line" style="animation-delay: 0.36s;">|         '---'   \/   '---'         |</text>
          <text x="15" y="151" class="ascii-line" style="animation-delay: 0.40s;">|            .----------.            |</text>
          <text x="15" y="166" class="ascii-line" style="animation-delay: 0.44s;">|           /   ====   /             |</text>
          <text x="15" y="181" class="ascii-line" style="animation-delay: 0.48s;">|          '----------'              |</text>
          <text x="15" y="196" class="ascii-line" style="animation-delay: 0.52s;">|           \________/               |</text>
          <text x="15" y="211" class="ascii-line" style="animation-delay: 0.56s;">|         .--------------.           |</text>
          <text x="15" y="226" class="ascii-line" style="animation-delay: 0.60s;">|        /  .----------.  \          |</text>
          <text x="15" y="241" class="ascii-line" style="animation-delay: 0.64s;">|       /  /  FULL STACK\  \         |</text>
          <text x="15" y="256" class="ascii-line" style="animation-delay: 0.68s;">|      |  |  ARCHITECT   |  |        |</text>
          <text x="15" y="271" class="ascii-line" style="animation-delay: 0.72s;">|       \  \  .------.  /  /         |</text>
          <text x="15" y="286" class="ascii-line" style="animation-delay: 0.76s;">|        \  '--------'  /            |</text>
          <text x="15" y="301" class="ascii-line" style="animation-delay: 0.80s;">|         '------------'             |</text>
          <text x="15" y="316" class="ascii-line" style="animation-delay: 0.84s;">|                                    |</text>
          <text x="15" y="331" class="ascii-line" style="animation-delay: 0.88s;">+------------------------------------+</text>
          <text x="15" y="346" class="ascii-line" style="animation-delay: 0.92s;">| KERNEL: 6.8 | SYSTEM STATUS: OK    |</text>
          <text x="15" y="361" class="ascii-line" style="animation-delay: 0.96s;">'------------------------------------'</text>
        </g>
      </g>
    </g>

    <!-- Bottom Terminal Status Bar -->
    <rect x="15" y="472" width="400" height="72" rx="10" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
    <text x="30" y="497" class="font-mono" font-size="11" fill="{text_secondary}">SYSTEM_PROMPT &gt;</text>
    <text x="145" y="497" class="font-mono" font-size="11" font-weight="600" fill="{accent_grad_2}">"Build the Future."</text>
    <text x="30" y="522" class="font-mono" font-size="10" fill="{text_secondary}">PING: 14ms  |  FPS: 60  |  LOC: 154,200</text>
    <text x="325" y="522" class="font-mono cursor-blink" font-size="12" font-weight="700" fill="{accent_grad_2}">_</text>
  </g>


  <!-- ============================================================ -->
  <!-- RIGHT PANEL: TERMINAL & DEVELOPER PROFILE                    -->
  <!-- ============================================================ -->
  <g transform="translate(474, 24)" filter="url(#softShadow)">
    <!-- Panel Background Frame -->
    <rect x="0" y="0" width="682" height="562" rx="16" fill="{panel_bg}" stroke="{panel_border}" stroke-width="1" />
    <rect x="0" y="0" width="682" height="562" rx="16" fill="url(#glassReflection)" />

    <!-- Right Titlebar -->
    <path d="M 0 16 A 16 16 0 0 1 16 0 L 666 0 A 16 16 0 0 1 682 16 L 682 42 L 0 42 Z" fill="{titlebar_bg}" />
    <line x1="0" y1="42" x2="682" y2="42" stroke="{panel_border}" stroke-width="1" />

    <!-- Window Control Buttons -->
    <circle cx="22" cy="21" r="5.5" fill="#FF5F56" />
    <circle cx="38" cy="21" r="5.5" fill="#FFBD2E" />
    <circle cx="54" cy="21" r="5.5" fill="#27C93F" />

    <!-- Titlebar Header Text -->
    <text x="78" y="25" class="font-mono" font-size="11" font-weight="600" fill="{titlebar_text}">alex@rivers-mbp: ~/developer_profile (zsh)</text>
    
    <!-- Right Badge -->
    <rect x="590" y="11" width="76" height="20" rx="10" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
    <text x="628" y="25" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="{text_secondary}">v2.4.0</text>


    <!-- TERMINAL CONTENT BODY -->

    <!-- Prompt Command Line -->
    <text x="32" y="74" class="font-mono" font-size="13" font-weight="600" fill="{text_accent_label}">alex@rivers:~$</text>
    <text x="165" y="74" class="font-mono" font-size="13" font-weight="500" fill="{text_primary}">./init_profile.sh --verbose</text>

    <!-- Greeting Row -->
    <text x="32" y="114" class="font-sans" font-size="26" font-weight="800" fill="{text_primary}">
      👋  Hi, I'm <tspan fill="url(#accentGradient)" filter="url(#neonGlow)">ALEX RIVERS</tspan>
    </text>

    <!-- Dynamic Typing Subtitle Row -->
    <g transform="translate(32, 144)">
      <text x="0" y="0" class="font-mono" font-size="14" font-weight="600" fill="{text_secondary}">&gt; Role:</text>
      
      <!-- Staggered Animated Typing Phrases with inline blinking cursor -->
      <g transform="translate(72, 0)">
        <text x="0" y="0" class="font-mono typing-phrase phrase-1" font-size="14" font-weight="700" fill="{accent_grad_2}">Frontend Engineer <tspan class="cursor-blink" fill="{accent_grad_2}">█</tspan></text>
        <text x="0" y="0" class="font-mono typing-phrase phrase-2" font-size="14" font-weight="700" fill="{accent_grad_2}">Full Stack Developer <tspan class="cursor-blink" fill="{accent_grad_2}">█</tspan></text>
        <text x="0" y="0" class="font-mono typing-phrase phrase-3" font-size="14" font-weight="700" fill="{accent_grad_2}">Open Source Contributor <tspan class="cursor-blink" fill="{accent_grad_2}">█</tspan></text>
        <text x="0" y="0" class="font-mono typing-phrase phrase-4" font-size="14" font-weight="700" fill="{accent_grad_2}">UI Systems Architect <tspan class="cursor-blink" fill="{accent_grad_2}">█</tspan></text>
        <text x="0" y="0" class="font-mono typing-phrase phrase-5" font-size="14" font-weight="700" fill="{accent_grad_2}">AI Enthusiast <tspan class="cursor-blink" fill="{accent_grad_2}">█</tspan></text>
      </g>
    </g>

    <!-- Divider Line -->
    <line x1="32" y1="160" x2="650" y2="160" stroke="{panel_border}" stroke-width="1" />


    <!-- SEQUENTIAL REVEAL INFORMATION GRID (NESTED GROUPS PREVENT OVERLAP) -->
    <g transform="translate(32, 172)">
      <!-- Row 1: Location -->
      <g transform="translate(0, 0)">
        <g class="seq-row seq-1">
          <rect x="0" y="0" width="618" height="26" rx="6" fill="{row_bg}" stroke="{pill_border}" stroke-width="0.5" />
          <text x="14" y="17" font-size="12">📍</text>
          <text x="36" y="17" class="font-mono" font-size="11.5" font-weight="600" fill="{text_secondary}">Location</text>
          <text x="135" y="17" class="font-mono" font-size="11.5" fill="{text_secondary}">→</text>
          <text x="160" y="17" class="font-sans" font-size="11.5" font-weight="600" fill="{text_primary}">San Francisco, CA</text>
        </g>
      </g>

      <!-- Row 2: Education -->
      <g transform="translate(0, 31)">
        <g class="seq-row seq-2">
          <rect x="0" y="0" width="618" height="26" rx="6" fill="{row_bg}" stroke="{pill_border}" stroke-width="0.5" />
          <text x="14" y="17" font-size="12">🎓</text>
          <text x="36" y="17" class="font-mono" font-size="11.5" font-weight="600" fill="{text_secondary}">Education</text>
          <text x="135" y="17" class="font-mono" font-size="11.5" fill="{text_secondary}">→</text>
          <text x="160" y="17" class="font-sans" font-size="11.5" font-weight="600" fill="{text_primary}">B.S. Computer Science @ Stanford</text>
        </g>
      </g>

      <!-- Row 3: Current Focus -->
      <g transform="translate(0, 62)">
        <g class="seq-row seq-3">
          <rect x="0" y="0" width="618" height="26" rx="6" fill="{row_bg}" stroke="{pill_border}" stroke-width="0.5" />
          <text x="14" y="17" font-size="12">⚡</text>
          <text x="36" y="17" class="font-mono" font-size="11.5" font-weight="600" fill="{text_secondary}">Focus</text>
          <text x="135" y="17" class="font-mono" font-size="11.5" fill="{text_secondary}">→</text>
          <text x="160" y="17" class="font-sans" font-size="11.5" font-weight="600" fill="{text_primary}">Next.js 14, WebGPU, LLM Agents</text>
        </g>
      </g>

      <!-- Row 4: Portfolio -->
      <g transform="translate(0, 93)">
        <g class="seq-row seq-4">
          <rect x="0" y="0" width="618" height="26" rx="6" fill="{row_bg}" stroke="{pill_border}" stroke-width="0.5" />
          <text x="14" y="17" font-size="12">🌐</text>
          <text x="36" y="17" class="font-mono" font-size="11.5" font-weight="600" fill="{text_secondary}">Portfolio</text>
          <text x="135" y="17" class="font-mono" font-size="11.5" fill="{text_secondary}">→</text>
          <text x="160" y="17" class="font-sans" font-size="11.5" font-weight="600" fill="{text_accent_label}">alexrivers.dev</text>
        </g>
      </g>

      <!-- Row 5: Email -->
      <g transform="translate(0, 124)">
        <g class="seq-row seq-5">
          <rect x="0" y="0" width="618" height="26" rx="6" fill="{row_bg}" stroke="{pill_border}" stroke-width="0.5" />
          <text x="14" y="17" font-size="12">✉️</text>
          <text x="36" y="17" class="font-mono" font-size="11.5" font-weight="600" fill="{text_secondary}">Email</text>
          <text x="135" y="17" class="font-mono" font-size="11.5" fill="{text_secondary}">→</text>
          <text x="160" y="17" class="font-sans" font-size="11.5" font-weight="600" fill="{text_primary}">alex@rivers.dev</text>
        </g>
      </g>
    </g>


    <!-- SKILLS SECTION -->
    <g transform="translate(32, 336)">
      <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" letter-spacing="1.5" fill="{text_secondary}">// CORE TECH STACK</text>
      
      <!-- Pills Grid Row 1 -->
      <g transform="translate(0, 12)">
        <!-- React -->
        <g class="skill-pill" transform="translate(0, 0)">
          <rect x="0" y="0" width="84" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#61DAFB" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">React</text>
        </g>
        <!-- Next.js -->
        <g class="skill-pill" transform="translate(92, 0)">
          <rect x="0" y="0" width="92" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="{text_primary}" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Next.js</text>
        </g>
        <!-- TypeScript -->
        <g class="skill-pill" transform="translate(192, 0)">
          <rect x="0" y="0" width="106" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#3178C6" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">TypeScript</text>
        </g>
        <!-- Node.js -->
        <g class="skill-pill" transform="translate(306, 0)">
          <rect x="0" y="0" width="88" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#5FA04E" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Node.js</text>
        </g>
        <!-- Tailwind -->
        <g class="skill-pill" transform="translate(402, 0)">
          <rect x="0" y="0" width="94" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#06B6D4" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Tailwind</text>
        </g>
        <!-- Python -->
        <g class="skill-pill" transform="translate(504, 0)">
          <rect x="0" y="0" width="86" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#3776AB" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Python</text>
        </g>
      </g>

      <!-- Pills Grid Row 2 -->
      <g transform="translate(0, 46)">
        <!-- Docker -->
        <g class="skill-pill" transform="translate(0, 0)">
          <rect x="0" y="0" width="88" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#2496ED" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Docker</text>
        </g>
        <!-- Postgres -->
        <g class="skill-pill" transform="translate(96, 0)">
          <rect x="0" y="0" width="98" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#4169E1" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Postgres</text>
        </g>
        <!-- AWS -->
        <g class="skill-pill" transform="translate(202, 0)">
          <rect x="0" y="0" width="74" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#FF9900" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">AWS</text>
        </g>
        <!-- Git -->
        <g class="skill-pill" transform="translate(284, 0)">
          <rect x="0" y="0" width="68" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#F05032" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Git</text>
        </g>
        <!-- Figma -->
        <g class="skill-pill" transform="translate(360, 0)">
          <rect x="0" y="0" width="82" height="26" rx="13" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <circle cx="15" cy="13" r="3.5" fill="#F24E1E" />
          <text x="26" y="17" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Figma</text>
        </g>
      </g>
    </g>


    <!-- SOCIAL LINKS SECTION -->
    <g transform="translate(32, 442)">
      <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" letter-spacing="1.5" fill="{text_secondary}">// CONNECT WITH ME</text>

      <g transform="translate(0, 12)">
        <!-- GitHub Button -->
        <g class="skill-pill" transform="translate(0, 0)">
          <rect x="0" y="0" width="138" height="32" rx="16" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <!-- GitHub Icon -->
          <path d="M 22 8 A 7 7 0 0 0 15 15 C 15 18.1 17 20.7 19.8 21.6 C 20.15 21.7 20.3 21.45 20.3 21.25 C 20.3 21.08 20.29 20.5 20.29 19.88 C 18.34 20.3 17.93 19.05 17.93 19.05 C 17.61 18.24 17.15 18.02 17.15 18.02 C 16.52 17.58 17.2 17.59 17.2 17.59 C 17.9 17.64 18.27 18.31 18.27 18.31 C 18.9 19.38 19.9 19.07 20.3 18.89 C 20.36 18.43 20.55 18.12 20.75 17.94 C 19.2 17.77 17.56 17.17 17.56 14.5 C 17.56 13.74 17.83 13.12 18.27 12.63 C 18.2 12.45 17.96 11.75 18.34 10.8 C 18.34 10.8 18.92 10.61 20.25 11.5 C 20.8 11.35 21.4 11.27 22 11.27 C 22.6 11.27 23.2 11.35 23.75 11.5 C 25.08 10.61 25.66 10.8 25.66 10.8 C 26.04 11.75 25.8 12.45 25.73 12.63 C 26.17 13.12 26.44 13.74 26.44 14.5 C 26.44 17.18 24.8 17.76 23.24 17.94 C 23.5 18.16 23.72 18.6 23.72 19.27 C 23.72 20.23 23.71 21 23.71 21.25 C 23.71 21.45 23.86 21.71 24.22 21.6 C 27 20.7 29 18.1 29 15 A 7 7 0 0 0 22 8 Z" fill="{text_primary}" />
          <text x="36" y="20" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">GitHub</text>
        </g>

        <!-- LinkedIn Button -->
        <g class="skill-pill" transform="translate(148, 0)">
          <rect x="0" y="0" width="138" height="32" rx="16" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <!-- LinkedIn Icon -->
          <rect x="14" y="11" width="3.5" height="10" fill="#0A66C2" />
          <circle cx="15.75" cy="8.5" r="2" fill="#0A66C2" />
          <path d="M 20 11 L 23.2 11 L 23.2 12.4 H 23.25 C 23.7 11.6 24.8 10.7 26.3 10.7 C 29.4 10.7 30 12.7 30 15.3 L 30 21 H 26.5 L 26.5 15.8 C 26.5 14.5 26 13.6 24.9 13.6 C 24 13.6 23.5 14.2 23.3 14.8 L 23.3 21 H 20 Z" fill="#0A66C2" />
          <text x="38" y="20" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">LinkedIn</text>
        </g>

        <!-- Twitter / X Button -->
        <g class="skill-pill" transform="translate(296, 0)">
          <rect x="0" y="0" width="138" height="32" rx="16" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <!-- Twitter/X Icon -->
          <path d="M 15 9 L 20 15.5 L 14.5 22 H 16 L 20.8 16.4 L 24.5 22 H 29 L 23.6 14.5 L 28.6 9 H 27.1 L 22.8 13.7 L 19.5 9 Z M 17 10 H 19 L 27 21 H 25 Z" fill="{text_primary}" />
          <text x="38" y="20" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Twitter / X</text>
        </g>

        <!-- Portfolio Button -->
        <g class="skill-pill" transform="translate(444, 0)">
          <rect x="0" y="0" width="144" height="32" rx="16" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1" />
          <!-- Globe Icon -->
          <circle cx="22" cy="16" r="6.5" fill="none" stroke="{accent_grad_2}" stroke-width="1.2" />
          <line x1="15.5" y1="16" x2="28.5" y2="16" stroke="{accent_grad_2}" stroke-width="1" />
          <ellipse cx="22" cy="16" rx="3" ry="6.5" fill="none" stroke="{accent_grad_2}" stroke-width="1" />
          <text x="38" y="20" class="font-sans" font-size="11" font-weight="600" fill="{pill_text}">Portfolio ↗</text>
        </g>
      </g>
    </g>

  </g>
</svg>'''
    return svg_content

if __name__ == "__main__":
    dark_svg = build_svg("dark")
    light_svg = build_svg("light")
    
    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open("light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)

    print("Re-generated dark.svg and light.svg successfully!")
