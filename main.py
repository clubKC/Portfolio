import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="centered")

# =====================================================
#  ✏️  EDIT THIS PART TO MAKE IT YOURS
# =====================================================
NAME = "X"
TAGLINE = "I draw, I code tiny games, and I'm always hanging out with my cat Biscuit."
ABOUT = (
    "I'm 12 years old and I love making things. Last year I taught myself "
    "Scratch, and now I'm learning Python. When I'm not on a screen, you'll "
    "find me sketching comics or building LEGO cities."
)
BADGES = ["🎨 Artist", "💻 Coder", "🐱 Cat person"]

PROJECTS = [
    {"emoji": "🎮", "title": "Space Dodger", "desc": "A game where you steer a rocket through falling asteroids.", "tag": "Scratch"},
    {"emoji": "📖", "title": "Biscuit's Adventures", "desc": "A comic series about a cat who thinks he's a detective.", "tag": "Drawing"},
    {"emoji": "🤖", "title": "Joke Bot", "desc": "A tiny program that tells a new joke every time you press a button.", "tag": "Python"},
    {"emoji": "🏙️", "title": "LEGO Skyline", "desc": "A city with 14 buildings and a working train track.", "tag": "LEGO"},
]

LOVES = ["Pizza 🍕", "Minecraft ⛏️", "Drawing ✏️", "Space 🪐", "Soccer ⚽", "Music 🎧", "Baking 🧁"]

SKILLS = {"Drawing": 90, "Scratch": 80, "Python": 45, "Teamwork": 85}
# =====================================================


# ---------- Looks (variations!) ----------
# Add your own by copying one and changing the colors.
THEMES = {
    "Sticker Pop": dict(bg="#F2F0FF", card="#FFFFFF", ink="#1B1B3A", line="#1B1B3A",
                        c1="#FFD23F", c2="#FF6F91", c3="#3DDC97", c4="#4D9DE0"),
}

t = THEMES["Sticker Pop"]

root_vars = (
    ":root{"
    f"--bg:{t['bg']};--card:{t['card']};--ink:{t['ink']};--line:{t['line']};"
    f"--c1:{t['c1']};--c2:{t['c2']};--c3:{t['c3']};--c4:{t['c4']};--on:#1B1B3A;"
    "}"
)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lilita+One&family=Nunito:wght@600;800&display=swap');

html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp {
  background-color: var(--bg);
  background-image: radial-gradient(color-mix(in srgb, var(--line) 18%, transparent) 1.5px, transparent 1.5px);
  background-size: 26px 26px;
}
.block-container { max-width: 820px; padding-top: 2rem; }

/* Hero */
.hero { text-align: center; padding: 2rem 1rem 1rem; }
.wave { font-size: 4rem; display: inline-block; transform-origin: 70% 70%; animation: wave 2s ease-in-out 1; }
@keyframes wave {
  0%, 60%, 100% { transform: rotate(0); }
  10%, 30%, 50% { transform: rotate(16deg); }
  20%, 40% { transform: rotate(-8deg); }
}
@media (prefers-reduced-motion: reduce) { .wave { animation: none; } }
.stApp .hero h1 {
  font-family: 'Lilita One', sans-serif; font-size: clamp(2.6rem, 8vw, 4.5rem);
  color: var(--ink); margin: .2rem 0; padding: 0; line-height: 1.05;
}
.tagline { font-size: 1.25rem; font-weight: 600; color: var(--ink); max-width: 560px; margin: .8rem auto 1.2rem; line-height: 1.5; }

/* Stickers (badges + chips) */
.sticker {
  display: inline-block; padding: .45rem 1rem; margin: .35rem; font-weight: 800;
  border: 3px solid var(--line); border-radius: 999px; box-shadow: 4px 4px 0 var(--line); color: var(--on);
}

/* Section titles */
.sec {
  display: inline-block; font-family: 'Lilita One', sans-serif; font-size: 1.8rem;
  background: var(--c1); color: var(--on); border: 3px solid var(--line);
  box-shadow: 4px 4px 0 var(--line); padding: .2rem 1rem; border-radius: 14px;
  transform: rotate(-1.5deg); margin: 2.5rem 0 1.2rem;
}

