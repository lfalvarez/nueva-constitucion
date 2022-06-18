from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_og_image(artículo_nombre, contenido):
    file_name = 'images_creator/plantilla.png'

    base = Image.open(file_name).convert('RGBA')
    font_titulo = ImageFont.truetype("images_creator/fonts/FredokaOne-Regular.ttf", 30)
    font_numero_articulo = ImageFont.truetype("images_creator/fonts/FredokaOne-Regular.ttf", 22)

    txt = Image.new('RGBA', base.size, (176, 129, 107, 0))

    d = ImageDraw.Draw(txt)
    lines = textwrap.wrap(contenido, width=50)
    max_lines = 5
    if len(lines) > max_lines:
        last_line = lines[max_lines - 1] + u'...'
        lines = lines[0:max_lines]
        lines[max_lines - 1] = last_line

    articulo_contenido = '\n'.join(lines)

    d.multiline_text((81, 200), articulo_contenido, font=font_titulo, fill=(255, 255, 255, 255))
    d.multiline_text((81, 550), artículo_nombre, font=font_numero_articulo, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(base, txt)

    return out


if __name__ == "__main__":
    im = generate_og_image("artículo 1", "Chile es un Estado social y democrático de derecho. Es plurinacional, intercultural, regional y ecológico.")
    im.save('prueba.png')