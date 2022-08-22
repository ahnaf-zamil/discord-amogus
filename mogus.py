from flask import Flask, send_file, request, redirect
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice
from io import BytesIO

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

redirect_links = [
    "https://www.youtube.com/watch?v=grd-K33tOSM",
    "https://www.youtube.com/watch?v=NOZONW-UK0w",
    "https://www.youtube.com/watch?v=ifB662xOZTw",
    "https://www.youtube.com/watch?v=EZEfN5z8Mlg",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # For whoever has the worst luck
    "https://www.youtube.com/watch?v=wpIEUIzGglY",
    "https://www.youtube.com/watch?v=ZYAPgPH9hsI",
    "https://www.youtube.com/watch?v=FhHeGZoWl0g",
    "https://www.youtube.com/watch?v=N3472Q6kvg0",
    "https://www.youtube.com/watch?v=Jrg9KxGNeJY",
    "https://www.youtube.com/watch?v=Jp5U50kzgIk",
]
agent_list = ["Intel Mac OS X 11.6; rv:92.0", "Discord", "curl"]


def gen_img() -> Image:
    msg1 = "Ahnaf (Mog33) asks"
    msg2 = "What number u seeing?"
    msg3 = str(randint(0, 100))

    img = Image.open("./mogus.jpg")
    W, H = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("JetBrains Mono Medium Nerd Font Complete.ttf", 30)

    w, h1 = draw.textsize(msg1, font=font)
    draw.text(((W - w) / 2, 20), msg1, stroke_width=2, stroke_fill=(0, 0, 0), font=font)

    w, h2 = draw.textsize(msg2, font=font)
    draw.text(
        ((W - w) / 2, h1 + 40), msg2, stroke_width=2, stroke_fill=(0, 0, 0), font=font
    )

    font = ImageFont.truetype("JetBrains Mono Medium Nerd Font Complete.ttf", 90)
    w, h = draw.textsize(msg3, font=font)
    draw.text(
        ((W - w) / 2, (H - h) / 2),
        msg3,
        stroke_width=2,
        stroke_fill=(0, 0, 0),
        font=font,
    )

    return img


@app.route("/amogus")
def amogus_root():
    return redirect("/amogus.png")


@app.route("/amogus.png")
def amogus():
    agent = request.headers.get("User-Agent")
    if not any(x in agent for x in agent_list):
        # return redirect(choice(links), code=302)
        return redirect(choice(redirect_links), code=302)

    img = gen_img()
    bio = BytesIO()
    img.save(bio, "JPEG", quality=70)
    bio.seek(0)
    return send_file(bio, mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(debug=True)