/* Cards */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.4rem; }
.card {
  background: var(--card); color: var(--ink); border: 3px solid var(--line); border-radius: 18px;
  box-shadow: 6px 6px 0 var(--line); overflow: hidden; transition: transform .15s, box-shadow .15s;
}
.card:hover { transform: translate(-2px, -2px); box-shadow: 8px 8px 0 var(--line); }
.card .top { font-size: 2.6rem; padding: .6rem; text-align: center; border-bottom: 3px solid var(--line); }
.card .body { padding: 1rem 1.1rem 1.2rem; }
.card .title { font-family: 'Lilita One', sans-serif; font-size: 1.35rem; }
.card .desc { margin: .3rem 0 .8rem; line-height: 1.5; font-weight: 600; }
.tag { font-weight: 800; font-size: .85rem; padding: .15rem .7rem; border: 2px solid var(--line); border-radius: 999px; background: var(--c4); color: var(--on); }
.about { padding: 1.3rem 1.5rem; font-size: 1.1rem; line-height: 1.7; font-weight: 600; }

/* Skill bars */
.skill { margin: .9rem 0; color: var(--ink); font-weight: 800; }
.track { height: 22px; border: 3px solid var(--line); border-radius: 999px; background: var(--card); overflow: hidden; margin-top: .3rem; }
.fill { height: 100%; border-right: 3px solid var(--line); }

/* Form */
[data-testid="stForm"] { border: 3px solid var(--line); border-radius: 18px; background: var(--card); box-shadow: 6px 6px 0 var(--line); padding: 1.2rem; }
[data-testid="stForm"] label p { color: var(--ink); font-weight: 800; }
[data-testid="stForm"] input, [data-testid="stForm"] textarea { color: #1B1B3A !important; background: #fff !important; }
[data-testid="stFormSubmitButton"] button {
  background: var(--c2); color: var(--on); border: 3px solid var(--line); border-radius: 14px;
  box-shadow: 4px 4px 0 var(--line); font-family: 'Lilita One', sans-serif; font-size: 1.1rem; padding: .3rem 1.4rem;
}
[data-testid="stFormSubmitButton"] button:hover { background: var(--c1); color: var(--on); border-color: var(--line); }

.footer { text-align: center; color: var(--ink); font-weight: 800; margin: 3rem 0 1rem; }
"""

st.markdown(f"<style>{root_vars}{CSS}</style>", unsafe_allow_html=True)

COLORS = ["--c1", "--c2", "--c3", "--c4"]
TILTS = [-2, 1.5, -1, 2]

# ---------- Hero ----------
badges = "".join(
    f'<span class="sticker" style="background:var({COLORS[i % 4]});transform:rotate({TILTS[i % 4]}deg)">{b}</span>'
    for i, b in enumerate(BADGES)
)
st.markdown(
    f'<div class="hero"><div class="wave">👋</div>'
    f"<h1>Hi, I'm {NAME}!</h1>"
    f'<div class="tagline">{TAGLINE}</div>{badges}</div>',
    unsafe_allow_html=True,
)

# ---------- About ----------
st.markdown(
    f'<div class="sec">About me</div><div class="card about">{ABOUT}</div>',
    unsafe_allow_html=True,
)

# ---------- Projects ----------
cards = "".join(
    f'<div class="card"><div class="top" style="background:var({COLORS[i % 4]})">{p["emoji"]}</div>'
    f'<div class="body"><div class="title">{p["title"]}</div><div class="desc">{p["desc"]}</div>'
    f'<span class="tag">{p["tag"]}</span></div></div>'
    for i, p in enumerate(PROJECTS)
)
st.markdown(f'<div class="sec">Things I made</div><div class="grid">{cards}</div>', unsafe_allow_html=True)

# ---------- Loves ----------
chips = "".join(
    f'<span class="sticker" style="background:var({COLORS[i % 4]});transform:rotate({TILTS[(i + 1) % 4]}deg)">{x}</span>'
    for i, x in enumerate(LOVES)
)
st.markdown(f'<div class="sec">Stuff I love</div><div>{chips}</div>', unsafe_allow_html=True)

# ---------- Skills ----------
bars = "".join(
    f'<div class="skill">{name}<div class="track"><div class="fill" style="width:{pct}%;background:var({COLORS[i % 4]})"></div></div></div>'
    for i, (name, pct) in enumerate(SKILLS.items())
)
st.markdown(f'<div class="sec">What I\'m good at</div>{bars}', unsafe_allow_html=True)

# ---------- Say hi ----------
st.markdown('<div class="sec">Say hi!</div>', unsafe_allow_html=True)
with st.form("say_hi"):
    who = st.text_input("Your name")
    msg = st.text_area("Your message")
    sent = st.form_submit_button("Send 🚀")

if sent:
    # NOTE: this is just for fun - the message isn't saved or emailed anywhere.
    st.balloons()
    st.success(f"Yay! Thanks for saying hi, {who or 'friend'} 🎉")

st.markdown('<div class="footer">Made with Python 🐍 😃</div>', unsafe_allow_html=True)
